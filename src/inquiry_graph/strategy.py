"""Paired bounded-performance certificates for strategy selection.

This benchmark fragment treats strategy selection as a metareasoning target.
Given paired task scores for a candidate strategy and a baseline strategy, with
each score in [0, 1], the per-task difference lies in [-1, 1].

Hoeffding's inequality then yields a lower confidence bound on the expected
paired advantage:

    E[D] >= mean(D) - sqrt(2 * log(1/delta) / n)

with probability at least 1-delta, under i.i.d. benchmark-task sampling.

The certificate does not establish transfer beyond the declared task
distribution or account for unmeasured execution costs. Those remain explicit
warrant assumptions/model inputs.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, log, sqrt
from typing import Iterable


@dataclass(frozen=True)
class StrategyPerformanceCertificate:
    id: str
    strategy_id: str
    baseline_id: str
    task_class: str
    strategy_scores: tuple[float, ...]
    baseline_scores: tuple[float, ...]
    delta: float
    per_task_costs: tuple[float, ...] | None = None
    baseline_costs: tuple[float, ...] | None = None

    def __init__(
        self,
        *,
        id: str,
        strategy_id: str,
        baseline_id: str,
        task_class: str,
        strategy_scores: Iterable[float],
        baseline_scores: Iterable[float],
        delta: float,
        per_task_costs: Iterable[float] | None = None,
        baseline_costs: Iterable[float] | None = None,
    ) -> None:
        if not id:
            raise ValueError("strategy certificate id must be non-empty")
        if not strategy_id or not baseline_id:
            raise ValueError("strategy and baseline ids must be non-empty")
        if not task_class:
            raise ValueError("task class must be non-empty")
        if strategy_id == baseline_id:
            raise ValueError("strategy and baseline ids must differ")
        if not isfinite(delta) or delta <= 0.0 or delta >= 1.0:
            raise ValueError("delta must lie strictly between 0 and 1")

        strategy = tuple(strategy_scores)
        baseline = tuple(baseline_scores)
        if not strategy or len(strategy) != len(baseline):
            raise ValueError("paired score sequences must be non-empty and equal length")
        for value in (*strategy, *baseline):
            if not isfinite(value) or value < 0.0 or value > 1.0:
                raise ValueError("strategy scores must lie in [0, 1]")

        costs = tuple(per_task_costs) if per_task_costs is not None else None
        base_costs = tuple(baseline_costs) if baseline_costs is not None else None
        if (costs is None) != (base_costs is None):
            raise ValueError("candidate and baseline costs must be supplied together")
        if costs is not None:
            if len(costs) != len(strategy) or len(base_costs) != len(strategy):
                raise ValueError("cost sequences must align with paired scores")
            for value in (*costs, *base_costs):
                if not isfinite(value) or value < 0.0:
                    raise ValueError("strategy costs must be finite and non-negative")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "strategy_id", strategy_id)
        object.__setattr__(self, "baseline_id", baseline_id)
        object.__setattr__(self, "task_class", task_class)
        object.__setattr__(self, "strategy_scores", strategy)
        object.__setattr__(self, "baseline_scores", baseline)
        object.__setattr__(self, "delta", delta)
        object.__setattr__(self, "per_task_costs", costs)
        object.__setattr__(self, "baseline_costs", base_costs)

    @property
    def sample_size(self) -> int:
        return len(self.strategy_scores)

    @property
    def score_differences(self) -> tuple[float, ...]:
        return tuple(
            candidate - baseline
            for candidate, baseline in zip(
                self.strategy_scores,
                self.baseline_scores,
            )
        )

    @property
    def mean_score_advantage(self) -> float:
        return sum(self.score_differences) / self.sample_size

    @property
    def mean_cost_advantage(self) -> float:
        """Baseline cost minus candidate cost; positive means candidate is cheaper."""
        if self.per_task_costs is None or self.baseline_costs is None:
            return 0.0
        return sum(
            baseline - candidate
            for candidate, baseline in zip(
                self.per_task_costs,
                self.baseline_costs,
            )
        ) / self.sample_size

    @property
    def mean_net_advantage(self) -> float:
        return self.mean_score_advantage + self.mean_cost_advantage

    @property
    def hoeffding_radius(self) -> float:
        # Net advantage is guaranteed to lie in [-1, 1] only when no cost term
        # is supplied. Cost-aware certificates therefore report empirical net
        # advantage but do not use this confidence radius for selection.
        return sqrt(2.0 * log(1.0 / self.delta) / self.sample_size)

    @property
    def lower_score_advantage_bound(self) -> float:
        return self.mean_score_advantage - self.hoeffding_radius

    @property
    def confidence(self) -> float:
        return 1.0 - self.delta

    @property
    def has_cost_model(self) -> bool:
        return self.per_task_costs is not None
