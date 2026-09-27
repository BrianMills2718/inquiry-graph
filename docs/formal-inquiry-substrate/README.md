# Formal Inquiry Substrate

**Companion graph:** [second inquiry trajectory](../../examples/formal-inquiry-2026-09-27/report.md) · [canonical JSON](../../examples/formal-inquiry-2026-09-27/graph.json) · [map](../../examples/formal-inquiry-2026-09-27/inquiry-map.md)

This is the fresh-agent handoff from the 2026-09-27 conversation about a possible **general formal substrate of inquiry**. It belongs in Inquiry Graph because the target is broader than any one analytic method: the same substrate should describe conceptual dialogue, statistical analysis, causal inference, experimentation, control, strategic interaction, and model/query revision.

This is **not a claim of novelty**. The working assumption is that most or all of the pieces are already well trodden; the task is to locate the smallest established synthesis and identify any genuinely missing structure.

See also the repository's existing [formalism](../formalism.md), [epistemic transition calculus](../epistemic-transition-calculus.md), [assumption-context meta-model](../assumption-context-meta-model.md), [metareasoning/strategy/reflection extension](../metareasoning-strategy-reflection.md), and [post-V1 research log](../research-log-post-v1.md).

## Current thesis

Do not take these as fundamental primitives without argument:

- agent versus world;
- internal versus external;
- observation versus intervention;
- measurement versus experiment;
- reasoning versus physical action.

Treat them first as distinctions induced by a chosen factorization, coarse-graining, stance, policy objective, or task.

The working slogan is:

> **canonical substrate, non-canonical factorizations, explicit relations between factorizations.**

Start instead with:

1. an evolving process/state space;
2. a chosen representation or factorization;
3. a model class relative to that representation;
4. a query / epistemic target;
5. operations that may change the process, the representation, the model class, the query, or the history;
6. a policy for selecting operations;
7. update and answer rules;
8. a typed warrant relation saying what conclusions are licensed under which assumptions.

## Trajectory of the conversation

### 1. Peirce, Pearl, Dennett, and Levin were initially conflated

The conversation began by trying to line up:

- Peirce: abduction, deduction, induction;
- Pearl: association, intervention, counterfactuals;
- Dennett: physical, design, intentional stances;
- Michael Levin: axis of persuadability;
- ontology/conceptualization and model choice.

The first useful correction was that these are **different dimensions**, not one ladder.

A more stable decomposition is:

- **inference operations**: deduction, induction, abduction, updating, model selection;
- **query/claim types**: description, association, prediction, causation, counterfactual, mechanism, goal, control;
- **representation/model class**: what variables, entities, boundaries, levels, goals, beliefs, or policies are admitted;
- **interaction policy**: how information is generated or the process is changed;
- **warrant**: what assumptions license which moves and claims.

Pearl's ladder is therefore one family of query semantics, not a universal hierarchy of inquiry.

### 2. Dennett became a representation/model-class idea

Dennett's stances are useful as candidate modeling strategies:

- physical/mechanistic;
- design/functional;
- intentional/agentic.

The important formal lesson is not to install these as ontological strata. A stance may reduce to a policy over representations, latent variables, and model classes.

This matters because the set of warranted analytic moves changes with the assumed kind of target.

### 3. Levin became the control-side complement

Levin's axis of persuadability suggested a complementary question:

- at what level does a description predict or compress well?
- at what level does an operation successfully steer the process?

This looks promising as a connection between abstraction and controllability, but should be mapped to established control/game-theoretic notions before introducing bespoke machinery.

### 4. Methodology and warrant became central

A useful working definition:

> An analytic methodology is a rule-governed policy for transforming an epistemic situation into a claim, together with the assumptions under which that transformation is warranted.

This is broader than "run a regression" or "use Bayesian inference." It includes representation, evidence-generation policy, update rule, answer rule, and guarantee/refusal conditions.

The key object became a **space of warranted analytic moves**.

### 5. Observation versus intervention was demoted

The conversation rejected observation/intervention as a foundational physical split.

Every observation is physically an interaction. A better distinction is functional/intentional:

- **measurement**: interaction chosen mainly for information, often with a constraint on relevant disturbance;
- **intervention**: interaction chosen mainly to change a target process;
- **experiment**: structured interaction chosen mainly to discriminate among hypotheses / answer a query;
- **probe**: interaction chosen for epistemic discrimination;
- **communication**: interaction modeled as changing another agent's informational or policy state.

These roles can overlap. The same physical act can be measurement, intervention, and experiment under different objectives or descriptions.

Quantum measurement was raised as a vivid reminder that "measurement" cannot simply mean "no causal influence."

### 6. Strategic/reactive targets exposed the real issue

Suppose a target changes behavior because it knows it is being observed.

A passive model might use

\[
P(o\mid \theta),
\]

while a strategic model may require

\[
P(o\mid \theta,\pi_A,h),
\]

where the evidence-generating process depends on the analyst's policy and interaction history.

The statistical machinery can remain mathematically correct while the intended estimand is no longer identified.

This is a central example:

> The same nominal analytic move may be warranted under one model class and unwarranted under another.

### 7. Queries became explicit

A query is the epistemic target: which distinctions among possible models/worlds matter for the inquiry.

In the simplest form:

\[
q:\mathcal M_F\to\mathcal Y.
\]

Two models are equivalent for the query when

\[
M\sim_q M' \iff q(M)=q(M').
\]

Association, prediction, causal effect, counterfactual, mechanism, goal inference, and decision/control are different query families over the same substrate.

### 8. Agent/world became a factorization

The largest conceptual move was recognizing that even perceptual/internal versus external space need not be primitive.

A factorization may identify some degrees of freedom as:

- analyst;
- target;
- environment;
- memory;
- observation channel;
- tool;
- other agent.

At a finer description these are all parts of one coupled process.

So the substrate should be able to describe both "internal reasoning" and "external action" using the same transformation machinery.

## Required stress test

A successful formalism should describe, with the same primitives:

- reading a dataset and fitting a regression;
- selecting a randomized experiment;
- asking a causal or counterfactual question;
- probing a reactive or adversarial actor;
- changing a model class after failed prediction;
- changing an ontology or coarse-graining;
- proving something;
- asking another scientist or LLM a question;
- revising the query itself;
- this conversation.

If conceptual inquiry requires an entirely separate formal machinery from statistical or causal inquiry, the proposed substrate is probably too narrow.

## Current concerns

1. **Reinventing established theory.** Relevant machinery already exists across statistical decision theory, Blackwell/Le Cam experiment comparison, POMDP/POSG theory, dynamic epistemic logic, epistemic planning, causal inference, experimental design, causal games, adaptive data analysis, causal abstraction, and formal theories of questions.
2. **Overloading "stance."** Dennett may be conceptually useful while adding no new primitive beyond factorization/model-class choice.
3. **Overclaiming invariance.** Coarse-graining can destroy information. The right target is query-relative equivalence or sufficiency, not invariance under arbitrary cuts.
4. **Query drift.** Real inquiry changes the question itself.
5. **Model-language drift.** Real inquiry can replace the model class or representation, not merely update parameters.
6. **Heterogeneous warrant.** Logical entailment, statistical error control, Bayesian posterior claims, causal identification, regret, robustness, equilibrium, and qualitative evidential adequacy are not one scalar notion.
7. **Vacuity risk.** "Everything is an operation" is useless unless the formalism recovers meaningful types, invariants, guarantees, and refusal conditions.

## Recommendation to the next agent

Assume the territory is well trodden until shown otherwise.

Try to reduce the substrate to established mathematics in roughly this order:

1. statistical experiments / decision theory;
2. Blackwell sufficiency and Le Cam deficiency;
3. POMDP/POSG or controlled stochastic processes;
4. dynamic epistemic logic / epistemic planning;
5. structural causal models and causal identification;
6. causal games / game theory for strategic response;
7. causal abstraction, bisimulation, and sufficient-statistic ideas for representation changes;
8. active learning / Bayesian experimental design for probe selection;
9. erotetic logic / inquisitive semantics for question structure and revision.

The most important open technical seam is:

> Can we define **inquiry-preserving transformations between factorizations** such that queries and operations map across representations and the preservation or loss of warrant is explicit?

