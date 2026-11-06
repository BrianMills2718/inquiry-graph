"""Structured sidecar for reviewing how well Inquiry Graph represented an inquiry.

This deliberately does not extend the core Graph schema. A fit review is evidence
about the representation and workflow, not automatically a new domain fact or
schema change.
"""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class FitRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


Diagnosis = Literal[
    "underfactored",
    "overfactored",
    "misfactored",
    "wrong_level",
    "hidden_coupling",
    "incomplete",
    "non_compositional",
    "capture_gap",
    "workflow_gap",
    "representation_gap",
    "no_gap",
]

Scope = Literal["ontology", "extraction", "workflow", "tooling", "documentation", "evaluation"]
Status = Literal["open", "accepted", "rejected", "resolved", "superseded"]
Severity = Literal["note", "material", "blocking"]


class FitFinding(FitRecord):
    id: str = Field(min_length=1)
    diagnosis: Diagnosis
    scope: Scope
    severity: Severity = "note"
    description: str = Field(min_length=1)
    evidence_refs: list[str] = Field(min_length=1)
    current_workaround: str | None = None
    proposed_change: str | None = None
    promotion_gate: str = Field(
        min_length=1,
        description=(
            "What additional evidence or explicit decision is required before "
            "this finding may change shared repository semantics or workflow."
        ),
    )
    status: Status = "open"


class FitReview(FitRecord):
    schema_version: Literal["1.0.0"] = "1.0.0"
    graph_id: str = Field(min_length=1)
    purpose: str = Field(min_length=1)
    findings: list[FitFinding]
    overall_assessment: str = Field(min_length=1)
    next_inquiry_question: str | None = None


def summarize(review: FitReview) -> dict[str, int]:
    """Return stable counts for lightweight checks and reporting."""
    counts: dict[str, int] = {"findings": len(review.findings)}
    for finding in review.findings:
        counts[f"diagnosis:{finding.diagnosis}"] = counts.get(
            f"diagnosis:{finding.diagnosis}", 0
        ) + 1
        counts[f"status:{finding.status}"] = counts.get(
            f"status:{finding.status}", 0
        ) + 1
    return counts
