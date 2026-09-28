import math

import pytest

from inquiry_graph.statistical import FiniteClassUniformConvergenceCertificate
from inquiry_graph.warrant import (
    EpistemicAction,
    FiniteClassUniformConvergenceWarrantRegime,
    Guarantee,
    WarrantJudgment,
)


def certificate() -> FiniteClassUniformConvergenceCertificate:
    return FiniteClassUniformConvergenceCertificate(
        id="pac:h1",
        hypothesis_id="h1",
        hypothesis_count=100,
        sample_size=1000,
        empirical_loss=0.08,
        delta=0.05,
    )


def judgment(
    *,
    assumptions=("iid-sample", "loss-bounded-0-1"),
    action_kind="record_generalization_bound",
    target="h1",
    guarantee_kind="finite-class-uniform-convergence",
) -> WarrantJudgment:
    return WarrantJudgment(
        regime="finite-class-uniform-convergence",
        certificate_id="pac:h1",
        assumptions=assumptions,
        action=EpistemicAction(action_kind, target),
        guarantee=Guarantee(
            guarantee_kind,
            "true loss is at most empirical loss plus the uniform-convergence radius",
        ),
    )


def test_uniform_convergence_certificate_computes_standard_bound():
    cert = certificate()
    expected = math.sqrt(math.log((2 * 100) / 0.05) / (2 * 1000))

    assert cert.epsilon == pytest.approx(expected)
    assert cert.upper_loss_bound == pytest.approx(0.08 + expected)
    assert cert.confidence == pytest.approx(0.95)


def test_statistical_regime_warrants_recording_bound_when_typed_correctly():
    cert = certificate()
    regime = FiniteClassUniformConvergenceWarrantRegime()

    assessment = regime.assess(judgment(), cert)

    assert assessment.warranted is True
    assert assessment.empirical_loss == pytest.approx(0.08)
    assert assessment.upper_loss_bound <= 1.0
    assert assessment.confidence == pytest.approx(0.95)


def test_statistical_warrant_and_current_license_are_distinct():
    cert = certificate()
    regime = FiniteClassUniformConvergenceWarrantRegime()

    assessment = regime.assess(judgment(), cert)
    decision = regime.derive_license(
        assessment,
        context_assumptions={"iid-sample"},
    )

    assert assessment.warranted is True
    assert decision.licensed is False
    assert decision.unmet_assumptions == frozenset({"loss-bounded-0-1"})


def test_statistical_regime_does_not_license_using_predictor_or_accepting_claim():
    cert = certificate()
    regime = FiniteClassUniformConvergenceWarrantRegime()

    use_predictor = regime.assess(
        judgment(action_kind="use_predictor"),
        cert,
    )
    assert use_predictor.warranted is False

    accept = regime.assess(
        judgment(action_kind="accept", target="h1"),
        cert,
    )
    assert accept.warranted is False


def test_statistical_regime_rejects_target_and_guarantee_mismatch():
    cert = certificate()
    regime = FiniteClassUniformConvergenceWarrantRegime()

    wrong_target = regime.assess(
        judgment(target="h2"),
        cert,
    )
    assert wrong_target.warranted is False
    assert "target" in wrong_target.reason

    wrong_guarantee = regime.assess(
        judgment(guarantee_kind="pac-use-predictor"),
        cert,
    )
    assert wrong_guarantee.warranted is False
    assert "outside" in wrong_guarantee.reason


def test_uniform_convergence_certificate_validation():
    with pytest.raises(ValueError, match="hypothesis_count"):
        FiniteClassUniformConvergenceCertificate(
            id="x",
            hypothesis_id="h",
            hypothesis_count=0,
            sample_size=10,
            empirical_loss=0.1,
            delta=0.1,
        )

    with pytest.raises(ValueError, match="sample_size"):
        FiniteClassUniformConvergenceCertificate(
            id="x",
            hypothesis_id="h",
            hypothesis_count=1,
            sample_size=0,
            empirical_loss=0.1,
            delta=0.1,
        )

    with pytest.raises(ValueError, match="empirical_loss"):
        FiniteClassUniformConvergenceCertificate(
            id="x",
            hypothesis_id="h",
            hypothesis_count=1,
            sample_size=10,
            empirical_loss=1.1,
            delta=0.1,
        )

    with pytest.raises(ValueError, match="delta"):
        FiniteClassUniformConvergenceCertificate(
            id="x",
            hypothesis_id="h",
            hypothesis_count=1,
            sample_size=10,
            empirical_loss=0.1,
            delta=1.0,
        )


def test_upper_bound_is_clipped_to_one():
    cert = FiniteClassUniformConvergenceCertificate(
        id="x",
        hypothesis_id="h",
        hypothesis_count=1000,
        sample_size=1,
        empirical_loss=0.9,
        delta=0.05,
    )
    assert cert.upper_loss_bound == 1.0
