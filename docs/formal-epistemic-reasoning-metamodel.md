# Formal Epistemic Reasoning Meta-Model — Closeout and Handoff

> **Status:** canonical project-1 handoff.
> **Purpose:** preserve the current state of the formal epistemic reasoning meta-model so a future agent can resume without reconstructing this long conversation.
> **Scope:** this document covers the foundational meta-model, not the product-level inquiry system. It also records the relation to the inquiry-representation project and the main open research directions.

## 1. Project identity

The cleanest name for the foundational project is:

# **Formal Epistemic Reasoning Meta-Model**

The project is not intended to be one theory of knowledge, one logic, one universal confidence calculus, one list of inference types, one cognitive architecture, or one argumentation formalism.

It is intended to be a **meta-model of epistemic reasoning**: a representation of the major kinds of objects, state, operations, support relations, warrants, actions, and control structures that occur across different reasoning regimes.

The central research question is:

> **What structure is required to represent and evaluate epistemic reasoning moves without collapsing deduction, statistical learning, defeasible reasoning, measurement, testimony, candidate generation, belief/update operations, and strategy selection into one undifferentiated notion of inference?**

A second foundational question motivated much of the work:

> **What warrants a reasoning move, and what warrants that warrant?**

The inquiry-graph project emerged later as a distinct but related project for representing actual inquiry histories.

## 2. Three related projects

### Project 1 — Formal Epistemic Reasoning Meta-Model

Goal:

\[
\text{represent the structure of epistemic reasoning itself.}
\]

### Project 2 — Inquiry Representation Model

A source-grounded representation of actual inquiry histories: utterances, claims, questions, moves, alternatives, objections, revisions, strategies, stance, provenance, and question status.

Goal:

\[
\text{represent how an inquiry actually develops.}
\]

### Project 3 — Inquiry System

A useful tool built on the first two.

Possible functions include navigating unresolved questions, recovering abandoned branches, inspecting assumptions and dependencies, comparing competing arguments, exposing why a view changed, identifying recurring reasoning strategies, recommending what to inspect next, and helping a person or model resume a long inquiry.

Goal:

\[
\text{make inquiry easier, more auditable, and potentially better.}
\]

These projects are related but should not be conflated.

## 3. Meta-relationship among the projects

The Inquiry Representation Model can represent the historical process by which the Formal Epistemic Reasoning Meta-Model was constructed.

The Formal Epistemic Reasoning Meta-Model can characterize operations represented inside an inquiry graph.

The future Inquiry System can use both models to reason about inquiry and potentially about its own reasoning.

Thus:

\[
\boxed{
\text{meta-model}
\leftrightarrow
\text{inquiry representation}
\leftrightarrow
\text{useful system}
}
\]

Reflection is represented relationally:

\[
\operatorname{about}(x,y).
\]

An object is “meta” relative to another object when it reasons about or controls that target.

## 4. Main substantive result

The original inquiry began with traditional categories such as:

\[
\text{deduction},\quad
\text{induction},\quad
\text{abduction}.
\]

The work strongly suggests that these are not an adequate primitive partition of epistemic reasoning.

The central reason is that they mix levels.

Something called “abduction” may include candidate generation, admissibility constraints, explanatory scoring, defeasible support, and a later epistemic update.

Something called “induction” may refer to a learning algorithm, a statistical theorem, a support change, a prediction policy, or an epistemic update.

Deduction is better defined, but even there:

\[
\text{derivation}
\neq
\text{acceptance of premises}
\neq
\text{state update}.
\]

The main replacement is therefore not a new flat taxonomy. It is a **factorized architecture**.

## 5. Canonical factorization

The current stable distinction is:

\[
\boxed{
\text{formal representation}
\neq
\text{candidate generation}
\neq
\text{support}
\neq
\text{argument/defeat}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{epistemic action/update}
\neq
\text{strategy/control}.
}
\]

These categories should not be treated as a partition of all objects. They are architectural dimensions/layers.

A useful high-level state description is:

\[
\boxed{
R=(\mathcal F,K_{\mathcal F},\Gamma,Q,\Pi)
}
\]

where:

- \(\mathcal F\): formal representation substrate;
- \(K_{\mathcal F}\): persistent support/provenance state;
- \(\Gamma\): temporary assumption context;
- \(Q\): current question/task;
- \(\Pi\): strategy/control state.

## 6. Formal representation layer

The representation layer is best understood through theory-graph/logical-framework ideas.

A compact candidate formal-artifact basis is:

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

Interpretation:

- formulas, terms, proofs: objects;
- predicates, constants, types, rules: declarations;
- collections/specifications: theories;
- translations/models/structure-preserving mappings: morphisms.

MMT-like theory graphs are the current preferred representation precedent.

LF may be used as a foundation/meta-theory inside such a framework rather than as a competing parallel layer.

Important distinction:

\[
\boxed{
\text{formal object identity}
\neq
\text{epistemic role}.
}
\]

An assumption is usually a role played by a proposition/declaration/object in an epistemic context, not necessarily a distinct formal artifact type.

## 7. Persistent support and temporary contexts

The ATMS-inspired persistent support state is:

\[
\boxed{
K_{\mathcal F}
=
(N,A,J,\lambda,\rho)
}
\]

where:

- \(N\): represented propositions/reports/hypotheses/etc.;
- \(A\subseteq N\): assumable nodes;
- \(J\): justification/dependency structure;
- \(\lambda(n)\): minimal assumption environments supporting \(n\);
- \(\rho\): optional typed graded interpretations.

A temporary reasoning context is:

\[
\Gamma\subseteq A.
\]

Its closure is:

\[
C(\Gamma)=\operatorname{Cl}_J(\Gamma).
\]

This supports a black-box/white-box distinction:

- persistent state retains multiple hypothetical alternatives;
- a temporary context can stipulate assumptions and inspect consequences.

Selecting \(\Gamma\) does not imply permanent acceptance.

## 8. Positive support algebra

For primitive assumption tokens \(X\), positive support is represented by finite antichains of finite assumption environments:

\[
\boxed{
\mathsf{Supp}(X)
=
\operatorname{Antichain}
(
\mathcal P_{\mathrm{fin}}(X)
).
}
\]

Normalization:

\[
\operatorname{Min}(S)
=
\{
E\in S:
\nexists E'\in S,\,
E'\subsetneq E
\}.
\]

Alternative support:

\[
A\oplus B
=
\operatorname{Min}(A\cup B).
\]

Joint support:

\[
A\otimes B
=
\operatorname{Min}
\{
E\cup F:
E\in A,\,
F\in B
\}.
\]

Identities:

\[
0=\varnothing,
\qquad
1=\{\varnothing\}.
\]

This is the free distributive lattice over \(X\), equivalently monotone Boolean provenance modulo logical equivalence, and an idempotent commutative semiring.

The information-loss boundary is explicit: this representation preserves minimal support environments but discards proof multiplicity, proof-tree identity, repeated-use counts, and chronological construction history.

That loss is intentional at the support layer.

## 9. Graded support

Numeric/ordinal support is not primitive.

The general pattern is:

\[
\boxed{
\rho_\eta:
\mathsf{Prov}
\to
V_\eta
}
\]

for an interpretation regime \(\eta\).

A concrete executable reference regime uses independent Bernoulli assumptions, optionally conditioned on nogoods.

If \(A\) is a support antichain:

\[
\rho_{\mathrm{Bern}}(A)
=
P(
\llbracket A\rrbracket
\mid
\text{consistency}
).
\]

Critical distinction:

\[
\boxed{
\rho_{\mathrm{Bern}}(\lambda(h))
\neq
P(h)
\text{ by definition}.
}
\]

The value is probability that the support condition holds under the model.

Turning that into proposition probability requires additional semantics/warrant.

## 10. Candidate generation

Candidate generation is separate from warrant and state update.

For a reasoning episode \(R\):

\[
\boxed{
\mathcal G_R
=
(
\mathcal D_R,
d_0,
\mathcal O_R,
\to_R
)
}
\]

where:

- \(\mathcal D_R\): admissible draft states;
- \(d_0\): initial/partial draft;
- \(\mathcal O_R\): construction/refinement operators;
- \(\to_R\): transition relation.

Reachable drafts:

\[
\operatorname{Reach}(R)
=
\{
d:
d_0
\xrightarrow{\mathcal O_R *}
d
\}.
\]

A strategy:

\[
\boxed{
\pi:
\operatorname{Hist}(R,\mathcal G_R)
\to
\mathcal P(
\mathcal O_R
\cup
\{\operatorname{stop}\}
).
}
\]

Formal elaboration:

\[
\operatorname{Elab}_{\mathcal F}(d)
=
\begin{cases}
c\in\mathcal F & \text{if formalizable}\\
\bot & \text{otherwise.}
\end{cases}
\]

Evaluation:

\[
V_j(R,c)
\to
(
\operatorname{status},
f_j
).
\]

Core distinction:

\[
\boxed{
\text{generative space}
\neq
\text{operators}
\neq
\text{strategy}
\neq
\text{evaluation}
\neq
\text{warrant}.
}
\]

This area remains the largest theoretical open question.

See Section 21.

## 11. Epistemic actions

An epistemic action is modeled schematically as a typed partial state transducer:

\[
\boxed{
a:
S
\rightharpoonup
S\times O_a.
}
\]

Candidate state coordinates include:

\[
\{
\mathcal F,
K_{\mathcal F},
\Gamma,
Q,
\Pi,
O
\}.
\]

Examples include deriving a consequence, recording a support grade, retaining a candidate, raising support, accepting, retracting, revising, changing temporary context, selecting a reasoning operator, and selecting a strategy.

No universal folk verb list is assumed primitive.

A primitive action basis is representation-relative:

\[
A
=
\langle B\rangle_{\mathcal A}.
\]

Whether there is a canonical/minimal basis is still open.

## 12. Warrant

The central warrant judgment is:

\[
\boxed{
\mathfrak W;
A
\vdash_\pi
a:G
}
\]

read:

> under warrant regime \(\mathfrak W\) and applicability assumptions \(A\), certificate/support object \(\pi\) warrants epistemic action \(a\) with guarantee \(G\).

Components:

- \(\mathfrak W\): warrant regime;
- \(A\): explicit applicability assumptions;
- \(\pi\): certificate/support object;
- \(a\): target epistemic action;
- \(G\): typed guarantee.

This preserves:

\[
\boxed{
\text{support}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{update}.
}
\]

A support object may exist without being adequate for a given action.

A warrant may be conditionally valid while not currently licensed.

A licensed action may not be executed.

## 13. License

Given current context \(C\):

\[
C\models A
\]

and:

\[
\mathfrak W;
A
\vdash_\pi
a:G,
\]

derive:

\[
\boxed{
\operatorname{Licensed}_{\mathfrak W,C}(a:G).
}
\]

Current executable benchmark regimes approximate:

\[
C\models A
\]

with explicit set inclusion.

That is an implementation simplification, not the foundational semantics.

## 14. Typed guarantees

Guarantee \(G\) is deliberately heterogeneous.

Examples include:

- deductive truth preservation relative to premises;
- defeasible acceptability under a declared argumentation semantics;
- computed support-event probability under a declared model;
- measurement result with stated uncertainty/calibration provenance;
- testimonial posterior under a declared source reliability model;
- population-loss bound with stated confidence under sampling assumptions;
- positive lower confidence bound on expected task utility advantage.

The project does not force these into one scalar confidence value.

## 15. Defeasible reasoning

Positive support remains separate from dialectical status.

Current decomposition:

\[
\boxed{
\text{positive support}
+
\text{structured attack}
+
\text{attack-to-defeat resolution}
+
\text{acceptability semantics}.
}
\]

The first executable argumentation bridge is ABA-like.

Assumptions have explicit contraries.

Basic attacks arise when one argument derives the contrary of an assumption used by another.

Attack-origin metadata retains distinctions such as undermine, undercut, and rebut.

The downstream abstract semantics currently uses Dung grounded semantics.

Thus:

\[
\boxed{
\text{argument has support}
\neq
\text{argument is dialectically acceptable}.
}
\]

## 16. Preference-sensitive defeat

The current binary preference regime uses a strict relation over assumptions.

If:

\[
\alpha<\beta
\]

means \(\alpha\) is less preferred than \(\beta\), an attack on \(\beta\) is blocked if the attacking support relies on such an \(\alpha\).

This is intentionally only the normal-attack filtering part of ABA+-style preference handling.

It is **not** claimed to be full ABA+.

Full ABA+ can require set-to-set attack reversal.

That richer path is explicitly deferred in GitHub issue #18.

## 17. Argument identity boundary

For the current ABA/ABA+-style executable layer, argument identity is quotiented by:

\[
\boxed{
(
\text{conclusion},
\text{minimal supporting assumption environment}
).
}
\]

This is sufficient for the selected assumption-centered semantics.

It is not a claim that proof objects themselves are identical.

Thus:

\[
\boxed{
\text{formal derivation identity}
\neq
\text{ABA dialectical argument identity}.
}
\]

First-class derivation/subargument structure is deferred until a semantics requires it.

That richer path is preserved in GitHub issue #17.

## 18. Executable warrant regimes

The repository contains executable benchmark instances spanning distinct guarantee types.

### 18.1 Grounded dialectical warrant

A certificate argument must be grounded-IN.

Only typed defeasible actions are warranted.

Grounded acceptability does not automatically license unconditional acceptance.

### 18.2 Graded support warrant

An independent-Bernoulli support certificate can warrant recording a support grade.

Even a grade such as \(0.99\) does not automatically warrant acceptance.

### 18.3 Deductive warrant

A checked strict-Horn certificate can warrant:

\[
\operatorname{derive}(h)
\]

relative to explicit premises.

A valid derivation does not warrant accepting the premises.

### 18.4 Measurement warrant

A measurement certificate can warrant recording value, unit, standard uncertainty, and calibration/model provenance.

It does not directly warrant exact proposition acceptance.

### 18.5 Testimony warrant

A source model specifies:

\[
P(R^+\mid H),
\qquad
P(R^+\mid\neg H)
\]

for a source/reference class.

A certificate can warrant recording the posterior under that model.

It does not make source reliability context-free.

### 18.6 Statistical warrant

A finite-class uniform-convergence certificate computes:

\[
\epsilon
=
\sqrt{
\frac{
\log(
2|\mathcal H|/\delta
)
}{
2m
}
}.
\]

It can warrant recording:

\[
L_D(h)
\le
L_S(h)+\epsilon
\]

with confidence \(1-\delta\), conditional on sampling assumptions.

It does not warrant predictor deployment.

### 18.7 Strategy-performance warrant

For paired normalized utilities:

\[
D_i
=
u_i(\pi)-u_i(\pi_0)
\in[-1,1].
\]

A strategy may be selected only when the lower confidence bound:

\[
\bar D
-
\sqrt{
\frac{
2\log(1/\delta)
}{
n
}
}
\]

is strictly positive, subject to task-distribution and utility assumptions.

## 19. Current verification status

The integrated current repository has been executed successfully on native Windows.

Current full result:

- **138 tests passed**;
- seed fixture rebuilt successfully;
- **8 generated artifacts** matched;
- graph validation: **0 errors / 0 warnings**;
- dependency check: no broken requirements.

The verification run includes support algebra, defeat, ABA, preference filtering, warrant/license, graded support, strict-Horn deduction, measurement/testimony, statistical/PAC, and strategy-performance.

Hosted GitHub Actions remains a separate infrastructure problem: runs have repeatedly failed or cancelled before runner steps/logs.

Do not treat hosted pre-run failure as an application-level failure.

## 20. Comparison to existing work

The current meta-model is best understood as a synthesis/interface, not as a replacement for the mature frameworks it uses.

### Formal epistemology

Formal epistemology uses probability, logic, ranking theory, belief revision, decision theory, and related mathematical tools to analyze epistemic states and norms.

The present project differs mainly in **architectural scope**: instead of choosing one formalism as the core epistemology, it tries to factor the interfaces among heterogeneous epistemic regimes.

### AGM / belief revision

AGM provides postulates and representation theorems for belief-state change.

This project reuses the idea that change operations deserve formal semantics, but does not make belief revision the universal form of reasoning.

The present action model is broader:

\[
a:
S
\rightharpoonup
S\times O_a.
\]

### Dynamic epistemic logic

DEL provides formal models of informational events and model transformation.

It is a strong precedent for structured epistemic actions.

This project is less committed to possible-worlds epistemic semantics and uses DEL mainly as evidence that epistemic actions should be first-class structured objects.

### ATMS

ATMS is the closest precedent for maintaining multiple assumption contexts and minimal support environments simultaneously.

The current support layer is directly ATMS-inspired.

The project extends beyond ATMS by separating support provenance, argument defeat, warrant, action license, and strategy.

### Provenance semirings / minimal witness provenance

These supply mature algebraic machinery for alternative versus joint provenance.

The current positive-support antichain algebra is essentially a minimal-witness/free-distributive-lattice instance of this family.

### Structured argumentation

ABA, ABA+, ASPIC+, Pollock, and Dung provide mature machinery for defeasible conflict.

The project uses an ABA-first executable substrate with explicit typed metadata and Dung acceptability.

It does not claim a novel replacement argumentation theory.

### Justification Logic

Justification Logic supplies a strong precedent for treating reasons/certificates as explicit objects.

The present warrant interface extends the target from “reason for proposition” to “certificate adequate for a typed epistemic action with a typed guarantee.”

### Formal learning theory / PAC

Formal learning theory shows that ampliative methods can receive rigorous method-level guarantees under explicit assumptions.

This is directly reflected in the statistical warrant regime.

### Metareasoning

Rational metareasoning and reflective architectures provide precedents for treating strategy selection and control as objects of reasoning.

The present project deliberately keeps generic strategy/control separate from any one utility-maximizing implementation.

### MMT/LF / theory graphs

MMT/LF-like work provides the likely formal substrate for theories, declarations, proofs/objects, and morphisms.

The project does not attempt to replace logical frameworks.

## 21. Major open theoretical questions

These should remain visible in any future handoff.

### 21.1 Candidate generation

This is the largest unresolved foundational area.

Current interface:

\[
\mathcal G_R
=
(
\mathcal D_R,
d_0,
\mathcal O_R,
\to_R
).
\]

We know how to represent generative spaces, construction/refinement operators, strategies, elaboration, and evaluators.

We do **not** yet have a satisfying general theory of how new hypotheses, predicates, concepts, analogies, representations, and explanatory structures are generated.

Important prior conclusions:

\[
\boxed{
\text{concept construction}
\neq
\text{concept invention}.
}
\]

and:

\[
\boxed{
\text{expression construction}
\neq
\text{definitional extension}
\neq
\text{substantive predicate invention}.
}
\]

The literature suggests constrained search over a generative space is a more robust abstraction than a universal “creativity operator” list.

Candidate generation has now received both a dedicated landscape survey and a five-framework mapping test. CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR theory formation, and conceptual blending all fit the revised typed generative-system interface without another top-level coordinate. The important refinements are that generation episodes should be separated from reusable regimes, artifact ontologies may be heterogeneous, draft states may be graphs, and transformationality is representation-relative. See `docs/candidate-generation-framework-mappings.md` and ADR 016.

### 21.2 Warrant composition

Multiple warrant regimes may support related actions.

There is currently no universal rule:

\[
\mathfrak W_1
+
\mathfrak W_2
\to
\mathfrak W_*.
\]

Questions include:

- when do independent warrants strengthen one another?
- when are guarantees incomparable?
- when should one regime dominate?
- how should conflicts between deductive, statistical, testimonial, and defeasible warrants be represented?
- can a meta-warrant justify an aggregation policy?

Current stance: do not introduce scalar aggregation by default.

### 21.3 Warrant of warrant

The regress remains explicit.

If:

\[
\mathfrak W;A
\vdash_\pi
a:G,
\]

the assumptions, certificate checker, reliability model, or warrant regime may themselves become targets of warrant.

The framework supports axiomatic stopping points, empirical reliability chains, proof chains, defeasible/coherence-based stopping, and unresolved assumptions.

No fake universal closure is assumed.

### 21.4 Context entailment

The foundational license condition is:

\[
C\models A.
\]

Executable benchmark regimes currently use explicit set inclusion.

Open problem: connect the warrant layer to richer theory/context semantics so context satisfaction can use actual logical entailment, morphism-aware entailment, graded assumptions, or defeasible context.

### 21.5 Epistemic action algebra

We have a generic action type:

\[
a:
S
\rightharpoonup
S\times O_a.
\]

But we do not have a representation theorem showing a unique/minimal primitive basis.

Likely result: primitive action bases are representation-relative.

Open questions include useful normal forms, action equivalence, and compositional generation of revision/update/accept/retract.

### 21.6 Candidate-generation/warrant interaction

Generation and evaluation are separated, but the feedback loop deserves deeper study:

\[
R_t
\xrightarrow[\pi]{\mathcal G}
d_t
\xrightarrow{\operatorname{Elab}}
c_t
\xrightarrow{V}
f_t
\xrightarrow{\operatorname{control/update}}
R_{t+1}.
\]

Open question: what general properties make such a loop effective?

Possible dimensions include completeness, convergence, search bias, cost, information gain, repairability, and representation change.

### 21.7 Reflection and self-application

Because strategies, warrants, and the meta-model itself are representable targets, the framework is reflectively closed at the representation level.

Open questions include fixed points, self-modifying warrant policies, trust bootstrapping, meta-regress control, and reflective consistency.

### 21.8 Empirical adequacy of the factorization

The architecture is conceptually coherent and executable in reference cases.

It is not yet empirically established that the factorization improves annotation reliability, reasoning quality, auditability, inquiry navigation, or strategy selection.

This is now primarily an empirical question.

## 22. Explicitly deferred richer branches

### GitHub issue #17 — first-class derivation/subargument structure

Escalate when subargument-specific attack matters, last-link/weakest-link preference matters, proof-sensitive warrant matters, or exact proof explanation is required.

Expected direction: canonical derivation DAGs.

### GitHub issue #18 — full ABA+ / set-to-set hyperargumentation

Escalate when attack reversal matters, collective/set-to-set attack changes semantics, or faithful ABA+ is required.

Expected direction: hyperargumentation/set-to-set semantics rather than forcing binary Dung edges.

## 23. Status classification

### Provisionally stable

- separation of representation, generation, support, warrant, license, action, control;
- ATMS-like assumption contexts;
- positive support antichain algebra;
- typed warrants;
- representation-relative epistemic actions;
- explicit separation of defeasible attack/defeat from support;
- relational reflection;
- candidate-generation interface.

### Implemented reference instances

- support antichain algebra;
- Bernoulli support interpretation;
- ABA construction;
- typed attack origins;
- binary preference filtering;
- grounded Dung semantics;
- grounded dialectical warrant;
- graded-support warrant;
- strict-Horn deductive warrant;
- measurement warrant;
- testimony posterior warrant;
- finite-class statistical warrant;
- strategy-performance warrant.

### Open research

- candidate generation theory;
- warrant composition;
- context entailment;
- action-algebra representation results;
- warrant regress/meta-warrant;
- reflective self-application;
- empirical validation.

## 24. What should not happen next

Do not continue importing formal systems merely because they are related.

Do not add more argumentation frameworks, probability calculi, belief-revision operators, proof logics, or warrant regime examples unless a concrete benchmark exposes a missing distinction.

The project has enough machinery to test.

## 25. Recommended next foundational discussion

The next theoretical discussion should be:

# **Candidate generation**

Specifically:

1. What is the object being generated?
2. What distinctions exist between expression construction, definitional extension, predicate invention, theory extension, analogy, and representation change?
3. What parts can be treated as constrained search?
4. What cannot?
5. Can mature frameworks such as program synthesis, ILP/MIL, anti-unification, abductive logic programming, theory morphisms, and concept learning be unified at the interface level?
6. Is there a useful factorization analogous to the warrant factorization?
7. What would count as a canonical or minimal generative basis?
8. How should representation-changing operations be modeled?
9. What guarantees can be stated about search without collapsing generation into evaluation?
10. How should learned/generated operators themselves become candidates?

This topic is intentionally left open for the next session.

## 26. Relation to the accompanying paper

The accompanying paper draft:

- states the architecture as a research contribution;
- compares it to adjacent formal traditions;
- frames the main contribution as **factorization and interface synthesis**, not invention of each component;
- identifies candidate generation and warrant composition as the major next research problems.

Future literature review should explicitly compare against formal epistemology, AGM and belief-base change, dynamic epistemic logic, ATMS and truth-maintenance, provenance semirings, Justification Logic, Dung/ABA/ASPIC+, probabilistic argumentation, formal learning theory, metareasoning, logical frameworks/theory graphs, and cognitive architectures if relevant.

## 27. Repository handoff map

Canonical high-level documents:

- docs/formal-epistemic-reasoning-metamodel.md — this document;
- docs/paper-formal-epistemic-reasoning-metamodel.md — paper draft;
- docs/project-status.md — current project-management status;
- docs/architecture-reassessment.md — stop-rule/reassessment;
- docs/research-log-post-v1.md — chronological research development;
- docs/warrant-license-interface.md — warrant formalism;
- docs/candidate-generation-interface.md — candidate-generation work;
- docs/end-to-end-warrant-benchmark.md — executable warrant benchmark;
- docs/epistemic-actions-support-algebra.md — actions/support;
- docs/support-antichain-probability.md — positive support;
- docs/defeat-argumentation-integration.md — defeat;
- docs/preference-regimes.md — preference boundary;
- docs/metareasoning-strategy-reflection.md — strategy/reflection;
- docs/assumption-context-meta-model.md — ATMS-style contexts;
- docs/epistemic-transition-calculus.md — earlier transition calculus;
- docs/decisions/ — ADRs.

Open architectural issues:

- issue #17 — derivation/subargument structure;
- issue #18 — full ABA+ / hyperargumentation.

## 28. Final closeout assessment

The meta-model is not “finished” in the sense of a complete philosophy of epistemology.

It is, however, **architecturally mature enough to freeze as a versioned research object**.

Its strongest current claim is:

\[
\boxed{
\text{epistemic reasoning is better modeled as a composition of distinct generative, support, warrant, action, and control structures than as a flat taxonomy of inference types.}
}
\]

The most important unresolved foundational problem is candidate generation.

The most important unresolved integrative problem is warrant composition.

The most important empirical question is whether the factorization improves actual reasoning/inquiry work.

# Closeout checklist

- [x] Canonical name chosen: **Formal Epistemic Reasoning Meta-Model**
- [x] Core factorization recorded
- [x] Main formal objects recorded
- [x] Warrant interface recorded
- [x] Executable benchmark regimes recorded
- [x] Verification status recorded
- [x] Deferred argumentation branches preserved
- [x] Candidate generation marked as major open problem
- [x] Warrant composition marked as major open problem
- [x] Context entailment/action algebra/reflection open questions recorded
- [x] Relation to Inquiry Representation Model recorded
- [x] Relation to future Inquiry System recorded
- [x] Paper draft prepared
- [x] Candidate-generation landscape survey resumed and adoption decision recorded
- [x] Candidate-generation framework mappings completed across CEGIS, MIL, anti-unification, HR, and conceptual blending
- [ ] Full comparison to adjacent existing meta-models/frameworks deepened
- [ ] Empirical usefulness study performed
