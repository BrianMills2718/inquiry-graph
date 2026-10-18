"""Cutoff-controlled resumption comparison. No model runs by default.

A = original visible transcript; B = Inquiry Graph at export cutoff;
C = B with a source-anchored terminal task encoded using existing schema.

Usage:
  python evaluation/terminal_state/experiment.py --transcript /path/to/export.md --out /tmp/terminal-eval
  python evaluation/terminal_state/experiment.py --transcript /path/to/export.md --out /tmp/terminal-eval --run-reader
The second command requires the separately authorized optional llm_client provider.
"""
import argparse
import copy
import json
from pathlib import Path

from inquiry_graph.model import Graph, Conversation, Message, Node, Move, QuestionEvent, anchor
from inquiry_graph.validate import validate
from inquiry_graph.views import open_questions
from inquiry_graph.render import report

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = Path(__file__).parent / "fixtures/semantic_factorization_20261018.json"
GRAPH = ROOT / "examples/conversations/semantic-factorization-2026-10-18/graph.json"
QUESTION = ("At the END of this conversation, what exact research activity was underway, "
            "what should be done next, and which claims or tests were still unverified? "
            "Distinguish the broad goal from the active task. Use only the provided material.")


def get_fixture():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))


def cutoff_graph():
    """Cut AFTER a13, pruning every semantic record unsupported by surviving messages."""
    g = Graph.model_validate_json(GRAPH.read_text(encoding="utf-8"))
    # Baseline B must reproduce the earlier *unreconciled* graph. The canonical
    # graph now also carries exact terminal excerpts, but those are withheld
    # from B to preserve a valid control; only C receives that evidence.
    original = "semantic-factorization-2026-10-18:conversation"
    g.conversations = [c for c in g.conversations if c.id == original]
    if len(g.conversations) != 1:
        raise ValueError("Expected exactly one original curated conversation")
    last = get_fixture()["cutoff_message_ordinal"]
    g.conversations[0].messages = [m for m in g.conversations[0].messages if m.ordinal <= last]
    mids = {m.id for m in g.conversations[0].messages}
    relevant = lambda obj: all(a.message_id in mids for a in obj.anchors)
    g.nodes = [x for x in g.nodes if relevant(x)]
    g.moves = [x for x in g.moves if relevant(x) and x.at_message_id in mids]
    g.relations = [x for x in g.relations if relevant(x)]
    g.question_events = [x for x in g.question_events if relevant(x) and x.at_message_id in mids]
    g.stance_events = [x for x in g.stance_events if relevant(x) and x.at_message_id in mids]
    # Repeatedly prune records referencing a record removed by the time boundary.
    while True:
        ids = {x.id for field in ("nodes", "moves", "relations") for x in getattr(g, field)}
        move_ids = {m.id for m in g.moves}
        old = (len(g.moves), len(g.relations))
        g.moves = [m for m in g.moves
                   if all(ref in ids for ref in m.input_ids + m.output_ids)
                   and all(ref in move_ids for ref in m.after_move_ids)]
        g.relations = [r for r in g.relations if all(b.ref in ids for b in r.bindings)]
        if old == (len(g.moves), len(g.relations)):
            break
    node_ids = {n.id for n in g.nodes}
    g.question_events = [e for e in g.question_events if e.question_id in node_ids
                         and all(ref in node_ids for ref in e.answer_ids)
                         and (e.replacement_id is None or e.replacement_id in node_ids)]
    g.stance_events = [e for e in g.stance_events if e.target_id in node_ids]
    # Notes are not anchored. Remove them to prevent leaked later events or outcomes.
    g.notes = ["Evaluation projection: synthetic IDs and curated excerpt messages, cutoff "
               "before post-export Python/Z3/Lean research. This is not the full transcript."]
    g.id = g.id + "-export-cutoff"
    result = validate(g)
    if not result["valid"]:
        raise ValueError(f"Cutoff graph invalid: {result['errors']}")
    return g


def augment(g):
    """Represent unfinished work using the existing task + open status + propose move."""
    g = copy.deepcopy(g)
    case = get_fixture()
    quote = case["terminal_quote"]
    conv = g.conversations[0]
    assistant = next(p for p in conv.participants if p.role == "assistant")
    m = Message(id="semantic-factorization:export-end:assistant-excerpt",
                actor_id=assistant.id, ordinal=1, text=quote,
                original_id=None, timestamp=None)
    g.conversations.append(Conversation(
        id="semantic-factorization:export-end:source-slice",
        title="Final visible assistant reply — one exact excerpt",
        source_kind="curated_excerpts",
        coverage_note=("One verbatim excerpt of the last visible assistant reply from the "
                       "2026-10-18 17:49 local ChatGPT Exporter Markdown. This is a source "
                       "slice, not an additional chronological turn or a complete native export. "
                       "Original message ID unavailable."),
        participants=[assistant], messages=[m]))
    a = anchor(m, quote)
    tid = "semantic-factorization:export-end:active-comparison-task"
    g.nodes.append(Node(id=tid, anchors=[a], origin="explicit", review_status="proposed",
                        kind="task", text=case["reference"]["active_task"]))
    g.question_events.append(QuestionEvent(
        id="semantic-factorization:export-end:task-open", anchors=[a],
        origin="inferred", review_status="proposed", question_id=tid,
        status="open", actor_id=assistant.id, at_message_id=m.id, answer_ids=[]))
    g.moves.append(Move(
        id="semantic-factorization:export-end:propose", anchors=[a],
        origin="inferred", review_status="proposed", kind="propose",
        actor_id=assistant.id,
        input_ids=["semantic-factorization-2026-10-18:n:c-five-case-evaluation"],
        output_ids=[tid], at_message_id=m.id, after_move_ids=[]))
    result = validate(g)
    if not result["valid"]:
        raise ValueError(f"Augmented graph invalid: {result['errors']}")
    return g


def prepare(transcript, out):
    case = get_fixture()
    raw = Path(transcript).read_text(encoding="utf-8")
    for key in ("terminal_quote", "last_user_quote", "integrity_quote", "validation_quote"):
        if case[key] not in raw:
            raise ValueError(f"Export does not contain exact {key}")
    if "A Lean 4.30.0 public-playground run" in raw:
        raise ValueError("Export unexpectedly contains post-cutoff Lean record")
    out = Path(out)
    out.mkdir(parents=True, exist_ok=True)
    b = cutoff_graph()
    c = augment(b)
    material = {"A": raw, "B": report(b), "C": report(c)}
    for cond, content in material.items():
        (out / f"{cond}.txt").write_text(content, encoding="utf-8")
    (out / "B_cutoff_graph.json").write_text(
        b.model_dump_json(indent=2), encoding="utf-8")
    (out / "C_augmented_graph.json").write_text(
        c.model_dump_json(indent=2), encoding="utf-8")
    # This is a deterministic *retrieval* check, not a model-reader score.
    task_id = "semantic-factorization:export-end:active-comparison-task"
    bagenda = open_questions(b)
    cagenda = open_questions(c)
    checks = {
        "source_quote_matches_export": True,
        "B_has_explicit_terminal_task": any(x["id"] == task_id for x in bagenda),
        "C_has_open_terminal_task": any(x["id"] == task_id and x["status"] == "open"
                                         and x["actor_id"] == "participant:assistant"
                                         for x in cagenda),
        "B_leaks_postcutoff_Lean_in_report": "Lean 4.30.0" in material["B"],
        "C_leaks_postcutoff_Lean_in_report": "Lean 4.30.0" in material["C"],
        "B_valid": validate(b)["valid"], "C_valid": validate(c)["valid"],
        "B_open_agenda_count": len(bagenda), "C_open_agenda_count": len(cagenda),
        "reader_comparison_complete": False
    }
    (out / "structural_checks.json").write_text(
        json.dumps(checks, indent=2), encoding="utf-8")
    if checks["B_has_explicit_terminal_task"] or not checks["C_has_open_terminal_task"]:
        raise AssertionError("Terminal task retrieval control failed")
    if checks["B_leaks_postcutoff_Lean_in_report"] or checks["C_leaks_postcutoff_Lean_in_report"]:
        raise AssertionError("Temporal contamination")
    return material, checks


def independent_reader(material, out):
    """Optional real A/B/C reader. Gold key is withheld from the answer model."""
    from pydantic import BaseModel
    from llm_client import call_llm_structured, get_model

    class Answer(BaseModel):
        answer: str
        source_evidence: list[str]
        cannot_answer: bool

    outputs = {}
    for cond in ("A", "B", "C"):
        prompt = (QUESTION + "\n\nMATERIAL:\n" + material[cond])
        result, meta = call_llm_structured(
            get_model("synthesis"), [{"role": "user", "content": prompt}],
            response_model=Answer, task="synthesis", reasoning_effort="medium",
            model_policy="enforce_allowlist", max_budget=3.00,
            trace_id=f"inquiry-graph/terminal-state/20261018/{cond}")
        outputs[cond] = {
            "answer": result.model_dump(), "model": get_model("synthesis"),
            "cost": meta.cost, "tokens": meta.usage.get("total_tokens"),
            "judged": False}
    Path(out, "reader_answers.json").write_text(
        json.dumps(outputs, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--transcript", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--run-reader", action="store_true")
    args = parser.parse_args()
    material, checks = prepare(args.transcript, args.out)
    if args.run_reader:
        independent_reader(material, args.out)
    print(json.dumps(checks, indent=2))


if __name__ == "__main__":
    main()
