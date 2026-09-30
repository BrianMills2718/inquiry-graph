# Inquiry Graph ↔ OntoCanon ↔ Scientific Hypergraph Crosswalk

## Status

Research/architecture crosswalk. This document does **not** change the executable
Inquiry Graph ontology or OntoCanon contracts.

This document supersedes the earlier architectural reading in which Scientific
Hypergraph owned the general carrier and OntoCanon sat outside it as a governance
layer.

The current target architecture is:

```text
OntoCanon
  domain-free governed semantic carrier
  + generic identity / alignment / provenance / governance mechanisms
        ↑
        ├── Inquiry ontology pack + profile
        │     -> governed Inquiry Graph instances
        │
        └── Scientific ontology pack + profile
              -> governed scientific semantic instances
```

Scientific Hypergraph remains highly relevant as:

- a proving domain;
- a donor of already-worked generic carrier semantics;
- concrete evidence for relation-as-participant and RoleBinding-as-participant;
- an interoperability/migration source while OntoCanon's general carrier is
  still being reconciled.

It should not remain the permanent owner of a second domain-free carrier if those
semantics are genuinely generic and belong in OntoCanon.

## 1. Architectural ownership

### Inquiry Graph

Owns inquiry-domain semantics and source-grounded reconstruction:

- concepts;
- claims;
- questions;
- hypotheses;
- methods;
- examples;
- goals;
- references;
- semantic relations;
- inquiry moves;
- stance events;
- question-state events;
- source conversations/messages/anchors;
- inquiry-specific invariants.

Inquiry Graph should not grow another general semantic carrier.

### OntoCanon

Target owner of the domain-free governed semantic substrate:

- generic semantic elements;
- first-class typed n-ary relation instances;
- optionally addressable RoleBindings where required;
- typed reference/identity primitives;
- source/evidence custody;
- proposal/review/activation governance;
- deterministic identity and fallible alignment separation;
- retraction/supersession/recanonicalization;
- profile-selected global validation;
- bounded/loss-aware exports.

Ontology packs carry domain semantics. Profiles configure policy.

### Scientific Hypergraph

Should be treated as:

- scientific-domain semantics over the general substrate;
- a proving consumer for richer relation/binding structures;
- a donor of generic carrier features already worked out there.

The generic features currently demonstrated in Scientific Hypergraph should be
audited for absorption into OntoCanon rather than preserved as a parallel
general-purpose kernel by default.

## 2. Inquiry Graph carrier correspondence

The current Inquiry Graph objects remain compatible with the general carrier
shape that OntoCanon is now targeting.

| Inquiry Graph object | General carrier representation | Notes |
|---|---|---|
| `Node` | semantic element | `kind` is Inquiry-profile typing, not a kernel primitive |
| `Relation` | relation instance | existing role bindings map directly |
| `Relation.Binding` | role binding/incidence | exact structural correspondence |
| `Move` | relation instance | actor/input/output/occurrence/after are roles |
| `StanceEvent` | relation instance | actor/target/stance/occurrence |
| `QuestionEvent` | relation instance | question/actor/status/answers/replacement/occurrence |
| `Conversation` | semantic/source element | source-domain object |
| `Participant` | semantic/source element | source-scoped identity unless reconciled |
| `Message` | semantic/source element | ordered source occurrence |
| `Anchor` | evidence/grounding relation or record | exact quote + offsets remain source evidence |
| `review_status` | governance state | not participant stance |
| `inference_family` | Inquiry-profile classification | not a kernel primitive |

No current Inquiry Graph object demonstrates a need for a second carrier outside
the proposed OntoCanon target.

## 3. Relations targeting relations

Inquiry Graph deliberately allows semantic relations to target other semantic
relations.

Example:

```text
R1 = supports(premise=P, conclusion=C)
R2 = challenges(challenger=X, target=R1)
```

This requires relation instances to be valid participants in other relations.

Scientific Hypergraph already demonstrates this directly.

OntoCanon's target carrier therefore needs to support the same generic capability
without coercing R1 into an entity-like surrogate or proposition-only special
case.

## 4. RoleBinding-as-participant

The stronger higher-order capability is to target one role assignment:

```text
R1 = supports(premise=P, conclusion=C)

B1 = binding(
  relation=R1,
  role=premise,
  participant=P
)

R2 = challenges(
  challenger=X,
  target=B1
)
```

This distinguishes:

- challenge P;
- challenge R1;
- challenge **P's use as premise in R1**.

Scientific Hypergraph already has a concrete fixture for this pattern.

The proposed OntoCanon architecture treats this as an **optionally addressable
kernel incidence**:

- most bindings may remain anonymous;
- a binding receives stable identity only when something needs to target,
  qualify, evidence, align, supersede, or otherwise govern it.

The exact OntoCanon storage/identity path remains pending the local carrier audit.

## Inquiry semantic contract

The carrier-independent domain semantics are frozen in
[`inquiry-ontology-pack-semantic-contract.md`](inquiry-ontology-pack-semantic-contract.md).
That document is the translation source for an eventual executable OntoCanon
Inquiry pack; current Pydantic/storage shapes are not automatically permanent
ontology semantics.

## 5. Inquiry ontology pack

The following belong in an Inquiry ontology pack rather than the carrier.

### Semantic/object types

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

### Semantic relation types

Current Inquiry Graph relations:

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

### Process/state relation schemas

- InquiryMove
- StanceEvent
- QuestionEvent
- GroundedIn / AnchoredTo

The pack defines their roles, permitted participant kinds, cardinalities,
directionality/algebra where relevant, and any domain-specific invariants.

## 6. Inquiry profile

The Inquiry profile should configure policy over the pack and shared OntoCanon
mechanisms.

Likely profile-controlled concerns include:

- open/closed/mixed treatment of unknown Inquiry vocabulary;
- allowed reference/filler kinds;
- role ordering/cardinality;
- review/activation policy;
- alignment predicates permitted for cross-trajectory integration;
- global invariant validators;
- identity/canonicalization policy where inquiry objects have stable semantic
  identity beyond source occurrences.

The profile should configure shared mechanisms rather than implement a second
governance or alignment stack.

## 7. Source grounding remains separate from semantic truth

Inquiry Graph's strongest existing contract remains:

```text
annotation -> exact source message substring
```

A governed OntoCanon representation must preserve:

- conversation/message identity;
- actor;
- source order;
- quote;
- Unicode offsets;
- annotation origin;
- review state.

Grounding establishes what text supports an annotation. It does not certify the
annotation as true.

This maps naturally onto OntoCanon source/evidence custody.

## 8. What current OntoCanon already appears to supply

Current OntoCanon evidence includes:

- reified n-ary predicate/role structures;
- role/cardinality/type validation;
- source/evidence custody;
- source-bound occurrence identity;
- source-independent content identity;
- assertion-to-assertion references;
- broader typed content-reference work;
- additive supersession/recanonicalization;
- deterministic identity separated from fallible semantic alignment;
- evidence-bearing alignment proposals;
- review/proposal governance;
- non-destructive canonical projections.

These are candidate reusable mechanisms, not automatically the optimal final
implementation.

The independent carrier audit decides how much is already genuinely generic.

## 9. Current unresolved OntoCanon seams

### 9.1 Generic semantic object lifecycle

Current product vocabulary remains:

```text
SourceMeaning
-> CandidateAssertion
-> GovernedAssertion
```

The unresolved question is whether this is:

- terminology/API debt over a generic substrate; or
- a real semantic/type constraint.

Inquiry objects such as QuestionEvent, InquiryMove and RoleBinding should not be
forced into proposition semantics merely to reuse governance.

### 9.2 Addressable RoleBinding

No current public OntoCanon contract has yet been established for a role binding
as a durable semantic target.

This remains the clearest potential kernel gap.

### 9.3 Alignment as ordinary governed relation

Current content alignment is pairwise and uses a narrow fixed relation enum.

The target architecture is:

```text
candidate correspondence
  -> adjudication proposal
  -> ordinary governed semantic alignment relation
  -> optional derived integrated projection
```

The mapping predicate belongs in pack/profile semantics.

Candidate-generation and adjudication algorithms remain replaceable.

## 10. Integration of the two inquiry trajectories

The repository contains two independently source-grounded inquiry graphs:

1. `examples/seed/graph.json`
2. `examples/formal-inquiry-2026-09-27/graph.json`

They should remain independently immutable.

Integration should be:

```text
G1 ─┐
    ├─ governed alignment relations A ─→ derived integrated projection P(G1,G2,A)
G2 ─┘
```

not destructive graph union.

Simple pairwise mappings may project to standards such as SSSOM.

Higher-order/n:m mappings remain ordinary governed n-ary relations internally
and should not be flattened merely to fit an interchange standard.

## 11. Cross-trajectory semantic prior art

Do not invent a bespoke relation taxonomy where existing semantics fit.

Relevant sources include:

- SKOS / OWL / RDFS mapping predicates for applicable identity/breadth cases;
- SSSOM for pairwise mapping interchange/provenance;
- EDOAL for complex ontology-correspondence prior art;
- inquisitive semantics for question refinement;
- inferential erotetic logic for question-to-question inquiry progression;
- AIF / abstract, bipolar and recursive argumentation for support/attack and
  higher-order argument structure;
- PROV-O for external provenance projection.

Inquiry-specific predicates should be introduced only for demonstrated semantic
gaps.

## 12. Stop rule

Do not add a new general semantic carrier to Inquiry Graph.

Do not preserve Scientific Hypergraph as a separate general carrier merely
because generic semantics were first implemented there.

If Inquiry Graph requires a genuinely domain-free carrier capability and
OntoCanon lacks it, the default architectural question is whether that capability
belongs in the OntoCanon kernel.

If the capability is genuinely inquiry-specific, it belongs in the Inquiry pack
or profile.

## 13. Current next step

Do not implement an Inquiry pack/profile against a carrier that is still being
reconciled.

The current dependency is the OntoCanon local carrier audit / proposed ADR-0042.

Once that is resolved:

1. update this crosswalk to the accepted OntoCanon carrier contract;
2. define the Inquiry ontology pack using existing Inquiry Graph semantics;
3. define the Inquiry profile using shared OntoCanon policy/governance
   mechanisms;
4. preserve the two existing inquiry trajectories as independent source
   instances;
5. express cross-trajectory mappings as governed semantic relations;
6. add interoperability projections only where justified.

No benchmark or comparative empirical evaluation is authorized without explicit
Brian approval.
