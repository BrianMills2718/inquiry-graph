# ADR 011 — Deductive warrant is checked derivability relative to explicit premises

## Status

Accepted for the current research architecture.

## Context

The warrant interface distinguishes support, warrant, license and update. The first executable warrant regimes covered defeasible grounded acceptability and graded-support reporting.

A deductive regime must preserve a different guarantee:

\[
\text{truth preservation relative to explicit premises}.
\]

It must not silently turn a valid derivation into unconditional acceptance of those premises.

## Decision

Add a small executable strict-Horn proof fragment.

A proof certificate contains:

- explicit premises;
- strict Horn rules;
- a target conclusion;
- a certificate identifier.

A deterministic checker computes the least Horn closure.

The deductive warrant regime may warrant only:

\[
\operatorname{derive}(h)
\]

when:

1. the certificate conclusion is derivable from its explicit premises;
2. the action target matches the certificate conclusion;
3. the warrant assumptions include all proof premises;
4. the guarantee kind is truth-preservation-relative-to-premises.

A current license additionally requires the current context to contain all warrant assumptions.

## Consequences

A valid proof can establish a conditional warrant even when the current context lacks one or more premises.

In that case:

\[
\text{warranted}
\land
\neg\text{licensed}.
\]

The regime never licenses acceptance of the premises merely because they occur in a valid derivation.

The strict-Horn fragment is a benchmark implementation, not a claim that the project's final formal proof layer should be Horn logic. Richer proof objects can later be supplied by MMT/LF or another formal checker through the same warrant interface.

## Why a checked fragment rather than a boolean proof flag

The project should not treat an unverified metadata field such as proof_valid=true as a certificate.

The benchmark regime therefore contains an actual deterministic derivability checker for its declared fragment.

## Escalation

Move to richer proof systems when benchmark cases require:

- quantifiers;
- equality;
- higher-order reasoning;
- dependent types;
- modal/temporal logics;
- proof-object interoperability with the formal representation layer.

The warrant interface should remain unchanged; only the certificate/checker regime should broaden.

## Related documents

- [warrant-license-interface.md](../warrant-license-interface.md)
- [end-to-end-warrant-benchmark.md](../end-to-end-warrant-benchmark.md)
- [project-status.md](../project-status.md)
