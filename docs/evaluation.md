# Evaluation plan

## What is evaluated in V1

Unit and integration tests verify structural invariants and tool behavior: schema conformance; exact quote/offset matching; valid references and role signatures; actor/source consistency; event ordering; expected handling of cycles; exact-identity union; safe output handling; active-branch export import; rendering escaping; and mocked provider refusal/truncation behavior.

The founding graph is a **curated fixture**, not an independent benchmark. Generating a graph and testing it against the same curation shows replayability, not extraction accuracy. No live model accuracy, psychological validity, or benefit to reasoning has been measured in this release.

## Stage A: extraction fidelity

Construct a held-out corpus of diverse conversations with permission to process them. Split by conversation/person or task family, not random overlapping turns. Have two annotators independently identify content, roles, moves, stance and question state. Adjudicate disagreements while preserving alternative valid analyses where granularity differs.

Report at least:

| Measure | Definition / risk detected |
|---|---|
| Grounding precision | Fraction of quoted spans/positions that exactly match their source |
| Attribution accuracy | Correct actor and correct distinction among question, conditional proposal and endorsement |
| Relation fidelity | Relation label and role players supported by context; distinguish undercutting from attacking a claim |
| Move fidelity | Recorded operation and inputs/outputs supported by the dialogue, not invented mental steps |
| Open-question recall | Unresolved questions retained at the end of the source; report false closures separately |
| Revision retention | Explicit retractions/corrections preserved with original target and later stance |
| Identity error | False merges of similar but scoped-differently claims; missed links evaluated separately |
| Structural rejection rate | Fraction of model responses rejected by each validator code |
| Review burden | Human correction time and edits per accepted conversation graph |

Source grounding should be near-perfect by construction, but semantic interpretation can still be poor. Report both, rather than advertising 100% correctness because every quote exists. Numeric confidence should only be added after calibration against adjudicated examples.

Baselines: plain summary; untyped entity-relation extraction; argument-only AIF/IAT-style extraction; this inquiry-layer schema. Ablations: remove actor stance, remove move inputs/outputs, remove question events, remove source grounding, remove cross-turn context. Use the same underlying model and comparable context/cost budgets.

## Stage B: usefulness for inquiry navigation

Measure whether a user can find an unresolved dependency, recover a correction, distinguish an assistant suggestion from their own endorsement, and resume an interrupted question. Compare raw transcript search, summary, concept graph, and inquiry graph. Use completion accuracy, time and mistaken closure/attribution—not only user preference or visual appeal.

Privacy constraints should be evaluated alongside utility. A false belief attribution in a personal worldview tool may matter more than a missing peripheral concept. Keep user review and deletion/export controls on the roadmap before broader deployment.

## Stage C: warrant annotation and discrimination

Before treating warrant as an executable or learnable layer, test whether annotators can reliably distinguish **support**, **warrant**, **license**, and **executed update** in grounded examples. Require explicit identification of the epistemic action being licensed, applicability assumptions, warrant regime, certificate/support object, and typed guarantee. Include deductive, defeasible, statistical, measurement/testimony, transition, and strategy-selection cases.

Evaluate common confusions separately: support mistaken for sufficient warrant; formal validity mistaken for content acceptance; license mistaken for actual update; assumptions hidden inside an unqualified guarantee; heterogeneous guarantees collapsed into one confidence score; and defeaters ignored. Agreement on the action target and guarantee type is more important than agreement on philosophical terminology.

## Stage D: strategy-episode annotation

Before learning policies, evaluate whether humans can reliably identify reusable reasoning strategies from grounded move sequences. Annotate strategy schema, episode boundaries, target (`about` relation), nested episodes and confidence/review status. Compare agreement on atomic moves with agreement on higher-level strategies; strategy segmentation is expected to be harder and may admit multiple defensible granularities.

Candidate strategies in the founding dialogue include canonical factorization, counterexample search, literature-before-invention, meta-model stress testing, goal restoration and reflective self-application. These labels are hypotheses to validate, not a complete strategy ontology.

Important error classes include hallucinating a private strategy from surface similarity, collapsing an isolated move into a full multi-step strategy, missing nested/meta episodes, and treating the same strategy name as intrinsically meta-level instead of relative to its target.

## Stage E: learning policies over reasoning moves and strategies

Only after reliable representation, compare policies over inquiry operations and strategy selection. Define task families with independently checkable outcomes, budgets and permissible actions. A policy can choose to seek a counterexample, inspect an assumption, clarify a term, test a prediction, decompose a question, activate a factorization strategy, or switch strategies. Graph annotations are observations of expressed behavior, not privileged access to computation.

Use randomized intervention studies or controlled ablations where feasible. Correlation between a move or strategy and success is not proof it caused success: difficult problems may provoke more reframing, reflection and failures. Control for task difficulty, model, token/tool budget and access to evidence. Hold out entire task families for transfer evaluation.

Outcomes may include answer correctness, calibration, error discovery, robustness to perturbed premises, evidence quality, strategy-switch efficiency and total cost. Rational-metareasoning objectives such as value of computation are candidate evaluation models, not foundational assumptions. Do not optimize a persuasion or aesthetic-preference score as a surrogate for epistemic reliability. No universal “best thinking sequence” is assumed; conditional policies are the target.

## Release evidence

Exact test counts and commands belong in `docs/verification.md` and the linked CI run. The optional provider adapter is protocol-tested with a fake client; the API boundary has not been tested with a paid live request. No human-reviewed belief map or learned policy is claimed.
