"""Paired bounded-performance certificates for strategy selection.

This benchmark fragment treats strategy selection as a metareasoning target.
Given paired task utilities for a candidate strategy and a baseline strategy,
with each normalized utility in [0, 1], the per-task difference lies in [-1, 1].

Hoeffding's inequality yields a lower confidence bound on expected paired
advantage:

    E[D] >= mean(D) - sqrt(2 * log(1/delta) / n)

with probability at least 1-delta, under i.i.d. benchmark-task sampling.

Any relevant execution cost must already be represented in the declared utility
function before scores enter this certificate. The certificate does not invent a
cross-unit aggregation between quality and cost.

It also does not establish transfer beyond the declared task distribution; that
remains an explicit warrant assumption.
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
    utility_definition: str
    strategy_utilities: tuple[float, ...]
    baseline_utilities: tuple[float, ...]
    delta: float

    def __init__(
        self,
        *,
        id: str,
        strategy_id: str,
        baseline_id: str,
        task_class: str,
        utility_definition: str,
        strategy_utilities: Iterable[float],
        baseline_utilities: Iterable[float],
        delta: float,
    ) -> None:
        if not id:
            raise ValueError("strategy certificate id must be non-empty")
        if not strategy_id or not baseline_id:
            raise ValueError("strategy and baseline ids must be non-empty")
        if strategy_id == baseline_id:
            raise ValueError("strategy and baseline ids must differ")
        if not task_class:
            raise ValueError("task class must be non-empty")
        if not utility_definition:
            raise ValueError("utility definition must be non-empty")
        if not isfinite(delta) or delta <= 0.0 or delta >= 1.0:
            raise ValueError("delta must lie strictly between 0 and 1")

        strategy = tuple(strategy_utilities)
        baseline = tuple(baseline_utilities)
        if not strategy or len(strategy) != len(baseline):
            raise ValueError(
                "paired utility sequences must be non-empty and equal length"
            )
        for value in (*strategy, *baseline):
            if not isfinite(value) or value < 0.0 or value > 1.0:
                raise ValueError("strategy utilities must lie in [0, 1]")

        object.__setattr__(self, "id", id)
        object.__setattr__(self, "strategy_id", strategy_id)
        object.__setattr__(self, "baseline_id", baseline_id)
        object.__setattr__(self, "task_class", task_class)
        object.__setattr__(self, "utility_definition", utility_definition)
        object.__setattr__(self, "strategy_utilities", strategy)
        object.__setattr__(self, "baseline_utilities", baseline)
        object.__setattr__(self, "delta", delta)

    @property
    def sample_size(self) -> int:
        return len(self.strategy_utilities)

    @property
    def utility_differences(self) -> tuple[float, ...]:
        return tuple(
            candidate - baseline
            for candidate, baseline in zip(
                self.strategy_utilities,
                self.baseline_utilities,
            )
        )

    @property
    def mean_advantage(self) -> float:
        return sum(self.utility_differences) / self.sample_size

    @property
    def hoeffding_radius(self) -> float:
        # Differences lie in [-1, 1], whose range width is 2.
        return sqrt(2.0 * log(1.0 / self.delta) / self.sample_size)

    @property
    def lower_advantage_bound(self) -> float:
        return self.mean_advantage - self.hoeffding_radius

    @property
    def confidence(self) -> float:
        return 1.0 - self.delta
