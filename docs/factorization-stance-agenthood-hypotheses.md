# Factorization, Stance, and Agenthood as Inquiry Hypotheses

**Date:** 2026-09-29  
**Status:** research formalism; carrier-independent  
**Scope:** representation choice, black-box/white-box modeling, stance choice, and agent attribution

## 1. Motivation

The inquiry formalism should not treat the following as primitive facts about the world:

- a privileged agent/environment boundary;
- a privileged black-box/white-box decomposition;
- a privileged physical/design/intentional stance;
- an intrinsic designation that some subsystem simply "is an agent."

Instead, these are represented as **hypotheses about how to factor and model a process for a particular inquiry**.

The foundational object remains a process or possibility space:

\[
z \in \mathcal Z.
\]

A representation introduces a factorization/modeling map over that substrate.

## 2. Factorization hypothesis

A **factorization hypothesis** proposes a decomposition of the process:

\[
H_F:
\mathcal Z \rightsquigarrow
(X_1,\ldots,X_n).
\]

This notation is intentionally permissive. The factors may be physical subsystems, variables, functional components, interacting organizations, latent states, black-box input/output interfaces, or any other inquiry-relevant decomposition.

A factorization hypothesis is not automatically asserted as uniquely correct. It is a candidate representation under which some questions, operations, or predictions may become tractable.

### Example: thermostat

One factorization may use:

\[
F_1(\mathcal Z)=(\text{controller},\text{heater},\text{room}).
\]

Another may use:

\[
F_2(\mathcal Z)=(\text{controller+heater},\text{room}).
\]

A black-box representation may instead expose only:

\[
F_3(\mathcal Z)=(\text{input},\text{system},\text{output}).
\]

The formalism does not assume one of these cuts is ontologically privileged.

## 3. Black-box and white-box models

A black-box model suppresses internal decomposition and represents externally relevant behavior:

\[
u \mapsto y.
\]

A white-box model introduces internal state or substructure:

\[
(u,x_t)\mapsto(x_{t+1},y_t).
\]

The white-box model is not automatically "truer." It makes additional distinctions. Whether those distinctions matter depends on the inquiry query.

A black-box hypothesis can therefore be written as a modeling commitment:

\[
H_B:
\text{for query }q,\text{ model factor }X\text{ only through interface }I_X.
\]

A white-box refinement proposes additional latent/internal structure:

\[
H_W:X\rightsquigarrow(X_1,\ldots,X_k).
\]

## 4. Stance hypothesis

A **stance hypothesis** proposes a modeling family for one factor or process.

Let

\[
s\in\{\mathsf{physical},\mathsf{design},\mathsf{intentional},\ldots\}.
\]

Then:

\[
H_S(X,s)
\]

means: for the present inquiry, model X using stance s.

Physical stance licenses a model in terms of lower-level state, dynamics, constraints, and interaction.

Design stance licenses a model in terms of functional organization or intended/selected role.

Intentional stance licenses a model in terms of informational state, goals/preferences, policy, choice, response, or related intentional variables.

These are modeling hypotheses, not declarations of metaphysical essence.

## 5. Agenthood as a compound hypothesis

Agent attribution can be represented as a compound hypothesis:

\[
H_A=(H_F,H_S,H_\pi),
\]

where H_F selects the candidate subsystem/factor, H_S licenses an intentional or agent-like stance, and H_pi posits a policy/response organization for that factor.

For example:

\[
H_\pi:a_t\sim\pi(\cdot\mid h_t).
\]

More generally, in a strategic/reactive setting:

\[
\pi_X=\pi_X(h_t,\pi_Y,\ldots).
\]

So "X is an agent" is replaced by the more explicit claim that treating factor X as governed by an agent-like policy is a warranted modeling hypothesis for query q under evidence E.

This avoids promoting Agent to a primitive category in the foundational substrate.

## 6. Query-relative warrant

The relevant judgment is not whether a stance/factorization is absolutely true. It is whether it is warranted for the inquiry target.

Write:

\[
\mathsf W(H_F,H_S,H_\pi,q,E,\Gamma)
\]

for warrant under query q, evidence/history E, and background assumptions/resources Gamma.

The same subsystem may support different warranted representations for different queries.

For example, predicting external input-output behavior may license a black-box intentional model, while identifying a physical failure mechanism may require a white-box physical model.

Therefore:

\[
\mathsf W(H_A,q_1)\not\Rightarrow\mathsf W(H_A,q_2).
\]

## 7. Model adequacy versus ontology

This formalism distinguishes:

\[
\text{useful model}\neq\text{fundamental ontology}.
\]

A stance can be useful because it supports prediction, compression, control, or explanation without implying that its entities are metaphysically fundamental.

Likewise, failure of an intentional model for one query does not prove the subsystem is "not an agent" in every useful sense.

## 8. Representation comparison

Given two factorization/model hypotheses:

\[
R_1=(F_1,\mathcal M_1,q_1),\qquad R_2=(F_2,\mathcal M_2,q_2),
\]

a transformation

\[
T:R_1\to R_2
\]

should be analyzed in terms of what it preserves.

### Query preservation

For a fixed query:

\[
q_1(M)=\tau(q_2(T(M)))
\]

for all admissible M, where tau translates answer spaces if needed.

### Refinement

R2 refines R1 when the distinctions needed by R1 remain recoverable while R2 introduces additional distinctions. Schematically, there is a projection:

\[
P:R_2\to R_1.
\]

### Reframing

If the query itself changes materially, q1 -> q2, represent that as an explicit inquiry transformation rather than silently calling the two representations equivalent.

This is compatible with Inquiry Graph's existing reframes semantics.

## 9. When a representation change is problematic

A representation change is potentially inquiry-distorting when it removes or conflates distinctions required by the query or warrant conditions.

Examples include merging causal roles the query needs, treating actor stance as target truth, collapsing source occurrence and semantic content identity, forcing an agent/environment cut that excludes strategically relevant feedback, or converting black-box predictive success into an unsupported claim about internal mechanism.

No global distortion predicate is introduced yet. The correct test is relative to declared query and warrant obligations.

## 10. Relation to Inquiry Graph

Current Inquiry Graph already has much of the vocabulary needed to record this reasoning without adding new executable primitives.

Use Hypothesis for H_F, H_S, and H_pi; Method for a reusable stance/modeling procedure; Question for the query; and Claim for adequacy/warrant conclusions.

Existing relations cover candidate_for, supports, challenges, depends_on, reframes, about, and supersedes. Existing moves cover hypothesize, decompose, scope, test, reframe, and distinguish.

Therefore this research layer currently **falls out of the existing Inquiry ontology** as content plus relations/moves.

No new executable Agent, FactorizationHypothesis, or StanceHypothesis primitive is required yet.

## 11. Relation to OntoCanon

OntoCanon's generalized kernel/IR should remain neutral.

It needs enough expressivity to carry hypotheses, typed semantic objects, typed n-ary relations, named role bindings, higher-order relations where needed, provenance, and governance.

It should not encode as kernel primitives Agent, Environment, Measurement, Intervention, PhysicalStance, or IntentionalStance.

Those belong in ontology packs when a domain requires them.

## 12. Decision rule for adding new primitives

Before adding any new representation primitive, ask:

1. Can the distinction already be represented as a Hypothesis/Method/Question plus existing semantic relations?
2. Does the distinction recur across multiple inquiry domains?
3. Does treating it relationally lose information required by a real query?
4. Is there established prior art with a more precise formalization?
5. Does it belong in the Inquiry pack, another domain pack, or the OntoCanon kernel?

Only add a new primitive if the existing substrate cannot express the required distinction cleanly and repeatedly.

## 13. Immediate consequence

Adopt the following research principle:

\[
\boxed{\text{agenthood is a query-relative modeling hypothesis over a chosen factorization}}
\]

and:

\[
\boxed{\text{agent/environment is a derived modeling cut, not foundational ontology}}
\]

This remains a research-formalism commitment, not yet an executable change to Inquiry Graph V1.
