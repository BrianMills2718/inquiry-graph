import pytest

from inquiry_graph.aba import (
    ABAAssumption,
    ABAFramework,
    ABARule,
    AssumptionPreferences,
)
from inquiry_graph.defeat import Argument, Defeat, DefeatFramework, GroundedStatus
from inquiry_graph.support import SupportAntichain
from inquiry_graph.warrant import (
    EpistemicAction,
    Guarantee,
    GroundedDialecticalWarrantRegime,
    WarrantJudgment,
)


def argument(name: str) -> Argument:
    return Argument(name, SupportAntichain.atom(name))


def judgment(
    certificate: str,
    assumptions=(),
) -> WarrantJudgment:
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


def test_grounded_in_certificate_warrants_conditionally_and_licenses_when_context_matches():
    framework = DefeatFramework([argument("cert")])
    regime = GroundedDialecticalWarrantRegime()
    claim = judgment("cert", assumptions={"instrument-calibrated"})

    assessment = regime.assess(claim, framework)
    assert assessment.warranted is True
    assert assessment.certificate_status is GroundedStatus.IN

    decision = regime.derive_license(
        assessment,
        context_assumptions={"instrument-calibrated"},
    )
    assert decision.licensed is True
    assert decision.unmet_assumptions == frozenset()


def test_warrant_and_license_remain_distinct_when_context_assumption_is_missing():
    framework = DefeatFramework([argument("cert")])
    regime = GroundedDialecticalWarrantRegime()
    claim = judgment("cert", assumptions={"instrument-calibrated"})

    assessment = regime.assess(claim, framework)
    decision = regime.derive_license(assessment, context_assumptions=())

    assert assessment.warranted is True
    assert decision.licensed is False
    assert decision.unmet_assumptions == frozenset({"instrument-calibrated"})


def test_defeated_certificate_is_not_warranted_or_licensed():
    framework = DefeatFramework(
        [argument("cert"), argument("defeater")],
        [Defeat("defeater", "cert", "rebut")],
    )
    regime = GroundedDialecticalWarrantRegime()
    decision = regime.evaluate(
        judgment("cert"),
        framework,
    )

    assert decision.assessment.certificate_status is GroundedStatus.OUT
    assert decision.assessment.warranted is False
    assert decision.licensed is False


def test_undecided_certificate_is_not_warranted_in_skeptical_grounded_regime():
    framework = DefeatFramework(
        [argument("cert"), argument("counter")],
        [
            Defeat("cert", "counter", "rebut"),
            Defeat("counter", "cert", "rebut"),
        ],
    )
    regime = GroundedDialecticalWarrantRegime()
    decision = regime.evaluate(judgment("cert"), framework)

    assert decision.assessment.certificate_status is GroundedStatus.UNDECIDED
    assert decision.assessment.warranted is False
    assert decision.licensed is False


def test_preference_filter_can_restore_certificate_warrant_and_license():
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

    certificate = next(
        arg.id
        for arg in aba.arguments()
        if arg.conclusion == "h"
    )
    claim = judgment(certificate)
    regime = GroundedDialecticalWarrantRegime()

    unfiltered = regime.evaluate(
        claim,
        aba.to_defeat_framework(),
    )
    assert unfiltered.licensed is False

    preferred = AssumptionPreferences(
        [("weak-counter", "evidence")]
    )
    filtered = regime.evaluate(
        claim,
        aba.to_preference_defeat_framework(preferred),
    )
    assert filtered.assessment.certificate_status is GroundedStatus.IN
    assert filtered.licensed is True


def test_regime_and_certificate_validation():
    framework = DefeatFramework([argument("cert")])
    regime = GroundedDialecticalWarrantRegime()

    wrong_regime = WarrantJudgment(
        regime="other",
        certificate_argument="cert",
        action=EpistemicAction("derive", "h"),
        guarantee=Guarantee("test", "test guarantee"),
    )
    with pytest.raises(ValueError, match="does not match"):
        regime.assess(wrong_regime, framework)

    with pytest.raises(ValueError, match="not present"):
        regime.assess(judgment("missing"), framework)


def test_warrant_value_object_validation():
    with pytest.raises(ValueError, match="action kind"):
        EpistemicAction("")

    with pytest.raises(ValueError, match="guarantee kind"):
        Guarantee("", "statement")

    with pytest.raises(ValueError, match="warrant regime"):
        WarrantJudgment(
            regime="",
            certificate_argument="cert",
            action=EpistemicAction("derive"),
            guarantee=Guarantee("deductive", "relative truth preservation"),
        )
