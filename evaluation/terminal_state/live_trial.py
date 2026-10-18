"""Import a ChatGPT Exporter Markdown transcript for private terminal-state testing.

The deterministic import/validation requires no provider. Optional extraction
and reader evaluation use a locally configured, authorized llm_client route.
The raw transcript, extracted graph, and answers are saved ONLY under --out;
never place --out under a tracked public repository directory.

Prepare:
 python -m evaluation.terminal_state.live_trial --transcript /path/chat.md --out private/terminal_trial

Live test (when llm_client is available):
 python -m evaluation.terminal_state.live_trial --transcript /path/chat.md --out private/terminal_trial \
   --extract --model codex/gpt-5.6-luna --reader

Reader A/B/C/D conditions share one prompt and preserve the original cutoff.
Judging against the separate six-point gold rubric remains a separate review.
"""
import argparse
import asyncio
import hashlib
import json
import re
from pathlib import Path

from inquiry_graph.model import Conversation, Graph, Message, Participant
from inquiry_graph.validate import validate
from inquiry_graph.views import open_questions
from inquiry_graph.render import report
from evaluation.terminal_state.experiment import QUESTION, get_fixture, prepare

HEAD = re.compile(
    r"(?m)^## (Prompt|Response):[ \t]*\n"
    r"(\d{1,2}/\d{1,2}/\d{4}, \d{1,2}:\d{2}:\d{2} [AP]M)"
    r"(?: · ([^\n]+))?[ \t]*\n"
)
EXPORT_FOOTER = re.compile(
    r"\n+---\s*\nPowered by \[ChatGPT Exporter\]\([^\n]+\)\s*$"
)


def import_visible_export(source: str) -> tuple[Conversation, dict]:
    """Preserve each actual visible response as ONE message, not tool-status turns."""
    matches = list(HEAD.finditer(source))
    if not matches or len(matches) % 2:
        raise ValueError("Missing or uneven Prompt/Response headings")
    if any(m.group(1) != ("Prompt" if i % 2 == 0 else "Response")
           for i, m in enumerate(matches)):
        raise ValueError("Expected alternating Prompt/Response sections")
    source_hash = hashlib.sha256(source.encode("utf-8")).hexdigest()[:12]
    title_match = re.search(r"(?m)^# ([^\n]+)", source)
    title = title_match.group(1).strip() if title_match else "ChatGPT Exporter conversation"
    msgs = []
    clocks = []
    for i, m in enumerate(matches):
        ending = matches[i + 1].start() if i + 1 < len(matches) else len(source)
        raw = source[m.end():ending]
        if i == len(matches) - 1:
            raw = EXPORT_FOOTER.sub("", raw)
        body = raw.strip()
        if not body:
            raise ValueError(f"Empty visible message {i + 1}")
        speaker = "user" if m.group(1) == "Prompt" else "assistant"
        msgs.append(Message(
            id=f"exporter-{source_hash}:m{i + 1:03d}",
            actor_id=f"participant:{speaker}", ordinal=i + 1,
            text=body, original_id=None, timestamp=None
        ))
        clocks.append({"ordinal": i + 1, "displayed_time": m.group(2),
                       "displayed_model": m.group(3)})
    conv = Conversation(
        id=f"exporter-{source_hash}",
        title=title, source_kind="normalized",
        coverage_note=("All visible Prompt/Response sections from one user-provided "
                       "ChatGPT Exporter Markdown file. Displayed timestamps are "
                       "retained separately in private import metadata; message IDs "
                       "are synthetic, NOT native ChatGPT IDs. Excludes hidden turns "
                       "and cannot establish underlying chat completeness."),
        participants=[
            Participant(id="participant:user", role="user", label="User"),
            Participant(id="participant:assistant", role="assistant", label="ChatGPT")
        ], messages=msgs
    )
    return conv, {"source_hash_prefix": source_hash, "visible_messages": len(msgs),
                  "visible_user_turns": len(msgs) // 2,
                  "visible_assistant_turns": len(msgs) // 2,
                  "displayed_times": clocks}


def terminal_detection(graph: Graph, final_message: Message) -> dict:
    """Deterministic diagnostic only: not a blind model-reader grade."""
    node_map = {n.id: n for n in graph.nodes}
    sourced_tasks = [
        n for n in graph.nodes
        if n.kind == "task" and any(a.message_id == final_message.id for a in n.anchors)
    ]
    task_ids = {n.id for n in sourced_tasks}
    open_status = [
        e for e in graph.question_events
        if e.question_id in task_ids and e.status == "open"
        and e.actor_id == final_message.actor_id
        and e.at_message_id == final_message.id
    ]
    matching = [
        n for n in sourced_tasks
        if any(x in n.text.lower() for x in ("framework", "comparison", "scenario"))
    ]
    return {
        "terminal_source_message_id": final_message.id,
        "terminal_source_tasks": [n.id for n in sourced_tasks],
        "terminal_source_open_status_events": [e.id for e in open_status],
        "terminal_comparative_task_detected": bool(matching),
        "candidate_count": len(matching),
        "structurally_valid": validate(graph)["valid"],
        "only_structural_evidence": True,
        "caution": ("This check establishes an anchored open task, not that an "
                    "independent reader resumes correctly.")
    }


def optional_extract(conv: Conversation, out: Path, model: str) -> Graph:
    from inquiry_graph.live_extract import extract_conversation
    graph, stats = asyncio.run(extract_conversation(
        conv, model=model, cache_dir=out / "llm_cache"
    ))
    result = validate(graph)
    if not result["valid"]:
        raise ValueError(f"Extracted graph invalid: {result['errors']}")
    (out / "D_live_graph.json").write_text(graph.model_dump_json(indent=2), encoding="utf-8")
    (out / "D_extraction_stats.json").write_text(
        json.dumps(stats, indent=2, default=str), encoding="utf-8")
    return graph


def optional_reader(material: dict[str, str], out: Path) -> None:
    from pydantic import BaseModel
    from llm_client import call_llm_structured, get_model

    class ReaderAnswer(BaseModel):
        answer: str
        source_evidence: list[str]
        cannot_answer: bool

    answers = {}
    model = get_model("synthesis")
    for cond in ("A", "B", "C", "D"):
        ans, meta = call_llm_structured(
            model,
            [{"role": "user", "content": QUESTION + "\n\nMATERIAL:\n" + material[cond]}],
            response_model=ReaderAnswer,
            task="synthesis", reasoning_effort="medium",
            model_policy="enforce_allowlist", max_budget=3.0,
            trace_id=f"inquiry-graph/terminal-state/exporter-20261018/{cond}"
        )
        answers[cond] = {
            "model": model, "answer": ans.model_dump(),
            "cost": meta.cost, "usage": meta.usage
        }
        (out / "reader_answers.json").write_text(
            json.dumps(answers, indent=2, ensure_ascii=False, default=str), encoding="utf-8")
    (out / "reader_grading_status.json").write_text(
        json.dumps({
            "gold_rubric": "evaluation/terminal_state/fixtures/semantic_factorization_20261018.json",
            "judged": False, "blinded_judgment_done": False,
            "warning": "Answers must be scored independently against all six rubric points."
        }, indent=2), encoding="utf-8"
    )




def optional_blind_judge(out: Path) -> None:
    """Separate model-assisted grading, followed by necessary human review."""
    import random
    from pydantic import BaseModel
    from llm_client import call_llm_structured, get_model

    class PointGrade(BaseModel):
        point_index: int
        covered: bool
        explanation: str

    class AnswerGrade(BaseModel):
        label: str
        points: list[PointGrade]
        unsupported_claims: list[str]

    class BlindGrades(BaseModel):
        grades: list[AnswerGrade]

    answers = json.loads((out / "reader_answers.json").read_text(encoding="utf-8"))
    expected = {"A", "B", "C", "D"}
    if set(answers) != expected:
        raise ValueError("Cannot grade without exactly A, B, C and D")
    gold = get_fixture()
    conditions = sorted(expected)
    random.Random(20261018).shuffle(conditions)
    aliases = dict(zip("WXYZ", conditions))
    answer_blocks = "\n\n".join(
        f"ANSWER {alias}:\n{answers[condition]['answer']['answer']}"
        for alias, condition in aliases.items()
    )
    points = "\n".join(f"{i + 1}. {p}" for i, p in enumerate(gold["grading"]["points"]))
    prompt = (
        "Score four answers to the SAME question against the six factual key points. "
        "The answer conditions have been randomized. Do not reward relevant but "
        "different facts, and do not assume that later work was already complete "
        "at the export cutoff. Each covered point must be unambiguously stated "
        "in the answer. Assess hallucinated or unsupported completion claims "
        "separately. Grade exactly points 1-6 for every answer label W,X,Y,Z. "
        "The key is from a manually checked transcript and was NOT given to "
        "the answering model.\n\n"
        f"QUESTION:\n{QUESTION}\n\nREFERENCE:\n"
        f"Active terminal quotation: {gold['terminal_quote']}\n"
        f"Validation limitation: {gold['validation_quote']}\n"
        f"Repository integrity activity: {gold['integrity_quote']}\n"
        f"Five cases: {', '.join(gold['five_cases'])}\n"
        f"POINTS:\n{points}\n\n{answer_blocks}"
    )
    judged, meta = call_llm_structured(
        get_model("judging"),
        [{"role": "user", "content": prompt}],
        response_model=BlindGrades,
        task="judging", reasoning_effort="medium",
        model_policy="enforce_allowlist", max_budget=3.0,
        trace_id="inquiry-graph/terminal-state/exporter-20261018/blind-judge"
    )
    labels = {g.label: g for g in judged.grades}
    if set(labels) != set("WXYZ"):
        raise ValueError("Blind grader did not return all four labels")
    outcome = {}
    for label, condition in aliases.items():
        result = labels[label]
        by_point = {p.point_index: p for p in result.points}
        if set(by_point) != set(range(1, 7)):
            raise ValueError(f"Blind grader missing or duplicated points for {label}")
        outcome[condition] = {
            "points": [by_point[i].model_dump() for i in range(1, 7)],
            "score": sum(by_point[i].covered for i in range(1, 7)),
            "unsupported_claims": result.unsupported_claims
        }
    (out / "reader_grades.json").write_text(
        json.dumps({
            "scores": outcome,
            "judge_model": get_model("judging"), "judge_cost": meta.cost,
            "judge_usage": meta.usage, "blind_alias_map": aliases,
            "human_review_complete": False,
            "warning": ("Model-assisted, condition-blinded grading; manual source "
                        "inspection is still required before publishing an accuracy claim.")
        }, indent=2, default=str), encoding="utf-8"
    )

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--transcript", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--extract", action="store_true")
    p.add_argument("--model", help="Authorized extraction model for --extract")
    p.add_argument("--reader", action="store_true",
                   help="Use llm_client for A/B/C/D; requires --extract")
    p.add_argument("--judge", action="store_true",
                   help="Run a condition-blinded model-assisted rubric judge; requires --reader")
    args = p.parse_args()
    if args.reader and not args.extract:
        p.error("--reader requires --extract")
    if args.judge and not args.reader:
        p.error("--judge requires --reader")
    if args.extract and not args.model:
        p.error("--extract requires an explicit --model")
    source = args.transcript.read_text(encoding="utf-8")
    case = get_fixture()
    for label in ("last_user_quote", "terminal_quote", "integrity_quote", "validation_quote"):
        if case[label] not in source:
            raise ValueError(f"Source is missing expected verbatim text: {label}")
    conv, import_meta = import_visible_export(source)
    if case["terminal_quote"] not in conv.messages[-1].text:
        raise ValueError("Final assistant reply did not retain exact terminal task quote")
    args.out.mkdir(parents=True, exist_ok=True)
    # Preserve private raw content in private run directory ONLY.
    (args.out / "source_normalized.json").write_text(
        conv.model_dump_json(indent=2), encoding="utf-8")
    (args.out / "source_metadata.json").write_text(
        json.dumps(import_meta, indent=2), encoding="utf-8")
    material, prep_checks = prepare(args.transcript, args.out)
    result = {
        "source": {"messages": import_meta["visible_messages"],
                   "user_turns": import_meta["visible_user_turns"],
                   "assistant_turns": import_meta["visible_assistant_turns"],
                   "last_displayed_time": import_meta["displayed_times"][-1]["displayed_time"]},
        "comparisons_prepared": sorted(material),
        "baseline_controls": prep_checks,
        "live_extractor_run": False,
        "reader_abcd_run": False,
    }
    if args.extract:
        graph = optional_extract(conv, args.out, args.model)
        material["D"] = report(graph)
        (args.out / "D.txt").write_text(material["D"], encoding="utf-8")
        result["live_extractor_run"] = True
        result["D_terminal_diagnostic"] = terminal_detection(graph, conv.messages[-1])
        if args.reader:
            optional_reader(material, args.out)
            result["reader_abcd_run"] = True
            if args.judge:
                optional_blind_judge(args.out)
                result["model_assisted_blind_grading_run"] = True
    (args.out / "trial_summary.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "baseline_controls"},
                     indent=2))


if __name__ == "__main__":
    main()
