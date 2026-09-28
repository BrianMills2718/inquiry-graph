# Inquiry Graph ↔ Hypergraph Kernel ↔ OntoCanon Crosswalk

## Status

Research/architecture crosswalk. This document does **not** change the executable Inquiry Graph ontology, Scientific Hypergraph kernel, or OntoCanon contracts.

## Result

The three systems are complementary:

```text
Inquiry Graph
  owns the domain semantics and source-grounded reconstruction of inquiry
        ↓ lossless structural projection

Scientific Hypergraph domain-free kernel
  owns the maximally permissive typed n-ary carrier:
  ModelElement + RelationInstance + RoleType + RoleBinding
        ↓ governed semantic admission / identity / reconciliation

OntoCanon
  owns evidence custody, governance, durable commitment,
  identity/canonicalization, semantic alignment, revision and export
```

The present Inquiry Graph ontology has **no known carrier-level structure that requires a new primitive beyond the Hypergraph kernel**.

The remaining integration gap is primarily at the **OntoCanon governance boundary**, especially first-class governance of arbitrary relation instances and addressable role bindings without coercing them into assertion-specific terminology/contracts.

## 1. Carrier correspondence

| Inquiry Graph object | Hypergraph representation | Notes |
|---|---|---|
| `Node` | `ModelElement` | `kind` becomes Inquiry-profile typing, not a kernel primitive |
| `Relation` | `RelationInstance` | Existing role bindings map directly |
| `Binding(role, ref)` | `RoleBinding` | Exact structural correspondence |
| `Move` | `RelationInstance` | Actor/input/output/occurrence/after are roles |
| `StanceEvent` | `RelationInstance` | Actor/target/stance/occurrence are roles or typed participants |
| `QuestionEvent` | `RelationInstance` | Question/actor/status/answers/replacement/occurrence are roles |
| `Conversation` | `ModelElement` | Source-domain object |
| `Participant` | `ModelElement` | Actor identity remains source scoped unless reconciled |
| `Message` | `ModelElement` | Ordered source occurrence |
| `Anchor` | relation or addressable evidence object | Exact quote + offsets remain source-grounding data |
| annotation `review_status` | qualification/governance state | Must not be confused with participant stance |
| `inference_family` | Inquiry-profile classification | Not a kernel primitive |

## 2. Relations targeting relations already fit

Inquiry Graph deliberately allows a challenge or other relation to target a reified relation.

For example:

```text
supports(premise=P, conclusion=C) = R
challenges(challenger=X, target=R)
```

The Hypergraph kernel represents this natively because `RelationInstance` is itself a `ModelElement` and may participate in another relation.

No assertion-specific workaround is required.

## 3. RoleBinding-as-participant is the stronger capability

The kernel also allows an **individual role assignment** to be addressable:

```text
R = supports(premise=P, conclusion=C)

B = binding(
      relation=R,
      role=premise,
      participant=P
    )

challenges(
  challenger=X,
  target=B
)
```

This expresses a distinction Inquiry Graph currently handles only indirectly:

> challenge P itself  
> versus challenge R as a whole  
> versus challenge **P's use in the premise role of R**.

That is the clearest carrier capability worth importing into the inquiry model if real annotations require it.

It should remain optional. Anonymous bindings are appropriate when nothing needs to target or qualify a particular assignment.

## 4. Inquiry profile over the kernel

The following belong in an Inquiry profile, not in the carrier:

### Element/domain types

- Concept
- Claim
- Question
- Hypothesis
- Method
- Example
- Goal
- Reference
- Conversation
- Participant
- Message

### Relation types

Current Inquiry Graph semantic relations:

- supports
- challenges
- depends_on
- distinguishes
- reframes
- motivates
- answers
- exemplifies
- candidate_for
- part_of
- about
- related_to
- supersedes

Process/state schemas:

- InquiryMove
- StanceEvent
- QuestionEvent
- AnchoredTo / GroundedIn

The kernel need not know what any of these mean. It only needs to preserve their relation identity, roles, participants, typing and higher-order reference.

## 5. Source grounding remains separate from semantic truth

Inquiry Graph's strongest current contract is source grounding:

```text
annotation → exact message substring
```

A hypergraph projection must preserve:

- message identity;
- actor;
- conversation;
- source order;
- quote;
- Unicode offsets;
- annotation origin;
- review state.

Grounding proves the interpretation points to actual source text. It does not certify the interpretation as true or semantically correct.

This maps naturally onto OntoCanon's evidence-custody principle.

## 6. What OntoCanon already supplies

Recent OntoCanon work already establishes most of the governance pattern needed here:

- n-ary first-class semantic relations;
- typed role/filler validation;
- source/evidence custody;
- deterministic source-bound assertion identity;
- source-independent content identity;
- assertion-to-assertion references in the promoted graph;
- richer typed content references in `gcontent2_`;
- immutable records and additive supersession/recanonicalization;
- separation of deterministic identity from fallible semantic alignment;
- evidence-bearing alignment proposals;
- explicit `uncertain` outcomes;
- review/governance before canonicalization;
- reversible/additive projections rather than destructive merge.

These should be reused rather than recreated in Inquiry Graph.

## 7. What is not yet cleanly solved in OntoCanon

### 7.1 General relation-instance governance

The implementation/public vocabulary is still centered on:

```text
SourceMeaning
→ CandidateAssertion
→ GovernedAssertion
```

The carrier we need is broader: a QuestionEvent, InquiryMove, Membership or RoleBinding is not naturally an assertion in the ordinary sense.

The first question for an OntoCanon integration should therefore be whether the current assertion lifecycle can govern a general typed relation instance **without semantic distortion**.

If not, the correct change is to generalize the governance contract while preserving assertion-specific compatibility.

### 7.2 First-class RoleBinding governance

OntoCanon can govern assertion/content references, but the current crosswalk has not established a lossless public contract for:

```text
relation → particular role binding → participant
```

where the binding itself has durable identity and can be:

- a target of another semantic relation;
- independently evidenced;
- qualified;
- aligned;
- superseded;
- governed.

This is the most concrete missing capability.

### 7.3 Alignment relation profiles

OntoCanon's current content alignment vocabulary is intentionally narrow:

```text
equivalent | compatible | contradicts | distinct | uncertain
```

Cross-inquiry integration requires domain relations such as:

- refines
- generalizes
- reframes
- continues
- answers_same_question
- same_strategy
- independent_convergence
- shared_ancestor

These semantics should belong to the Inquiry profile while OntoCanon governs the mapping records and their evidence/review lifecycle.

## 8. Two existing inquiry trajectories

The repository now contains two independent source-grounded inquiry graphs:

1. `examples/seed/graph.json`
2. `examples/formal-inquiry-2026-09-27/graph.json`

They should remain independently immutable.

The intended future integration is not:

```text
G1 + G2 → destructive merged graph
```

but:

```text
G1 ─┐
    ├─ governed alignment graph A ─→ derived integrated projection P(G1,G2,A)
G2 ─┘
```

This mirrors OntoCanon's accepted identity/alignment posture.

## 9. Cross-graph alignment object

A first alignment record should preserve at least:

```text
left_ref
right_ref
relation_type
evidence_left
evidence_right
rationale
confidence / calibrated support if applicable
proposal provenance
review decision
supersession lineage
profile/version
```

Absence of a mapping must remain distinguishable from:

- examined and distinct;
- rejected proposal;
- unresolved;
- uncertain;
- accepted mapping.

## 10. Cross-graph relation classes

Do not force all integration into equivalence.

A useful initial factorization is:

### Identity-like
- exact_identity
- semantic_equivalence

### Directional abstraction/revision
- refines
- generalizes
- reframes
- supersedes
- continues

### Shared function
- answers_same_question
- same_strategy
- same_method_family

### Epistemic relation
- supports
- challenges
- contradicts

### Historical/structural relation
- independent_convergence
- shared_ancestor
- derived_from

### Negative/epistemic status
- distinct
- uncertain

Only explicitly declared relation types should receive transitive/symmetric semantics.

## 11. Architectural stop rule

Do **not** add a new general semantic carrier to Inquiry Graph.

A new kernel primitive is justified only if an Inquiry Graph object cannot be represented losslessly as:

```text
ModelElement
RelationInstance
RoleBinding
typing/meta-relations
```

with the source/provenance/governance layer supplied externally.

Similarly, do not generalize OntoCanon merely because its terminology feels narrow. Generalize only where an executable Inquiry Graph integration demonstrates loss or semantic coercion.

## 12. Next proof

The next bounded proof should:

1. define an Inquiry profile over the Hypergraph kernel;
2. project both current Inquiry Graphs into that carrier;
3. verify exact reconstruction of the original Inquiry Graph records;
4. exercise relation-as-participant;
5. add one fixture exercising RoleBinding-as-participant;
6. pass the Hypergraph validator;
7. test whether OntoCanon can govern the projected objects losslessly;
8. record every mismatch as either:
   - carrier gap,
   - Inquiry-profile gap,
   - OntoCanon-governance gap,
   - projection-only issue.

The proof should not merge the two inquiry trajectories.
