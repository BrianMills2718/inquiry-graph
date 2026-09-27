"""Experimental positive support algebra for minimal assumption environments.

This module is intentionally small and semantics-first. It models an ATMS-style
label as an antichain of finite assumption environments. Alternative support is
antichain union followed by subsumption; joint support is pairwise environment
union followed by subsumption.

The numeric helper is a reference regime over independent Bernoulli
assumptions, optionally conditioned on avoiding minimal nogoods. It computes the
probability that the symbolic support formula is satisfied. That quantity should
not be called P(h) unless a surrounding warrant regime justifies that
interpretation.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import isfinite
from typing import Iterable, Mapping

Environment = frozenset[str]


def _environment(value: Iterable[str]) -> Environment:
    return frozenset(value)


def _minimal(environments: Iterable[Iterable[str]]) -> frozenset[Environment]:
    """Return the subset-minimal environments as an antichain."""
    unique = {_environment(env) for env in environments}
    return frozenset(
        env
        for env in unique
        if not any(other < env for other in unique)
    )


@dataclass(frozen=True)
class SupportAntichain:
    """Finite antichain of subset-minimal assumption environments."""

    environments: frozenset[Environment]

    def __init__(self, environments: Iterable[Iterable[str]] = ()) -> None:
        object.__setattr__(self, "environments", _minimal(environments))

    @classmethod
    def zero(cls) -> "SupportAntichain":
        """No support routes."""
        return cls(())

    @classmethod
    def one(cls) -> "SupportAntichain":
        """Unconditional support: the empty environment."""
        return cls(((),))

    @classmethod
    def atom(cls, assumption: str) -> "SupportAntichain":
        if not assumption:
            raise ValueError("assumption must be non-empty")
        return cls(((assumption,),))

    @property
    def assumptions(self) -> frozenset[str]:
        return frozenset().union(*self.environments) if self.environments else frozenset()

    def alternative(self, other: "SupportAntichain") -> "SupportAntichain":
        """Alternative support routes (semiring addition / logical OR)."""
        return SupportAntichain(self.environments | other.environments)

    def joint(self, other: "SupportAntichain") -> "SupportAntichain":
        """Joint support (semiring multiplication / logical AND)."""
        if not self.environments or not other.environments:
            return SupportAntichain.zero()
        return SupportAntichain(
            left | right
            for left in self.environments
            for right in other.environments
        )

    def holds_in(self, assumptions: Iterable[str]) -> bool:
        """Whether at least one minimal support environment is contained in a world."""
        world = _environment(assumptions)
        return any(env <= world for env in self.environments)

    def __add__(self, other: "SupportAntichain") -> "SupportAntichain":
        return self.alternative(other)

    def __mul__(self, other: "SupportAntichain") -> "SupportAntichain":
        return self.joint(other)


@dataclass(frozen=True)
class IndependentBernoulliRegime:
    """Reference graded interpretation over independent assumption variables.

    probabilities[a] is P(a). nogoods contains minimal inconsistent
    environments; worlds containing a nogood are excluded and probabilities are
    renormalized. Exact enumeration is exponential and is intended for tests,
    examples, and small research fixtures, not large-scale inference.
    """

    probabilities: Mapping[str, float]
    nogoods: SupportAntichain = SupportAntichain.zero()

    def __post_init__(self) -> None:
        normalized = dict(self.probabilities)
        for name, probability in normalized.items():
            if not name:
                raise ValueError("assumption names must be non-empty")
            if not isfinite(probability) or probability < 0.0 or probability > 1.0:
                raise ValueError(f"invalid probability for {name!r}: {probability}")
        missing = self.nogoods.assumptions - normalized.keys()
        if missing:
            raise ValueError(f"missing probabilities for nogood assumptions: {sorted(missing)}")
        object.__setattr__(self, "probabilities", normalized)

    def support_probability(self, support: SupportAntichain) -> float:
        """Probability that the positive support formula holds, conditioned on consistency."""
        missing = support.assumptions - self.probabilities.keys()
        if missing:
            raise ValueError(f"missing probabilities for support assumptions: {sorted(missing)}")

        names = tuple(sorted(self.probabilities))
        numerator = 0.0
        denominator = 0.0

        for bits in product((False, True), repeat=len(names)):
            world = frozenset(name for name, bit in zip(names, bits) if bit)
            mass = 1.0
            for name, bit in zip(names, bits):
                p = self.probabilities[name]
                mass *= p if bit else (1.0 - p)

            if self.nogoods.holds_in(world):
                continue

            denominator += mass
            if support.holds_in(world):
                numerator += mass

        if denominator == 0.0:
            raise ValueError("consistency conditioning event has zero probability")
        return numerator / denominator
