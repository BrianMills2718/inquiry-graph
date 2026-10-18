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
    assert set(material) == {"A", "B", "C", "E"}
    assert checks["source_quote_matches_export"]
    assert checks["B_valid"] and checks["C_valid"]
    assert not checks["B_has_explicit_terminal_task"]
    assert checks["C_has_open_terminal_task"]
    assert checks["E_has_exact_terminal_quote"]
    assert checks["C_has_exact_terminal_quote"]
    assert checks["E_adds_no_semantic_task_record"]
    assert case["terminal_quote"] in material["C"]
    assert case["terminal_quote"] in material["E"]
    assert material["E"].split("## Supplementary primary-source excerpt")[0] == material["B"]
    assert material["C"].split("## Supplementary primary-source excerpt")[1] == material["E"].split("## Supplementary primary-source excerpt")[1]
    assert case["reference"]["active_task"] not in material["E"]
    assert case["reference"]["active_task"] in material["C"]
    assert not checks["B_leaks_postcutoff_Lean_in_report"]
    assert not checks["C_leaks_postcutoff_Lean_in_report"]
    assert not checks["reader_comparison_complete"]
    assert (tmp_path / "out" / "structural_checks.json").exists()


def test_current_canonical_graph_exposes_source_grounded_terminal_tasks():
    from inquiry_graph.model import Graph
    from inquiry_graph.views import open_questions
    from inquiry_graph.validate import validate
    from evaluation.terminal_state.experiment import GRAPH

    canonical = Graph.model_validate_json(GRAPH.read_text(encoding="utf-8"))
    assert validate(canonical)["valid"], validate(canonical)["errors"]
    slices = [c for c in canonical.conversations if c.id.endswith(":terminal:source-slices")]
    assert len(slices) == 1
    excerpts = slices[0].messages
    assert len(excerpts) == 2
    case = get_fixture()
    assert excerpts[0].text == case["integrity_quote"]
    assert excerpts[1].text == case["terminal_quote"]
    for m in excerpts:
        assert m.original_id is None and m.timestamp is None
        assert m.actor_id == "participant:assistant"

    agenda = open_questions(canonical)
    tasks = {row["id"]: row for row in agenda if row["id"].startswith("semantic-factorization-2026-10-18:terminal:")}
    assert len(tasks) == 2
    for row in tasks.values():
        assert row["status"] == "open"
        assert row["review_status"] == "proposed"
        assert row["actor_id"] == "participant:assistant"
        assert row["anchors"][0]["quote"] in {case["integrity_quote"], case["terminal_quote"]}
    texts = [row["text"] for row in tasks.values()]
    assert any("five-case" in t and "source-supported" in t for t in texts)
    assert any("relation-role signatures" in t for t in texts)

    # Historical control B still suppresses corrected source excerpts and later
    # proofs; C alone adds the exact final-response evidence.
    baseline = cutoff_graph()
    assert len(baseline.conversations) == 1
    assert not any(n.id in tasks for n in baseline.nodes)
