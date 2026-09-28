"""Executable warrant/license boundaries for typed warrant regimes.

The core distinction is:

    certificate/support -> regime-specific warrant assessment -> current license

A warrant assessment is conditional on explicit applicability assumptions.
A license is derived only when the warrant is adequate under its regime and the
current context satisfies those assumptions.

No epistemic action is executed automatically.

Two narrow regimes are currently executable:

- skeptical grounded-dialectical acceptability;
- exact reporting of an independent-Bernoulli support probability.

The second regime deliberately licenses only recording/reporting the computed
support grade. It does not turn a probability into unconditional acceptance.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .defeat import DefeatFramework, GroundedStatus
from .proof import StrictHornProofCertificate
from .support import IndependentBernoulliRegime, SupportAntichain


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
    certificate_id: str
    action: EpistemicAction
    guarantee: Guarantee

    def __init__(
        self,
        *,
        regime: str,
        assumptions: Iterable[str] = (),
        certificate_id: str | None = None,
        certificate_argument: str | None = None,
        action: EpistemicAction,
        guarantee: Guarantee,
    ) -> None:
        if not regime:
            raise ValueError("warrant regime must be non-empty")
        if certificate_id and certificate_argument and certificate_id != certificate_argument:
            raise ValueError("certificate_id and certificate_argument disagree")
        certificate = certificate_id or certificate_argument
        if not certificate:
            raise ValueError("certificate id must be non-empty")

        normalized = frozenset(assumptions)
        if any(not assumption for assumption in normalized):
            raise ValueError("warrant assumptions must be non-empty strings")

        object.__setattr__(self, "regime", regime)
        object.__setattr__(self, "assumptions", normalized)
        object.__setattr__(self, "certificate_id", certificate)
        object.__setattr__(self, "action", action)
        object.__setattr__(self, "guarantee", guarantee)

    @property
    def certificate_argument(self) -> str:
        return self.certificate_id


@dataclass(frozen=True)
class WarrantAssessment:
    judgment: WarrantJudgment
    warranted: bool
    reason: str


@dataclass(frozen=True)
class GroundedWarrantAssessment(WarrantAssessment):
    certificate_status: GroundedStatus


@dataclass(frozen=True)
class SupportProbabilityAssessment(WarrantAssessment):
    value: float


@dataclass(frozen=True)
class DeductiveProofAssessment(WarrantAssessment):
    proof_valid: bool


@dataclass(frozen=True)
class LicenseDecision:
    assessment: WarrantAssessment
    context_assumptions: frozenset[str]
    licensed: bool
    unmet_assumptions: frozenset[str]
    reason: str


def derive_license(
    assessment: WarrantAssessment,
    context_assumptions: Iterable[str] = (),
) -> LicenseDecision:
    """Derive a current license from a conditional warrant assessment."""
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


class GroundedDialecticalWarrantRegime:
    """Skeptical defeasible regime using grounded IN status as adequacy."""

    id = "grounded-dialectical"
    allowed_action_kinds = frozenset(
        {"retain_candidate", "raise_support", "use_defeasibly"}
    )
    guarantee_kind = "defeasible-acceptability"

    def assess(
        self,
        judgment: WarrantJudgment,
        framework: DefeatFramework,
    ) -> GroundedWarrantAssessment:
        if judgment.regime != self.id:
            raise ValueError(
                f"judgment regime {judgment.regime!r} does not match {self.id!r}"
            )
        if judgment.certificate_id not in framework.arguments:
            raise ValueError(
                "certificate argument is not present in the defeat framework"
            )

        status = framework.grounded_statuses()[judgment.certificate_id]

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

        return GroundedWarrantAssessment(
            judgment=judgment,
            warranted=warranted,
            certificate_status=status,
            reason=reason,
        )

    def derive_license(
        self,
        assessment: GroundedWarrantAssessment,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        if assessment.judgment.regime != self.id:
            raise ValueError(
                f"assessment regime {assessment.judgment.regime!r} "
                f"does not match {self.id!r}"
            )
        return derive_license(assessment, context_assumptions)

    def evaluate(
        self,
        judgment: WarrantJudgment,
        framework: DefeatFramework,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        return self.derive_license(
            self.assess(judgment, framework),
            context_assumptions,
        )


@dataclass(frozen=True)
class SupportProbabilityCertificate:
    id: str
    support: SupportAntichain
    model: IndependentBernoulliRegime

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("support-probability certificate id must be non-empty")


class IndependentBernoulliSupportWarrantRegime:
    """Warrant exact reporting of support probability under explicit assumptions.

    This regime licenses only recording the computed support grade. It does not
    license accepting the proposition or treating the value as P(h).
    """

    id = "independent-bernoulli-support"
    action_kind = "record_support_grade"
    guarantee_kind = "support-probability"

    def assess(
        self,
        judgment: WarrantJudgment,
        certificate: SupportProbabilityCertificate,
    ) -> SupportProbabilityAssessment:
        if judgment.regime != self.id:
            raise ValueError(
                f"judgment regime {judgment.regime!r} does not match {self.id!r}"
            )
        if judgment.certificate_id != certificate.id:
            raise ValueError(
                "warrant certificate id does not match supplied certificate"
            )

        value = certificate.model.support_probability(certificate.support)

        if judgment.action.kind != self.action_kind:
            warranted = False
            reason = (
                f"action kind {judgment.action.kind!r} is outside the "
                "independent-Bernoulli support regime"
            )
        elif judgment.guarantee.kind != self.guarantee_kind:
            warranted = False
            reason = (
                f"guarantee kind {judgment.guarantee.kind!r} is outside the "
                "independent-Bernoulli support regime"
            )
        else:
            warranted = True
            reason = (
                "support probability was computed under the explicit "
                "independent-Bernoulli model"
            )

        return SupportProbabilityAssessment(
            judgment=judgment,
            warranted=warranted,
            value=value,
            reason=reason,
        )

    def derive_license(
        self,
        assessment: SupportProbabilityAssessment,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        if assessment.judgment.regime != self.id:
            raise ValueError(
                f"assessment regime {assessment.judgment.regime!r} "
                f"does not match {self.id!r}"
            )
        return derive_license(assessment, context_assumptions)

    def evaluate(
        self,
        judgment: WarrantJudgment,
        certificate: SupportProbabilityCertificate,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        return self.derive_license(
            self.assess(judgment, certificate),
            context_assumptions,
        )

class StrictHornDeductiveWarrantRegime:
    """Checked deductive warrant for the finite strict-Horn fragment.

    A valid certificate warrants only deriving its stated conclusion relative to
    its explicit premises. It does not warrant accepting those premises.
    """

    id = "strict-horn-deductive"
    action_kind = "derive"
    guarantee_kind = "truth-preservation-relative-to-premises"

    def assess(
        self,
        judgment: WarrantJudgment,
        certificate: StrictHornProofCertificate,
    ) -> DeductiveProofAssessment:
        if judgment.regime != self.id:
            raise ValueError(
                f"judgment regime {judgment.regime!r} does not match {self.id!r}"
            )
        if judgment.certificate_id != certificate.id:
            raise ValueError(
                "warrant certificate id does not match supplied certificate"
            )

        if not certificate.premises <= judgment.assumptions:
            missing = certificate.premises - judgment.assumptions
            return DeductiveProofAssessment(
                judgment=judgment,
                warranted=False,
                proof_valid=certificate.valid,
                reason=(
                    "warrant assumptions omit proof premises: "
                    f"{sorted(missing)}"
                ),
            )

        if judgment.action.kind != self.action_kind:
            return DeductiveProofAssessment(
                judgment=judgment,
                warranted=False,
                proof_valid=certificate.valid,
                reason=(
                    f"action kind {judgment.action.kind!r} is outside the "
                    "strict-Horn deductive regime"
                ),
            )

        if judgment.action.target != certificate.conclusion:
            return DeductiveProofAssessment(
                judgment=judgment,
                warranted=False,
                proof_valid=certificate.valid,
                reason="action target does not match proof conclusion",
            )

        if judgment.guarantee.kind != self.guarantee_kind:
            return DeductiveProofAssessment(
                judgment=judgment,
                warranted=False,
                proof_valid=certificate.valid,
                reason=(
                    f"guarantee kind {judgment.guarantee.kind!r} is outside the "
                    "strict-Horn deductive regime"
                ),
            )

        if not certificate.valid:
            return DeductiveProofAssessment(
                judgment=judgment,
                warranted=False,
                proof_valid=False,
                reason="certificate conclusion is not derivable from its premises",
            )

        return DeductiveProofAssessment(
            judgment=judgment,
            warranted=True,
            proof_valid=True,
            reason=(
                "strict-Horn checker derives the target conclusion from the "
                "explicit proof premises"
            ),
        )

    def derive_license(
        self,
        assessment: DeductiveProofAssessment,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        if assessment.judgment.regime != self.id:
            raise ValueError(
                f"assessment regime {assessment.judgment.regime!r} "
                f"does not match {self.id!r}"
            )
        return derive_license(assessment, context_assumptions)

    def evaluate(
        self,
        judgment: WarrantJudgment,
        certificate: StrictHornProofCertificate,
        context_assumptions: Iterable[str] = (),
    ) -> LicenseDecision:
        return self.derive_license(
            self.assess(judgment, certificate),
            context_assumptions,
        )

