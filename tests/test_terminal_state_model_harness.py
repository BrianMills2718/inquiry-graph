"""Offline contract tests for the five-condition reader and blind judge.

The fake provider checks orchestration only. It MUST NOT be counted as a real
LLM response, extraction result, or continuation-accuracy score.
"""
import json
import sys
import types
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from evaluation.terminal_state.experiment import ROOT, safe_output_directory
from evaluation.terminal_state import live_trial


def test_evaluation_outputs_cannot_be_written_to_tracked_repo():
    with pytest.raises(ValueError, match="raw transcript"):
        safe_output_directory(ROOT / "evaluation" / "terminal_state" / "private_data")
    with pytest.raises(ValueError, match="raw transcript"):
        safe_output_directory(ROOT / "evaluation" / "terminal_state")
    assert safe_output_directory(ROOT / "private" / "terminal_trial") == (
        ROOT / "private" / "terminal_trial"
    ).resolve()


def test_output_outside_checkout_is_allowed(tmp_path):
    assert safe_output_directory(tmp_path) == tmp_path.resolve()


def test_five_condition_reader_and_blind_judge_contract(monkeypatch, tmp_path):
    calls = []

    def fake_get_model(purpose):
        assert purpose in ("synthesis", "judging")
        return "offline-test-fixture/" + purpose

    def fake_call(model, messages, *, response_model, **kwargs):
        calls.append({
            "model": model,
            "message": messages[0]["content"],
            "schema": response_model.__name__,
            "kwargs": kwargs,
        })
        meta = types.SimpleNamespace(cost=0.0, usage={"total_tokens": 0})
        if response_model.__name__ == "ReaderAnswer":
            return response_model.model_validate({
                "answer": "Stub only — not a research answer",
                "source_evidence": [],
                "cannot_answer": True,
            }), meta
        if response_model.__name__ == "BlindGrades":
            return response_model.model_validate({
                "grades": [
                    {
                        "label": label,
                        "points": [
                            {"point_index": idx, "covered": False,
                             "explanation": "Stub only"}
                            for idx in range(1, 7)
                        ],
                        "unsupported_claims": [],
                    } for label in "VWXYZ"
                ]
            }), meta
        raise AssertionError("Unexpected output schema")

    fake = types.ModuleType("llm_client")
    fake.get_model = fake_get_model
    fake.call_llm_structured = fake_call
    monkeypatch.setitem(sys.modules, "llm_client", fake)

    conditions = {key: f"CONDITION-{key}-ISOLATED-MATERIAL" for key in "ABECD"}
    live_trial.optional_reader(conditions, tmp_path)
    answers = json.loads((tmp_path / "reader_answers.json").read_text("utf-8"))
    assert set(answers) == set("ABECD")
    reader_calls = [x for x in calls if x["schema"] == "ReaderAnswer"]
    assert len(reader_calls) == 5
    assert all(x["model"] == "offline-test-fixture/synthesis" for x in reader_calls)
    for key in conditions:
        assert sum(conditions[key] in call["message"] for call in reader_calls) == 1
    assert all("POINTS:" not in call["message"] for call in reader_calls)

    live_trial.optional_blind_judge(tmp_path)
    grade_calls = [x for x in calls if x["schema"] == "BlindGrades"]
    assert len(grade_calls) == 1
    assert grade_calls[0]["model"] == "offline-test-fixture/judging"
    assert all(f"ANSWER {label}:" in grade_calls[0]["message"] for label in "VWXYZ")

    report = json.loads((tmp_path / "reader_grades.json").read_text("utf-8"))
    assert set(report["scores"]) == set("ABECD")
    assert set(report["blind_alias_map"]) == set("VWXYZ")
    assert set(report["blind_alias_map"].values()) == set("ABECD")
    assert all(
        len(record["points"]) == 6 and record["score"] == 0
        for record in report["scores"].values()
    )
    assert report["human_review_complete"] is False
    assert report["judge_cost"] == 0.0
