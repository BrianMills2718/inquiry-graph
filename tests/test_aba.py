import pytest

from inquiry_graph.aba import (
    ABAAssumption,
    ABAFramework,
    ABARule,
    AssumptionPreferences,
    translate_defeasible_rule,
)
from inquiry_graph.defeat import GroundedStatus


def test_minimal_support_argument_construction():
    framework = ABAFramework(
        rules=[
            ABARule("h", ("a", "b")),
            ABARule("h", ("c",)),
            ABARule("h", ("a", "b", "c")),
        ],
        assumptions=[
            ABAAssumption("a", "not-a"),
            ABAAssumption("b", "not-b"),
            ABAAssumption("c", "not-c"),
        ],
    )

    assert framework.support_labels()["h"].environments == frozenset(
        {
            frozenset({"a", "b"}),
            frozenset({"c"}),
        }
    )


def test_unconditional_fact_and_empty_body_rule_have_empty_environment():
    framework = ABAFramework(
        rules=[ABARule("q")],
        facts=["p"],
    )
    labels = framework.support_labels()
    assert labels["p"].environments == frozenset({frozenset()})
    assert labels["q"].environments == frozenset({frozenset()})


def test_basic_aba_attack_derives_contrary_of_target_assumption():
    framework = ABAFramework(
        rules=[
            ABARule("h", ("a",)),
            ABARule("not-a"),
        ],
        assumptions=[ABAAssumption("a", "not-a")],
    )

    attacks = framework.attacks()
    target = next(argument for argument in framework.arguments() if argument.conclusion == "h")
    source = next(argument for argument in framework.arguments() if argument.conclusion == "not-a")

    assert any(
        attack.source == source.id
        and attack.target == target.id
        and attack.attacked_assumption == "a"
        and attack.kind == "undermine"
        for attack in attacks
    )


def test_rule_undercut_translation_is_reversible():
    guard, rule = translate_defeasible_rule(
        "r1",
        "h",
        ["p"],
    )
    framework = ABAFramework(
        rules=[
            rule,
            ABARule(guard.contrary),
        ],
        assumptions=[guard],
        facts=["p"],
    )

    assert guard.role == "rule_applicability"
    assert guard.source_ref == "r1"
    assert guard.attacked_as == "undercut"
    assert rule.body == ("p", guard.name)

    h_argument = next(argument for argument in framework.arguments() if argument.conclusion == "h")
    undercut = next(
        attack
        for attack in framework.attacks()
        if attack.target == h_argument.id
    )
    assert undercut.attacked_assumption == guard.name
    assert undercut.kind == "undercut"


def test_attack_origin_can_preserve_rebut_encoding():
    guard, rule = translate_defeasible_rule(
        "r-rebut",
        "h",
        ["p"],
        role="conclusion_guard",
        attack_kind="rebut",
    )
    framework = ABAFramework(
        rules=[rule, ABARule(guard.contrary)],
        assumptions=[guard],
        facts=["p"],
    )

    assert any(attack.kind == "rebut" for attack in framework.attacks())


def test_basic_aba_projects_to_grounded_defeat_framework():
    framework = ABAFramework(
        rules=[
            ABARule("h", ("a",)),
            ABARule("not-a"),
        ],
        assumptions=[ABAAssumption("a", "not-a")],
    )

    defeat = framework.to_defeat_framework()
    statuses = defeat.grounded_statuses()

    h_id = next(argument.id for argument in framework.arguments() if argument.conclusion == "h")
    contrary_id = next(
        argument.id
        for argument in framework.arguments()
        if argument.conclusion == "not-a"
    )

    assert statuses[contrary_id] is GroundedStatus.IN
    assert statuses[h_id] is GroundedStatus.OUT


def test_cycles_without_fact_or_assumption_seed_do_not_derive():
    framework = ABAFramework(
        rules=[
            ABARule("p", ("q",)),
            ABARule("q", ("p",)),
        ]
    )
    assert framework.support_labels() == {}
    assert framework.arguments() == ()


def test_validation_rejects_duplicate_assumptions_and_rule_ids():
    with pytest.raises(ValueError, match="assumption names must be unique"):
        ABAFramework(
            assumptions=[
                ABAAssumption("a", "not-a"),
                ABAAssumption("a", "different"),
            ]
        )

    with pytest.raises(ValueError, match="rule ids must be unique"):
        ABAFramework(
            rules=[
                ABARule("p", id="r"),
                ABARule("q", id="r"),
            ]
        )


def test_translation_and_assumption_validation():
    with pytest.raises(ValueError, match="rule_id"):
        translate_defeasible_rule("", "h", ["p"])
    with pytest.raises(ValueError, match="unknown assumption role"):
        ABAAssumption("a", "not-a", role="mystery")  # type: ignore[arg-type]
    with pytest.raises(ValueError, match="unknown attack kind"):
        ABAAssumption("a", "not-a", attacked_as="mystery")  # type: ignore[arg-type]


def test_preference_filter_conservatively_extends_basic_aba_without_preferences():
    framework = ABAFramework(
        rules=[ABARule("not-b", ("a",))],
        assumptions=[
            ABAAssumption("a", "not-a"),
            ABAAssumption("b", "not-b"),
        ],
    )
    preferences = AssumptionPreferences()

    assert framework.preference_filtered_attacks(preferences) == framework.attacks()
    assert all(
        resolution.status == "defeat"
        for resolution in framework.resolve_attacks(preferences)
    )


def test_less_preferred_attacker_is_blocked():
    framework = ABAFramework(
        rules=[ABARule("not-b", ("a",))],
        assumptions=[
            ABAAssumption("a", "not-a"),
            ABAAssumption("b", "not-b"),
        ],
    )
    preferences = AssumptionPreferences([("a", "b")])

    resolutions = framework.resolve_attacks(preferences)
    relevant = next(
        resolution
        for resolution in resolutions
        if resolution.attack.attacked_assumption == "b"
    )

    assert relevant.status == "blocked"
    assert relevant.blocking_preferences == (("a", "b"),)
    assert relevant.attack not in framework.preference_filtered_attacks(preferences)


def test_incomparable_attacker_still_defeats():
    framework = ABAFramework(
        rules=[ABARule("not-b", ("a",))],
        assumptions=[
            ABAAssumption("a", "not-a"),
            ABAAssumption("b", "not-b"),
            ABAAssumption("c", "not-c"),
        ],
    )
    preferences = AssumptionPreferences([("c", "b")])

    assert framework.preference_filtered_attacks(preferences) == framework.attacks()


def test_preference_relation_is_transitively_closed_and_acyclic():
    preferences = AssumptionPreferences(
        [
            ("a", "b"),
            ("b", "c"),
        ]
    )

    assert preferences.is_less_preferred("a", "c")
    assert preferences.assumptions == frozenset({"a", "b", "c"})

    with pytest.raises(ValueError, match="acyclic"):
        AssumptionPreferences([("a", "b"), ("b", "a")])


def test_unknown_preference_assumption_is_rejected_by_framework():
    framework = ABAFramework(
        assumptions=[ABAAssumption("a", "not-a")],
    )

    with pytest.raises(ValueError, match="unknown assumptions"):
        framework.resolve_attacks(AssumptionPreferences([("a", "missing")]))


def test_preference_filter_changes_grounded_status_without_attack_reversal():
    framework = ABAFramework(
        rules=[ABARule("not-b", ("a",))],
        assumptions=[
            ABAAssumption("a", "not-a"),
            ABAAssumption("b", "not-b"),
        ],
    )
    preferences = AssumptionPreferences([("a", "b")])

    basic_status = framework.to_defeat_framework().grounded_statuses()
    filtered_status = framework.to_preference_defeat_framework(
        preferences
    ).grounded_statuses()

    b_id = next(
        argument.id
        for argument in framework.arguments()
        if argument.conclusion == "b"
    )

    assert basic_status[b_id] is GroundedStatus.OUT
    assert filtered_status[b_id] is GroundedStatus.IN


def test_rule_undercut_can_be_blocked_by_assumption_preference():
    guard, rule = translate_defeasible_rule("r1", "h", ["p"])
    attacker = ABAAssumption("weak-source", "not-weak")
    framework = ABAFramework(
        rules=[
            rule,
            ABARule(guard.contrary, ("weak-source",)),
        ],
        assumptions=[guard, attacker],
        facts=["p"],
    )
    preferences = AssumptionPreferences(
        [("weak-source", guard.name)]
    )

    undercut = next(
        resolution
        for resolution in framework.resolve_attacks(preferences)
        if resolution.attack.kind == "undercut"
    )

    assert undercut.status == "blocked"
