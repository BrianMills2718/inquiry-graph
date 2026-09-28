# ADR 010 — Numeric support warrants grade reporting, not acceptance

## Status

Accepted for the current research architecture.

## Context

The project already has a symbolic positive-support algebra and a concrete independent-Bernoulli interpretation:

\[
\rho_{\mathrm{Bern}}:
\mathsf{Supp}(X)
\to
[0,1].
\]

The value is the probability that the positive support condition holds under the explicit model, conditioned on consistency.

A key risk is to treat a high numeric grade as if it automatically licensed acceptance of the proposition, action on the proposition, conversion of support probability into truth probability, or comparison across unrelated warrant regimes.

That would collapse descriptive support evaluation into normative epistemic action.

## Decision

The first executable graded-support warrant regime licenses only:

\[
\operatorname{recordSupportGrade}(h,\rho).
\]

Its guarantee is:

\[
\text{the recorded value equals the support-event probability under the explicit independent-Bernoulli model}.
\]

It does **not** license unconditional acceptance, belief revision, use-for-action, treating the value as \(P(h)\), or any universal confidence threshold.

The regime is identified as:

\[
\mathfrak W_{\mathrm{independent\text{-}bernoulli\text{-}support}}.
\]

A later policy/regime may consume the grade and license some further epistemic action, but that requires a separate warrant judgment.

## Rationale

This keeps:

\[
\boxed{
\text{graded support evaluation}
\neq
\text{acceptance policy}.
}
\]

The distinction matches the project's broader factorization:

\[
\text{support}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{update}.
\]

It also avoids introducing arbitrary global thresholds such as “accept whenever confidence exceeds 0.9.”

## Certificate generalization

The warrant interface previously named its certificate field specifically for argument certificates, which overfit the first dialectical implementation.

The general warrant judgment now uses a regime-neutral certificate identifier. The dialectical argument ID remains available as a compatibility alias.

Certificates may therefore denote arguments, proofs, support computations, calibration results, statistical theorems, benchmark results, or other regime-specific evidence objects.

## Consequences

The current graded-support vertical slice can:

1. preserve symbolic provenance;
2. evaluate it under an explicit probabilistic model;
3. warrant recording the resulting support grade;
4. separately check applicability assumptions for current license.

It cannot, by itself, accept the supported proposition.

## Escalation

A future regime that uses grades to license actions must make explicit:

- target action;
- loss/risk semantics;
- calibration assumptions;
- threshold or decision rule;
- domain/task scope;
- guarantee.

Such a regime should be benchmarked independently rather than folded into this one.

## Related documents

- [support-antichain-probability.md](../support-antichain-probability.md)
- [warrant-license-interface.md](../warrant-license-interface.md)
- [end-to-end-warrant-benchmark.md](../end-to-end-warrant-benchmark.md)
- [project-status.md](../project-status.md)
