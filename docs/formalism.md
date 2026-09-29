# Formalism: an attributed inquiry hypergraph

## 1. Object of representation

The subject is **expressed inquiry reconstructed from records**. It is not an agent's inaccessible internal cognition. Let

`G = (C, P, X, N, R, M, S, Q, A, E)`

where C are conversations; P participants; X ordered source messages; N content objects; R reified semantic/argument relations; M inquiry-move activities; S stance events; Q question-status events; A source anchors; and E extraction metadata. Every non-source object has a stable identifier, anchors, an explicit/inferred annotation flag, and a proposed/confirmed/rejected review flag.

`kind : N → {concept, claim, question, hypothesis, method, example, goal, reference}`

These are pragmatic annotation classes, not a complete ontology of thought. “Observation” is not a magical access-to-reality type: an observation report is a source-grounded claim/example whose evidential use is represented by a relation.

## 2. Reification and role players

A relation is `r = (id, type, {(role_i, object_i)}, anchors, annotation_state)`.

Its signature specifies allowed role names, participant types, and cardinality. For example:

`support(premise: {p1, p2, ...}, conclusion: c)`

This is not equivalent to separate independent edges `p1 supports c` and `p2 supports c`: linked premises may support a conclusion jointly. A challenge may target that support relation itself, distinguishing criticism of a warrant from denial of a premise or conclusion. A derived bipartite view creates a vertex for the relation. The same data can later map to TypeDB relations and role players; V1 needs no TypeDB server.

A move is `m = (kind, actor, inputs*, outputs*, source_occurrence, after*, anchors, state)`.

Inputs and outputs can reference content, relations, or moves. A distinction can produce two concepts; a reframing can take one question to another; a challenge can target an inference. Move kinds and the optional induction/abduction/deduction tags are descriptive vocabularies, not claims to exhaustive primitives or truth preservation.

## 3. Source grounding

An anchor `a = (message_id, start, end, quote)` is valid exactly when

`0 ≤ start < end ≤ len(message.text)` and `message.text[start:end] = quote`.

Offsets count Unicode code points, not bytes or UTF-16 code units. The `anchor()` helper finds exact occurrences and rejects an ambiguous repeated quote unless an occurrence is selected. Imported source IDs come from the export; curated excerpt IDs are explicitly local surrogates. Source ordering is preserved independently of semantic relation direction.

Grounding establishes that an annotation points to actual text. It does not prove the annotation correctly interprets that text. A model can attach a real quote to an unreasonable claim; human review and evaluation must address that separate failure mode.

## 4. Stance is relative to an actor

`stance_event = (actor, target, stance, occurrence, anchors, review_state)`.

“Posits,” “endorses,” “questions,” “rejects,” “suspends,” and “retracts” have different meanings. A position can be entertained conditionally. An assistant's statement must not become the user's belief merely because the user continued the discussion. Even an assertion records a public act, not proof of sincere private belief.

V1 preserves the full stance history in `trace`. It does not collapse it to a single worldview truth score. A rejected annotation is also different from a participant rejecting a hypothesis: the former says the extraction was wrong, the latter is content within the inquiry.

## 5. Question state and an open agenda

Question events are scoped by `(question, actor, conversation)`. Within a scope, the latest non-rejected event by source ordinal is the current recorded state. The code never compares an ordinal in one conversation with an ordinal in another as if they were a universal clock.

`status ∈ {open, answered, resolved, deferred, superseded, reopened}`.

An `answers` relation identifies a proposed response. An `answered` status does not imply sufficient resolution. A resolved event requires answer references or an explicit resolution basis; a superseded question requires another question. Only a **confirmed** resolved/deferred/superseded status removes that scope from the open agenda. A proposed closure remains visible for review. A question without active status annotations is displayed as unclassified, not silently considered settled.

This is a conservative retrieval rule, not a proof of “what Brian should think about next.” Ranking by number of dependencies is not the same as expected value of information. V1 provides the agenda; a principled ranking policy is a later experimental feature.

## 6. Time, feedback, and coherence

`after` is a strictly earlier within-conversation relation between moves; its directed graph must be acyclic. V1 rejects cross-conversation after-links because no cross-chat clock or causal ordering is established. Supersession must also be acyclic. Semantic dependencies and inference-feedback relations may cycle; a dependency cycle produces a warning, not rejection of the entire graph.

“Coherent” in V1 means executable structural invariants hold. It does not mean all claims are consistent with one another. Retaining `claim X`, `challenge to X`, and `retraction of X` is often the point. No classical explosion rule is applied to contradictory recorded statements.

## 7. Persistence and aggregation

Canonical snapshots are JSON documents under Git. New reasoning occurrences receive new IDs. An evolving inquiry can be written `G_t → G_(t+1)`, with earlier snapshots recoverable by commit. This is **not** a fully event-sourced database: review metadata can be changed in a review commit; Git supplies that change history and author. There is no concurrent distributed review protocol in V1.

Merge is an exact-identity union: identical records at the same ID collapse; different records at the same ID produce a hard conflict. Similar wording never automatically identifies two beliefs, questions, or people. Cross-chat identity reconciliation is an explicit future step, not a cosine-similarity threshold hidden inside “merge.”

## 8. Conditional usefulness, not an axiomatic theory of learning

The graph supports asking which states and moves are associated with better outcomes. A policy could be written `π(move | expressed_state, history, task)`. V1 neither learns that policy nor equates observed move sequences with the model's actual computation. Empirical comparisons need independent task outcomes, matched baselines and held-out tasks. The representation makes such work possible without claiming to solve induction, abduction, or the metaphysics of observers.

## 9. Research formalism versus graph ontology

The later dialogue develops a separate research proposal for factoring epistemic states, candidate generation, reasoning operators, strategy control and warrant. The state-delta stage is preserved in [epistemic-transition-calculus.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/epistemic-transition-calculus.md), the assumption-context stage in [assumption-context-meta-model.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/assumption-context-meta-model.md), the strategy/reflection stage in [metareasoning-strategy-reflection.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/metareasoning-strategy-reflection.md), the candidate-generation interface in [candidate-generation-interface.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/candidate-generation-interface.md), the warrant refactoring in [warrant-license-interface.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/warrant-license-interface.md), the action/support refinement in [epistemic-actions-support-algebra.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/epistemic-actions-support-algebra.md), the defeat/argumentation integration in [defeat-argumentation-integration.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/defeat-argumentation-integration.md), the ABA/ASPIC+ decision benchmark in [aba-aspic-benchmark.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/aba-aspic-benchmark.md), the argument-identity decision in [argument-identity-boundary.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/argument-identity-boundary.md), and the current preference-regime boundary in [preference-regimes.md](https://github.com/BrianMills2718/epistemic-warrant/blob/main/docs/preference-regimes.md). None should be confused with the executable inquiry-graph schema above. The graph records those proposals, objections and revisions; it does not enforce the research calculus as its own ontology.

The current research endpoint keeps positive support and defeasible acceptability in separate layers. Positive ATMS-style support uses the finite-antichain/free-distributive-lattice algebra of minimal assumption environments. Supported arguments can then participate in typed conflicts (rebut, undercut, undermine, or ABA-style contrary attacks); successful attacks become defeats, and a Dung-style abstract argumentation layer determines acceptability. The first executable semantics is grounded semantics, implemented separately from the inquiry-graph ontology. Warrant remains `W; A |-π a : G`, with acceptability of the supporting certificate/argument as an additional condition in defeasible regimes. The six-case ABA/ASPIC+ benchmark selects an ABA-like executable attack-construction bridge while retaining ASPIC+-compatible metadata for rebut/undercut/undermine origin, rule applicability, and preference provenance. That basic ABA core is now implemented with Horn-style closure over minimal-support antichains, explicit assumptions/contraries, typed attacks, and projection to the Dung defeat layer. Argument identity is explicitly quotiented by conclusion + supporting assumption environment for ABA/ABA+ semantics; formal proof/derivation identity remains a separate richer layer and becomes mandatory only if later semantics distinguish derivations with the same quotient. The current binary preference regime filters ABA attacks when the attacking support contains an assumption strictly less preferred than the attacked assumption, with blocked attacks retained as audit records. This is deliberately not full ABA+: full attack reversal is tracked separately because general ABA+ is set-to-set and may require a hyperargumentation layer. The first executable warrant specialization now consumes grounded acceptability, but only for typed defeasible actions/guarantees, and derives a current license only when explicit applicability assumptions are satisfied. A second executable regime now warrants recording an independently modeled support probability while explicitly refusing to turn that number into acceptance. A checked strict-Horn deductive regime licenses derivation relative to explicit premises without licensing premise acceptance. Narrow measurement and testimony regimes now license only model-relative result/posterior recording with uncertainty, calibration and source/reference-class assumptions explicit. A finite-class statistical regime now records a Hoeffding/union-bound generalization bound under explicit sampling assumptions. A strategy-performance regime now warrants selecting a strategy only when a paired bounded-utility benchmark yields a strictly positive lower confidence bound over the declared task class, while the source-grounding and graph-validation rules in sections 1–7 are implemented contracts.
