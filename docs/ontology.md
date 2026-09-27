# Ontology and annotation roles

The executable contract is [`src/inquiry_graph/model.py`](../src/inquiry_graph/model.py); generated JSON Schemas are in [`schemas/`](../schemas). This document explains semantics rather than introducing a second schema.

## Layers

| Layer | Records | Distinction preserved |
|---|---|---|
| Source | Conversation, Participant, Message, Anchor | What is actually in the record versus the analyst's interpretation |
| Content | Node | Concept, claim, question, hypothesis, method, example, goal or reference |
| Argument/semantic | Relation, Binding | Role-typed connection, including an inference that can itself be challenged |
| Inquiry process | Move | Who asked, clarified, reframed, challenged or retracted, using what inputs and outputs |
| State history | StanceEvent, QuestionEvent | Actor-relative position and open-question status, separately |
| Extraction/review | Extraction; grounded-record metadata | How graph annotations were produced and whether reviewed |

A content node is not identical to an utterance: repeated utterances may express the same claim, and one utterance can express multiple claims. V1 demands explicit identity decisions rather than automatically merging repeated paraphrases.

A question is a node kind. “Unresolved” is a state recorded by events, not a node kind. “Hypothesis” does not mean endorsed. “Rejected extraction” does not mean false proposition. These separations correct conflations present in our initial conversational sketches.

## Relation signatures

Each role occurs exactly once except `supports.premise`, which may occur more than once. Duplicate `(role, ref)` pairs are invalid. `any` below means content node, relation, or move—not source messages or status events.

| Relation | Input role → output role | Permitted players |
|---|---|---|
| supports | premise → conclusion | premise: claim/hypothesis/example; conclusion: claim/hypothesis |
| challenges | challenger → target | challenger: claim/hypothesis/example/question; target: any |
| depends_on | dependent → prerequisite | any → any |
| distinguishes | left → right | any → any; display orientation is not logical asymmetry |
| reframes | original → replacement | question → question |
| motivates | reason → result | any → any; interpreted motivation, not proven causation |
| answers | answer → question | claim/hypothesis/method/example → question |
| exemplifies | example → general | example → any |
| candidate_for | candidate → problem | any → question/goal |
| part_of | part → whole | any → any |
| about | subject → object | any → any; explicit semantic target for reflective/meta-level analysis |
| related_to | source → target | any → any; display orientation only |
| supersedes | new → old | any → any; acyclic |

A challenge need not refute its target. It can question its applicability or sufficiency. Where that distinction matters, an annotator should add a more precise claim and target the exact relation rather than labeling a whole concept “wrong.” V1 deliberately uses a small vocabulary; later specializations need fixtures and review, not arbitrary edge strings.

## Moves

`ask`, `clarify`, `distinguish`, `challenge`, `retract`, `hypothesize`, `generalize`, `deduce`, `test`, `reframe`, `decompose`, `connect`, `scope`, `summarize`, `propose`.

A move has actor, inputs, outputs, occurrence, anchors, and optional previous-move IDs. A `retract` move and a `retracts` stance event are related but not redundant: one is the episode/process record, the other is an actor's change toward a particular target. They can share anchors.

The optional `inference_family` is `induction`, `abduction`, `deduction`, or `unspecified`. The seed leaves it unspecified: adjudicating the exact taxonomy was itself disputed. A graph can describe the dispute without settling it in its annotation scheme.

## Strategy and reflection annotations

The executable graph still has no dedicated `StrategyEpisode` record. For the current research pass, reusable strategies are represented as `method` nodes and reconstructed strategy occurrences as grounded `example` nodes. Atomic moves can be linked to an episode with `part_of`; an episode can `exemplify` a strategy method. The `about` relation records the explicit target of reflective/meta-level reasoning.

This is deliberately conservative. Strategy attribution remains a proposed analyst interpretation of public dialogue, not a claim that the graph directly observes a participant's private control state. A later schema may reify strategy episodes if span-level strategy analysis becomes central.

## Example: imagination

A hypothesis node records the assistant's suggestion. The user's challenge is another node and a challenge move. The assistant's response generates a revised claim and a retracts stance event toward the earlier suggestion. The user need not be assigned an endorsement of either proposition. The question can be answered in the assistant's scope while remaining open in the user's scope.

## Standards alignment—not interchange conformance

AIF/IAT contributes the distinction between informational content, argumentative relationships, locutions, transitions, and anchoring. PROV-O contributes the conceptual separation of entities, activities and agents. Web Annotation contributes source-selection concepts. SKOS offers a useful reference for controlled concept vocabularies. These are correspondences; this JSON format is **not** a complete AIF, RDF, PROV-O, Web Annotation, or TypeDB serialization.

A future TypeDB mapping is direct in shape: content records as entity subtypes, reified argument relations with named roles, move activities with input/output/actor roles, occurrence/anchor records, and stance relations connecting actor and target. No untested TypeQL schema is presented as deployable V1. See [ADR-001](decisions/001-reified-inquiry.md) and [references](references.md).
