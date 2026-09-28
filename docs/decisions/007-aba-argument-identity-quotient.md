# ADR 007 — Keep ABA argument identity as a semantic quotient

## Status

Accepted for the current research architecture.

## Context

The minimal ABA bridge currently collapses distinct deductions when they have the same conclusion and the same minimal supporting assumption environment.

That loses proof-tree identity.

Before adding preference-sensitive defeat, the project needed to determine whether this loss is already unsound or whether first-class derivation/subargument structure should be introduced immediately.

## Decision

For the current ABA/ABA+ bridge, identify dialectical arguments by:

\[
(\text{conclusion},\text{supporting assumption environment}).
\]

Do **not** add first-class derivation DAGs solely for ABA/ABA+ semantics.

Treat this as an explicit semantic quotient, not as a claim that proof objects are identical.

The richer formal-representation layer may continue to distinguish derivations/proofs independently.

## Rationale

Basic ABA attacks depend on:

- the attacker's conclusion;
- the target's supporting assumptions.

ABA+ adds preferences over assumptions.

Therefore deductions with the same conclusion and same assumption support are behaviorally equivalent for the currently selected ABA/ABA+ dialectical semantics.

The project also translates defeasible rules into typed applicability assumptions that retain source-rule and attack-origin metadata. This preserves the defeasible commitments relevant to the ABA bridge.

## Consequences

The project may proceed to assumption-preference semantics without first refactoring argument identity.

The quotient becomes invalid if later semantics distinguish derivations with the same conclusion/support, including:

- ASPIC+ subargument attacks;
- unguarded rule-application undercuts;
- last-link or other proof-structure-sensitive preferences;
- proof-sensitive warrant regimes;
- explanation requirements needing exact derivation trees.

Those are explicit escalation triggers.

## Relationship to support and formal artifacts

Positive support remains a summary over minimal assumption environments.

Formal proof/derivation identity and dialectical argument identity are separate layers:

\[
\text{formal artifact identity}
\neq
\text{ABA dialectical quotient identity}.
\]

This is deliberate.

## Next step

Implement and test ABA+ preference-sensitive attack/reversal over assumptions while preserving typed provenance for generated assumptions.

See [argument-identity-boundary.md](../argument-identity-boundary.md) for the stress test and reasoning.
