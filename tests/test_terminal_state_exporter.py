"""Importer fidelity and terminal-state diagnostic; no external model calls."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pytest

from inquiry_graph.model import Graph, Node, QuestionEvent, anchor
from evaluation.terminal_state.live_trial import import_visible_export, terminal_detection


SYNTHETIC = """# Example transcript

**Exported:** 10/18/2026 17:49:13

## Prompt:
10/18/2026, 4:20:52 PM

What should we compare?

## Response:
10/18/2026, 4:20:54 PM · gpt-6

Compare existing frameworks using five cases.

## Prompt:
10/18/2026, 5:12:24 PM

Proceed.

## Response:
10/18/2026, 5:12:27 PM · gpt-6

I am still making scenario-by-scenario judgments.

---
Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)
"""


def test_exporter_markdown_import_preserves_typed_visible_response():
    conv, meta = import_visible_export(SYNTHETIC)
    assert meta["visible_messages"] == 4
    assert meta["visible_user_turns"] == 2
    assert meta["visible_assistant_turns"] == 2
    assert meta["displayed_times"][-1]["displayed_time"] == "10/18/2026, 5:12:27 PM"
    assert conv.title == "Example transcript"
    assert [m.actor_id for m in conv.messages] == [
        "participant:user", "participant:assistant",
        "participant:user", "participant:assistant"
    ]
    assert conv.messages[-1].text == "I am still making scenario-by-scenario judgments."
    assert all(m.original_id is None and m.timestamp is None for m in conv.messages)
    assert conv.messages[-1].ordinal == 4


def test_exporter_parser_rejects_imbalanced_headings():
    s = SYNTHETIC.replace("## Response:\n10/18/2026, 4:20:54 PM", 
                          "## Prompt:\n10/18/2026, 4:20:54 PM")
    with pytest.raises(ValueError, match="alternating"):
        import_visible_export(s)
    with pytest.raises(ValueError, match="uneven"):
        import_visible_export(SYNTHETIC.rsplit("## Response:", 1)[0])


def test_diagnostic_recovers_last_response_task_not_user_stance():
    conv, _ = import_visible_export(SYNTHETIC)
    msg = conv.messages[-1]
    a = anchor(msg, msg.text)
    task = Node(id="t", kind="task",
                text="Finish the scenario-by-scenario framework comparison.",
                anchors=[a])
    event = QuestionEvent(id="e", question_id="t", status="open",
                          actor_id=msg.actor_id, at_message_id=msg.id, anchors=[a])
    graph = Graph(id="g", conversations=[conv], nodes=[task],
                  question_events=[event])
    checks = terminal_detection(graph, msg)
    assert checks["structurally_valid"]
    assert checks["terminal_comparative_task_detected"]
    assert checks["terminal_source_open_status_events"] == ["e"]
    assert checks["only_structural_evidence"] is True


def test_terminal_activity_requires_explicit_open_status_not_keyword_only():
    conv, _ = import_visible_export(SYNTHETIC)
    msg = conv.messages[-1]
    task = Node(
        id="t", kind="task",
        text="Finish the scenario-by-scenario framework comparison.",
        anchors=[anchor(msg, msg.text)]
    )
    without_status = Graph(id="missing-open-status", conversations=[conv], nodes=[task])
    verdict = terminal_detection(without_status, msg)
    assert verdict["structurally_valid"]
    assert verdict["terminal_source_tasks"] == ["t"]
    assert verdict["terminal_source_open_status_events"] == []
    assert verdict["terminal_comparative_task_detected"] is False
