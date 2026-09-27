"""Minimal defeasible-argumentation layer over positive support provenance.

The positive support algebra answers how an argument is supported. This module
answers a different question: whether an argument survives explicit defeat.

Attack construction/resolution (for example, ASPIC+ rebut/undercut/undermine
rules, preferences, ABA contraries) is intentionally external. The framework
consumes successful defeats and applies Dung-style grounded semantics.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Literal, Mapping

from .support import SupportAntichain

AttackKind = Literal["rebut", "undercut", "undermine"]


@dataclass(frozen=True)
class Argument:
    id: str
    support: SupportAntichain

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("argument id must be non-empty")


@dataclass(frozen=True)
class Defeat:
    """A successful typed attack between two arguments.

    The kind records the structured attack type that produced the defeat.
    Whether a rebut/undermine attack succeeds may depend on preferences in the
    upstream framework; undercuts may have different success conditions. This
    module does not infer success from attack kind alone.
    """

    source: str
    target: str
    kind: AttackKind

    def __post_init__(self) -> None:
        if not self.source or not self.target:
            raise ValueError("defeat endpoints must be non-empty")


class GroundedStatus(str, Enum):
    IN = "in"
    OUT = "out"
    UNDECIDED = "undecided"


class DefeatFramework:
    """Finite Dung-style defeat graph retaining structured defeat kinds."""

    def __init__(self, arguments: Iterable[Argument], defeats: Iterable[Defeat] = ()) -> None:
        items = tuple(arguments)
        by_id = {arg.id: arg for arg in items}
        if len(by_id) != len(items):
            raise ValueError("argument ids must be unique")

        edges = tuple(defeats)
        unknown = {
            endpoint
            for edge in edges
            for endpoint in (edge.source, edge.target)
            if endpoint not in by_id
        }
        if unknown:
            raise ValueError(f"unknown argument ids in defeats: {sorted(unknown)}")

        self.arguments: Mapping[str, Argument] = by_id
        self.defeats = edges

        attackers: dict[str, set[str]] = {arg_id: set() for arg_id in by_id}
        targets: dict[str, set[str]] = {arg_id: set() for arg_id in by_id}
        for edge in edges:
            attackers[edge.target].add(edge.source)
            targets[edge.source].add(edge.target)

        self._attackers = {k: frozenset(v) for k, v in attackers.items()}
        self._targets = {k: frozenset(v) for k, v in targets.items()}

    def attackers_of(self, argument_id: str) -> frozenset[str]:
        return self._attackers[argument_id]

    def targets_of(self, argument_id: str) -> frozenset[str]:
        return self._targets[argument_id]

    def characteristic(self, accepted: Iterable[str]) -> frozenset[str]:
        """Dung characteristic function F(S): arguments defended by S."""
        defenders = frozenset(accepted)
        unknown = defenders - self.arguments.keys()
        if unknown:
            raise ValueError(f"unknown accepted argument ids: {sorted(unknown)}")

        defended = set()
        for arg_id in self.arguments:
            attackers = self._attackers[arg_id]
            if all(any(attacker in self._targets[d] for d in defenders) for attacker in attackers):
                defended.add(arg_id)
        return frozenset(defended)

    def grounded_extension(self) -> frozenset[str]:
        """Least fixed point of the characteristic function."""
        current = frozenset()
        while True:
            updated = self.characteristic(current)
            if updated == current:
                return current
            current = updated

    def grounded_statuses(self) -> dict[str, GroundedStatus]:
        """IN/OUT/UNDECIDED labeling induced by the grounded extension."""
        accepted = self.grounded_extension()
        attacked_by_in = frozenset(
            target
            for source in accepted
            for target in self._targets[source]
        )

        result: dict[str, GroundedStatus] = {}
        for arg_id in self.arguments:
            if arg_id in accepted:
                result[arg_id] = GroundedStatus.IN
            elif arg_id in attacked_by_in:
                result[arg_id] = GroundedStatus.OUT
            else:
                result[arg_id] = GroundedStatus.UNDECIDED
        return result
