# ADR 014 — Strategy selection requires a positive lower confidence bound on paired utility advantage

## Status

Accepted for the current research architecture.

## Context

The research layer treats strategy selection as a metareasoning target rather than as a hidden implementation detail.

A strategy-performance warrant therefore needs to justify an action such as:

\[
\operatorname{selectStrategy}(\pi)
\]

relative to an explicit task class and performance objective.

A raw average score is insufficient because it does not express uncertainty, task-distribution assumptions, or comparison against a baseline.

## Decision

Use a paired bounded-utility benchmark.

For each benchmark task \(i\), record:

\[
u_i(\pi)\in[0,1]
\]

for the candidate strategy and:

\[
u_i(\pi_0)\in[0,1]
\]

for the baseline.

Define paired difference:

\[
D_i=u_i(\pi)-u_i(\pi_0)\in[-1,1].
\]

For \(n\) i.i.d. benchmark tasks and confidence parameter \(\delta\), Hoeffding gives:

\[
E[D]
\ge
\bar D
-
\sqrt{
\frac{2\log(1/\delta)}{n}
}
\]

with probability at least \(1-\delta\) for one pre-specified comparison at fixed sample size.

### Statistical scope refinement (PR #36)

If \(k\) candidate strategies are screened against the same baseline, the implementation uses the per-comparison error budget:

\[
\delta_c=\delta/k
\]

so the fixed-sample Hoeffding radius becomes:

\[
\sqrt{
\frac{2\log(1/\delta_c)}{n}
}.
\]

If results may be inspected repeatedly with data-dependent stopping, the implementation can instead use a conservative anytime-valid union-bound radius:

\[
\sqrt{
\frac{2\log(n(n+1)/\delta_c)}{n}
},
\]

corresponding to \(\delta_{c,n}=\delta_c/[n(n+1)]\).

The caller must truthfully declare the comparison count and stopping regime. Benchmark reuse or adaptive candidate generation can still create additional selection effects not captured by those declarations and therefore remains an applicability-assumption question.

The strategy-performance warrant regime may license:

\[
\operatorname{selectStrategy}(\pi)
\]

only when the lower confidence bound is strictly positive.

## Applicability assumptions

The benchmark theorem does not establish its own transfer conditions.

The warrant should therefore keep assumptions such as:

- i.i.d. benchmark-task sampling;
- stable task distribution;
- validity of the declared utility function;
- utility values bounded in \([0,1]\);
- declared comparison count covers the screening family for which the family-wise guarantee is claimed;
- declared stopping rule matches the actual fixed-sample or sequential evaluation procedure;
- no hidden benchmark leakage or adaptive re-use invalidating the stated correction;

explicit in the warrant/context.

## Utility and cost

The certificate accepts one normalized utility value per strategy/task.

If reasoning cost matters, it must already be incorporated into the declared utility function before the certificate is formed.

The implementation deliberately does not add raw quality and raw cost numbers with incompatible units.

## What the regime does not establish

It does not establish that:

- the benchmark task distribution matches every future task;
- the utility function captures every relevant objective;
- the selected strategy is globally optimal;
- the strategy will outperform every alternative;
- a statistically positive advantage is practically meaningful outside the declared regime.

## Consequences

This provides the first executable warrant whose target is a **reasoning strategy itself**.

It also closes the initial benchmark set spanning proposition-level support, deduction, evidence-channel reliability, statistical generalization, and metareasoning.

## Escalation

Use richer strategy-performance models when cases require:

- non-i.i.d. task sequences;
- online regret;
- adaptive benchmark selection;
- multiple baselines;
- multi-objective or non-scalar utility;
- explicit computation-time distributions;
- transfer across task families.

## Related documents

- [metareasoning-strategy-reflection.md](../metareasoning-strategy-reflection.md)
- [warrant-license-interface.md](../warrant-license-interface.md)
- [end-to-end-warrant-benchmark.md](../end-to-end-warrant-benchmark.md)
- [project-status.md](../project-status.md)
