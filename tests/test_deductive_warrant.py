import pytest

from inquiry_graph.proof import (
    StrictHornProofCertificate,
    StrictHornRule,
    horn_closure,
)
from inquiry_graph.warrant import (
    EpistemicAction,
    Guarantee,
    StrictHornDeductiveWarrantRegime,
    WarrantJudgment,
)


def proof() -> StrictHornProofCertificate:
    return StrictHornProofCertificate(
        id="proof:h",
        premises={"p", "q"},
        conclusion="h",
        rules=[
            StrictHornRule("r", ("p",), id="r1"),
            StrictHornRule("h", ("r", "q"), id="r2"),
        ],
    )


def judgment(
    certificate_id: str = "proof:h",
    *,
    target: str = "h",
    assumptions=("p", "q"),
    action_kind: str = "derive",
    guarantee_kind: str = "truth-preservation-relative-to-premises",
) -> WarrantJudgment:
    return WarrantJudgment(
        regime="strict-horn-deductive",
        certificate_id=certificate_id,
        assumptions=assumptions,
        action=EpistemicAction(action_kind, target),
        guarantee=Guarantee(
            guarantee_kind,
            "conclusion is truth-preserving relative to explicit premises",
        ),
    )


def test_strict_horn_closure_and_valid_certificate():
    certificate = proof()
    assert horn_closure(certificate.premises, certificate.rules) == frozenset(
        {"p", "q", "r", "h"}
    )
    assert certificate.valid is True


def test_valid_proof_warrants_derive_relative_to_premises_and_licenses_in_context():
    certificate = proof()
    regime = StrictHornDeductiveWarrantRegime()

    assessment = regime.assess(judgment(), certificate)
    decision = regime.derive_license(
        assessment,
        context_assumptions={"p", "q"},
    )

    assert assessment.proof_valid is True
    assert assessment.warranted is True
    assert decision.licensed is True


def test_valid_proof_does_not_license_when_premises_are_not_in_current_context():
    certificate = proof()
    regime = StrictHornDeductiveWarrantRegime()

    decision = regime.evaluate(
        judgment(),
        certificate,
        context_assumptions={"p"},
    )

    assert decision.assessment.warranted is True
    assert decision.licensed is False
    assert decision.unmet_assumptions == frozenset({"q"})


def test_invalid_proof_does_not_warrant_derive():
    certificate = StrictHornProofCertificate(
        id="proof:h",
        premises={"p"},
        conclusion="h",
        rules=[StrictHornRule("q", ("p",))],
    )
    regime = StrictHornDeductiveWarrantRegime()

    assessment = regime.assess(
        judgment(assumptions={"p"}),
        certificate,
    )

    assert assessment.proof_valid is False
    assert assessment.warranted is False


def test_deductive_regime_rejects_target_and_action_scope_mismatches():
    certificate = proof()
    regime = StrictHornDeductiveWarrantRegime()

    wrong_target = regime.assess(
        judgment(target="other"),
        certificate,
    )
    assert wrong_target.warranted is False
    assert "target" in wrong_target.reason

    wrong_action = regime.assess(
        judgment(action_kind="accept"),
        certificate,
    )
    assert wrong_action.warranted is False
    assert "outside" in wrong_action.reason


def test_deductive_regime_does_not_warrant_when_judgment_omits_proof_premise():
    certificate = proof()
    regime = StrictHornDeductiveWarrantRegime()

    assessment = regime.assess(
        judgment(assumptions={"p"}),
        certificate,
    )

    assert assessment.warranted is False
    assert "omit proof premises" in assessment.reason


def test_proof_validation_rejects_bad_inputs():
    with pytest.raises(ValueError, match="certificate id"):
        StrictHornProofCertificate(id="", conclusion="h")

    with pytest.raises(ValueError, match="conclusion"):
        StrictHornProofCertificate(id="p", conclusion="")

    with pytest.raises(ValueError, match="rule head"):
        StrictHornRule("")

    with pytest.raises(ValueError, match="rule ids"):
        StrictHornProofCertificate(
            id="p",
            conclusion="h",
            rules=[
                StrictHornRule("a", id="r"),
                StrictHornRule("b", id="r"),
            ],
        )
