"""Small Assumption-Based Argumentation bridge over minimal support provenance.

This module implements the deliberately small ABA core selected by the
ABA/ASPIC+ benchmark:

- finite Horn-style rules;
- defeasible assumptions with explicit contraries;
- minimal-support argument construction;
- attacks induced by deriving assumption contraries;
- reversible metadata for generated assumptions;
- projection of basic-ABA attacks to the downstream Dung defeat framework.

Basic ABA has no preference-sensitive attack-to-defeat filter, so every ABA
attack projects to a defeat. ABA+/ASPIC+-style preferences remain an upstream
extension point.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Literal, Mapping

from .defeat import AttackKind, Argument as DefeatArgument, Defeat, DefeatFramework
from .support import Environment, SupportAntichain

AssumptionRole = Literal[
    "ordinary",
    "rule_applicability",
    "preference_guard",
    "conclusion_guard",
]


@dataclass(frozen=True)
class ABAAssumption:
    name: str
    contrary: str
    role: AssumptionRole = "ordinary"
    source_ref: str | None = None
    attacked_as: AttackKind = "undermine"

    def __post_init__(self) -> None:
        if not self.name or not self.contrary:
            raise ValueError("assumption name and contrary must be non-empty")
        if self.role not in {
            "ordinary",
            "rule_applicability",
            "preference_guard",
            "conclusion_guard",
        }:
            raise ValueError(f"unknown assumption role: {self.role!r}")
        if self.attacked_as not in {"rebut", "undercut", "undermine"}:
            raise ValueError(f"unknown attack kind: {self.attacked_as!r}")


@dataclass(frozen=True)
class ABARule:
    head: str
    body: tuple[str, ...] = ()
    id: str | None = None

    def __post_init__(self) -> None:
        if not self.head:
            raise ValueError("rule head must be non-empty")
        if any(not item for item in self.body):
            raise ValueError("rule body literals must be non-empty")


@dataclass(frozen=True)
class ABAArgument:
    conclusion: str
    environment: Environment

    @property
    def id(self) -> str:
        encoded = ",".join(sorted(self.environment))
        return f"{self.conclusion} <- [{encoded}]"

    @property
    def support(self) -> SupportAntichain:
        return SupportAntichain((self.environment,))


@dataclass(frozen=True)
class ABAAttack:
    source: str
    target: str
    attacked_assumption: str
    kind: AttackKind


class ABAFramework:
    """Finite basic-ABA framework with minimal-environment construction."""

    def __init__(
        self,
        rules: Iterable[ABARule] = (),
        assumptions: Iterable[ABAAssumption] = (),
        facts: Iterable[str] = (),
    ) -> None:
        rule_items = tuple(rules)
        assumption_items = tuple(assumptions)
        fact_items = frozenset(facts)

        if any(not fact for fact in fact_items):
            raise ValueError("facts must be non-empty")

        by_name = {assumption.name: assumption for assumption in assumption_items}
        if len(by_name) != len(assumption_items):
            raise ValueError("assumption names must be unique")

        explicit_rule_ids = [rule.id for rule in rule_items if rule.id is not None]
        if len(explicit_rule_ids) != len(set(explicit_rule_ids)):
            raise ValueError("explicit rule ids must be unique")

        self.rules = rule_items
        self.assumptions: Mapping[str, ABAAssumption] = by_name
        self.facts = fact_items

    def support_labels(self) -> dict[str, SupportAntichain]:
        """Least Horn closure, annotated by subset-minimal assumption supports."""
        labels: dict[str, SupportAntichain] = {
            fact: SupportAntichain.one() for fact in self.facts
        }

        for assumption in self.assumptions.values():
            prior = labels.get(assumption.name, SupportAntichain.zero())
            labels[assumption.name] = prior + SupportAntichain.atom(assumption.name)

        changed = True
        while changed:
            changed = False
            for rule in self.rules:
                support = SupportAntichain.one()
                for premise in rule.body:
                    support = support * labels.get(premise, SupportAntichain.zero())
                    if not support.environments:
                        break

                if not support.environments:
                    continue

                prior = labels.get(rule.head, SupportAntichain.zero())
                updated = prior + support
                if updated != prior:
                    labels[rule.head] = updated
                    changed = True

        return labels

    def arguments(self) -> tuple[ABAArgument, ...]:
        """One argument per conclusion/minimal supporting environment."""
        labels = self.support_labels()
        result: list[ABAArgument] = []

        for conclusion in sorted(labels):
            environments = sorted(
                labels[conclusion].environments,
                key=lambda env: (len(env), tuple(sorted(env))),
            )
            result.extend(
                ABAArgument(conclusion=conclusion, environment=environment)
                for environment in environments
            )

        return tuple(result)

    def attacks(self) -> tuple[ABAAttack, ...]:
        """Construct basic-ABA attacks from conclusions that are contraries."""
        arguments = self.arguments()
        result: list[ABAAttack] = []

        for source in arguments:
            for target in arguments:
                for assumption_name in sorted(target.environment):
                    assumption = self.assumptions[assumption_name]
                    if source.conclusion == assumption.contrary:
                        result.append(
                            ABAAttack(
                                source=source.id,
                                target=target.id,
                                attacked_assumption=assumption_name,
                                kind=assumption.attacked_as,
                            )
                        )

        return tuple(result)

    def to_defeat_framework(self) -> DefeatFramework:
        """Project basic-ABA attacks to successful defeats for Dung semantics."""
        arguments = self.arguments()
        defeat_arguments = tuple(
            DefeatArgument(id=argument.id, support=argument.support)
            for argument in arguments
        )
        defeats = tuple(
            Defeat(source=attack.source, target=attack.target, kind=attack.kind)
            for attack in self.attacks()
        )
        return DefeatFramework(defeat_arguments, defeats)


def translate_defeasible_rule(
    rule_id: str,
    head: str,
    body: Iterable[str],
    *,
    assumption_name: str | None = None,
    contrary: str | None = None,
    role: AssumptionRole = "rule_applicability",
    attack_kind: AttackKind = "undercut",
) -> tuple[ABAAssumption, ABARule]:
    """Compile a defeasible rule to a strict rule guarded by an ABA assumption.

    The generated assumption retains reversible provenance to the source rule and
    an ASPIC+-compatible attack-origin kind.
    """
    if not rule_id:
        raise ValueError("rule_id must be non-empty")

    guard = assumption_name or f"applicable:{rule_id}"
    guard_contrary = contrary or f"not:{guard}"

    assumption = ABAAssumption(
        name=guard,
        contrary=guard_contrary,
        role=role,
        source_ref=rule_id,
        attacked_as=attack_kind,
    )
    rule = ABARule(
        id=rule_id,
        head=head,
        body=tuple(body) + (guard,),
    )
    return assumption, rule
