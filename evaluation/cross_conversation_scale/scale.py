"""Scale test for the cross-chat linker (goal C2–C5).

The default OpenRouter run is cached under private/xconv/scale_run/. An opt-in
Codex subscription run uses a separate private campaign directory and manifest.

Corpus: the previous goal's 5 chats (private/xconv/<id8>.*) plus every transcript in
private/xconv/scale/<id8>.md. Routes, all answered by the same model and graded blind:
  A  search-then-read: BM25 over whole chats per question, read top chats up to READ_BUDGET chars
  B  Brian's positions (status, dates, quotes) + typed cross-chat links
  C  Brian's positions only (ablation of the links)
"""
import asyncio
import argparse
import json
import math
import random
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "evaluation/cross_conversation"))
import build_key  # noqa: E402
from inquiry_graph.model import Conversation  # noqa: E402
from llm_client import (  # noqa: E402
    ObservabilityContentPolicy,
    call_llm_structured,
    get_model,
)

PRIV = ROOT / "private/xconv"
DEFAULT_RUN = PRIV / "scale_run"
RUN = DEFAULT_RUN
FIRST5 = ["6ab8563b", "6ab96260", "69c07755", "6a988a7a", "6a171ac3"]
READ_BUDGET = 600_000   # chars an agent may read per question in route A (~150k tokens)
DEFAULT_MODEL, DEFAULT_JUDGE = get_model("synthesis"), get_model("judging")
MODEL, JUDGE = DEFAULT_MODEL, DEFAULT_JUDGE
CALL_OPTIONS = {}
MODEL_JUSTIFICATION = None
OBSERVABILITY_POLICY = None
KEY_TRACE_PREFIX = "inquiry-graph/xconv-key"
TRACE_PREFIX = "inquiry-graph/xconv-scale"
CLI = str(ROOT / ".venv/bin/inquiry-graph")

SPEC = """Write 15 questions an AI assistant to Brian might be asked about his views ACROSS these conversations:
- 3 agreement_across_chats: the same view expressed in two or more chats;
- 3 conflict_or_tension: views in different chats that pull against each other (say how);
- 3 recurring_open_question: a question he raises in more than one chat and never settles;
- 3 change_over_time: a view that shifts between chats (use the dates);
- 3 position_summary: his overall position on a named topic, drawing on several chats.
Name each question's topic concretely, in words Brian might use when asking."""


def run(cmd):
    """Run a step; on failure show its own output instead of hiding it."""
    done = subprocess.run(cmd, capture_output=True, text=True)
    if done.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd[:3])} failed ({done.returncode}):\n{done.stdout[-1500:]}\n{done.stderr[-1500:]}")
    return done


def corpus() -> list[tuple[str, Path]]:
    """(id8, directory) for every chat; scale chats are imported and extracted here if needed."""
    scale_dir = PRIV / "scale"
    chats = [(c, PRIV) for c in FIRST5]
    for md in sorted(scale_dir.glob("*.md")):
        cid = md.stem
        conv, graph = scale_dir / f"{cid}.conv.json", scale_dir / f"{cid}.graph.json"
        if not conv.exists():
            run([CLI, "import-bridge", str(md), str(conv)])
        if not graph.exists():
            run([CLI, "extract", str(conv), str(graph), "--llm", "--report",
                 str(scale_dir / f"{cid}.report.json"), "--cache-dir", str(PRIV / "llm-cache")])
        chats.append((cid, scale_dir))
    return chats


def load_conv(cid, d) -> Conversation:
    return Conversation.model_validate_json((d / f"{cid}.conv.json").read_text(encoding="utf-8"))


def render(conv: Conversation) -> str:
    label = {p.id: ("BRIAN" if p.role == "user" else "ASSISTANT") for p in conv.participants}
    date = (conv.messages[0].timestamp or "")[:10]
    body = "\n\n".join(f"[{m.ordinal}] {label[m.actor_id]}:\n{m.text}" for m in conv.messages)
    return f"===== CHAT: {conv.title} ({date}) =====\n{body}"


TOKEN = re.compile(r"[a-z][a-z0-9]+")
STOP = set("the a an and or of to in on for is are was were be been with that this it as at by from what which how why "
           "does do did his he brian brian's across chats chat conversations view views about has have not".split())


def tokens(text):
    return [t for t in TOKEN.findall(text.lower()) if t not in STOP]


def bm25_rank(query: str, docs: dict[str, str], k1=1.5, b=0.75) -> list[str]:
    tf = {d: Counter(tokens(t)) for d, t in docs.items()}
    lens = {d: sum(c.values()) for d, c in tf.items()}
    avg = sum(lens.values()) / len(lens)
    df = Counter(w for c in tf.values() for w in c)
    n = len(docs)
    def score(d):
        s = 0.0
        for w in set(tokens(query)):
            if w not in tf[d]:
                continue
            idf = math.log(1 + (n - df[w] + 0.5) / (df[w] + 0.5))
            f = tf[d][w]
            s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * lens[d] / avg))
        return s
    return sorted(docs, key=score, reverse=True)


class Answer(BaseModel):
    question_number: int
    answer: str
    cannot_answer: bool


class AnswerSet(BaseModel):
    answers: list[Answer]


class Grade(BaseModel):
    label: Literal["X", "Y", "Z"]
    points_covered: int
    contradicts_key: bool
    attribution_error: bool
    unsupported_claims: bool


class GradeSet(BaseModel):
    grades: list[Grade]


ASK = """You are an AI assistant that must understand Brian's views across his conversations.
You are given {desc}. Answer using only this material. Be specific (2-5 sentences), name the chats
(and dates where known) that support the answer, and distinguish Brian's own views from assistant suggestions.
If the material does not support an answer, say so and set cannot_answer.

QUESTIONS:
{qs}

MATERIAL:
{material}"""


def call(prompt, trace, model=MODEL, schema=AnswerSet, task="synthesis"):
    options = {
        "reasoning_effort": "medium",
        "model_policy": "enforce_allowlist",
        "task": task,
        "trace_id": trace,
        "max_budget": 6.00,
        **CALL_OPTIONS,
    }
    if MODEL_JUSTIFICATION:
        options["model_justification"] = MODEL_JUSTIFICATION
    if OBSERVABILITY_POLICY is not None:
        options["observability_content_policy"] = OBSERVABILITY_POLICY
    res, meta = call_llm_structured(model, [{"role": "user", "content": prompt}], response_model=schema,
                                    **options)
    return res, meta


def cache(name, build):
    path = RUN / name
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    data = build()
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    return data


def _inside_private(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    try:
        resolved.relative_to(PRIV.resolve())
    except ValueError as exc:
        raise ValueError(f"private campaign paths must stay under {PRIV}") from exc
    if resolved == PRIV.resolve():
        raise ValueError("a campaign path must name a directory below private/xconv")
    return resolved


def configure_campaign(args):
    """Select a non-mixing campaign directory and provider route."""
    global RUN, MODEL, JUDGE, CALL_OPTIONS, MODEL_JUSTIFICATION, OBSERVABILITY_POLICY
    global KEY_TRACE_PREFIX, TRACE_PREFIX

    if args.codex_subscription:
        MODEL = args.model or "codex/gpt-5.6-luna"
        JUDGE = args.judge_model or "codex/gpt-5.6-sol"
        MODEL_JUSTIFICATION = args.model_justification or (
            "Use Brian's active Codex subscription for this private evaluation because the OpenRouter account "
            "could not afford the full-context reference-key call."
        )
        CALL_OPTIONS = {
            "codex_transport": "cli",
            "sandbox_mode": "read-only",
            "approval_policy": "never",
            "working_directory": str(ROOT),
        }
        OBSERVABILITY_POLICY = ObservabilityContentPolicy(mode="metadata_only")
        default_dir = PRIV / "scale_run_codex"
    else:
        if any((args.model, args.judge_model, args.model_justification, args.campaign_dir)):
            raise ValueError("custom models and campaign directories require --codex-subscription")
        MODEL, JUDGE = DEFAULT_MODEL, DEFAULT_JUDGE
        CALL_OPTIONS = {}
        MODEL_JUSTIFICATION = None
        OBSERVABILITY_POLICY = None
        default_dir = DEFAULT_RUN

    RUN = _inside_private(args.campaign_dir or default_dir)
    if RUN == DEFAULT_RUN and args.codex_subscription:
        raise ValueError("Codex subscription outputs must use a separate campaign directory")
    if args.codex_subscription:
        campaign = {
            "model": MODEL,
            "judge_model": JUDGE,
            "transport": "codex-cli",
            "sandbox_mode": "read-only",
            "approval_policy": "never",
            "observability": "metadata_only",
            "model_justification": MODEL_JUSTIFICATION,
        }
        RUN.mkdir(parents=True, exist_ok=True)
        manifest_path = RUN / "campaign.json"
        if manifest_path.exists():
            existing = json.loads(manifest_path.read_text(encoding="utf-8"))
            if existing != campaign:
                raise ValueError(f"campaign settings differ from existing manifest: {manifest_path}")
        else:
            existing_files = [p.name for p in RUN.iterdir()]
            if existing_files:
                raise ValueError(f"refusing to adopt a nonempty campaign without a manifest: {RUN}")
            manifest_path.write_text(json.dumps(campaign, indent=1), encoding="utf-8")
        KEY_TRACE_PREFIX = "inquiry-graph/xconv-key/codex"
        TRACE_PREFIX = "inquiry-graph/xconv-scale-codex"
    else:
        KEY_TRACE_PREFIX = "inquiry-graph/xconv-key"
        TRACE_PREFIX = "inquiry-graph/xconv-scale"

    linker_dir = args.linker_dir or (DEFAULT_RUN / "linker" if args.codex_subscription else RUN / "linker")
    return _inside_private(linker_dir)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-subscription", action="store_true",
                        help="use Codex CLI subscription calls in an isolated private campaign")
    parser.add_argument("--campaign-dir", type=Path,
                        help="private campaign directory; defaults to scale_run_codex for Codex calls")
    parser.add_argument("--model", help="Codex model for answer/key generation")
    parser.add_argument("--judge-model", help="Codex model for blind grading")
    parser.add_argument("--model-justification", help="reason for this non-default model route")
    parser.add_argument("--linker-dir", type=Path,
                        help="existing private linker export directory to reuse")
    parser.add_argument("--keys-only", action="store_true",
                        help="build the independent reference key, then stop before answer routes")
    args = parser.parse_args(argv)
    linker_out = configure_campaign(args)

    RUN.mkdir(parents=True, exist_ok=True)
    chats = corpus()
    convs = {cid: load_conv(cid, d) for cid, d in chats}
    sizes = {cid: sum(len(m.text) for m in c.messages) for cid, c in convs.items()}
    graphs_valid = {}
    for cid, d in chats:
        out = subprocess.run([CLI, "validate", str(d / f"{cid}.graph.json")], capture_output=True, text=True)
        graphs_valid[cid] = json.loads(out.stdout)["valid"] and not json.loads(out.stdout)["errors"]
    reports = {cid: json.loads((d / f"{cid}.report.json").read_text()) for cid, d in chats}
    corpus_info = {"chats": [{"id8": cid, "title": convs[cid].title, "date": (convs[cid].messages[0].timestamp or "")[:10],
                              "visible_chars": sizes[cid], "graph_valid": graphs_valid[cid],
                              "extract_cost": reports[cid].get("new_call_cost_usd")} for cid, _ in chats],
                   "total_visible_chars": sum(sizes.values()),
                   "one_call_context_tokens": 1_050_000,
                   "approx_total_tokens": sum(sizes.values()) // 4}
    (RUN / "corpus.json").write_text(json.dumps(corpus_info, indent=1, ensure_ascii=False))
    print(f"{len(chats)} chats, {corpus_info['total_visible_chars']:,} visible chars "
          f"(~{corpus_info['approx_total_tokens']:,} tokens); all graphs valid: {all(graphs_valid.values())}",
          flush=True)

    key_dir = RUN / "key"
    key_dir.mkdir(exist_ok=True)
    per = [build_key.per_chat(cid, priv=d, out=key_dir, model=MODEL,
                              call_options={**CALL_OPTIONS, **({"model_justification": MODEL_JUSTIFICATION}
                                                               if MODEL_JUSTIFICATION else {}),
                                            **({"observability_content_policy": OBSERVABILITY_POLICY}
                                               if OBSERVABILITY_POLICY else {})},
                              trace_prefix=KEY_TRACE_PREFIX) for cid, d in chats]
    key = build_key.cross(per, out=key_dir, spec=SPEC, n_chats=len(chats), model=MODEL,
                          call_options={**CALL_OPTIONS, **({"model_justification": MODEL_JUSTIFICATION}
                                                           if MODEL_JUSTIFICATION else {}),
                                        **({"observability_content_policy": OBSERVABILITY_POLICY}
                                           if OBSERVABILITY_POLICY else {})},
                          trace_prefix=KEY_TRACE_PREFIX)
    items = key["kept"]
    print(f"key: {sum(len(p['kept']) for p in per)} verified positions; {len(items)} cross-chat questions", flush=True)

    if args.keys_only:
        print(f"C3 reference key ready: {key_dir}; traces use prefix {KEY_TRACE_PREFIX}", flush=True)
        return

    if not (linker_out / "export_B.json").exists():
        subprocess.run([sys.executable, str(ROOT / "evaluation/cross_conversation_scale/run_linker.py"), str(linker_out)]
                       + [str(d / f"{cid}.graph.json") for cid, d in chats], check=True)

    docs = {cid: render(c) for cid, c in convs.items()}

    def route_a():
        answers, cost, read = [], 0.0, []
        for qi, it in enumerate(items, 1):
            picked, used = [], 0
            for cid in bm25_rank(it["question"], docs):
                if used + len(docs[cid]) > READ_BUDGET and picked:
                    continue
                picked.append(cid); used += len(docs[cid])
                if used >= READ_BUDGET:
                    break
            res, meta = call(ASK.format(desc="the full text of the conversations an archive search returned for this question",
                                        qs=f"1. {it['question']}", material="\n\n".join(docs[c] for c in picked)),
                             f"{TRACE_PREFIX}/answer-A/q{qi:02d}")
            a = res.answers[0].model_dump(); a["question_number"] = qi
            answers.append(a); cost += meta.cost; read.append({"q": qi, "chats": picked, "chars": used})
        return {"cost": cost, "answers": answers, "read": read}

    def route_bc(route):
        material = (linker_out / f"export_{route}.json").read_text(encoding="utf-8")
        desc = ("Brian's positions extracted from all his conversations (stance, question status, chat title, date, "
                "verbatim quote) plus typed cross-chat links between them" if route == "B" else
                "Brian's positions extracted from all his conversations (stance, question status, chat title, date, verbatim quote)")
        qs = "\n".join(f"{i + 1}. {it['question']}" for i, it in enumerate(items))
        res, meta = call(ASK.format(desc=desc, qs=qs, material=material), f"{TRACE_PREFIX}/answer-{route}")
        got = {a.question_number: a.model_dump() for a in res.answers}
        if sorted(got) != list(range(1, len(items) + 1)):
            raise ValueError(f"route {route}: answers for {sorted(got)}")
        return {"cost": meta.cost, "chars": len(material), "answers": [got[i + 1] for i in range(len(items))]}

    answers = {"A": cache("answers_A.json", route_a), "B": cache("answers_B.json", lambda: route_bc("B")),
               "C": cache("answers_C.json", lambda: route_bc("C"))}

    def judge():
        rng, out = random.Random(59), []
        for qi, it in enumerate(items):
            routes = ["A", "B", "C"]; rng.shuffle(routes)
            labels = dict(zip("XYZ", routes))
            block = "\n\n".join(f"ANSWER {lab}: {answers[r]['answers'][qi]['answer']}" for lab, r in labels.items())
            prompt = (f"Grade three answers against the answer key. Judge only agreement with the key.\n"
                      f"QUESTION: {it['question']}\nANSWER KEY: {it['answer_key']}\n"
                      f"KEY POINTS ({len(it['key_points'])}): {json.dumps(it['key_points'], ensure_ascii=False)}\n\n"
                      f"{block}\n\nReturn one grade per answer, labels X, Y and Z.")
            res, _ = call(prompt, f"{TRACE_PREFIX}/judge-q{qi + 1:02d}", model=JUDGE, schema=GradeSet, task="judging")
            g = {x.label: x.model_dump() for x in res.grades}
            if set(g) != {"X", "Y", "Z"}:
                raise ValueError(f"q{qi + 1}: judge labels {sorted(g)}")
            out.append({r: g[lab] for lab, r in labels.items()})
        return out

    grades = cache("grades.json", judge)
    rows, tot = [], {r: Counter() for r in "ABC"}
    for qi, (it, g) in enumerate(zip(items, grades), 1):
        k = len(it["key_points"]); row = {"q": qi, "category": it["category"]}
        for r in "ABC":
            s = min(g[r]["points_covered"], k) / k
            row[r] = round(s, 2)
            tot[r]["points"] += s; tot[r]["fully_right"] += (s == 1 and not g[r]["contradicts_key"])
            for f in ("contradicts_key", "attribution_error", "unsupported_claims"):
                tot[r][f] += g[r][f]
            tot[r]["cannot_answer"] += answers[r]["answers"][qi - 1]["cannot_answer"]
        rows.append(row)
    cats = sorted({r["category"] for r in rows})
    by_cat = {c: {r: round(sum(x[r] for x in rows if x["category"] == c) / sum(1 for x in rows if x["category"] == c), 2)
                  for r in "ABC"} for c in cats}
    summary = {r: {"mean_points": round(t["points"] / len(items), 2), **{k: v for k, v in t.items() if k != "points"},
                   "answer_cost": round(answers[r]["cost"], 3)} for r, t in tot.items()}
    (RUN / "summary.json").write_text(json.dumps({"rows": rows, "by_category": by_cat, "summary": summary,
                                                  "route_A_reads": answers["A"]["read"],
                                                  "models": {"answers": MODEL, "judge": JUDGE}}, indent=1))
    for row in rows:
        print(row, flush=True)
    print(json.dumps({"by_category": by_cat, "summary": summary}, indent=1), flush=True)


if __name__ == "__main__":
    main()
