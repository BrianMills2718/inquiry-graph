import json
from pathlib import Path

from inquiry_graph.fit_review import FitReview, summarize


def test_fit_review_example_parses_and_summarizes():
    path = (
        Path(__file__).parents[1]
        / "examples"
        / "conversations"
        / "2026-10-05-semantic-modeling"
        / "fit-review.json"
    )
    review = FitReview.model_validate(json.loads(path.read_text()))
    counts = summarize(review)
    assert review.graph_id == "semantics-2026-10-05"
    assert counts["findings"] >= 3
    assert counts["status:open"] >= 1


def test_fit_review_requires_promotion_gate():
    payload = {
        "schema_version": "1.0.0",
        "graph_id": "g",
        "purpose": "p",
        "findings": [
            {
                "id": "f",
                "diagnosis": "workflow_gap",
                "scope": "workflow",
                "description": "d",
                "evidence_refs": ["x"],
            }
        ],
        "overall_assessment": "a",
    }
    try:
        FitReview.model_validate(payload)
    except Exception:
        return
    raise AssertionError("finding without promotion_gate must be rejected")
