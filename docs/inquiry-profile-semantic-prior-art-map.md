# Inquiry Profile Semantic Prior-Art Map

**Date:** 2026-09-29  
**Status:** research/specification note; no executable profile yet  
**Carrier dependency:** proposed OntoCanon general governed semantic carrier  
**Empirical rule:** no benchmark or comparative empirical evaluation without explicit Brian approval

## Purpose

Identify which Inquiry Graph semantics should be imported from established
theories/standards and which are genuinely inquiry-specific.

The goal is to avoid inventing a bespoke ontology where mature semantics already
exist.

This document concerns **domain semantics**, not storage.

## Architectural assumption

The intended shape is:

```text
OntoCanon kernel
  generic semantic carrier + governance

Inquiry ontology pack
  inquiry-domain object/relation semantics

Inquiry profile
  policy, validation, alignment/integration configuration

Inquiry Graph instances
  source-grounded concrete inquiry trajectories
```

The pack/profile should reuse established semantics where they fit and retain
local predicates only where their intended meaning is genuinely different.

## 1. Provenance and source grounding

### Current Inquiry Graph semantics

- Conversation
- Participant
- Message
- Anchor
- annotation origin
- review status

### Prior art

W3C PROV-O provides a general provenance model centered on:

- Entity
- Activity
- Agent
- derivation
- attribution
- use/generation
- association

PROV-O is intentionally extensible for domain-specific provenance.

Reference:

- https://www.w3.org/TR/prov-o/

### Disposition

**Reuse as interoperability/reference semantics, not as the Inquiry carrier.**

Inquiry Graph has source-specific needs that are more concrete than generic
PROV-O:

- exact message identity;
- exact Unicode span;
- quote;
- conversational ordinal;
- annotation origin/review status.

Keep those native Inquiry/source semantics, but provide a clean PROV projection
where useful.

Do not reinterpret semantic relations such as `supports` as PROV derivation
merely because both involve dependency.

## 2. Concept mapping and cross-trajectory concept alignment

### Relevant Inquiry objects

- Concept
- Method
- Reference
- some Goal/Hypothesis abstractions

### Prior art

SKOS defines cross-scheme mapping predicates:

- `skos:exactMatch`
- `skos:closeMatch`
- `skos:broadMatch`
- `skos:narrowMatch`
- `skos:relatedMatch`

It explicitly distinguishes exact, close, hierarchical and associative mapping
semantics.

Reference:

- https://www.w3.org/TR/skos-reference/#mapping

### Disposition

Use SKOS mapping semantics **only when the aligned Inquiry objects function as
concept-scheme concepts**.

Do not use:

- `skos:broadMatch` as a generic substitute for question refinement;
- `skos:exactMatch` as a generic instance identity relation;
- SKOS predicates for moves/events merely because they are pairwise.

## 3. Questions and issue structure

### Current Inquiry Graph semantics

- Question node
- QuestionEvent state history
- `answers`
- `reframes`
- candidate question decomposition/progression semantics

### Prior art: inquisitive semantics

Inquisitive semantics gives a formal notion of **issues** and defines relations
including when:

- an information state resolves an issue;
- one issue is a refinement of another;
- a proposition supports/resolves relevant information.

This is substantially closer to the semantics of "one question is a more
specific/refined issue than another" than generic SKOS broader/narrower.

Reference:

- Ciardelli, Groenendijk, Roelofsen, *Inquisitive Semantics*
- https://academic.oup.com/book/35968
- basic notions / issue refinement:
  https://academic.oup.com/book/35968/chapter/311287548

### Prior art: inferential erotetic logic

Inferential erotetic logic provides formal relations including:

- question evocation;
- erotetic implication.

Erotetic implication is relevant when one question follows from another
question plus declarative premises in a way that advances inquiry.

Reference:

- Wiśniewski, work on inferential erotetic logic
- example open-access formal treatment:
  https://link.springer.com/article/10.1007/s11225-017-9738-8

### Disposition

Do **not** make one vague local `refinesQuestion` relation carry every form of
question progression.

Likely distinctions:

1. **issue refinement** — answering/resolving the refined issue settles the
   coarser one in the intended formal sense;
2. **erotetic implication / inquiry progression** — one question is a useful
   inferential successor given premises;
3. **reframing** — same practical inquiry is recast under a different
   factorization/conceptualization;
4. **replacement/supersession** — workflow/state relation, not question
   semantics.

Current Inquiry `reframes` should remain local unless/until its semantics are
proved reducible to a formal issue relation.

## 4. Argument structure

### Current Inquiry Graph semantics

- `supports`
- `challenges`
- relation-as-target
- premise/conclusion roles
- Moves that challenge/deduce/hypothesize/etc.

### Prior art: Argument Interchange Format

AIF separates informational content from argument/inference structure and
supports interlinked argument networks.

AIF work explicitly supports attacking/supporting parts of existing arguments
and reusing argument components.

Reference:

- Rahwan, Zablith, Reed, "Laying the foundations for a World Wide Argument Web"
  https://doi.org/10.1016/j.artint.2007.04.015

### Prior art: abstract/bipolar/recursive argumentation

Relevant established distinctions include:

- attack;
- support;
- argument acceptability;
- bipolar support + attack;
- recursive attack/support where the target may itself be an attack/support
  relation.

### Disposition

Treat current Inquiry `supports` / `challenges` as candidates for mapping to
established argumentation semantics, but do not force equivalence prematurely.

Important Inquiry-specific distinctions to preserve:

- a challenge need not be a logical rebuttal;
- it may target applicability, sufficiency, framing, or one role assignment;
- a support relation may be evidential, inferential, explanatory, or
  motivational.

Therefore the Inquiry pack may ultimately specialize `supports` and
`challenges` rather than treating them as semantically atomic.

Relation-as-participant and RoleBinding-as-participant are carrier requirements,
not argumentation-specific hacks.

## 5. Moves / dialogue acts

### Current Inquiry moves

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

### Prior art

AIF/AIF+ and dialogue/argumentation work provide useful distinctions between:

- informational content;
- locutions;
- transitions;
- inference/argument schemes;
- dialogue moves.

Speech-act/dialogue-act standards and taxonomies are relevant prior art, but
there is no reason to force the current Inquiry move vocabulary into one external
taxonomy unless its semantics match.

### Disposition

Keep `InquiryMove` as an Inquiry-domain process relation.

Before adding new move types:

1. check dialogue-act / argumentation prior art;
2. distinguish a **move occurrence** from the semantic content it creates;
3. distinguish a move type from a reusable strategy/meta-strategy.

No separate generic carrier primitive is needed.

## 6. Stance

### Current semantics

`StanceEvent` records:

- actor;
- target;
- stance;
- occurrence.

This is separate from the truth/status of the target.

### Prior art

Argumentation, provenance and epistemic-state models all contain adjacent
machinery, but none should be imported merely by name.

### Disposition

Retain actor-relative stance as an explicit Inquiry semantic relation.

Core invariant:

```text
actor stance toward X != truth/status of X
```

Cross-trajectory integration must never collapse stance-bearing occurrences just
because their targets align.

This is likely Inquiry-specific policy over a generic relation structure.

## 7. Question state

### Current semantics

`QuestionEvent` carries:

- question;
- status;
- actor;
- occurrence;
- answers;
- resolution basis;
- replacement.

### Prior art

Inquisitive semantics gives semantics for issues and resolution, but it does not
by itself encode the operational history of an inquiry conversation.

### Disposition

Keep QuestionEvent as an Inquiry workflow/state relation.

Where possible:

- use formal issue semantics to define what counts as semantic resolution;
- keep conversational/workflow statuses distinct from formal semantic
  resolution;
- preserve actor scope.

Example:

```text
answered for assistant
!= resolved for user
!= logically settled issue
```

## 8. Current semantic relation inventory

| Inquiry relation | Prior-art candidate | Current disposition |
|---|---|---|
| `supports` | AIF / bipolar argumentation / proof-support relations | **Retain; likely specialize later.** Current meaning is intentionally broad. |
| `challenges` | attack/rebut/undercut / recursive argumentation | **Retain; likely specialize later.** Challenge is broader than refutation. |
| `depends_on` | dependency / prerequisite vocabularies | **Retain local generic relation** until a more precise semantics is declared. |
| `distinguishes` | no single standard equivalent | **Retain Inquiry-local.** Symmetric conceptual differentiation, not inequality identity. |
| `reframes` | issue reformulation / discourse transition | **Retain Inquiry-local** pending formal semantics. |
| `motivates` | provenance/causal/influence vocabularies are only partial analogues | **Retain local.** Do not misstate as causation. |
| `answers` | erotetic/inquisitive answer-resolution semantics | **Map conceptually; retain relation with stronger formal constraints later.** |
| `exemplifies` | SKOS/example/instance-style relations only partially fit | **Retain local unless type semantics make standard relation exact.** |
| `candidate_for` | hypothesis/problem relation; no universal standard | **Retain Inquiry-local.** |
| `part_of` | mereology / Dublin Core / PROV collections depending object type | **Profile specialization needed.** Avoid one universal semantics if composition types differ. |
| `about` | topic/aboutness vocabularies | **Retain simple reflective relation** unless a precise imported predicate fits. |
| `related_to` | SKOS related / generic association | **Use sparingly; candidate for deprecation if more precise relations cover uses.** |
| `supersedes` | PROV invalidation/revision/versioning analogues | **Retain governed lifecycle relation; consider PROV projection.** |

## 9. Cross-trajectory alignment relations

The alignment vocabulary should be derived from established semantics before
introducing local terms.

### Reuse where exact

- concept exact/close/broad/narrow mapping: SKOS where object semantics qualify;
- genuine logical/class identity: OWL/RDFS where object semantics qualify;
- issue refinement: inquisitive semantics;
- question progression: erotetic implication where formal conditions hold;
- argument support/attack: established argumentation semantics where exact;
- provenance/derivation: PROV-O where exact.

### Do not add yet without demonstrated gap

- `sameStrategy`
- `sameMethodFamily`
- `continuesInquiryEpisode`
- `independentConvergence`
- `sharedAncestor`

These may be legitimate Inquiry predicates, but their semantics should be
specified from actual use cases and prior art before they become pack
vocabulary.

## 10. What is genuinely custom today

The clearest current Inquiry-specific semantic commitments are:

1. source-grounded reconstruction of public inquiry episodes;
2. actor-relative stance separated from target truth;
3. operational question-state history separated from semantic question content;
4. InquiryMove as a process occurrence distinct from its inputs/outputs;
5. reframing as an explicit inquiry transformation;
6. reflective relations where inquiry can target its own moves/relations;
7. strategy/meta-strategy attribution as reviewed analyst interpretation rather
   than direct access to private control state.

These are good candidates for the Inquiry pack/profile.

## 11. Pack/profile design rule

For every proposed Inquiry predicate/type:

```text
intended semantics
  -> established prior-art candidate
  -> exact fit? use/import it
  -> partial fit? specialize/map explicitly
  -> no fit? define Inquiry-local term with invariants
```

Do not choose vocabulary based on convenient labels alone.

Do not use an external ontology term when its formal semantics are materially
different merely to maximize standards reuse.

## 12. Next action after OntoCanon carrier reconciliation

Once ADR-0042/local carrier reconciliation settles the kernel contract:

1. turn the existing Inquiry Graph ontology into an authored Inquiry ontology
   pack;
2. define profile-level policy separately;
3. annotate each imported/mapped external semantic term with provenance;
4. preserve local Inquiry terms only where the prior-art map above shows a real
   semantic gap;
5. keep both existing inquiry trajectories as source-grounded proving instances.

No benchmark is required for this semantic design work.
