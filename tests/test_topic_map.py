from __future__ import annotations

import pytest

from inquiry_graph.model import Graph
from tools.topic_map import assert_view, build_chat_view, build_overview, build_topic_view


REVISION = "sha256:test-source"


def test_topic_detail_keeps_exact_evidence_and_omits_judged_unrelated_pairs() -> None:
    positions = {
        "p1": {"id": "p1", "chat_id": "c1", "chat_title": "Chat one", "date": "2026-09-01",
               "kind": "claim", "stance": "endorses", "text": "A first extracted claim",
               "quote": "The exact source wording.", "question_status": None},
        "p2": {"id": "p2", "chat_id": "c2", "chat_title": "Chat two", "date": "2026-09-02",
               "kind": "question", "stance": "questions", "text": "A second extracted claim",
               "quote": "A second exact quote.", "question_status": "open"},
        "p3": {"id": "p3", "chat_id": "c3", "chat_title": "Chat three", "date": "2026-09-03",
               "kind": "claim", "stance": "posits", "text": "A different extracted claim",
               "quote": "A third exact quote.", "question_status": None},
    }
    links = [
        {"a": "p1", "b": "p2", "relation": "extends", "rationale": "Builds on it.", "cosine": 0.81},
        {"a": "p1", "b": "p3", "relation": "unrelated", "rationale": "Only shared terms.", "cosine": 0.62},
    ]

    view = build_topic_view(0, ["p1", "p2"], positions, links, REVISION)

    assert view["nodes"][0]["epistemic_status"] == "inferred"
    assert view["nodes"][0]["evidence"][0]["quote"] == "The exact source wording."
    assert len(view["relations"]) == 1
    assert view["relations"][0]["directed"] is False
    assert view["relations"][0]["kind"] == "extends"
    assert_view(view)


def test_topic_overview_marks_groups_interpretive_and_aggregates_link_types() -> None:
    positions = {
        "p1": {"chat_id": "c1", "chat_title": "Chat one"},
        "p2": {"chat_id": "c2", "chat_title": "Chat two"},
        "p3": {"chat_id": "c3", "chat_title": "Chat three"},
    }
    groups = [["p1", "p2"], ["p3"]]
    names = [
        {"topic": 1, "name": "Topic alpha", "summary": "A short interpretive summary."},
        {"topic": 2, "name": "Topic beta", "summary": "Another interpretive summary."},
    ]
    links = [
        {"a": "p1", "b": "p3", "relation": "agrees", "rationale": "", "cosine": 0.8},
        {"a": "p2", "b": "p3", "relation": "extends", "rationale": "", "cosine": 0.7},
        {"a": "p1", "b": "p2", "relation": "same", "rationale": "", "cosine": 0.9},
        {"a": "p2", "b": "p3", "relation": "unrelated", "rationale": "", "cosine": 0.6},
    ]

    view, topics = build_overview(groups, names, positions, links, REVISION)

    assert view["nodes"][0]["epistemic_status"] == "interpretive"
    assert len(view["relations"]) == 1
    assert view["relations"][0]["attributes"] == {
        "count_agrees": 1, "count_extends": 1, "total_links": 2,
    }
    assert topics[0]["chat_count"] == 2
    assert_view(view)


def test_conversation_view_preserves_binary_direction_and_uses_hub_for_nary_relations() -> None:
    source = Graph.model_validate({
        "id": "graph:c1",
        "conversations": [{
            "id": "c1", "title": "Conversation one", "source_kind": "normalized",
            "coverage_note": "Complete fixture.",
            "participants": [
                {"id": "user", "label": "User", "role": "user"},
                {"id": "assistant", "label": "Assistant", "role": "assistant"},
            ],
            "messages": [{
                "id": "m1", "actor_id": "user", "ordinal": 1,
                "text": "An exact sentence from the user.", "timestamp": "2026-09-01T12:00:00Z",
            }],
        }],
        "nodes": [
            {"id": "n1", "kind": "claim", "text": "Claim one", "anchors": [{"message_id": "m1", "start": 0, "end": 25, "quote": "An exact sentence from the user."}]},
            {"id": "n2", "kind": "claim", "text": "Claim two", "anchors": [{"message_id": "m1", "start": 0, "end": 25, "quote": "An exact sentence from the user."}]},
            {"id": "n3", "kind": "example", "text": "An example", "anchors": [{"message_id": "m1", "start": 0, "end": 25, "quote": "An exact sentence from the user."}]},
        ],
        "relations": [
            {"id": "r-binary", "kind": "supports", "anchors": [{"message_id": "m1", "start": 0, "end": 25, "quote": "An exact sentence from the user."}],
             "bindings": [{"role": "premise", "ref": "n3"}, {"role": "conclusion", "ref": "n1"}]},
            {"id": "r-nary", "kind": "related_to", "anchors": [{"message_id": "m1", "start": 0, "end": 25, "quote": "An exact sentence from the user."}],
             "bindings": [{"role": "source", "ref": "n1"}, {"role": "target", "ref": "n2"}, {"role": "context", "ref": "n3"}]},
        ],
        "stance_events": [{
            "id": "s1", "anchors": [{"message_id": "m1", "start": 0, "end": 25, "quote": "An exact sentence from the user."}],
            "actor_id": "user", "target_id": "n1", "stance": "endorses", "at_message_id": "m1",
        }],
    })

    view = build_chat_view(source, {
        "n1": {"chat_id": "c1", "date": "2026-09-01", "kind": "claim", "text": "Claim one",
               "stance": "endorses", "question_status": None, "quote": "An exact sentence from the user."},
        "n2": {"chat_id": "c1", "date": "2026-09-01", "kind": "claim", "text": "Claim two",
               "stance": "endorses", "question_status": None, "quote": "An exact sentence from the user."},
        "n3": {"chat_id": "c1", "date": "2026-09-01", "kind": "example", "text": "An example",
               "stance": "endorses", "question_status": None, "quote": "An exact sentence from the user."},
    }, REVISION)

    binary = [relation for relation in view["relations"] if relation["id"].startswith("role:r-binary")]
    nary = [relation for relation in view["relations"] if relation["id"].startswith("role:r-nary")]
    assert [relation["directed"] for relation in binary] == [True, True]
    assert [relation["directed"] for relation in nary] == [False, False, False]
    assert any(node["id"] == "source-relation:r-nary" for node in view["nodes"])
    assert view["nodes"][0]["evidence"][0]["quote"] == "An exact sentence from the user."
    assert_view(view)


def test_view_structure_rejects_dangling_links() -> None:
    with pytest.raises(ValueError, match="dangling"):
        assert_view({
            "graph_id": "g", "nodes": [{"id": "n1"}],
            "relations": [{"id": "r1", "source": "n1", "target": "missing"}],
        })
