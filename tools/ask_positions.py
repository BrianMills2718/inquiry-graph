"""Ask a cross-chat question of Brian's extracted positions; every cited quote is checked against the source.

Usage: ask_positions.py "<question>" <graphs_dir> [<graphs_dir> ...] --out answer.json [--top 60] [--model M]
Brian-attributed stance and question events (speaker == actor, quote verbatim in that message) become evidence
records {id, chat, title, date, kind, target, quote}. BM25 retrieves the top records for the question, the model
answers in structured claims that cite record ids, and code then verifies each cite exists and its quote is verbatim
in the source message. Output keeps the full evidence table so the answer can be hand-checked.
"""
import argparse
import asyncio
import json
import re
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from rank_bm25 import BM25Okapi


def records(graph_dirs, skip=frozenset()):
    out, seen = [], set()   # one chat can have graphs in several folders (different runs/models): count each quoted message once
    for d in graph_dirs:
        for f in sorted(Path(d).glob("*.graph.json")):
            g = json.loads(f.read_text(encoding="utf-8"))
            conv = g["conversations"][0]
            msgs = {m["id"]: m for m in conv["messages"]}
            nodes = {n["id"]: n for n in g["nodes"]}
            for kind in ("stance_events", "question_events"):
                for e in g[kind]:
                    if e["actor_id"] != "participant:brian":
                        continue
                    for a in e["anchors"]:
                        m = msgs.get(a["message_id"])
                        if not m or m["actor_id"] != "participant:brian" or a["quote"] not in m["text"]:
                            continue
                        if (a["message_id"], a["quote"]) in skip:   # pasted or quoted text, not Brian's words
                            continue
                        if (a["message_id"], a["quote"]) in seen:
                            continue
                        seen.add((a["message_id"], a["quote"]))
                        tgt = nodes.get(e.get("target_id") or e.get("question_id"), {}).get("text", "")
                        out.append({"id": f"E{len(out):05d}", "chat": conv["id"], "title": conv["title"].strip().replace("\n", " ")[:120], "date": (m.get("timestamp") or "")[:10],
                                    "kind": e.get("stance") or ("question:" + e.get("status", "")), "target": tgt, "quote": a["quote"],
                                    "message_id": a["message_id"]})
    return out


class Claim(BaseModel):
    statement: str = Field(description="One supported statement about Brian's views.")
    kind: Literal["position", "change", "conflict", "open_question"]
    cites: list[str] = Field(description="Evidence record ids supporting it. A change or conflict needs at least two cites from different chats or dates.")


class Answer(BaseModel):
    summary: str
    claims: list[Claim]
    unsupported_or_unknown: str = Field(description="What the evidence cannot establish.")


def tok(s):
    return re.findall(r"[a-z0-9]+", s.lower())


async def ask(question, recs, top, model):
    from llm_client import acall_llm_structured
    bm = BM25Okapi([tok(r["target"] + " " + r["quote"] + " " + r["title"]) for r in recs])
    scores = bm.get_scores(tok(question))
    seen, pick = set(), []
    for i in sorted(range(len(recs)), key=lambda i: -scores[i]):
        k = (recs[i]["message_id"], recs[i]["quote"])
        if k in seen:   # one message can back several ideas; show it once so repetition is not inflated
            continue
        seen.add(k)
        pick.append(recs[i])
        if len(pick) == top:
            break
    pick.sort(key=lambda r: r["date"])
    ev = "\n".join(f'{r["id"]} | {r["date"]} | {r["title"]} | {r["kind"]} | idea: {r["target"][:200]} | Brian said: "{r["quote"][:300]}"' for r in pick)
    system = ("You answer questions about Brian's own views using ONLY the evidence records below, each of which is his own words "
              "with the idea he was reacting to. Cite record ids. A change is an earlier and a later statement on the SAME topic that differ. A conflict is two statements Brian made that cannot both hold, each cited; statements that merely lean the same way, or that concern different topics, are NOT a conflict. An open question needs Brian to actually ask or express uncertainty, not just state a position. Prefer fewer, well-supported claims. "
              "Do not use outside knowledge about Brian. Say what the evidence cannot establish.")
    out, meta = await acall_llm_structured(
        model, [{"role": "system", "content": system}, {"role": "user", "content": f"Question: {question}\n\nEvidence:\n{ev}"}],
        response_model=Answer, reasoning_effort="medium", model_policy="enforce_allowlist", task="position-answer",
        trace_id="inquiry-graph/ask-positions", max_budget=2.00,
        **({"codex_transport": "cli", "sandbox_mode": "read-only", "approval_policy": "never", "working_directory": str(Path("private/ask_cwd").resolve()),
            "model_justification": "Brian's Codex subscription for private archive answers (2026-10-03)."} if model.startswith("codex/") else {}))
    return out, pick, meta


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("question")
    ap.add_argument("graph_dirs", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--top", type=int, default=60)
    ap.add_argument("--authorship", type=Path, help="authorship JSON from check_authorship.py (needs --records); pasted_or_quoted events are left out")
    ap.add_argument("--records", type=Path)
    ap.add_argument("--model", default="openrouter/openai/gpt-5.6-luna")
    a = ap.parse_args()
    skip = frozenset()
    if a.authorship and a.records:
        lab = json.loads(a.authorship.read_text())
        skip = frozenset((r["message_id"], r["quote"]) for r in json.loads(a.records.read_text())["records"] if lab.get(r["id"], {}).get("label") == "pasted_or_quoted")
    recs = records(a.graph_dirs, skip)
    answer, pick, meta = asyncio.run(ask(a.question, recs, a.top, a.model))
    by = {r["id"]: r for r in pick}
    report = []
    for c in answer.claims:
        bad = [i for i in c.cites if i not in by]
        dates = {by[i]["date"] for i in c.cites if i in by}
        chats = {by[i]["chat"] for i in c.cites if i in by}
        weak = c.kind in ("change", "conflict") and len(dates | chats) < 2
        report.append({**c.model_dump(), "cites_resolved": not bad, "unresolved": bad, "needs_two_sources_ok": not weak,
                       "evidence": [by[i] for i in c.cites if i in by]})
    a.out.write_text(json.dumps({"question": a.question, "records_total": len(recs), "records_shown": len(pick), "summary": answer.summary,
                                 "unsupported_or_unknown": answer.unsupported_or_unknown, "claims": report,
                                 "trace": str(meta)[:400]}, indent=1), encoding="utf-8")
    ok = sum(1 for r in report if r["cites_resolved"] and r["needs_two_sources_ok"])
    print(json.dumps({"records_total": len(recs), "claims": len(report), "claims_passing_code_checks": ok}))


if __name__ == "__main__":
    main()
