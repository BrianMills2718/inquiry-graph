# Formal Inquiry Substrate — Provisional Core

This is coordination notation, not a canonical theory.

## 1. Underlying process

Let

\[
z_t\in\mathcal Z
\]

represent the state/configuration of the process at time \(t\).

Do not assume an agent/world split at this level.

A controlled or operation-indexed transition can be written

\[
K_\alpha(z_{t+1}\mid z_t,h_t).
\]

## 2. Factorization / representation

A representation or coarse-graining is

\[
F:\mathcal Z\rightsquigarrow \mathcal X.
\]

A deterministic factorization might be

\[
F:\mathcal Z\to \mathcal X_1\times\cdots\times\mathcal X_n,
\]

while a lossy/stochastic representation can be written as a channel

\[
\kappa_F(x\mid z).
\]

The factorization may introduce variables interpreted as analyst, target, environment, observation channel, memory, tool, mechanism, goal, belief, policy, or utility.

## 3. Model class and epistemic state

Let

\[
\mathcal M_F
\]

be the model class admitted under representation \(F\).

Let

\[
B_t
\]

encode the current epistemic state over the relevant possibilities/models.

\(B_t\) could be a set, posterior, credal set, logical theory, structured argument state, or another representation appropriate to the method.

A Dennett-style stance is provisionally treated as a policy or constraint over choices of \(F\) and \(\mathcal M_F\), not as a separate primitive.

## 4. Query

A query is an epistemic target

\[
q_t:\mathcal M_{F_t}\to\mathcal Y_t.
\]

Equivalently,

\[
M\sim_{q_t}M'
\iff
q_t(M)=q_t(M').
\]

The query specifies which distinctions in model space matter.

Examples include descriptive, associational, predictive, causal, counterfactual, mechanistic, intentional/goal, and decision/control queries.

## 5. Operation

An operation is any admissible transformation in the inquiry:

\[
\alpha_t\in\mathcal A_t.
\]

At the most general level, allow

\[
\alpha_t:
(z_t,F_t,\mathcal M_t,B_t,q_t,h_t)
\mapsto
\Delta(z_{t+1},F_{t+1},\mathcal M_{t+1},B_{t+1},q_{t+1},h_{t+1}).
\]

This intentionally permits an operation to change:

- the physical/process state;
- the retained evidence/history;
- the epistemic state;
- the model class;
- the factorization;
- the query.

Examples include measurement, intervention, experiment, communication, statistical estimation, deduction, simulation, literature search, tool use, model revision, query revision, and asking another agent.

## 6. Policy / methodology

A methodology contains a policy for selecting operations:

\[
\pi(\alpha_t\mid h_t,F_t,\mathcal M_t,B_t,q_t,\Gamma),
\]

where \(\Gamma\) is the current assumption set.

A provisional methodology tuple is

\[
\mathfrak m=(\pi,U,\delta,G),
\]

where:

- \(\pi\): operation-selection policy;
- \(U\): epistemic/model update rule;
- \(\delta\): answer/decision rule;
- \(G\): claimed guarantee or warrant type.

This tuple is a coordination device, not yet canonical.

## 7. Intentional roles are derived

Measurement/intervention/experiment need not be physical primitives.

One schematic objective is

\[
J(\alpha)
=
\lambda_E V_E(\alpha)
+
\lambda_C V_C(\alpha)
+
\lambda_S V_S(\alpha)
-
C(\alpha),
\]

with epistemic value \(V_E\), control value \(V_C\), strategic/signaling value \(V_S\), and cost/risk \(C\).

Then:

- **measurement**: primarily epistemic, often disturbance-constrained;
- **intervention**: primarily control/state-directed;
- **experiment**: structured interaction selected for epistemic discrimination, often using intervention;
- **probe**: operation selected for expected discrimination among answers/models;
- **communication**: operation whose model includes effects on another agent's information or policy.

These roles can overlap.

## 8. History

Let

\[
h_t=(\alpha_0,r_1,\alpha_1,r_2,\ldots,\alpha_{t-1},r_t),
\]

where \(r_t\) is whatever result is retained at the current representation.

Results can include measurements, computed statistics, messages, proofs, model failures, source documents, or reframings.

## 9. Update

An update rule

\[
U_t:(B_t,\mathcal M_t,h_t,\Gamma)\to(B_{t+1},\mathcal M_{t+1})
\]

may also trigger changes in \(F\) or \(q\).

Peircean abduction, deduction, and induction can be treated as families of inquiry operations/update patterns rather than as levels of claim.

## 10. Warrant

Use a typed warrant relation

\[
\mathsf W_g(\Gamma,F,q,\mathfrak m,h),
\]

meaning that under assumptions \(\Gamma\), representation \(F\), query \(q\), history \(h\), and methodology \(\mathfrak m\), the answer has guarantee type \(g\).

Possible guarantee types include:

- logical entailment;
- statistical coverage/error control;
- Bayesian posterior validity conditional on model/prior;
- causal identification;
- regret bound;
- robustness/minimax bound;
- equilibrium property;
- qualitative evidential adequacy under a named method.

Do not collapse these into a single scalar unless a specific decision problem supplies a principled reduction.

## 11. Strategic/reactive evidence

If the represented target reacts to the analyst, the evidence channel may be policy-dependent:

\[
P(r_t\mid M,\pi_A,h_t).
\]

A more strategic model may include the target's policy

\[
\pi_T(a_T\mid h_t,\widehat{\pi_A},B_T,\ldots).
\]

"Passive observation" is then a special case in which the relevant policy dependence is assumed ignorable for the current query.

## 12. Factorization change

Let

\[
\tau:(F,\mathcal M_F,q)\to(F',\mathcal M_{F'},q')
\]

be a representation change.

The central technical problem is defining when \(\tau\) preserves the inquiry.

Candidate conditions include query commutation

\[
q'\circ\tau_M \approx \tau_Y\circ q,
\]

operation correspondence

\[
\tau\circ\alpha \approx \alpha'\circ\tau,
\]

and warrant preservation or controlled degradation

\[
\mathsf W_g(\Gamma,F,q,\mathfrak m,h)
\Rightarrow
\mathsf W_{g'}(\Gamma',F',q',\mathfrak m',h')
\]

with any information loss or approximation made explicit.

Likely relevant mathematics: sufficient statistics, Blackwell sufficiency, Le Cam deficiency, bisimulation/state abstraction, causal abstraction, and possibly category-theoretic commuting diagrams.

## 13. This conversation as a required instance

The conversation that generated this proposal should fit without a separate "reasoning" ontology:

- \(F_t\): current conceptual decomposition;
- \(\mathcal M_t\): candidate explanatory/formal frameworks;
- \(q_t\): current question;
- \(\alpha_t\): propose distinction, object, search literature, reframe;
- \(r_t\): reply, contradiction, source, clarification;
- \(U_t\): update the conceptual/epistemic state;
- \(q_{t+1}\): refined or replaced question.

If that cannot be represented non-vacuously, the substrate is incomplete.
