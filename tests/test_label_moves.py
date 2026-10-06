import importlib.util

import pytest
from pathlib import Path

spec = importlib.util.spec_from_file_location("label_moves", Path(__file__).resolve().parents[1] / "tools/label_moves.py")
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)


def test_vocabulary_is_the_agreed_set():
    ontology = Path(__file__).resolve().parents[1] / "docs/ontology.md"
    text = ontology.read_text()
    inhouse = [m for m in lm.MOVES if m not in {"define_by_role", "frame_as_hypothesis", "request_example", "factor_and_check", "step_back", "none_of_these"}]
    assert len(inhouse) == 15 and all(f"`{m}`" in text for m in inhouse)
    assert len(lm.MOVES) == 21 and set(lm.POLICY) == {"prior_art_first", "over_engineering_critique"}
    assert not set(lm.POLICY) & set(lm.MOVES)


def test_seed_list_has_22_unique_entries():
    assert len(set(lm.SEEDS)) == len(lm.SEEDS) == 22


def test_definitions_exclude_task_orders_and_define_by_role_is_distinct():
    assert "NOT a proposal" in lm.MOVES["propose"]
    for k in ("task order", "traceback", "give me the full code"):
        assert k in lm.MOVES["none_of_these"]
    d = lm.MOVES["define_by_role"]
    assert "Example:" in d and "Not distinguish" in d and "not reframe" in d
    assert lm.MOVES["define_by_role"] != lm.MOVES["distinguish"] != lm.MOVES["reframe"]


def test_policy_cutoff_is_stricter_than_the_pilot_default():
    assert lm.POLICY_CUTOFF >= 0.9 and 0 < lm.GATE_CUTOFF < 1 and "NO if it is a task order" in lm.GATE


def test_label_questions_are_typed_per_stage_without_network():
    pytest.importorskip("llm_client")
    rows = [{"id": "a", "text": "why not reuse X?", "prev": ""}, {"id": "b", "text": "ok", "prev": "hi"}]
    gate = lm.label_questions(rows, "gate")
    move = lm.label_questions(rows, "move")
    assert set(gate) == {"g0", "g1", "prior_art_first0", "prior_art_first1", "over_engineering_critique0", "over_engineering_critique1"}
    assert set(move) == {"m0", "m1"} and all(type(q).__name__ == "ChoiceQuestion" for q in move.values())
    assert all(type(q).__name__ == "NoulQuestion" for q in gate.values())
