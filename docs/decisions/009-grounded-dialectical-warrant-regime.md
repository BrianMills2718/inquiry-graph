# ADR 009 — First executable warrant regime is grounded and dialectical

## Status

Accepted for the current research architecture.

## Context

The project already had a formal warrant judgment:

\[
\mathfrak W;A\vdash_\pi a:G.
\]

What was missing was an executable bridge from dialectical acceptability to warrant and then from warrant to current license.

A naive implementation would risk treating any grounded argument as a universal permission to accept its conclusion.

That would collapse:

- acceptability;
- warrant;
- action typing;
- guarantee typing;
- contextual applicability.

## Decision

Introduce a narrow first executable regime:

\[
\mathfrak W_{\mathrm{grounded\text{-}dialectical}}.
\]

A warrant claim is adequate under this regime only when:

1. its certificate argument is grounded-IN;
2. its action kind is one of the regime's explicitly allowed defeasible actions;
3. its guarantee kind is defeasible-acceptability.

The current allowed actions are:

- retain candidate;
- raise support;
- use defeasibly.

Unconditional acceptance and deductive truth claims are out of scope.

A current license additionally requires the active context to satisfy all explicit warrant assumptions.

The first executable context check is set inclusion:

\[
A\subseteq C.
\]

This is a deliberate approximation to general logical entailment.

## Consequences

The implementation now keeps:

\[
\text{certificate acceptability}
\neq
\text{conditional warrant}
\neq
\text{current license}
\neq
\text{execution}.
\]

A grounded-IN certificate may still fail to warrant an action when the action or guarantee type is outside the regime.

A conditionally warranted action may still be unlicensed when current applicability assumptions are unmet.

No epistemic update is executed automatically.

## Benchmark role

This regime supplies the first complete executable vertical slice from minimal support through defeat and grounded acceptability to warrant/license.

It is not a universal warrant regime.

Future deductive, graded, statistical, measurement/testimony, transition and strategy regimes should instantiate the same action-targeted interface with their own guarantee semantics.

## Related documents

- [warrant-license-interface.md](../warrant-license-interface.md)
- [end-to-end-warrant-benchmark.md](../end-to-end-warrant-benchmark.md)
- [preference-regimes.md](../preference-regimes.md)
- [project-status.md](../project-status.md)
