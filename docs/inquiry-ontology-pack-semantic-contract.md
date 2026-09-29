# Inquiry Ontology Pack Semantic Contract

**Date:** 2026-09-29  
**Status:** carrier-independent semantic contract; not yet an executable OntoCanon pack  
**Source of truth for current executable Inquiry Graph:** `src/inquiry_graph/model.py` + `src/inquiry_graph/validate.py`  
**Carrier dependency:** proposed OntoCanon general governed semantic carrier / ADR-0042 reconciliation  
**Empirical rule:** no benchmark or comparative empirical evaluation without explicit Brian approval

## Purpose

Freeze the **domain semantics** that an eventual OntoCanon Inquiry ontology pack
must preserve, independent of the final carrier API.

This avoids two failure modes:

1. letting the eventual OntoCanon implementation accidentally redefine Inquiry
   Graph semantics;
2. prematurely encoding current Pydantic/storage shapes as permanent ontology
   semantics.

The contract distinguishes:

- **current executable semantics** — already enforced by Inquiry Graph;
- **proposed semantic refinements** — justified by prior art but not yet adopted
  into the executable ontology;
- **profile policy** — governance/validation choices that should not live in the
  ontology pack itself.

## 1. Semantic layers

### Source layer

Types:

- Conversation
- Participant
- Message
- Anchor

Purpose:

- preserve exact public source context;
- distinguish source occurrence from semantic interpretation;
- support exact grounding and provenance.

### Content layer

Current content kinds:

- Concept
- Claim
- Question
- Hypothesis
- Method
- Example
- Goal
- Reference

A content object is not identical to one message or utterance.

One source message may ground several semantic objects.

Several source messages may ground the same semantic object only through an
explicit identity decision; lexical similarity alone does not merge them.

### Semantic / argument layer

Current relation kinds:

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

Relations are first-class semantic occurrences with named role bindings.

A relation may itself be a semantic target where the carrier permits it.

### Inquiry-process layer

InquiryMove is a process occurrence with:

- actor;
- move type;
- inputs;
- outputs;
- occurrence message;
- predecessor moves;
- optional inference-family annotation.

### State-history layer

- StanceEvent
- QuestionEvent

These are histories/events, not intrinsic properties of the semantic target.

### Extraction/governance layer

Current annotation metadata includes:

- origin = explicit | inferred;
- review_status = proposed | confirmed | rejected;
- extraction method/provider/model/prompt metadata.

This is governance/provenance state, not semantic content.

## 2. Core semantic distinctions

The Inquiry pack must preserve these distinctions.

### 2.1 Source occurrence != semantic object

```text
message span
!=
claim/question/concept
```

Grounding links them.

### 2.2 Question content != question status

```text
Question
!=
open/answered/resolved/deferred/superseded/reopened state
```

Question status is actor- and occurrence-relative through QuestionEvent.

### 2.3 Actor stance != target truth/status

```text
actor endorses X
!=
X is true

actor rejects X
!=
X is false
```

### 2.4 InquiryMove != semantic result

A `hypothesize` move may produce a Hypothesis, but the move occurrence and
hypothesis content are distinct objects.

### 2.5 Review status != epistemic truth

```text
annotation rejected
!=
proposition false
```

A rejected extraction means the annotation is not accepted into the reviewed
graph.

### 2.6 Relation target != role-binding target

Where supported by the carrier:

```text
challenge P
challenge supports(P,C)
challenge P-as-premise-of-supports(P,C)
```

are three distinct semantics.

## 3. Content types

| Type | Intended semantics | Current executable status | Prior-art relation |
|---|---|---|---|
| **Concept** | conceptual object/category used in inquiry | current | may map to SKOS concept only where actual concept-scheme semantics fit |
| **Claim** | declarative content presented as assertible | current | compatible with informational content / proposition-like models |
| **Question** | issue/interrogative content | current | connect to inquisitive/erotetic semantics; not reducible to Concept |
| **Hypothesis** | candidate explanatory/predictive/declarative content not thereby endorsed | current | proposition-like content with inquiry role |
| **Method** | reusable procedure/strategy/method description | current | local semantic type; may align with external method ontologies when exact |
| **Example** | concrete illustrative/case content | current | local semantic type |
| **Goal** | desired inquiry/result state | current | local semantic type; do not conflate with Question |
| **Reference** | cited external work/resource/conceptual reference | current | provenance/bibliographic mappings may apply externally |

## 4. Current semantic relation contracts

### supports

Roles:

- `premise`: Claim | Hypothesis | Example; one or more
- `conclusion`: Claim | Hypothesis; exactly one

Semantics:

> the premise(s) are represented as supporting the conclusion.

This is intentionally broader than formal logical entailment.

Do not infer truth of conclusion from existence of the relation.

Potential future specialization:

- evidential support;
- deductive inference;
- abductive support;
- explanatory support.

### challenges

Roles:

- `challenger`: Claim | Hypothesis | Example | Question; exactly one
- `target`: any semantic content/relation/move currently permitted; exactly one

Semantics:

> the challenger raises a substantive challenge to the target.

A challenge need not be a rebuttal or contradiction.

Potential future specialization may distinguish:

- rebuttal;
- undercut/applicability challenge;
- sufficiency challenge;
- framing challenge;
- RoleBinding-targeted challenge.

### depends_on

Roles:

- dependent
- prerequisite

Each exactly one.

Semantics:

> the dependent inquiry object relies on the prerequisite in the represented
> analysis.

Cycles are allowed and surfaced as warnings, because circular reasoning or
reciprocal dependency may itself be meaningful data.

### distinguishes

Roles:

- left
- right

Each exactly one.

Semantics:

> the inquiry explicitly treats the two targets as a distinction worth
> maintaining.

Display orientation is not intended as logical asymmetry.

Do not infer ontological disjointness.

### reframes

Roles:

- original: Question
- replacement: Question

Each exactly one.

Semantics:

> the replacement question recasts the inquiry represented by the original
> question.

This is not automatically issue refinement, logical equivalence, or
supersession.

### motivates

Roles:

- reason
- result

Each exactly one.

Semantics:

> the reason is represented as motivating the result in the inquiry process.

This is interpreted motivation, not proven physical causation.

### answers

Roles:

- answer: Claim | Hypothesis | Method | Example
- question: Question

Each exactly one.

Semantics:

> the answer is presented as answering the question.

This does not imply that the question is resolved for every actor or under every
standard of resolution.

### exemplifies

Roles:

- example: Example
- general: any semantic content/relation/move currently allowed

Each exactly one.

Semantics:

> the example instantiates or illustrates the general target for inquiry
> purposes.

Do not automatically infer formal instance-of semantics.

### candidate_for

Roles:

- candidate: any semantic content/relation/move
- problem: Question | Goal

Each exactly one.

Semantics:

> the candidate is under consideration as a response/solution/method for the
> question or goal.

### part_of

Roles:

- part
- whole

Each exactly one.

Semantics:

> structural/compositional membership under the current inquiry model.

This relation is intentionally underspecified in V1.

Future pack refinement may split:

- strategy episode contains move;
- document contains component;
- decomposition contains subproblem;
- other mereological/process composition relations.

### about

Roles:

- subject
- object

Each exactly one.

Semantics:

> explicit reflective/aboutness target.

This is important for self-applicative inquiry where the inquiry process
describes itself.

### related_to

Roles:

- source
- target

Each exactly one.

Semantics:

> weak generic association when no more precise current relation is justified.

This should be used sparingly and is a candidate for future contraction.

### supersedes

Roles:

- new
- old

Each exactly one.

Semantics:

> the new semantic object/relation/move supersedes the old one in the represented
> inquiry history.

Current invariant: supersession graph is acyclic.

Supersession does not delete old history.

## 5. InquiryMove contract

Current move types:

- ask
- clarify
- distinguish
- challenge
- retract
- hypothesize
- generalize
- deduce
- test
- reframe
- decompose
- connect
- scope
- summarize
- propose

Required roles/fields:

- actor: Participant
- input: zero or more semantic objects
- output: zero or more semantic objects
- occurrence: Message
- after: zero or more prior InquiryMoves
- inference_family: induction | abduction | deduction | unspecified

Current invariants:

1. a move must have at least one input or output;
2. every referenced input/output must exist;
3. every `after` reference must target a Move;
4. `after` links must stay within one conversation;
5. predecessor occurrence must be earlier than successor occurrence;
6. move-order graph is acyclic;
7. actor must equal the speaker at the occurrence message;
8. at least one anchor must ground the move in its occurrence message.

The move taxonomy is descriptive, not claimed exhaustive.

`inference_family=unspecified` is semantically meaningful: the graph may record
a disputed inference without forcing a taxonomy decision.

## 6. StanceEvent contract

Roles/fields:

- actor: Participant
- target: semantic object
- stance:
  - posits
  - endorses
  - questions
  - rejects
  - suspends
  - retracts
- occurrence: Message

Core invariant:

> stance is actor-relative historical state, not target truth.

Actor must equal the source-message speaker at the event occurrence.

Stance vocabulary may later map to more formal argumentation/epistemic
vocabularies, but no exact external equivalence is currently adopted.

## 7. QuestionEvent contract

Roles/fields:

- question: Question
- status:
  - open
  - answered
  - resolved
  - deferred
  - superseded
  - reopened
- actor: Participant
- occurrence: Message
- zero or more answer references
- optional resolution basis
- optional replacement Question

Current invariants:

1. status target must be a Question;
2. `resolved` requires at least one answer or explicit resolution basis;
3. `superseded` requires a replacement;
4. replacement must be a different Question;
5. only one status event may exist for the same
   `(actor, question, occurrence-message)` tuple;
6. actor equals source-message speaker at occurrence.

Important semantic distinction:

```text
answered
!= resolved
!= superseded
```

and all are actor-/history-relative operational states.

Formal issue resolution from inquisitive semantics may inform future validation,
but does not replace QuestionEvent history.

## 8. Source-grounding contract

Every grounded Inquiry annotation currently has at least one Anchor.

Anchor:

- message_id;
- start;
- end;
- quote.

Required invariants:

1. message exists;
2. offsets are half-open Unicode character offsets;
3. `message.text[start:end] == quote`;
4. event-like records with an occurrence message have an anchor in that
   occurrence message;
5. conversation message ordinals are unique and increasing;
6. message actor is a declared participant of its conversation.

This source contract should map into OntoCanon evidence custody without losing
the exact Inquiry-specific offset/quote semantics.

## 9. Identity and reference contract

Current Inquiry Graph rules:

- IDs are globally unique within a graph;
- participant IDs may repeat across conversations only if definitions are
  identical;
- source IDs are conventionally namespaced by conversation;
- semantic references must resolve;
- relation/move targets are explicit IDs;
- lexical similarity never creates identity automatically.

Future OntoCanon integration should preserve separate:

- source occurrence identity;
- semantic content identity where applicable;
- governed cross-trajectory alignment.

The two existing inquiry trajectories remain independently immutable.

## 10. Graph-global invariants

### Hard invariants

Current validator treats these as invalid:

- duplicate IDs;
- invalid/missing anchors;
- actor/source mismatch;
- dangling semantic references;
- invalid relation roles;
- invalid role cardinality;
- invalid role target type;
- duplicate role-player pair;
- move temporal/order violations;
- move-order cycles;
- supersession cycles;
- invalid question-state targets/replacements;
- unsupported resolution;
- ambiguous duplicate status event.

### Non-fatal structural findings

Dependency cycles are retained and surfaced as warnings.

This is intentional:

> a reasoning graph may describe circular or reciprocal reasoning without the
> annotation system deleting or exploding on it.

## 11. Proposed semantic refinements not yet executable

These should **not** be added to the current executable ontology merely because
they are useful ideas.

### Question semantics

Candidate future distinctions informed by prior art:

- issue refinement;
- erotetic implication/inquiry progression;
- reframing;
- workflow supersession.

### Argument semantics

Potential specialization:

- evidential support;
- deductive support;
- explanatory support;
- rebuttal;
- undercut;
- applicability challenge;
- framing challenge.

### Composition

Potential split of generic `part_of` by object/process semantics.

### Strategy

A future StrategyEpisode may become first-class if the use case requires:

- occurrence identity;
- participating moves;
- evidence;
- alignment across trajectories;
- supersession/revision.

Until then:

- Method represents reusable strategy/method;
- Example can represent reconstructed strategy occurrence;
- `part_of` links moves to reconstructed episode;
- `exemplifies` links episode to Method.

## 12. Inquiry alignment semantics

Cross-trajectory alignment must be governed separately from source graph
identity.

### Reuse established predicates only when exact

Examples:

- SKOS mapping relations for actual concept-scheme concepts;
- issue refinement for formal question refinement;
- erotetic implication for formal question progression;
- established argumentation support/attack semantics;
- PROV relations for actual provenance/derivation.

### Inquiry-local predicates require explicit semantics

Do not add terms such as:

- same_strategy;
- independent_convergence;
- continues_inquiry_episode;
- shared_ancestor;

until their intended semantics, role signatures, algebraic properties, and
non-equivalences are written down.

### No generic closure

No alignment predicate is assumed:

- symmetric;
- transitive;
- reflexive;
- substitutive;

unless its pack declaration explicitly says so.

## 13. Pack versus profile ownership

### Inquiry ontology pack owns

- semantic type vocabulary;
- relation vocabulary;
- role signatures;
- allowed participant types;
- cardinality;
- declared symmetry/directionality/algebra;
- imported external semantic mappings;
- Inquiry-specific semantic invariants.

### Inquiry profile owns

- open/closed/mixed vocabulary policy;
- review/activation rules;
- unknown-vocabulary handling;
- permitted alignment relation subset;
- selected global validators;
- identity/canonicalization policy;
- source-grounding publication requirements;
- automation versus human-review policy.

### OntoCanon kernel/governance owns

- generic relation/binding carrier;
- evidence/provenance mechanism;
- identity machinery;
- proposal/review/activation lifecycle;
- retraction/supersession history;
- validator contract;
- loss-aware projection.

## 14. Translation rule once the carrier settles

When OntoCanon ADR-0042/local carrier reconciliation is complete:

```text
this semantic contract
  -> authored OntoCanon Inquiry ontology pack
  -> Inquiry profile
  -> adapter from current Inquiry Graph V1
```

The adapter must preserve current executable semantics.

If an OntoCanon constraint language cannot express one current invariant, record
that as a profile/validator gap rather than silently weakening the Inquiry
semantics.

## 15. Change discipline

Changes to this semantic contract should answer:

1. Which inquiry requirement/use case requires the change?
2. Is there established prior art with exact semantics?
3. Does the change belong in the pack, profile, or kernel?
4. What current distinction would be lost if it were not added?
5. Does it alter the meaning of existing graphs, or only add a new optional
   semantic distinction?

Do not widen the ontology simply because an external standard contains more
terms.


## 16. Factorization / stance hypotheses remain representable, not primitive

The research formalism in [factorization-stance-agenthood-hypotheses.md](factorization-stance-agenthood-hypotheses.md) currently requires no new executable Inquiry type.

Represent factorization, stance, black-box/white-box, and agenthood proposals using existing Hypothesis/Method/Question objects plus candidate/support/challenge/dependency/reframing relations and inquiry moves.

Do not add Agent, Environment, FactorizationHypothesis, or StanceHypothesis as foundational Inquiry or OntoCanon kernel primitives merely because they are useful modeling concepts.

Promote a distinct Inquiry-pack term only if repeated real cases demonstrate that the current content/relation representation loses a required semantic distinction.
