import pytest

from inquiry_graph.defeat import Argument, Defeat, DefeatFramework, GroundedStatus
from inquiry_graph.support import SupportAntichain


def arg(name: str) -> Argument:
    return Argument(name, SupportAntichain.atom(name))


def test_unattacked_arguments_are_grounded_in():
    framework = DefeatFramework([arg("a"), arg("b")])
    assert framework.grounded_extension() == frozenset({"a", "b"})


def test_simple_defeat_marks_target_out():
    framework = DefeatFramework(
        [arg("a"), arg("b")],
        [Defeat("a", "b", "rebut")],
    )
    assert framework.grounded_extension() == frozenset({"a"})
    assert framework.grounded_statuses() == {
        "a": GroundedStatus.IN,
        "b": GroundedStatus.OUT,
    }


def test_defence_restores_argument():
    framework = DefeatFramework(
        [arg("a"), arg("b"), arg("c")],
        [
            Defeat("b", "a", "undermine"),
            Defeat("c", "b", "rebut"),
        ],
    )
    assert framework.grounded_extension() == frozenset({"a", "c"})


def test_mutual_defeat_is_undecided_under_grounded_semantics():
    framework = DefeatFramework(
        [arg("a"), arg("b")],
        [
            Defeat("a", "b", "rebut"),
            Defeat("b", "a", "rebut"),
        ],
    )
    assert framework.grounded_extension() == frozenset()
    assert framework.grounded_statuses() == {
        "a": GroundedStatus.UNDECIDED,
        "b": GroundedStatus.UNDECIDED,
    }


def test_self_defeat_is_not_grounded_in():
    framework = DefeatFramework([arg("a")], [Defeat("a", "a", "undercut")])
    assert framework.grounded_extension() == frozenset()
    assert framework.grounded_statuses()["a"] is GroundedStatus.UNDECIDED


def test_typed_defeat_kind_is_retained_but_not_interpreted_as_preference():
    edge = Defeat("a", "b", "undercut")
    framework = DefeatFramework([arg("a"), arg("b")], [edge])
    assert framework.defeats[0].kind == "undercut"
    assert framework.grounded_extension() == frozenset({"a"})


def test_validation_rejects_duplicates_unknown_ids_and_bad_endpoints():
    with pytest.raises(ValueError, match="unique"):
        DefeatFramework([arg("a"), arg("a")])
    with pytest.raises(ValueError, match="unknown argument"):
        DefeatFramework([arg("a")], [Defeat("a", "b", "rebut")])
    with pytest.raises(ValueError, match="non-empty"):
        Defeat("", "a", "rebut")


def test_characteristic_rejects_unknown_seed():
    framework = DefeatFramework([arg("a")])
    with pytest.raises(ValueError, match="unknown accepted"):
        framework.characteristic({"missing"})
