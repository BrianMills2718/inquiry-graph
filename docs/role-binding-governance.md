# RoleBinding Governance — Integration Requirement

## Purpose

This note isolates the one concrete capability exposed by the Inquiry Graph ↔ Hypergraph ↔ OntoCanon crosswalk that is not yet clearly owned end-to-end.

## Required semantic capability

Given a relation:

```text
R = supports(
      premise=P,
      conclusion=C
    )
```

the system may need to represent a statement about the **specific incidence**:

```text
B = roleBinding(
      relation=R,
      role=premise,
      participant=P
    )
```

rather than about:

- `P` alone; or
- `R` as a whole.

Example:

```text
challenges(
  challenger=X,
  target=B
)
```

means:

> X challenges the use of P as a premise in R.

That distinction is semantically real in argumentation, provenance, uncertainty and inquiry analysis.

## Existing support

### Scientific Hypergraph

Already supported.

An addressable `RoleBinding`:

- has an ID in the common identity namespace;
- can participate in another relation;
- can carry qualification;
- remains tied to its parent relation, role and participant.

The current acceptance fixture demonstrates a claim whose scope is one specific `analysisModel` binding.

### Inquiry Graph

The need is representable only indirectly today.

Inquiry Graph can target:

- a content object;
- a reified relation;
- a move.

It does not have a first-class record for one role assignment within a relation.

This is not yet proven to be a practical deficiency. It becomes one only when an authentic annotation needs to distinguish "target the relation" from "target this role assignment."

### OntoCanon

Recent work supports:

- `assertion_ref`;
- canonical content references;
- typed/stratified filler categories;
- higher-order assertion/content semantics.

The crosswalk has **not** established a generic governed contract for an independently addressable role binding.

## Governance requirements

If RoleBindings become durable governed targets, OntoCanon should preserve:

1. **Stable identity**
   - identity must depend on the exact relation, role and participant;
   - ordering/ordinal must participate where the role permits multiple ordered fillers.

2. **Typed ownership**
   - the binding is not a free-floating edge;
   - its parent relation and role contract remain authoritative.

3. **Evidence**
   - evidence may support/challenge the binding specifically;
   - source evidence for the parent relation must not automatically be treated as evidence for every higher-order interpretation of its bindings.

4. **Lifecycle**
   - removal/supersession of the parent relation invalidates or supersedes the binding;
   - participant replacement creates a different binding identity;
   - historical bindings remain inspectable.

5. **Reference integrity**
   - a semantic record targeting a binding must fail loud on missing/stale/incompatible binding IDs;
   - no silent retargeting after recanonicalization.

6. **Alignment**
   - binding equivalence across representations is separate from parent-relation equivalence;
   - alignment may need to map:
     ```text
     (R1, roleA, P1) ↔ (R2, roleB, P2)
     ```
     even when the relation schemas differ.

7. **Projection**
   - consumers that cannot represent first-class bindings must receive an explicit declared-loss projection, not silent flattening.

## Do not overbuild

RoleBinding identity should remain optional.

Most role assignments need no independent identifier. Create/address a binding only when another record needs to:

- target it;
- qualify it;
- attach evidence/provenance to it;
- align it;
- govern/revise it independently.

This preserves the compact ordinary n-ary relation representation.

## Acceptance fixture

A minimal cross-project proof should include:

```text
Question Q
Claim P
Claim C

R1 = supports(premise=P, conclusion=C)
B1 = addressable binding R1.premise=P

R2 = challenges(challenger=Q, target=B1)
```

Acceptance requires:

- Hypergraph carrier validation;
- exact round-trip identity for R1, B1 and R2;
- OntoCanon governance without coercing B1 into an entity or proposition;
- evidence can point specifically to B1;
- a lossy export that cannot preserve B1 declares the loss.
