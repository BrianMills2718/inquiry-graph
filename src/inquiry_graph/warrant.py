"""Executable warrant/license boundary for dialectical certificates.

This module makes one narrow part of the research formalism executable:

    support/argument -> acceptability -> warrant assessment -> license

It deliberately does not execute the epistemic action itself.

The core distinction is:
- a warrant judgment is a conditional claim under applicability assumptions;
- a license is derived only when the warrant is adequate under its regime and
  the current context satisfies those assumptions.

The first executable regime is skeptical grounded acceptability over the
existing binary DefeatFramework.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .defeat import DefeatFramework, GroundedStatus


@dataclass(frozen=True)
class EpistemicAction:
    kind: str
    target: str | None = None

    def __post_init__(self) -> None:
        if not self.kind:
            raise ValueError("action kind must be non-empty")


@dataclass(frozen=True)
class Guarantee:
    kind: str
    statement: str

    def __post_init__(self) -> None:
        if not self.kind or not self.statement:
            raise ValueError("guarantee kind and statement must be non-empty")


@dataclass(frozen=True)
class WarrantJudgment:
    """Conditional warrant claim W ; A |-_{pi} a : G."""

    regime: str
    assumptions: frozenset[str]
    certificate_argument: str
    action: EpistemicAction
    guarantee: Guarantee

    def __init__(
        self,
        *,
        regime: str,
        assumptions: Iterable[str] = (),
        certificate_argument: str,
        action: EpistemicAction,
        guarantee: Guarantee,
    ) -> None:
        if not regime:
            raise ValueError("warrant regime must be non-empty")
        if not certificate_argument:
            raise ValueError("certificate argument must be non-empty")
        normalized = frozenset(assumptions)
        if any(not assumption for assumption in normalized):
            raise ValueError("warrant assumptions must be non-empty strings")

        object.__setattr__(self, "regime", regime)
        object.__setattr__(self, "assumptions", normalized)
        object.__setattr__(self, "certificate_argument", certificate_argument)
        object.__setattr__(self, "action", action)
        object.__setattr__(self, "guarantee", guarantee)


@dataclass(frozen=True)
class WarrantAssessment:
    judgment: WarrantJudgment
    warranted: bool
    certificate_status: GroundedStatus
    reason: str


@dataclass(frozen=True)
class LicenseDecision:
    assessment: WarrantAssessment
    context_assumptions: frozenset[str]
    licensed: bool
    unmet_assumptions: frozenset[str]
    reason: str


class GroundedDialecticalWarrantRegime:
    """Skeptical defeasible regime using grounded IN status as adequacy.

    This regime is intentionally narrow. Grounded acceptability is sufficient
    only for defeasible actions whose guarantee is itself dialectical
    acceptability. It does not license unconditional acceptance, deductive truth
    claims, or arbitrary actions merely because some argument is grounded-in.
    """

    id = "grounded-dialectical"
    allowed_action_kinds = frozenset(
        {
            "retain_candidate",
            "raise_support",
            "use_defeasibly",
        }
    )
    guarantee_kind = "defeasible-acceptability"

    def assess(
        self,
        judgment: WarrantJudgment,
        framework: DefeatFramework,
    ) -> WarrantAssessment:
        if judgment.regime != self.id:
            raise ValueError(
                f"judgment regime {judgment.regime!r} does not match {self.id!r}"
            )
        if judgment.certificate_argument not in framework.arguments:
            raise ValueError(
                "certificate argument is not present in the defeat framework"
            )

        status = framework.grounded_statuses()[judgment.certificate_argument]

        if judgment.action.kind not in self.allowed_action_kinds:
            warranted = False
            reason = (
                f"action kind {judgment.action.kind!r} is outside the "
                "grounded-dialectical regime"
            )
        elif judgment.guarantee.kind != self.guarantee_kind:
            warranted = False
            reason = (
                f"guarantee kind {judgment.guarantee.kind!r} is outside the "
                "grounded-dialectical regime"
            )
        elif status is GroundedStatus.IN:
            warranted = True
            reason = "typed certificate argument is grounded-in"
        elif status is GroundedStatus.OUT:
            warranted = False
            reason = "certificate argument is defeated under grounded semantics"
        else:
            warranted = False
            reason = "certificate argument is undecided under grounded semantics"

        return WarrantAssessment(
            judgment=judgment,
            warranted=warranted,
            certificate_status=status,
            reason=reason,
        )

    def derive_license(
        self,
        assessment: WarrantAssessment,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        if assessment.judgment.regime != self.id:
            raise ValueError(
                f"assessment regime {assessment.judgment.regime!r} "
                f"does not match {self.id!r}"
            )

        context = frozenset(context_assumptions)
        if any(not assumption for assumption in context):
            raise ValueError("context assumptions must be non-empty strings")

        unmet = assessment.judgment.assumptions - context
        licensed = assessment.warranted and not unmet

        if not assessment.warranted:
            reason = "conditional warrant is not adequate under the regime"
        elif unmet:
            reason = "current context does not satisfy all warrant assumptions"
        else:
            reason = "warrant is adequate and current assumptions are satisfied"

        return LicenseDecision(
            assessment=assessment,
            context_assumptions=context,
            licensed=licensed,
            unmet_assumptions=frozenset(unmet),
            reason=reason,
        )

    def evaluate(
        self,
        judgment: WarrantJudgment,
        framework: DefeatFramework,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        """Convenience composition of warrant assessment and license derivation."""
        assessment = self.assess(judgment, framework)
        return self.derive_license(assessment, context_assumptions)
