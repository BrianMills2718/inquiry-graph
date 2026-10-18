"""Regression controls for continuation-state preservation, using no external LLM."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from inquiry_graph.validate import validate
from inquiry_graph.views import open_questions
from inquiry_graph.render import report
from evaluation.terminal_state.experiment import cutoff_graph, augment, get_fixture, prepare


def test_cutoff_has_no_post_export_research():
    g = cutoff_graph()
    assert validate(g)["valid"], validate(g)["errors"]
    assert len(g.conversations) == 1
    assert g.conversations[0].messages[-1].id.endswith(":a13")
    all_messages = " ".join(m.text for c in g.conversations for m in c.messages)
    assert "A Lean 4.30.0 public-playground run" not in all_messages
    assert "Z3 5.3.1.0 was downloaded" not in all_messages
    assert "I’m now turning these findings into explicit scenario-by-scenario judgments" not in all_messages


def test_existing_schema_encodes_terminal_activity_and_projects_it():
    b = cutoff_graph()
    c = augment(b)
    assert validate(c)["valid"], validate(c)["errors"]
    expected = get_fixture()["reference"]["active_task"]
    assert all(row["text"] != expected for row in open_questions(b))
    candidates = [row for row in open_questions(c) if row["text"] == expected]
    assert len(candidates) == 1
    assert candidates[0]["status"] == "open"
    assert candidates[0]["actor_id"] == "participant:assistant"
    assert expected in report(c)
    # The original source excerpt was not silently converted into a new factual
    # claim about the user's beliefs or a completed task.
    assert not any(e.stance == "endorses" and e.target_id == candidates[0]["id"]
                   for e in c.stance_events)


def test_terminal_quote_is_exactly_anchored():
    c = augment(cutoff_graph())
    task = next(n for n in c.nodes if n.id.endswith("active-comparison-task"))
    excerpt = c.conversations[-1].messages[0]
    quote = get_fixture()["terminal_quote"]
    assert excerpt.text == quote
    assert task.anchors[0].quote == quote
    assert excerpt.text[task.anchors[0].start:task.anchors[0].end] == quote


def test_prepare_materials_are_cutoff_safe(tmp_path):
    case = get_fixture()
    # This synthetic input tests anchoring/control logic; it is NOT an A/B/C
    # reader evaluation and cannot establish real transcript performance.
    fake_source = "\n\n".join(case[k] for k in
                              ("last_user_quote", "validation_quote",
                               "integrity_quote", "terminal_quote"))
    source = tmp_path / "source.md"
    source.write_text(fake_source, encoding="utf-8")
    material, checks = prepare(source, tmp_path / "out")
    assert set(material) == {"A", "B", "C"}
    assert checks["source_quote_matches_export"]
    assert checks["B_valid"] and checks["C_valid"]
    assert not checks["B_has_explicit_terminal_task"]
    assert checks["C_has_open_terminal_task"]
    assert not checks["B_leaks_postcutoff_Lean_in_report"]
    assert not checks["C_leaks_postcutoff_Lean_in_report"]
    assert not checks["reader_comparison_complete"]
    assert (tmp_path / "out" / "structural_checks.json").exists()
