import json

import pytest

from inquiry_graph.coding_session import parse_session, reply_field_candidates, session_digest
from inquiry_graph.io import ingest
from inquiry_graph.model import Graph, QuestionEvent
from inquiry_graph.validate import validate

REPLY1 = """Built the importer.

- **Session goal** — Make coding sessions searchable.
- **Active subgoals** — Current: write the importer. Other: add a topic step; check claude-mem
- **Done** — Nothing yet.
- **Need anything from human** — **Decision:** build it now?"""
REPLY2 = """Done.

- **Session goal** — Make coding sessions searchable.
- **Active subgoals** — Current: write the tests
- **Done** — Closed: write the importer (done). Closed: check claude-mem (dropped). Closed: add a topic step (replaced by cluster topics afterwards).
- **Need anything from human** — No"""


def claude_record(tmp_path):
    rows = [
        {"type": "user", "sessionId": "s1", "cwd": "/home/brian/code/demo", "timestamp": "t1",
         "message": {"content": "<system-reminder>injected</system-reminder>"}},
        {"type": "user", "timestamp": "t2", "message": {"content": "please build it"}},
        {"type": "assistant", "timestamp": "t3", "message": {"content": [{"type": "text", "text": "Starting."},
                                                                         {"type": "tool_use", "id": "x"}]}},
        {"type": "user", "timestamp": "t4", "message": {"content": [{"type": "tool_result", "content": "[main 1a2b3c4d] Add importer\n 2 files changed"}]}},
        {"type": "assistant", "isSidechain": True, "message": {"content": [{"type": "text", "text": "subagent chatter"}]}},
        {"type": "assistant", "timestamp": "t5", "message": {"content": [{"type": "text", "text": REPLY1}]}},
        {"type": "pr-link", "prUrl": "https://github.com/o/r/pull/7", "timestamp": "t6"},
        {"type": "user", "timestamp": "t7", "message": {"content": "yes"}},
        {"type": "assistant", "timestamp": "t8", "message": {"content": [{"type": "text", "text": REPLY2}]}},
    ]
    p = tmp_path / "s1.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows) + '\n{"type": "user", "trunc', encoding="utf-8")
    return p


def graph_for(path):
    conv = parse_session(path)
    return ingest(conv, reply_field_candidates(conv), method="reply-fields")


def test_claude_record_keeps_typed_text_turns_and_work_only(tmp_path):
    conv = parse_session(claude_record(tmp_path))
    assert conv.id == "claude-code:s1"
    expected = [("brian", "please build it"), ("assistant", "Starting.\n\nBuilt the importer"),
                ("tool", "[main 1a2b3c4d] Add importer"), ("tool", "https://github.com/o/r/pull/7"),
                ("brian", "yes"), ("assistant", "Done.\n\n- **Session goal")]
    # injected reminder, sidechain text and the half-written last line are gone; one assistant message per turn
    assert len(conv.messages) == len(expected)
    for m, (actor, start) in zip(conv.messages, expected):
        assert m.actor_id == f"participant:{actor}" and m.text.startswith(start)
    assert "1 unreadable record line(s) skipped" in conv.coverage_note


def test_reply_fields_give_grounded_tasks_closures_and_requests(tmp_path):
    g = graph_for(claude_record(tmp_path))
    assert validate(g)["valid"]
    digest = session_digest(g)
    assert digest["goals"] == ["Make coding sessions searchable."]
    assert digest["open"] == ["write the tests"]
    assert sorted((c["item"], c["status"]) for c in digest["closed"]) == [
        ("add a topic step", "superseded"), ("check claude-mem", "dropped"), ("write the importer", "resolved")]
    assert digest["requests_open"] == []            # Brian replied "yes" after the request
    assert digest["work"] == ["[main 1a2b3c4d] Add importer", "https://github.com/o/r/pull/7"]
    superseded = next(e for e in g.question_events if e.status == "superseded")
    assert next(n for n in g.nodes if n.id == superseded.replacement_id).text == "cluster topics afterwards"


def test_item_missing_from_last_listing_is_unknown_not_open(tmp_path):
    reply2 = REPLY2.replace("Closed: check claude-mem (dropped). ", "")
    p = claude_record(tmp_path)
    p.write_text(p.read_text(encoding="utf-8").replace(json.dumps(REPLY2)[1:-1], json.dumps(reply2)[1:-1]), encoding="utf-8")
    digest = session_digest(graph_for(p))
    assert "check claude-mem" in digest["unknown_status"] and "check claude-mem" not in digest["open"]


def test_codex_record(tmp_path):
    rows = [
        {"type": "session_meta", "timestamp": "t0", "payload": {"id": "c1", "cwd": "/home/brian/code/demo"}},
        {"type": "response_item", "timestamp": "t1", "payload": {"type": "message", "role": "user", "content": [
            {"type": "input_text", "text": "# AGENTS.md instructions\n..."}, {"type": "input_text", "text": "fix it"}]}},
        {"type": "response_item", "timestamp": "t2", "payload": {"type": "function_call_output",
                                                                  "output": "opened https://github.com/o/r/pull/9"}},
        {"type": "response_item", "timestamp": "t3", "payload": {"type": "message", "role": "assistant", "content": [
            {"type": "output_text", "text": REPLY1}]}},
    ]
    p = tmp_path / "rollout.jsonl"
    p.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    g = graph_for(p)
    assert g.conversations[0].id == "codex:c1" and validate(g)["valid"]
    digest = session_digest(g)
    assert digest["requests_open"] == ["**Decision:** build it now?"]
    assert digest["open"] == ["write the importer", "add a topic step", "check claude-mem"]
    assert digest["work"] == ["https://github.com/o/r/pull/9"]


def test_status_events_still_refuse_non_question_non_task_targets(tmp_path):
    g = graph_for(claude_record(tmp_path))
    goal = next(n for n in g.nodes if n.kind == "goal")
    ev = g.question_events[0].model_copy(update={"id": "bad", "question_id": goal.id})
    bad = Graph.model_validate({**g.model_dump(), "question_events": [*g.model_dump()["question_events"], ev.model_dump()]})
    assert any(e["code"] == "question_type" for e in validate(bad)["errors"])


def test_empty_record_fails_loudly(tmp_path):
    p = tmp_path / "empty.jsonl"
    p.write_text(json.dumps({"type": "user", "message": {"content": "<command-name>/x</command-name>"}}), encoding="utf-8")
    with pytest.raises(ValueError):
        parse_session(p)
