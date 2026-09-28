"""Finite-class uniform-convergence certificates for statistical warrant.

This benchmark fragment implements the standard Hoeffding + union-bound result
for a finite hypothesis class and losses in [0, 1]:

    with probability at least 1-delta, simultaneously for all h in H,

        L_D(h) <= L_S(h) + sqrt(log(2|H|/delta) / (2m)).

The certificate records the theorem inputs for one selected hypothesis. It does
not infer that samples were actually i.i.d. or that the deployed distribution
matches the sampling distribution; those remain explicit warrant assumptions.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, log, sqrt


@dataclass(frozen=True)
class FiniteClassUniformConvergenceCertificate:
    id: str
    hypothesis_id: str
    hypothesis_count: int
    sample_size: int
    empirical_loss: float
    delta: float

    def __post_init__(self) -> None:
        if not self.id:
            raise ValueError("statistical certificate id must be non-empty")
        if not self.hypothesis_id:
            raise ValueError("hypothesis id must be non-empty")
        if self.hypothesis_count < 1:
            raise ValueError("hypothesis_count must be at least 1")
        if self.sample_size < 1:
            raise ValueError("sample_size must be at least 1")
        if (
            not isfinite(self.empirical_loss)
            or self.empirical_loss < 0.0
            or self.empirical_loss > 1.0
        ):
            raise ValueError("empirical_loss must lie in [0, 1]")
        if not isfinite(self.delta) or self.delta <= 0.0 or self.delta >= 1.0:
            raise ValueError("delta must lie strictly between 0 and 1")

    @property
    def epsilon(self) -> float:
        return sqrt(
            log((2.0 * self.hypothesis_count) / self.delta)
            / (2.0 * self.sample_size)
        )

    @property
    def upper_loss_bound(self) -> float:
        return min(1.0, self.empirical_loss + self.epsilon)

    @property
    def confidence(self) -> float:
        return 1.0 - self.delta
