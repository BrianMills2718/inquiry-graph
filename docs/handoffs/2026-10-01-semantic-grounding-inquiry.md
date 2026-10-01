# Semantic grounding inquiry checkpoint — 2026-10-01

## Status

This is a durable checkpoint of a live inquiry, not a validated transcript extraction and not a settled design. It records the current research direction so the inquiry can resume without relying on conversational memory.

The attempt to build a full repository-native continuation fixture locally reached an environment failure before validation: WSL became unavailable after the fixture files were prepared. Those local changes were intentionally left untouched rather than discarded. This note is the recoverable GitHub checkpoint.

## Core question

Can Linguistic Core become a more stable, comprehensive, and grounded semantic basis for neuro-symbolic AI and world modeling by factoring lexical/formal meanings through explicit lower-level semantic structures rather than treating ontology predicates as opaque canonical labels?

The motivating problem is recursive definitional dependence: dictionary-style definitions expand into more words whose definitions eventually form a cyclic semantic network. Cycles are not necessarily bad; the harder question is whether the network has explicit non-lexical grounding paths and whether those paths are preserved across representation changes.

## Current hypothesis

A useful architecture may have several distinct levels:

```text
phenomenal / psychophysical structure
  -> learned sensorimotor and similarity structure
  -> persistent object / event / affordance invariants
  -> grounded semantic factors
  -> structured concepts
  -> lexical senses
  -> formal predicates / models
```

Higher layers can also influence attention, categorization, and future sampling, so the full system is coupled rather than purely feed-forward.

Grounding should not mean "the one true definition." A definition may be disputed, culturally contingent, prototype-like, or application-specific while still being formally stabilized, decomposable, versioned, and traceable to lower-level structures.

## Phenomenal Meaning Generator

Phenomenal Meaning Generator is a candidate source for the lowest grounding layer. Its relevant commitments are:

- phenomenal states have similarity/difference structure;
- learning is sensitive to that structure;
- memory, association, reactivation, attention, temporal succession, and binding can generate learned structure;
- persistent proto-objects and categories should be derived rather than assumed;
- symbols attach to already structured meanings rather than creating meaning ex nihilo.

Psychophysics is relevant because it can constrain at least some phenomenal/perceptual geometry empirically, especially for color and other discriminable quality spaces.

## Chair as a test case

"Chair" should not be treated as a primitive.

A candidate factorization is:

```text
persistent object structure
+ support disposition / affordance
+ characteristic human-body interaction
+ participation in sitting events
+ artifact / conventional-use structure
-> chair concept
-> lexical sense "chair"
```

The point is not to establish a universally accepted chair definition. The point is to make the chosen definition an explicit semantic construction whose dependencies and grounding points are inspectable.

## Grounding IR proposal

Do not map Phenomenal Meaning Generator directly and exclusively into DOLCE.

Instead introduce a small neutral Grounding IR and project that IR into upper ontologies:

```text
Phenomenal / psychophysical evidence
  -> Grounding IR
  -> DOLCE
  -> BFO
  -> UFO
```

The ontology projections should not default to equivalence. A projection should record:

- source grounded factor;
- target ontology category or relation;
- mapping relation, such as structural analogue or licenses-classification-as;
- conditions;
- preserved structure;
- lost structure;
- unsupported commitments;
- provenance and review status.

This makes ontology differences useful evidence rather than a forced choice of one "correct" top-level ontology.

## Why DOLCE, BFO, and UFO all matter

Working hypothesis, subject to source verification:

- DOLCE is particularly relevant to phenomenal/perceptual grounding because of its treatment of qualities, qualia/regions, and quality spaces.
- BFO contributes strong distinctions around continuants/occurrents, qualities, roles, dispositions, and realization.
- UFO contributes rich object/event, relator, role, situation, social, and conceptual-modeling machinery.

The likely canonical factors should come from structures that survive, or whose losses are explicit, across several such projections rather than from inheriting one ontology's vocabulary wholesale.

## Semantic-basis prior art

Several existing traditions are directly relevant and should constrain rather than be reinvented:

- symbol grounding;
- Conceptual Spaces;
- DOLCE, BFO, UFO;
- Generative Lexicon;
- FrameNet and PropBank;
- OntoLex-Lemon;
- Natural Semantic Metalanguage (NSM);
- Longman Defining Vocabulary;
- grounded / embodied cognition;
- image schemas and affordance semantics.

A critical distinction is between three different notions that should not be collapsed:

1. **lexical primitive** — treated as irreducible within a lexical semantic system, e.g. an NSM prime;
2. **definitional basis** — selected because it is useful for defining a broad vocabulary, e.g. Longman's controlled defining vocabulary;
3. **grounding primitive** — selected because it has an explicit lower-level experiential, psychophysical, sensorimotor, or otherwise non-lexical derivation/measurement path.

A lexical primitive may still be high-level from the standpoint of grounding.

## Implication for Linguistic Core

The goal should not merely be to increase predicate count or force SUMO, PropBank, FrameNet, and other resources into direct equivalence.

A stronger target is a canonical semantic factorization in which donor senses map to compositions of stable factors:

```text
donor sense A -> {f1, f2, f3}
donor sense B -> {f1, f2, f4}
donor sense C -> {f1, f3}
```

This exposes overlap and disagreement mechanically.

Coverage can then be evaluated as coverage of semantic-factor space and grounded constructions rather than raw predicate count. Useful questions include:

- Which factors recur independently across donors?
- Which apparent synonyms differ by exactly one factor?
- Which donor distinctions are silently lost by a proposed equivalence?
- Which canonical factors are missing?
- Which predicates are symbolic islands with no grounding path?
- How much new factor novelty appears as domains are added?

This is a plausible neuro-symbolic boundary: neural systems can predict or infer grounded factors, while formal systems compose those factors into stable predicates and world-model structures.

## Recommended next experiment

Do not immediately redesign or republish Linguistic Core.

Build a small semantic-basis / grounding benchmark over approximately 20–25 concepts, for example:

```text
red, see, touch, move, part, place, body, someone, thing,
happen, do, support, inside, sit, chair, tool, cause, want,
know, same, different, before, because, number, measure
```

For each concept record:

1. whether NSM treats it as a prime or molecule;
2. whether it appears in the Longman defining vocabulary;
3. relevant FrameNet / PropBank / Generative-Lexicon-style structure;
4. candidate DOLCE / BFO / UFO projections;
5. proposed grounded factors;
6. explicit grounding path, or a declared gap;
7. information preserved and lost by each projection;
8. candidate Linguistic Core identity and donor mappings;
9. review status and provenance.

### Success criterion

The experiment succeeds if, for overlapping candidate definitions or semantic resources, the system can mechanically explain:

- what they share;
- what differs;
- what is grounded;
- what remains assumed;
- and what information would be lost by treating them as equivalent.

It does **not** need to discover the universally correct ontology or definition.

## Open questions

- What is the smallest useful Grounding IR?
- Which PMG primitives are genuine grounding primitives versus merely placeholders?
- Which psychophysical structures can actually be recovered empirically?
- How should learned invariants and affordances be represented without smuggling in the target concept?
- Which parts of DOLCE/BFO/UFO are projections of grounded structure, and which add independent metaphysical commitments?
- Can a finite semantic-factor basis stabilize, or does marginal factor novelty continue growing with domain expansion?
- Which factors are appropriate interfaces for learned neural representations?
- Should Scientific Hypergraph be the normalized carrier for GroundingClaim and OntologyProjection records?
- How should category/model/institution-theoretic preservation conditions be stated over these cross-level mappings?

## Immediate next action

Construct the benchmark schema and instantiate a very small first slice: **red, object, event, support, sit, chair**.

That slice spans phenomenal geometry, persistence, occurrence, affordance, bodily interaction, social/conventional categorization, lexicalization, and ontology projection. If those six cannot be represented coherently without hidden primitives, expanding to the larger benchmark is premature.

## Provenance / confidence boundary

This note summarizes a conversation plus assistant-led prior-art synthesis. It is not a primary-source literature review. External claims about specific frameworks must be independently checked before being promoted into an authoritative design. User goals and hypotheses are recorded as inquiry context; assistant proposals are not user-endorsed conclusions.
