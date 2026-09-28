import math

import pytest

from inquiry_graph.strategy import StrategyPerformanceCertificate
from inquiry_graph.warrant import (
    EpistemicAction,
    Guarantee,
    StrategyPerformanceWarrantRegime,
    WarrantJudgment,
)


def certificate(
    strategy_utilities,
    baseline_utilities,
    *,
    delta=0.05,
) -> StrategyPerformanceCertificate:
    return StrategyPerformanceCertificate(
        id="strategy:canonical-factorization",
        strategy_id="canonical-factorization",
        baseline_id="baseline-search",
        task_class="factorization-benchmarks",
        utility_definition="normalized task utility including declared reasoning cost",
        strategy_utilities=strategy_utilities,
        baseline_utilities=baseline_utilities,
        delta=delta,
    )


def judgment(
    *,
    assumptions=(
        "iid-benchmark-tasks",
        "stable-task-distribution",
        "utility-definition-valid",
    ),
    action_kind="select_strategy",
    target="canonical-factorization",
    guarantee_kind="positive-expected-utility-advantage",
) -> WarrantJudgment:
    return WarrantJudgment(
        regime="strategy-performance",
        certificate_id="strategy:canonical-factorization",
        assumptions=assumptions,
        action=EpistemicAction(action_kind, target),
        guarantee=Guarantee(
            guarantee_kind,
            "candidate strategy has positive expected utility advantage over baseline",
        ),
    )


def test_strategy_certificate_computes_paired_advantage_bound():
    cert = certificate(
        [0.9] * 100,
        [0.5] * 100,
        delta=0.05,
    )
    expected_radius = math.sqrt(2 * math.log(1 / 0.05) / 100)

    assert cert.mean_advantage == pytest.approx(0.4)
    assert cert.hoeffding_radius == pytest.approx(expected_radius)
    assert cert.lower_advantage_bound == pytest.approx(0.4 - expected_radius)
    assert cert.confidence == pytest.approx(0.95)


def test_positive_lower_bound_can_warrant_strategy_selection():
    cert = certificate(
        [1.0] * 500,
        [0.5] * 500,
    )
    regime = StrategyPerformanceWarrantRegime()

    assessment = regime.assess(judgment(), cert)

    assert assessment.lower_advantage_bound > 0
    assert assessment.warranted is True
    assert assessment.task_class == "factorization-benchmarks"
    assert assessment.baseline_id == "baseline-search"


def test_nonpositive_lower_bound_does_not_warrant_selection():
    cert = certificate(
        [0.7] * 20,
        [0.6] * 20,
    )
    regime = StrategyPerformanceWarrantRegime()

    assessment = regime.assess(judgment(), cert)

    assert assessment.lower_advantage_bound <= 0
    assert assessment.warranted is False


def test_strategy_warrant_still_requires_context_assumptions_for_license():
    cert = certificate(
        [1.0] * 500,
        [0.5] * 500,
    )
    regime = StrategyPerformanceWarrantRegime()

    assessment = regime.assess(judgment(), cert)
    decision = regime.derive_license(
        assessment,
        context_assumptions={
            "iid-benchmark-tasks",
            "utility-definition-valid",
        },
    )

    assert assessment.warranted is True
    assert decision.licensed is False
    assert decision.unmet_assumptions == frozenset(
        {"stable-task-distribution"}
    )


def test_strategy_regime_rejects_wrong_action_target_or_guarantee():
    cert = certificate(
        [1.0] * 500,
        [0.5] * 500,
    )
    regime = StrategyPerformanceWarrantRegime()

    wrong_action = regime.assess(
        judgment(action_kind="record_strategy_score"),
        cert,
    )
    assert wrong_action.warranted is False

    wrong_target = regime.assess(
        judgment(target="other"),
        cert,
    )
    assert wrong_target.warranted is False

    wrong_guarantee = regime.assess(
        judgment(guarantee_kind="generic-performance"),
        cert,
    )
    assert wrong_guarantee.warranted is False


def test_strategy_certificate_validation():
    with pytest.raises(ValueError, match="must differ"):
        StrategyPerformanceCertificate(
            id="x",
            strategy_id="same",
            baseline_id="same",
            task_class="tasks",
            utility_definition="u",
            strategy_utilities=[0.5],
            baseline_utilities=[0.4],
            delta=0.05,
        )

    with pytest.raises(ValueError, match="equal length"):
        StrategyPerformanceCertificate(
            id="x",
            strategy_id="s",
            baseline_id="b",
            task_class="tasks",
            utility_definition="u",
            strategy_utilities=[0.5, 0.6],
            baseline_utilities=[0.4],
            delta=0.05,
        )

    with pytest.raises(ValueError, match="utilities"):
        StrategyPerformanceCertificate(
            id="x",
            strategy_id="s",
            baseline_id="b",
            task_class="tasks",
            utility_definition="u",
            strategy_utilities=[1.2],
            baseline_utilities=[0.4],
            delta=0.05,
        )
