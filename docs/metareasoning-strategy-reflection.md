# Metareasoning, strategy, and reflection — current extension

> **Status:** research draft extending the assumption-context meta-model. It integrates established work on metareasoning, strategy selection, and reflective architectures with the project's existing formal representation, support-context, and dialogue-provenance layers. It is not a claim that one optimal strategy calculus has been established.

## 1. Why another layer is needed

The previous stages separated:

1. formal representation;
2. persistent epistemic/support state;
3. temporary assumption context;
4. candidate generation;
5. warrant/evaluation.

The dialogue then exposed a different kind of object: **a reusable strategy for deciding which reasoning operations to perform and how to sequence them**.

Canonical factorization is the running example. It is not itself a sentence, theory, candidate model, or primitive inference rule. It is a reusable control pattern that can orchestrate many lower-level operations:

- propose a decomposition;
- search for counterexamples;
- test completeness;
- split or merge factors;
- distinguish type from role;
- change representation;
- consult literature;
- stop when the requested criteria are sufficiently met.

This belongs to the established domain of **metareasoning**: monitoring and controlling reasoning rather than merely performing the object-level reasoning itself.

## 2. Formal representation substrate: use MMT-like artifacts

The representation layer can be kept small.

An MMT-like theory graph supplies four useful formal artifact classes:

\[
\boxed{
\mathcal F=
\{
\mathsf{Theory},
\mathsf{Declaration},
\mathsf{Object},
\mathsf{Morphism}
\}.
}
\]

This collapses several earlier candidate types:

- formulas, terms, proofs and derivations are formal **objects**;
- new constants, predicates, types and definitions are **declarations**;
- structured bodies of assumptions/axioms are **theories**;
- models, implementations and theory translations can be represented as **morphisms**.

LF is best treated as one possible foundation/meta-theory represented inside MMT rather than as a parallel implementation layer.

The institution-theory perspective remains useful semantically:

\[
(\mathbf{Sig},\operatorname{Sen},\operatorname{Mod},\models)
\]

but need not be a separate software layer if the chosen formal representation system already supports heterogeneous theories and morphisms.

## 3. Draft candidate versus formal artifact

Candidate generation must be allowed to produce something that is not yet a valid formal object.

Write:

\[
g(R)\to d
\]

for a **draft candidate**.

Elaboration/validation against the formal substrate is then:

\[
\operatorname{Elab}_{\mathcal F}(d)=
\begin{cases}
c\in\mathcal F & \text{if the candidate can be made well formed},\\
\bot & \text{if elaboration/checking fails}.
\end{cases}
\]

This yields an important boundary:

\[
\boxed{
\text{well formed}
\neq
\text{warranted}.
}
\]

A proof checker can establish typing or deductive validity. It does not establish that a proposed latent variable, causal model, extrapolation, analogy, or source-selection choice was epistemically warranted.

## 4. Operator layer

Let \(\mathcal O\) be the available reasoning operators.

Examples include:

- logical construction;
- deduction;
- anti-unification/generalization;
- signature extension;
- predicate invention;
- theory translation;
- model construction;
- counterexample construction;
- evidence/research retrieval;
- query transformation;
- support-graph modification.

An operator is an object-level transformation or candidate generator. The exact typing depends on the formal artifacts involved.

The project should continue to import precise operators from existing formal disciplines rather than promote broad English verbs into primitives.

## 5. Strategy layer

A **strategy** controls which operators are invoked and in what order.

A deliberately weak descriptive definition is:

\[
\boxed{
\pi:
\operatorname{Hist}(R)
\longrightarrow
\mathcal P(\mathcal O\cup\{\operatorname{stop}\})
}
\]

where \(\operatorname{Hist}(R)\) is the observable reasoning history available to the controller.

This form is intentionally nondeterministic. A deterministic strategy is a special case. A probabilistic policy can replace the power set with a distribution.

The definition does **not** require utility maximization.

Rational metareasoning is then a stronger specialization in which strategy/operator selection is optimized relative to benefits, costs and resource constraints. That literature is useful, but optimization should not be baked into the foundational definition because the current project first needs to represent what strategy was used before deciding whether it was optimal.

## 6. Strategy episode

A **strategy schema** is reusable. A **strategy episode** is an occurrence of a strategy in a particular reasoning trajectory.

Schematically:

\[
\epsilon_\pi=
(R_0,o_0,R_1,o_1,\ldots,R_n)
\]

where the operator sequence is attributed to strategy \(\pi\).

This distinction matters for conversation annotation:

- “canonical factorization” is a reusable strategy schema;
- the stretch of this conversation where factors were repeatedly split, merged, retyped and stress-tested is a strategy episode.

A strategy episode may itself contain lower-level strategy episodes.

## 7. Canonical factorization as a strategy

MECE is one special-case diagnostic for a partition. The more general reusable strategy is **primitive-factorization analysis** or **canonical-factorization analysis**.

Given target representation \(X\), the strategy seeks a decomposition appropriate to the target structure:

- partition;
- product/coordinate system;
- feature/power-set composition;
- algebraic generation;
- factorization/normal form.

Candidate decompositions are tested against explicit desiderata.

### 7.1 Completeness

Can every relevant target object/case be represented?

### 7.2 Nonredundancy/minimality

Can a factor be removed or derived from the others without losing required expressive power?

### 7.3 Independence/orthogonality

Do purported factors represent distinct degrees of freedom, or are they secretly coupled?

### 7.4 Compositionality

Can complex cases legitimately involve several factors simultaneously?

### 7.5 Uniqueness/canonicality

Given the declared representation/equivalence relation, does an object receive one decomposition or many arbitrary ones?

Canonicality is always relative to a representation contract and equivalence criterion.

## 8. Factorization failure diagnostics

The conversation developed useful diagnostic language.

### Underfactored

A proposed factor bundles distinctions that matter to reconstruction, explanation, or allowed transformations.

Typical repair:

\[
p
\rightsquigarrow
(p_1,p_2,\ldots).
\]

Example: “reframe” bundled query change, representation change and assumption-context change.

### Overfactored

Two or more proposed factors are redundant, derivable from one another, or distinctions at the wrong level.

Typical repair:

\[
(p_1,p_2)\rightsquigarrow p.
\]

Example: treating proof/derivation and expression as wholly different representation primitives when both can be formal objects in an LF/MMT-like substrate.

### Misfactored

The candidate decomposition mixes unlike dimensions, especially **type** with **role**, or object-level structure with control-level status.

Example:

\[
\{
\text{expression},
\text{assumption},
\text{model}
\}
\]

is misfactored because “assumption” is normally a role played by an expression/theory, not the same ontological kind as expression or model.

These diagnoses are relative to a target semantics; they are not absolute metaphysical properties.

## 9. Strategy versus metastrategy

A separate infinite hierarchy of Strategy, MetaStrategy, MetaMetaStrategy, ... is unnecessary.

Treat strategies as first-class representable objects.

A strategy is **meta-level relative to a target** when it monitors, selects, modifies, composes or evaluates another reasoning process or strategy.

Thus a metastrategy is not a new ontological type. It is a strategy whose controlled objects/actions include strategies or reasoning episodes.

Canonical factorization is therefore:

- an ordinary reasoning strategy when applied to a domain model;
- a metareasoning strategy when applied to the taxonomy of reasoning operators or to the meta-model itself.

## 10. Reflection and self-application

The literature on reflective architectures supports an object/meta distinction in which the meta-level represents and reasons about the object-level process, and reflection principles connect the levels.

For this project, however, fixed numerical levels \(L_0,L_1,L_2,\ldots\) should be **derived rather than primitive**.

Introduce an explicit semantic relation:

\[
\boxed{
\operatorname{about}(x,y)
}
\]

where \(x\) is a represented reasoning artifact/episode and \(y\) is what it targets.

Then meta-level status is relational:

\[
x\text{ is meta with respect to }y
\quad\Longleftrightarrow\quad
\operatorname{about}(x,y)
\]

when \(y\) is itself a reasoning artifact, strategy, episode, model of reasoning, or control process.

Nesting depth can be recovered from chains of about relations when needed.

This is better than assigning permanent levels because the same strategy may be object-level in one task and meta-level in another.

## 11. Closure under self-description

The key architectural property behind the user's repeated self-application is:

\[
\boxed{
\text{reasoning episodes, strategies, and the meta-model itself are representable targets.}
}
\]

That gives **closure under self-description**.

The system can therefore instantiate:

\[
\operatorname{about}(R,\mathcal M)
\]

when a reasoning episode analyzes the meta-model \(\mathcal M\), or

\[
\operatorname{about}(R,\pi)
\]

when an episode evaluates a reasoning strategy.

Self-application is the special case where the process being analyzed includes the process that produced the analysis/model.

This is reflection in the useful engineering sense. It does not require unrestricted logical self-reference, and it should not silently imply introspective access to hidden model internals.

## 12. Monitoring and control

Metareasoning literature usually distinguishes:

- **monitoring**: inspect the state/progress/quality of object-level reasoning;
- **control**: select, continue, interrupt, replace or allocate resources to reasoning operations.

These should be represented separately.

For example, a factorization strategy might monitor:

- unresolved counterexamples;
- overlap among factors;
- uncovered cases;
- dependence among axes.

Its control responses might be:

- split a factor;
- merge two factors;
- introduce a role/type distinction;
- search literature;
- change representation;
- stop.

Rational-metareasoning models may place a value/cost function over these control actions, but that is an optional evaluation layer.

## 13. Conversation-level instantiation

The inquiry graph provides public observational data about reasoning trajectories.

A conversation can be segmented into:

1. source utterances;
2. atomic inquiry moves;
3. reconstructed strategy episodes;
4. reusable strategy schemas;
5. reflective/meta relations among episodes and targets.

The current graph already represents source utterances and atomic moves. For the present version:

- reusable strategies are represented as method nodes;
- reconstructed strategy episodes can be represented as grounded example nodes;
- moves can be linked to episodes with part_of;
- episodes can exemplify strategy methods;
- the new about relation records reflective targeting.

This is intentionally conservative. A future schema may add a dedicated StrategyEpisode record if span-level strategy analysis becomes central.

## 14. Strategies visible in the founding conversation

The current conversation contains at least the following **proposed** strategy annotations:

### Canonical / primitive factorization

Repeatedly propose a decomposition, test it for overlap/gaps, diagnose over/under/misfactoring, and revise.

### Adversarial counterexample search

Try to construct cases that violate a proposed exhaustive partition or claimed primitive distinction.

### Literature-before-invention

When a conceptual structure appears well-trodden, search for established formal machinery and replace home-grown primitives where appropriate.

### Meta-model stress testing

Force newly imported machinery to map onto the existing meta-model; treat mismatches as evidence of an omitted coordinate or bad factorization.

### Goal restoration

When the inquiry drifts into implementation or optimization before the foundational question is settled, explicitly return to the earlier open obligation.

### Reflective self-application

Use the developing framework to classify the reasoning moves and strategies used to build the framework itself.

These are interpretive annotations of the public dialogue, not claims about inaccessible private cognition.

## 15. Empirical application

This creates a concrete research program.

For conversation \(D\), infer a trajectory:

\[
D
\rightsquigarrow
(\epsilon_1,\epsilon_2,\ldots,\epsilon_n)
\]

with strategy annotations:

\[
\epsilon_i \models \pi_j.
\]

Then ask empirically:

- which strategies are invoked under which problem states?
- which strategies trigger useful representation changes?
- which strategies tend to repair stalled inquiry?
- which meta-strategies select among strategies effectively?
- which sequences correlate with independently measured outcomes?

This is where the existing inquiry graph becomes an observational/annotation substrate and the formal meta-model supplies the semantic vocabulary.

The project therefore has two connected halves:

\[
\boxed{
\text{formal/normative representation of reasoning strategies}
}
\]

and

\[
\boxed{
\text{empirical annotation/evaluation of strategy use in real reasoning trajectories}.
}
\]

## 16. Current architecture

The current stack is:

\[
\boxed{
\begin{array}{c}
\textbf{Formal representation}\\
\mathcal F\text{ (MMT-like theory graph)}
\\[4pt]
\downarrow
\\[4pt]
\textbf{Epistemic/support overlay}\\
K_{\mathcal F}=(N,A,J,\lambda,\rho)
\\[4pt]
\downarrow
\\[4pt]
\textbf{Reasoning episode}\\
R=(\mathcal F,K_{\mathcal F},\Gamma,Q)
\\[4pt]
\downarrow
\\[4pt]
\textbf{Operators / candidate generation}\\
\mathcal O,\quad g(R)\to d,\quad \operatorname{Elab}_{\mathcal F}(d)
\\[4pt]
\downarrow
\\[4pt]
\textbf{Strategy/control}\\
\pi:\operatorname{Hist}(R)\to\mathcal P(\mathcal O\cup\{\operatorname{stop}\})
\end{array}
}
\]

Reflection is not another stack layer. It is enabled because the objects in these layers are first-class targets connected by about.

## 17. What remains genuinely unresolved

The research frontier is now narrower:

1. the algebra/basis of draft candidate generation;
2. the minimal candidate/draft type system before elaboration;
3. the warrant semantics for non-entailing candidates;
4. the relation between graded support \(\rho\) and ATMS-style support environments;
5. strategy segmentation/identification from dialogue;
6. strategy evaluation without conflating descriptive occurrence with optimality;
7. whether a dedicated executable strategy-episode schema is needed;
8. how reflective self-application should be bounded in a formal implementation.

The core conceptual split is now concrete: **formal artifacts**, **support contexts**, **operators**, **strategies**, and **reflection/provenance** are different things.
