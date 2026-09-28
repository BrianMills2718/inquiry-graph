from inquiry_graph.aba import (
    ABAAssumption,
    ABAFramework,
    ABARule,
    AssumptionPreferences,
)
from inquiry_graph.defeat import GroundedStatus
from inquiry_graph.warrant import (
    EpistemicAction,
    Guarantee,
    GroundedDialecticalWarrantRegime,
    WarrantJudgment,
)


def claim(certificate: str, assumptions=()) -> WarrantJudgment:
    return WarrantJudgment(
        regime="grounded-dialectical",
        assumptions=assumptions,
        certificate_argument=certificate,
        action=EpistemicAction("raise_support", "h"),
        guarantee=Guarantee(
            "defeasible-acceptability",
            "certificate remains acceptable under grounded semantics",
        ),
    )


def certificate_for(framework: ABAFramework, conclusion: str, support: set[str] | None = None) -> str:
    candidates = [
        argument
        for argument in framework.arguments()
        if argument.conclusion == conclusion
    ]
    if support is not None:
        candidates = [
            argument
            for argument in candidates
            if argument.environment == frozenset(support)
        ]
    assert len(candidates) == 1
    return candidates[0].id


def test_e2e_unchallenged_defeasible_support_yields_license():
    aba = ABAFramework(
        rules=[ABARule("h", ("evidence",))],
        assumptions=[ABAAssumption("evidence", "not-evidence")],
    )
    cert = certificate_for(aba, "h")
    regime = GroundedDialecticalWarrantRegime()

    decision = regime.evaluate(claim(cert), aba.to_defeat_framework())

    assert decision.assessment.certificate_status is GroundedStatus.IN
    assert decision.assessment.warranted is True
    assert decision.licensed is True


def test_e2e_successful_counterargument_removes_license():
    aba = ABAFramework(
        rules=[
            ABARule("h", ("evidence",)),
            ABARule("not-evidence", ("counter",)),
        ],
        assumptions=[
            ABAAssumption("evidence", "not-evidence"),
            ABAAssumption("counter", "not-counter"),
        ],
    )
    cert = certificate_for(aba, "h")
    regime = GroundedDialecticalWarrantRegime()

    decision = regime.evaluate(claim(cert), aba.to_defeat_framework())

    assert decision.assessment.certificate_status is GroundedStatus.OUT
    assert decision.assessment.warranted is False
    assert decision.licensed is False


def test_e2e_preference_blocks_weaker_counterargument_and_restores_license():
    aba = ABAFramework(
        rules=[
            ABARule("h", ("evidence",)),
            ABARule("not-evidence", ("weak-counter",)),
        ],
        assumptions=[
            ABAAssumption("evidence", "not-evidence"),
            ABAAssumption("weak-counter", "not-weak-counter"),
        ],
    )
    cert = certificate_for(aba, "h")
    regime = GroundedDialecticalWarrantRegime()

    unfiltered = regime.evaluate(claim(cert), aba.to_defeat_framework())
    assert unfiltered.licensed is False

    preferences = AssumptionPreferences([("weak-counter", "evidence")])
    filtered = regime.evaluate(
        claim(cert),
        aba.to_preference_defeat_framework(preferences),
    )

    assert filtered.assessment.certificate_status is GroundedStatus.IN
    assert filtered.licensed is True


def test_e2e_context_failure_blocks_license_without_erasing_conditional_warrant():
    aba = ABAFramework(
        rules=[ABARule("h", ("evidence",))],
        assumptions=[ABAAssumption("evidence", "not-evidence")],
    )
    cert = certificate_for(aba, "h")
    regime = GroundedDialecticalWarrantRegime()

    decision = regime.evaluate(
        claim(cert, assumptions={"sensor-calibrated"}),
        aba.to_defeat_framework(),
        context_assumptions=(),
    )

    assert decision.assessment.warranted is True
    assert decision.licensed is False
    assert decision.unmet_assumptions == frozenset({"sensor-calibrated"})


def test_e2e_alternative_support_survives_when_one_route_is_defeated():
    aba = ABAFramework(
        rules=[
            ABARule("h", ("e1",)),
            ABARule("h", ("e2",)),
            ABARule("not-e1", ("counter",)),
        ],
        assumptions=[
            ABAAssumption("e1", "not-e1"),
            ABAAssumption("e2", "not-e2"),
            ABAAssumption("counter", "not-counter"),
        ],
    )
    regime = GroundedDialecticalWarrantRegime()

    cert_e1 = certificate_for(aba, "h", {"e1"})
    cert_e2 = certificate_for(aba, "h", {"e2"})
    defeat = aba.to_defeat_framework()

    first = regime.evaluate(claim(cert_e1), defeat)
    second = regime.evaluate(claim(cert_e2), defeat)

    assert first.assessment.certificate_status is GroundedStatus.OUT
    assert first.licensed is False
    assert second.assessment.certificate_status is GroundedStatus.IN
    assert second.licensed is True


def test_e2e_preference_changes_license_without_changing_positive_support():
    aba = ABAFramework(
        rules=[
            ABARule("h", ("evidence",)),
            ABARule("not-evidence", ("weak-counter",)),
        ],
        assumptions=[
            ABAAssumption("evidence", "not-evidence"),
            ABAAssumption("weak-counter", "not-weak-counter"),
        ],
    )
    before_labels = aba.support_labels()
    cert = certificate_for(aba, "h")
    regime = GroundedDialecticalWarrantRegime()

    preferences = AssumptionPreferences([("weak-counter", "evidence")])
    decision = regime.evaluate(
        claim(cert),
        aba.to_preference_defeat_framework(preferences),
    )
    after_labels = aba.support_labels()

    assert before_labels == after_labels
    assert decision.licensed is True
