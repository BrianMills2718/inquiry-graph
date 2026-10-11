"""Follow-up 2026-10-11: re-score condition C after report() started carrying relations as text.

Reuses the saved questions and the saved A/B answers; only condition C is re-answered.
  render   the pilot-era seed graph (commit 45b1e82, the one the pilot's C report came from)
           is rendered with the current report() into private/usefulness/C2_graph_report.md
  answer   the pilot's answer prompt, condition C2, same model family through Codex
  judge    the pilot's blind three-answer judge prompt, run twice through Codex:
           (A, B, C2) and (A, B, old C), so old and new C are graded by the same judge route
Stages are cached under private/usefulness/; copies of the results go to data/.
"""
import json, subprocess, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run  # noqa: E402

ROOT = run.ROOT
PILOT_GRAPH_COMMIT = "45b1e82"
MODEL = "codex/gpt-5.6-luna"
OPTS = dict(model_policy="enforce_allowlist", max_budget=3.00, codex_transport="cli", sandbox_mode="read-only",
            approval_policy="never", working_directory=str(run.PRIV),
            model_justification="Brian (2026-10-11): re-score the usefulness pilot on his Codex subscription, not OpenRouter; "
                                "same gpt-5.6-luna model the pilot used for answering and judging.")


def render_c2():
    from inquiry_graph.io import load
    from inquiry_graph.model import Graph
    from inquiry_graph.render import report
    raw = subprocess.run(["git", "show", f"{PILOT_GRAPH_COMMIT}:examples/seed/graph.json"], cwd=ROOT,
                         check=True, capture_output=True, text=True, encoding="utf-8").stdout
    tmp = run.PRIV / "pilot_graph_45b1e82.json"
    tmp.write_text(raw, encoding="utf-8")
    text = report(load(tmp, Graph))
    (run.PRIV / "C2_graph_report.md").write_text(text, encoding="utf-8")
    return len(text)


def score(items, grades, cond):
    fr = [min(g[cond]["points_covered"], len(it["key_points"])) / len(it["key_points"]) for it, g in zip(items, grades)]
    return {"mean": round(sum(fr) / len(fr), 3), "fully_right": sum(f == 1 for f in fr),
            "contradicts": sum(g[cond]["contradicts_key"] for g in grades), "per_question": [round(f, 2) for f in fr]}


def main():
    items = run.cache("questions.json", lambda: sys.exit("missing saved questions"))["kept"]
    print(f"C2 report: {render_c2()} chars")
    answers = {c: run.cache(f"answers_{c}.json", lambda: sys.exit(f"missing saved answers_{c}")) for c in "ABC"}
    answers["C2"] = run.cache("answers_C2.json", lambda: run.answer("C2", items, model=MODEL, opts=OPTS))
    new = run.cache("grades_followup_C2.json", lambda: run.judge(items, answers, model=MODEL, opts=OPTS,
                                                               conds_order=("A", "B", "C2"), tag="-followup-C2"))
    old = run.cache("grades_followup_C.json", lambda: run.judge(items, answers, model=MODEL, opts=OPTS,
                                                              conds_order=("A", "B", "C"), tag="-followup-C"))
    saved = run.cache("grades.json", lambda: sys.exit("missing saved grades"))
    summary = {"saved_openrouter_judge": {c: score(items, saved, c) for c in "ABC"},
               "codex_judge_with_C2": {c: score(items, new, c) for c in ("A", "B", "C2")},
               "codex_judge_with_old_C": {c: score(items, old, c) for c in "ABC"}}
    for name in ("answers_C2.json", "grades_followup_C2.json", "grades_followup_C.json"):
        (run.OUT / "data" / name).write_text((run.PRIV / name).read_text(encoding="utf-8"), encoding="utf-8")
    (run.OUT / "data" / "followup_summary.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps({k: {c: (v["mean"], v["fully_right"]) for c, v in s.items()} for k, s in summary.items()}, indent=1))


if __name__ == "__main__":
    main()
