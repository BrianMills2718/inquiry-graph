"""Fidelity invariants for one curated conversation, not truth/coverage proofs."""
import html
import json
from pathlib import Path
import runpy

import pytest

from inquiry_graph.model import Binding, Graph, Relation
from inquiry_graph.render import report
from inquiry_graph.validate import validate
from inquiry_graph.views import open_questions, stats, trace

FIXTURE = Path(__file__).resolve().parents[1] / "examples/conversations/2026-09-30-level-one"
BUILD = runpy.run_path(str(FIXTURE / "build.py"))


@pytest.fixture
def graph():
    return BUILD["build_graph"]()


def test_native_v1_validation(graph):
    assert validate(graph) == {"valid": True, "errors": [], "warnings": []}
    assert graph.schema_version == "1.0.0"


def test_each_visible_prose_turn_has_a_source(graph):
    turns = {int(m.id.split(":t")[1][:2]) for m in graph.conversations[0].messages}
    assert turns == set(range(1, 39))
    # Turn representation is not a claim of complete transcript/token coverage.
    assert len(graph.conversations[0].messages) == 94
    assert graph.conversations[0].source_kind == "curated_excerpts"
    assert "neither a complete export" in graph.conversations[0].coverage_note


def test_sources_have_no_invented_native_ids_or_times(graph):
    assert all(m.original_id is None and m.timestamp is None
               for m in graph.conversations[0].messages)


def test_all_annotations_await_review(graph):
    assert stats(graph)["review"] == {"proposed": 302, "confirmed": 0, "rejected": 0}


def test_proceed_is_not_theory_adoption(graph):
    for event in graph.stance_events:
        if event.at_message_id == "s30:t09":
            assert event.target_id == "s30:g-proceed-one"
        if event.at_message_id == "s30:t11":
            assert event.target_id == "s30:g-proceed-two"
    forbidden = {"s30:c-commonkads-strong", "s30:c-rewrite-proposal",
                 "s30:c-assurance-fit", "s30:c-federation-proposal"}
    assert not any(e.actor_id == "s30:brian" and e.stance == "endorses"
                   and (e.target_id in forbidden or e.target_id.startswith("s30:r-"))
                   for e in graph.stance_events)


def test_fixed_space_result_is_provisional_and_reopened(graph):
    events = [e for e in graph.question_events if e.question_id == "s30:q-fixed-space"]
    assert any(e.actor_id == "s30:assistant" and e.status == "answered" for e in events)
    assert any(e.actor_id == "s30:assistant" and e.status == "reopened" for e in events)
    assert any(e.actor_id == "s30:assistant" and e.status == "answered" and e.at_message_id == "s30:t38" for e in events)
    assert not any(e.actor_id == "s30:brian" and e.status in {"answered", "resolved"} and e.at_message_id in {"s30:t31", "s30:t32"} for e in events)
    assert any(e.actor_id == "s30:brian" and e.stance == "endorses" and e.target_id == "s30:g-proceed-fixed" for e in graph.stance_events)
    assert not any(e.actor_id == "s30:brian" and e.stance == "endorses" and e.target_id in {"s30:c-three-functions", "s30:c-two-axis"} for e in graph.stance_events)


def test_canonical_question_remains_open_for_both_actors(graph):
    rows = [r for r in open_questions(graph) if r["id"] == "s30:q-canonical"]
    assert {(r["actor_id"], r["status"]) for r in rows} == {
        ("s30:brian", "reopened"), ("s30:assistant", "reopened")}
    assert not any(e.status == "resolved" for e in graph.question_events)


def test_earlier_answer_and_later_retraction_survive(graph):
    history = trace(graph, "s30:c-commonkads-strong")["linked"]
    assert any(x.get("stance") == "posits" for x in history)
    assert any(x.get("stance") == "retracts" for x in history)
    assert any(x.get("kind") == "supersedes" for x in history)
    question_history = trace(graph, "s30:q-canonical")["linked"]
    assert any(x.get("status") == "answered" for x in question_history)
    assert any(x.get("status") == "reopened" for x in question_history)


def test_deferred_is_not_erased_or_permanently_abandoned(graph):
    rows = open_questions(graph)
    for question in ("s30:q-product", "s30:q-strategy", "s30:q-representation-change"):
        assert any(r["id"] == question and r["status"] == "deferred" for r in rows)
    events = {e.id: e for e in graph.question_events}
    assert "not a user-approved permanent exclusion" in events["s30:e35"].resolution_basis
    assert "not the recursive use" in events["s30:e13"].resolution_basis


def test_rationale_is_linked_to_the_actual_revision_move(graph):
    relations = {r.id: r for r in graph.relations}
    assert [b.ref for b in relations["s30:r72"].bindings] == ["s30:g-policy", "s30:m22"]
    assert [b.ref for b in relations["s30:r73"].bindings] == ["s30:g-strategy-later", "s30:m30"]
    assert [b.ref for b in relations["s30:r74"].bindings] == ["s30:g-preserve", "s30:m08"]


def test_multiple_anchors_preserve_nonleading_rationale(graph):
    move = next(m for m in graph.moves if m.id == "s30:m27")
    assert len(move.anchors) > 1
    assert any("stances and the persuadability axis" in a.quote for a in move.anchors[1:])
    assert "stances and the persuadability axis" in json.dumps(trace(graph, move.id))


def test_builder_is_deterministic_and_native_json_roundtrips(graph):
    first = BUILD["graph_text"](graph)
    assert first == BUILD["graph_text"](BUILD["build_graph"]())
    assert Graph.model_validate_json(first) == graph


def test_bad_quote_is_rejected(graph):
    broken = graph.model_copy(deep=True)
    broken.nodes[0].anchors[0].quote = "not present in the source"
    assert any(e["code"] == "anchor_mismatch" for e in validate(broken)["errors"])


def test_actor_mismatch_is_rejected(graph):
    broken = graph.model_copy(deep=True)
    broken.stance_events[0].actor_id = "s30:brian"
    assert any(e["code"] == "event_actor" for e in validate(broken)["errors"])


def audit_probes(graph):
    """Return observed boundaries, without requiring future versions to retain gaps."""
    trial = graph.model_copy(deep=True)
    reason = next(n for n in graph.nodes if n.id == "s30:c-game-relative")
    trial.relations.append(Relation(
        id="s30:probe-event-reason", kind="motivates", anchors=reason.anchors,
        bindings=[Binding(role="reason", ref=reason.id), Binding(role="result", ref="s30:e32")]))
    event_report = validate(trial)
    move = next(m for m in graph.moves if m.id == "s30:m27")
    phrase = "stances and the persuadability axis"
    rendered = html.unescape(report(graph))
    return {
        "event_targeting": {"accepted": event_report["valid"], "errors": event_report["errors"]},
        "rationale_projection": {
            "phrase": phrase,
            "in_nonleading_move_anchor": any(phrase in a.quote for a in move.anchors[1:]),
            "in_native_trace": phrase in json.dumps(trace(graph, move.id)),
            "in_default_report": phrase in rendered,
        },
    }


def test_audit_probes_run_on_a_copy(graph):
    before = graph.model_dump_json()
    findings = audit_probes(graph)
    assert "event_targeting" in findings and "rationale_projection" in findings
    assert graph.model_dump_json() == before
    assert validate(graph)["valid"]
