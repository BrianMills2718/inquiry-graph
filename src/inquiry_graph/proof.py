"""Small checked strict-Horn proof fragment for deductive warrant benchmarks.

This module is not a universal proof assistant. It supplies one executable
deductive fragment with explicit premises, strict rules, and a deterministic
closure checker so the warrant layer can distinguish checked derivability from
mere possession of an argument-like object.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class StrictHornRule:
    head: str
    body: tuple[str, ...] = ()
    id: str | None = None

    def __post_init__(self) -> None:
        if not self.head:
            raise ValueError("rule head must be non-empty")
        if any(not premise for premise in self.body):
            raise ValueError("rule body literals must be non-empty")


def horn_closure(
    premises: Iterable[str],
    rules: Iterable[StrictHornRule],
) -> frozenset[str]:
    """Least closure of premises under finite strict Horn rules."""
    closure = set(premises)
    if any(not premise for premise in closure):
        raise ValueError("premises must be non-empty strings")

    rule_items = tuple(rules)
    explicit_ids = [rule.id for rule in rule_items if rule.id is not None]
    if len(explicit_ids) != len(set(explicit_ids)):
        raise ValueError("explicit rule ids must be unique")

    changed = True
    while changed:
        changed = False
        for rule in rule_items:
            if all(premise in closure for premise in rule.body):
                if rule.head not in closure:
                    closure.add(rule.head)
                    changed = True

    return frozenset(closure)


@dataclass(frozen=True)
class StrictHornProofCertificate:
    """Checked-certificate input for one strict-Horn derivability claim."""

    id: str
    premises: frozenset[str]
    conclusion: str
    rules: tuple[StrictHornRule, ...]

    def __init__(
        self,
        *,
        id: str,
        premises: Iterable[str] = (),
        conclusion: str,
        rules: Iterable[StrictHornRule] = (),
    ) -> None:
        if not id:
            raise ValueError("proof certificate id must be non-empty")
        if not conclusion:
            raise ValueError("proof conclusion must be non-empty")

        normalized = frozenset(premises)
        if any(not premise for premise in normalized):
            raise ValueError("proof premises must be non-empty strings")

        rule_items = tuple(rules)
        explicit_ids = [rule.id for rule in rule_items if rule.id is not None]
        if len(explicit_ids) != len(set(explicit_ids)):
            raise ValueError("explicit rule ids must be unique")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "premises", normalized)
        object.__setattr__(self, "conclusion", conclusion)
        object.__setattr__(self, "rules", rule_items)

    @property
    def closure(self) -> frozenset[str]:
        return horn_closure(self.premises, self.rules)

    @property
    def valid(self) -> bool:
        return self.conclusion in self.closure
