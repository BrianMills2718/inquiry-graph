from itertools import combinations

import pytest

from inquiry_graph.support import IndependentBernoulliRegime, SupportAntichain


def all_antichains(tokens=("a", "b", "c")):
    subsets = [frozenset(s) for r in range(len(tokens) + 1) for s in combinations(tokens, r)]
    seen = set()
    out = []
    for mask in range(1 << len(subsets)):
        candidate = SupportAntichain(subsets[i] for i in range(len(subsets)) if mask & (1 << i))
        if candidate.environments not in seen:
            seen.add(candidate.environments)
            out.append(candidate)
    return out


def test_two_generator_free_distributive_lattice_has_six_elements():
    assert len(all_antichains(("a", "b"))) == 6


def test_normalization_keeps_only_minimal_environments():
    support = SupportAntichain((("a",), ("a", "b"), ("b", "c"), ("a",)))
    assert support.environments == frozenset({frozenset({"a"}), frozenset({"b", "c"})})


def test_semiring_identities_absorption_and_distributivity():
    zero, one = SupportAntichain.zero(), SupportAntichain.one()
    values = all_antichains(("a", "b"))

    for x in values:
        assert x + zero == x
        assert x * one == x
        assert x + x == x
        assert x * x == x
        c = SupportAntichain.atom("c")
        assert x + (x * c) == x
        assert x * (x + c) == x

    for x in values:
        for y in values:
            assert x + y == y + x
            assert x * y == y * x
            for z in values:
                assert (x + y) + z == x + (y + z)
                assert (x * y) * z == x * (y * z)
                assert x * (y + z) == (x * y) + (x * z)


def test_alternative_and_joint_support_remain_distinct():
    a, b, c = map(SupportAntichain.atom, ("a", "b", "c"))
    support = (a * b) + c
    assert support.environments == frozenset(
        {frozenset({"a", "b"}), frozenset({"c"})}
    )
    assert support.holds_in({"a", "b"})
    assert support.holds_in({"c"})
    assert not support.holds_in({"a"})


def test_independent_probability_handles_overlapping_alternatives_without_double_counting():
    a, b = SupportAntichain.atom("a"), SupportAntichain.atom("b")
    regime = IndependentBernoulliRegime({"a": 0.5, "b": 0.5})
    assert regime.support_probability(a + b) == pytest.approx(0.75)
    assert regime.support_probability(a * b) == pytest.approx(0.25)


def test_probability_conditions_on_consistency_nogoods():
    a, b = SupportAntichain.atom("a"), SupportAntichain.atom("b")
    nogoods = a * b
    regime = IndependentBernoulliRegime({"a": 0.5, "b": 0.5}, nogoods=nogoods)
    assert regime.support_probability(a + b) == pytest.approx(2 / 3)
    assert regime.support_probability(a) == pytest.approx(1 / 3)


def test_probability_validation_and_zero_consistency_mass():
    a = SupportAntichain.atom("a")
    with pytest.raises(ValueError, match="invalid probability"):
        IndependentBernoulliRegime({"a": 1.2})
    with pytest.raises(ValueError, match="missing probabilities"):
        IndependentBernoulliRegime({}).support_probability(a)
    with pytest.raises(ValueError, match="zero probability"):
        IndependentBernoulliRegime({"a": 1.0}, nogoods=a).support_probability(a)
