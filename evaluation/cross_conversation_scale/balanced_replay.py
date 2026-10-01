"""Balanced, resumable per-question replay for the 30-chat C4 comparison.

Private quote-bearing inputs and outputs stay under private/xconv. This runner
reuses A's already per-question answers, regenerates B/C at the same granularity,
and blindly grades all three routes together per question.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "evaluation/cross_conversation_scale"))
import scale  # noqa: E402

SOURCE_RUN = scale.PRIV / "scale_run_codex_rerun_20260930"
DEFAULT_RUN = scale.PRIV / "scale_run_codex_balanced_20260930"
LINKER_RUN = scale.DEFAULT_RUN / "linker"
TRACE_PREFIX = "inquiry-graph/xconv-scale-codex-balanced-20260930"


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=1, ensure_ascii=False), encoding="utf-8")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def metadata(args):
    key_path = SOURCE_RUN / "key/cross_key.json"
    a_path = SOURCE_RUN / "answers_A.json"
    b_path, c_path = LINKER_RUN / "export_B.json", LINKER_RUN / "export_C.json"
    for path in (key_path, a_path, b_path, c_path):
        if not path.is_file():
            raise FileNotFoundError(path)
    key = read_json(key_path)
    answers_a = read_json(a_path)["answers"]
    items = key["kept"]
    if len(items) != 13 or len(answers_a) != 13:
        raise ValueError(f"expected 13 key items and A answers; got {len(items)} and {len(answers_a)}")
    if [a.get("question_number") for a in answers_a] != list(range(1, 14)):
        raise ValueError("saved A answers are not the expected one-per-question set")
    if any(not it.get("question") or not it.get("answer_key") or not it.get("key_points") for it in items):
        raise ValueError("reference key has an incomplete question")
    return key, answers_a, items, b_path, c_path


def configure(args):
    if not args.codex_subscription:
        raise ValueError("this replay is authorized/configured for the Codex subscription route")
    import os
    run = args.campaign_dir.resolve()
    llm_data = run / "llm-data"
    os.environ["LLM_CLIENT_DATA_ROOT"] = str(llm_data)
    os.environ["LLM_CLIENT_DB_PATH"] = str(llm_data / "llm_observability.db")
    linker = scale.configure_campaign(args)
    scale.TRACE_PREFIX = TRACE_PREFIX
    return linker


def validate_graphs():
    chats = scale.corpus()
    if len(chats) != 30:
        raise ValueError(f"expected 30 chats, got {len(chats)}")
    for cid, directory in chats:
        path = directory / f"{cid}.graph.json"
        done = subprocess.run(
            [scale.CLI, "validate", str(path)], capture_output=True, text=True, check=True
        )
        result = json.loads(done.stdout)
        if not result.get("valid") or result.get("errors"):
            raise ValueError(f"invalid graph {cid}: {result.get('errors')}")
    return chats


def control(run: Path):
    path = run / "grader_control/positive_negative.json"
    if path.exists():
        saved = read_json(path)
        if saved.get("trace_id") != f"{TRACE_PREFIX}/grader-positive-control":
            raise ValueError("grader control artifact has an unexpected trace ID")
        print("grader positive/negative control already recorded", flush=True)
        return

    prompt = (
        "Grade three answers against the answer key. Judge only agreement with the key.\n"
        "QUESTION: What color did the test author choose, and how should it be used?\n"
        "ANSWER KEY: Blue is the chosen color, and it should be used consistently.\n"
        'KEY POINTS (2): ["The chosen color is blue.", "The choice should be used consistently."]\n\n'
        "ANSWER X: The chosen color is blue, and the choice should be used consistently.\n\n"
        "ANSWER Y: The chosen color is red, and no consistent use was requested.\n\n"
        "ANSWER Z: The chosen color is blue.\n\n"
        "Return one grade per answer, labels X, Y and Z."
    )
    trace = f"{TRACE_PREFIX}/grader-positive-control"
    res, meta = scale.call(prompt, trace, model=scale.JUDGE,
                           schema=scale.GradeSet, task="judging")
    grades = {g.label: g.model_dump() for g in res.grades}
    expected = {
        "X": (2, False),
        "Y": (0, True),
    }
    for label, (points, contradicts) in expected.items():
        got = grades.get(label, {})
        if got.get("points_covered") != points or got.get("contradicts_key") is not contradicts:
            raise ValueError(f"grader control failed for label {label}")
    write_json(path, {
        "trace_id": trace,
        "model": scale.JUDGE,
        "billing_mode": "subscription_included",
        "recorded_cost_usd": meta.cost,
        "known_correct": grades["X"],
        "known_wrong": grades["Y"],
    })
    print(f"grader control passed; trace={trace}; cost=${meta.cost:.6f}", flush=True)


def route_answer(route: str, qi: int, item: dict, material: str, run: Path):
    path = run / f"answers_{route}" / f"q{qi:02d}.json"
    trace = f"{TRACE_PREFIX}/answer-{route}/q{qi:02d}"
    if path.exists():
        saved = read_json(path)
        answer = saved.get("answer", {})
        if saved.get("trace_id") != trace or answer.get("question_number") != qi:
            raise ValueError(f"cached route {route} answer {qi} has the wrong identity")
        return answer

    desc = (
        "Brian's positions extracted from all his conversations (stance, question status, chat title, date, "
        "verbatim quote) plus typed cross-chat links between them" if route == "B" else
        "Brian's positions extracted from all his conversations (stance, question status, chat title, date, verbatim quote)"
    )
    prompt = scale.ASK.format(desc=desc, qs=f"1. {item['question']}", material=material)
    print(f"calling route {route} q{qi:02d}; input_chars={len(material):,}; trace={trace}", flush=True)
    res, meta = scale.call(prompt, trace)
    if len(res.answers) != 1 or res.answers[0].question_number != 1:
        raise ValueError(f"route {route} q{qi}: expected one answer numbered 1")
    answer = res.answers[0].model_dump()
    answer["question_number"] = qi
    write_json(path, {"trace_id": trace, "answer": answer, "recorded_cost_usd": meta.cost})
    print(f"completed route {route} q{qi:02d}; cost=${meta.cost:.6f}", flush=True)
    return answer


def judge(qi: int, item: dict, answers: dict, labels: dict, run: Path):
    path = run / "grades" / f"q{qi:02d}.json"
    trace = f"{TRACE_PREFIX}/judge-q{qi:02d}"
    if path.exists():
        saved = read_json(path)
        if saved.get("trace_id") != trace or set(saved.get("routes", {})) != {"A", "B", "C"}:
            raise ValueError(f"cached grade {qi} has the wrong identity/routes")
        if saved.get("labels") != labels:
            raise ValueError(f"cached grade {qi} has a different blinded label assignment")
        return saved["routes"]
    block = "\n\n".join(
        f"ANSWER {lab}: {answers[route]['answer']}" for lab, route in labels.items()
    )
    prompt = (
        "Grade three answers against the answer key. Judge only agreement with the key.\n"
        f"QUESTION: {item['question']}\nANSWER KEY: {item['answer_key']}\n"
        f"KEY POINTS ({len(item['key_points'])}): {json.dumps(item['key_points'], ensure_ascii=False)}\n\n"
        f"{block}\n\nReturn one grade per answer, labels X, Y and Z."
    )
    res, meta = scale.call(prompt, trace, model=scale.JUDGE,
                           schema=scale.GradeSet, task="judging")
    by_label = {g.label: g.model_dump() for g in res.grades}
    if set(by_label) != {"X", "Y", "Z"}:
        raise ValueError(f"judge q{qi}: expected labels X/Y/Z")
    by_route = {route: by_label[label] for label, route in labels.items()}
    write_json(path, {
        "trace_id": trace,
        "labels": labels,
        "routes": by_route,
        "recorded_cost_usd": meta.cost,
    })
    print(f"completed blind grade q{qi:02d}; trace={trace}; cost=${meta.cost:.6f}", flush=True)
    return by_route


def run(args):
    linker = configure(args)
    key, answers_a, items, b_path, c_path = metadata(args)
    chats = validate_graphs()
    if linker != LINKER_RUN.resolve():
        raise ValueError(f"expected the cached linker export at {LINKER_RUN}, got {linker}")
    b_material, c_material = b_path.read_text(encoding="utf-8"), c_path.read_text(encoding="utf-8")
    print(f"preflight: chats={len(chats)} questions={len(items)} A/B/C batch=1; "
          f"B_chars={len(b_material):,} C_chars={len(c_material):,}; graphs=30/30 valid", flush=True)
    manifest = {
        "plan": "evaluation/cross_conversation_scale/balanced-replay-2026-09-30.md",
        "source_campaign": str(SOURCE_RUN),
        "question_count": len(items),
        "batch_size": 1,
        "model": "codex/gpt-5.6-luna",
        "judge_model": "codex/gpt-5.6-sol",
        "key_sha256": sha256(SOURCE_RUN / "key/cross_key.json"),
        "answers_a_sha256": sha256(SOURCE_RUN / "answers_A.json"),
        "export_b_sha256": sha256(b_path),
        "export_c_sha256": sha256(c_path),
        "source_revision": subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True
        ).stdout.strip(),
    }
    manifest_path = args.campaign_dir.resolve() / "balanced_replay.json"
    if manifest_path.exists() and read_json(manifest_path) != manifest:
        raise ValueError("replay inputs/revision differ from the existing private manifest")
    write_json(manifest_path, manifest)
    if args.plan_only:
        return

    control(args.campaign_dir.resolve())
    answers = {"A": [{**a, "question_number": i} for i, a in enumerate(answers_a, 1)]}
    materials = {"B": b_material, "C": c_material}
    for route in ("B", "C"):
        answers[route] = [route_answer(route, qi, item, materials[route], args.campaign_dir.resolve())
                          for qi, item in enumerate(items, 1)]

    rng = random.Random(59)
    blinded_labels = []
    for _ in items:
        routes = ["A", "B", "C"]
        rng.shuffle(routes)
        blinded_labels.append(dict(zip("XYZ", routes)))
    grades = []
    for qi, item in enumerate(items, 1):
        per_q = {route: {"answer": answers[route][qi - 1]["answer"]} for route in ("A", "B", "C")}
        grades.append(judge(qi, item, per_q, blinded_labels[qi - 1], args.campaign_dir.resolve()))
    write_json(args.campaign_dir.resolve() / "grades.json", grades)
    write_json(args.campaign_dir.resolve() / "summary.json", {
        "status": "complete",
        "questions": len(items),
        "answers_per_route": {route: len(rows) for route, rows in answers.items()},
        "grades": len(grades),
        "answer_model": scale.MODEL,
        "judge_model": scale.JUDGE,
        "trace_prefix": TRACE_PREFIX,
    })
    print(f"replay complete: questions={len(items)} answer_counts={{A:13,B:13,C:13}} grades={len(grades)}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex-subscription", action="store_true")
    parser.add_argument("--campaign-dir", type=Path, default=DEFAULT_RUN)
    parser.add_argument("--model", default="codex/gpt-5.6-luna")
    parser.add_argument("--judge-model", default="codex/gpt-5.6-sol")
    parser.add_argument("--model-justification", default=(
        "Use Brian's active Codex subscription for the balanced replay after the earlier OpenRouter "
        "campaign could not afford the full-context reference key."
    ))
    parser.add_argument("--linker-dir", type=Path, default=LINKER_RUN)
    parser.add_argument("--plan-only", action="store_true",
                        help="validate inputs and write the private manifest without making LLM calls")
    args = parser.parse_args()
    run(args)


if __name__ == "__main__":
    main()
