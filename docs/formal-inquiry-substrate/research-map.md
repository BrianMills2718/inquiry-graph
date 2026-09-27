# Formal Inquiry Substrate — Research Map and Open Questions

## Established neighborhoods to compare

| Literature | Likely contribution |
| --- | --- |
| Statistical decision theory | Model/state space, experiment/information channel, decision rule, loss/risk, admissibility |
| Blackwell comparison of experiments | Query/decision-relative comparison of information structures |
| Le Cam theory | Approximate comparison of statistical experiments / deficiency |
| Bayesian experimental design | Choosing interactions for expected information or decision value |
| Active learning / active sensing | Epistemically motivated data acquisition |
| POMDPs / controlled stochastic processes | Unified state/action/observation dynamics under partial observability |
| POSGs / stochastic games | Multiple adaptive agents and strategic interaction |
| Dynamic epistemic logic | Information-changing actions and belief/knowledge updates |
| Epistemic planning | Planning over epistemic states |
| Structural causal models | Interventional/counterfactual query semantics and identification |
| Causal games | Causal models with strategic agents and policy response |
| Adaptive data analysis | Guarantees under feedback between analysis and data selection |
| Causal abstraction / coarse-graining | Mappings between causal models at different levels |
| Bisimulation / state abstraction | Conditions under which coarse states preserve behavior/value |
| Sufficient statistics / experiment sufficiency | Query-relative information preservation |
| Erotetic logic / inquisitive semantics | Formal structure of questions, answers, and issue resolution |
| Philosophy of scientific inquiry | Abduction, explanation, model revision, methodology, evidential warrant |
| Cybernetics / control theory | Regulation, feedback, model/control relationships |
| Active inference | Coupled perception/action under generative models |
| Game theory / mechanism design | Strategic response, signaling, recursive modeling |
| Category-theoretic formalisms | Possible language for compositionality and representation-preserving maps |

## Relationship to existing Inquiry Graph work

This research note should be read alongside:

- [formalism](../formalism.md): current V1 graph formalism;
- [epistemic transition calculus](../epistemic-transition-calculus.md): explicit epistemic transitions;
- [assumption-context meta-model](../assumption-context-meta-model.md): assumptions and context;
- [metareasoning/strategy/reflection](../metareasoning-strategy-reflection.md): reasoning about inquiry strategy;
- [candidate-generation interface](../candidate-generation-interface.md): operational extraction boundary.

The new substrate is **not yet a replacement** for any of those. It is a possible higher-level account of why those pieces fit together and how Inquiry Graph might eventually represent both the content of an inquiry and the warranted moves available at each state.

## Main unresolved questions

### 1. What is the minimal non-vacuous substrate?

Can one formulation cover:

- internal computation;
- external action;
- communication;
- statistical inference;
- causal intervention;
- strategic interaction;
- model revision;
- query revision;

without reducing to the useless statement that "everything is a state transition"?

A satisfactory answer must recover meaningful operation types, invariants, guarantees, and refusal conditions.

### 2. What exactly is a factorization?

Candidate meanings include:

- measurable coarse-graining;
- quotient space;
- latent-variable model;
- state abstraction;
- causal abstraction;
- partition / sigma-algebra;
- computational interface.

The framework should not silently treat these as identical.

### 3. What maps preserve inquiry?

Need a precise notion of when two representations are equivalent **for a query**.

Candidate tools:

- sufficient statistics;
- Blackwell sufficiency;
- Le Cam deficiency;
- bisimulation;
- causal-abstraction commuting diagrams;
- information-preserving maps;
- query-preserving homomorphisms.

This is the strongest current technical seam.

### 4. How should query revision be modeled?

Most decision/experimental formalisms assume a fixed target:

\[
q.
\]

Real inquiry often has

\[
q_t\rightarrow q_{t+1}.
\]

Examples: discovering the original variable was ill-defined, realizing the system is strategic, or replacing a causal question with a mechanism question.

### 5. How should model-class and stance revision be modeled?

Similarly:

\[
\mathcal M_t\rightarrow \mathcal M_{t+1}.
\]

Changing representational language is more than Bayesian updating inside a fixed model family.

### 6. What is the right formal object for warrant?

The working form is

\[
\mathsf W_g(\Gamma,F,q,\mathfrak m,h).
\]

Need to understand:

- which guarantee types compose;
- which are incomparable;
- how qualification/refusal is represented;
- how warrant changes under representation maps.

### 7. How do intentional roles attach to operations?

Measurement, intervention, experiment, probe, communication, and deception may be better modeled as roles relative to policy/objective than as event types.

Stress-test this against:

- quantum measurement;
- active sensing;
- human-subject reactivity;
- strategic games;
- ordinary randomized experiments.

### 8. How much of Dennett is formally necessary?

Dennett's stances may reduce to:

- variable/latent-state choice;
- factorization choice;
- model-class choice;
- complexity/predictive tradeoffs.

Do not force stance vocabulary into the mathematical core if established model-selection language does the work.

### 9. How does Levin's persuadability fit?

Possible interpretations:

- a hierarchy over operation classes at which reliable control is achieved;
- a relation between abstraction and controllability;
- the degree to which a high-level signal delegates problem solving to the target.

Find the closest existing control/game-theoretic analogue before defining a new quantity.

### 10. When is observation "passive enough"?

Replace the binary observation/intervention split with conditions under which an interaction's effect on the target can be ignored **for a specific query**.

Possible connections:

- ignorability;
- non-reactive measurement;
- no-signaling conditions;
- interference assumptions;
- measurement back-action;
- adaptive sampling;
- strategic response.

## Toy cases the framework must recover

### Passive statistical target
Estimate association in a fixed data-generating process.

### Causal experiment
Randomize treatment to identify a causal contrast.

### Reactive subject
A person changes behavior because they are observed.

### Strategic adversary
The target models the investigator and manipulates the evidence channel.

### Scientific conceptual revision
The original ontology/model class fails and the investigator changes the representation.

### Dialogue
Two reasoners exchange arguments, challenge assumptions, search literature, and revise the question.

All should be expressible in the same substrate.

## Recommended research order

1. **Blackwell / Le Cam:** how much of "warranted move" reduces to comparison of information structures and decision problems?
2. **Causal abstraction:** which query/intervention semantics survive coarse-graining?
3. **Bisimulation / sufficient statistics:** what is "the same inquiry under a different cut"?
4. **Dynamic epistemic logic / epistemic planning:** how naturally do information-changing acts and issue changes fit?
5. **POSG / causal games:** strategic response and recursive modeling.
6. **Erotetic / inquisitive semantics:** question structure and query revision.
7. **Only then category theory:** use it if it solves a concrete composition/commutation problem.

## Criteria for real progress

A useful next result should do at least one of:

- show that an established formalism already subsumes one allegedly novel piece;
- identify a precise incompatibility between two existing formalisms;
- define a representation map preserving a named query and warrant;
- demonstrate a toy case where a method is warranted under one model class but not another;
- reduce an informal distinction to an established mathematical object.

Do not measure progress by adding more terminology.
