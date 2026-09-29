# A Factorized Meta-Model for Epistemic Reasoning

**Author:** TBD  
**Draft status:** preprint / arXiv-style research draft  
**Repository artifact:** Formal Epistemic Reasoning Meta-Model project

## Abstract

Formal epistemology contains mature theories of belief revision, probabilistic updating, structured argumentation, justification, formal learning, epistemic action, and metareasoning. These theories are powerful, but they often take different objects as primitive and therefore answer different questions. A recurring source of confusion is to treat “inference” as one undifferentiated operation, or to classify all reasoning under a small flat taxonomy such as deduction, induction, and abduction. This paper proposes a factorized meta-model in which formal representation, candidate generation, support provenance, structured defeat, warrant, license, epistemic action, and strategy/control are represented separately and composed through explicit interfaces. The central warrant judgment is written

\[
\mathfrak W;A\vdash_\pi a:G,
\]

meaning that under warrant regime \(\mathfrak W\) and applicability assumptions \(A\), certificate \(\pi\) warrants epistemic action \(a\) with typed guarantee \(G\). Positive support is represented independently using finite antichains of minimal assumption environments, while defeasible conflict is handled by structured attack/defeat semantics. The architecture is instantiated with executable reference regimes for deductive derivation, defeasible acceptability, probabilistic support reporting, measurement, testimony, finite-class statistical learning, and strategy selection. The proposal is not a new replacement logic for these domains. Its intended contribution is an interface-level factorization that clarifies how heterogeneous epistemic guarantees, actions, and reasoning processes relate without forcing them into one confidence scalar or one universal inference taxonomy. We identify candidate generation, warrant composition, context entailment, and reflective self-application as major open problems.

## 1. Introduction

A large part of formal epistemology can be understood as the construction of precise models for epistemic states and epistemic change. Probability theory models graded credence and updating. AGM-style belief revision models rational belief change. Dynamic epistemic logic models informational actions. Structured argumentation models defeasible support and attack. Justification Logic makes reasons explicit. Formal learning theory provides convergence and generalization guarantees. Metareasoning studies the selection and control of reasoning procedures.

These traditions overlap, but they are not interchangeable.

A deductive proof, a testimonial report, a statistical generalization bound, an undefeated defeasible argument, a calibrated measurement, and a strategy benchmark can all provide epistemically relevant support. Yet they do not provide the same kind of guarantee, justify the same epistemic action, or have the same failure conditions.

This motivates a different question from the usual search for a single formal epistemology:

> What meta-level structure is required to represent heterogeneous forms of epistemic reasoning without collapsing their distinctions?

A related motivation comes from traditional classifications of inference. Deduction, induction, and abduction are often treated as major kinds of reasoning. But when these categories are used operationally, they frequently mix several different dimensions.

For example, an “abductive inference” may involve generation of a candidate explanation, formal admissibility conditions, explanatory comparison, defeasible argumentation, and a later change of epistemic state. An “inductive inference” may refer to a learning algorithm, a statistical theorem, a numerical update, or a decision to deploy a predictor.

This paper argues that the more productive foundational object is not a flat taxonomy of inference types but a factorized architecture.

The proposed architecture distinguishes:

\[
\boxed{
\text{representation}
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
\text{epistemic action}
\neq
\text{strategy/control}.
}
\]

The goal is not to replace mature formalisms, but to specify how they can occupy different roles within a common epistemic reasoning model.

## 2. Motivating distinctions

### 2.1 Cognitive novelty is not logical ampliation

A representation may make an implicit relation explicit without logically adding content beyond the assumptions.

Thus:

\[
\text{new to the reasoner}
\neq
\text{non-entailing relative to the formal assumptions}.
\]

This matters for pattern recognition, measurement, theorem proving, and representation change.

### 2.2 Candidate production is not warrant

Generating a hypothesis does not warrant it.

A system may generate:

- a new explanatory hypothesis;
- a new predicate;
- a theory translation;
- an analogy;
- a revised decomposition;
- a program;
- a conjecture.

The generative mechanism and the warrant for later epistemic action should be represented independently.

### 2.3 Support is not acceptance

A proposition may have positive support while remaining defeated, undecided, or outside the scope of a current license.

Thus:

\[
\text{support}
\neq
\text{dialectical acceptability}.
\]

### 2.4 Warrant is not update

Even if an epistemic action is warranted, it need not be executed.

This motivates:

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

## 3. Related work

### 3.1 Formal epistemology

Formal epistemology is methodologically plural. It uses probability theory, logic, ranking functions, decision theory, belief revision, and related mathematical tools to study epistemic states and norms. This pluralism is one motivation for the present proposal: the field already contains heterogeneous formal resources rather than one universally accepted epistemic calculus.

The contribution proposed here is therefore architectural rather than foundational in the sense of replacing that plurality.

### 3.2 AGM belief revision and belief change

AGM theory represents belief-state change through postulates and representation theorems for operations such as expansion, contraction, and revision. Closely related work distinguishes belief sets from belief bases and studies iterated revision.

The present framework shares the commitment to explicit epistemic-state transformations, but it generalizes the target beyond revision:

\[
a:S\rightharpoonup S\times O_a.
\]

This includes operations that do not mutate persistent belief state at all, such as deriving a result or recording a measurement.

### 3.3 Dynamic epistemic logic

Dynamic epistemic logic treats information-changing events as structured formal objects with preconditions and model-transforming semantics.

This is an important precedent for making epistemic actions explicit.

The present framework is less committed to one possible-worlds semantics, using epistemic action as an interface across multiple regimes.

### 3.4 Assumption-based truth maintenance

de Kleer’s Assumption-Based Truth Maintenance System maintains multiple sets of assumptions under which propositions are derivable, instead of committing to one global belief state.

This architecture strongly motivates the persistent support representation used here.

### 3.5 Provenance

Provenance semirings distinguish alternative derivations from joint dependence.

Minimal-witness provenance gives a particularly close algebraic match to ATMS-style labels.

The present positive-support representation is:

\[
\mathsf{Supp}(X)
=
\operatorname{Antichain}
(
\mathcal P_{\mathrm{fin}}(X)
),
\]

with alternative and joint support given by normalized union and pairwise union.

### 3.6 Justification Logic

Justification Logic makes reasons explicit through forms such as:

\[
t:F.
\]

This provides a strong precedent for reifying reasons/certificates.

The present framework differs in making the target of warrant an epistemic action with a typed guarantee.

### 3.7 Structured argumentation

Dung’s abstract argumentation framework separates arguments from their acceptability under attack.

ABA makes assumptions and their contraries central.

ASPIC+ explicitly distinguishes undermining, rebutting, and undercutting, as well as strict and defeasible rules and preference-sensitive defeat.

The current executable layer uses an ABA-like construction substrate while retaining typed attack-origin metadata and Dung-style grounded acceptability.

### 3.8 Formal learning theory

PAC learning and uniform-convergence theory show that inductive procedures can receive precise theorem-level guarantees, provided the problem class and sampling assumptions are explicit.

This is used here as a model case showing that a warrant can be method-level and statistical rather than proof-like.

### 3.9 Metareasoning

Metareasoning studies reasoning about computational or inferential processes, including strategy selection under resource constraints.

This supports the distinction between object-level operators and strategies controlling those operators.

### 3.10 Logical frameworks and theory graphs

LF and MMT provide mature machinery for representing formal languages, declarations, proofs, and theory morphisms.

The present meta-model treats this as a likely formal substrate rather than reinventing a universal syntax layer.

## 4. Formal architecture

We represent a reasoning episode as:

\[
\boxed{
R=
(
\mathcal F,
K_{\mathcal F},
\Gamma,
Q,
\Pi
).
}
\]

Here:

- \(\mathcal F\) is the formal representation layer;
- \(K_{\mathcal F}\) is persistent epistemic support state;
- \(\Gamma\) is a temporary assumption environment;
- \(Q\) is the current task/question;
- \(\Pi\) is the strategy/control component.

These coordinates are not intended as metaphysically primitive entities. They are a working factorization.

## 5. Formal representation

A compact formal-artifact vocabulary is:

\[
\mathcal F
=
\{
\mathsf{Theory},
\mathsf{Declaration},
\mathsf{Object},
\mathsf{Morphism}
\}.
\]

This follows theory-graph/logical-framework practice.

Expressions and proofs are formal objects.

New symbols and definitions are declarations.

Collections of declarations form theories.

Structure-preserving translations are morphisms.

This layer is deliberately separated from epistemic role.

A proposition may be an assumption in one reasoning context and a derived conclusion in another.

## 6. Support state

The persistent support state is:

\[
K_{\mathcal F}
=
(
N,A,J,\lambda,\rho
).
\]

Here:

- \(N\) is a set of represented nodes;
- \(A\subseteq N\) is a set of assumables;
- \(J\) is a justification/dependency graph;
- \(\lambda(n)\) is a set of minimal assumption environments supporting \(n\);
- \(\rho\) is an optional family of typed graded interpretations.

A temporary environment is:

\[
\Gamma\subseteq A.
\]

Its deductive closure may be written:

\[
C(\Gamma)=\operatorname{Cl}_J(\Gamma).
\]

This separates persistent alternatives from temporary reasoning contexts.

## 7. Positive support algebra

Let \(X\) be primitive assumption tokens.

Define:

\[
\mathsf{Supp}(X)
=
\operatorname{Antichain}
(
\mathcal P_{\mathrm{fin}}(X)
).
\]

For support values \(A,B\):

\[
A\oplus B
=
\operatorname{Min}(A\cup B)
\]

and:

\[
A\otimes B
=
\operatorname{Min}
\{
E\cup F:
E\in A,
F\in B
\}.
\]

with:

\[
0=\varnothing,
\qquad
1=\{\varnothing\}.
\]

The structure is a free distributive lattice over \(X\), and equivalently an idempotent commutative semiring.

This representation intentionally quotients away proof multiplicity.

## 8. Graded interpretations

A general graded interpretation is:

\[
\rho_\eta:
\mathsf{Prov}
\to
V_\eta.
\]

For an independent-Bernoulli reference regime:

\[
\rho_{\mathrm{Bern}}(A)
=
P(
\llbracket A\rrbracket
\mid
C
),
\]

where \(C\) denotes consistency relative to explicit nogoods.

This quantity is a probability of the support event, not automatically the probability that the supported proposition is true.

Thus:

\[
\boxed{
\text{support grade}
\neq
\text{truth probability}
}
\]

without further warrant.

## 9. Candidate generation

For a reasoning episode \(R\), define a draft-generation system:

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

Reachability is:

\[
\operatorname{Reach}(R)
=
\{
d:
d_0
\xrightarrow{\mathcal O_R*}
d
\}.
\]

A strategy controls operator choice:

\[
\pi:
\operatorname{Hist}(R,\mathcal G_R)
\to
\mathcal P(
\mathcal O_R
\cup
\{\operatorname{stop}\}
).
\]

Formal elaboration maps drafts into formal artifacts when possible:

\[
\operatorname{Elab}_{\mathcal F}(d)
=
c
\]

or fails.

Evaluation functions produce diagnostic feedback:

\[
V_j(R,c)
\to
(
\operatorname{status},
f_j
).
\]

This yields the loop:

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

Candidate generation remains the least developed theoretical component.

## 10. Defeasible argumentation

Positive support and defeasible acceptability are represented separately.

The pipeline is:

\[
\text{positive support}
\to
\text{argument construction}
\to
\text{attack}
\to
\text{defeat}
\to
\text{acceptability}.
\]

The first executable bridge uses ABA-style assumptions and contraries.

Attack metadata preserves richer origin distinctions such as rebut, undercut, and undermine.

Grounded Dung semantics supplies the first acceptability semantics.

## 11. Warrant

The core judgment is:

\[
\boxed{
\mathfrak W;
A
\vdash_\pi
a:G.
}
\]

Interpretation:

under warrant regime \(\mathfrak W\) and applicability assumptions \(A\), certificate \(\pi\) is sufficient to warrant epistemic action \(a\) with guarantee \(G\).

This formulation has several consequences.

First, warrant is action-relative.

Second, guarantees are typed.

Third, warrant can be defeasible.

Fourth, heterogeneous warrant regimes need not collapse into a common scalar.

## 12. License

Given current context \(C\):

\[
C\models A
\]

and a valid warrant judgment, define:

\[
\operatorname{Licensed}_{\mathfrak W,C}(a:G).
\]

This distinguishes conditional warrant from current applicability.

An action can be warranted in principle but not licensed in the current context.

## 13. Epistemic action

An epistemic action is represented as:

\[
a:
S
\rightharpoonup
S\times O_a.
\]

This permits:

- readout-only actions;
- persistent-state updates;
- temporary-context changes;
- strategy/control actions.

“Primitive action” is therefore relative to an action algebra and representation rather than assumed metaphysically.

## 14. Executable reference regimes

The meta-model has been tested using heterogeneous warrant regimes.

### 14.1 Defeasible acceptability

A grounded-IN certificate can warrant typed defeasible actions such as retaining a candidate or raising support.

Grounded status does not warrant arbitrary acceptance.

### 14.2 Graded support

A probabilistic support certificate warrants only recording its computed support grade.

No universal confidence threshold is assumed.

### 14.3 Deduction

A strict-Horn checker verifies whether:

\[
\Gamma\vdash h.
\]

The corresponding warrant licenses derivation relative to \(\Gamma\), not acceptance of \(\Gamma\).

### 14.4 Measurement

A measurement certificate includes value, unit, uncertainty, and calibration provenance.

It warrants recording the measurement result, not exact proposition acceptance.

### 14.5 Testimony

A source model gives:

\[
P(R^+\mid H)
\]

and:

\[
P(R^+\mid\neg H).
\]

With an explicit prior, a posterior can be computed and recorded.

The source reliability model remains reference-class relative.

### 14.6 Statistical learning

A finite-class uniform-convergence certificate computes:

\[
\epsilon
=
\sqrt{
\frac{
\log(2|\mathcal H|/\delta)
}{
2m
}
}
\]

and records the corresponding population-loss upper bound with confidence \(1-\delta\).

The theorem does not verify its own sampling assumptions.

### 14.7 Strategy selection

For paired normalized utilities:

\[
D_i
=
u_i(\pi)-u_i(\pi_0).
\]

A strategy-selection action can be warranted when:

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
>
0.
\]

The conclusion remains relative to the declared task distribution and utility function.

## 15. Why this is not a unified confidence theory

The architecture deliberately refuses to assign all epistemic objects one scalar.

A deductive truth-preservation guarantee, a measurement uncertainty statement, a PAC bound, a grounded argument status, and a strategy-performance bound are not values on one natural common scale.

They may ultimately inform one decision, but that aggregation itself requires a warrant regime.

This yields a general principle:

\[
\boxed{
\text{heterogeneous epistemic guarantees remain typed until an explicit aggregation policy is warranted.}
}
\]

## 16. Reflection and metareasoning

Strategy is represented as control over reasoning operators.

A strategy may itself become the target of warrant.

More generally, the framework uses a relational notion of reflection:

\[
\operatorname{about}(x,y).
\]

This avoids imposing a permanent hierarchy of object level, meta-level, meta-meta-level, and so on.

The architecture is closed under self-description at the representation level.

## 17. Argument identity and abstraction boundaries

The current executable ABA layer identifies arguments by:

\[
(
\text{conclusion},
\text{minimal support environment}
).
\]

This is an explicit semantic quotient.

It is sufficient for current assumption-centered attack semantics.

It is not sufficient for every structured-argumentation semantics.

If subargument attack, rule-level preference, or proof-sensitive warrant becomes necessary, first-class derivation DAGs are the planned extension.

Similarly, the current preference regime is not full ABA+.

General ABA+ may require set-to-set attacks and hyperargumentation.

These boundaries are intentionally explicit rather than silently approximated.

## 18. Evaluation and implementation status

The current implementation includes reference modules for:

- support algebra;
- probabilistic support interpretation;
- ABA construction;
- defeat;
- preference filtering;
- warrant/license;
- strict-Horn proof checking;
- measurement/testimony models;
- statistical-learning bounds;
- strategy-performance bounds.

The integrated repository has been executed on native Windows:

- 138 tests passed;
- the seed fixture rebuilt;
- 8 generated artifacts matched;
- graph validation returned zero errors and warnings;
- dependency checks were clean.

This verifies internal implementation consistency, not philosophical correctness or empirical usefulness.

## 19. What appears to be new

Most mathematical components are established.

The proposed contribution should therefore be stated conservatively.

The likely novelty is the **factorization and interface synthesis**:

1. separating candidate generation from evaluation and warrant;
2. targeting warrant at typed epistemic actions rather than only propositions;
3. separating conditional warrant from context-relative license and execution;
4. treating typed heterogeneous guarantees as first-class;
5. integrating ATMS-like provenance, structured argumentation, formal-learning guarantees, measurement/testimony certificates, and strategy warrants through one action-targeted interface;
6. making reflection relational rather than committing to a fixed meta-level hierarchy.

A strong novelty claim would require a deeper systematic literature review.

## 20. Open problem: candidate generation

Candidate generation is the largest unresolved part.

Existing mature approaches cover important fragments:

- program synthesis searches program spaces under specifications;
- CEGIS alternates candidate generation and counterexample-guided repair;
- inductive logic programming searches hypotheses under background knowledge and examples;
- meta-interpretive learning introduces reusable predicates and metarules;
- anti-unification computes generalizations;
- abductive logic programming generates hypotheses constrained by integrity conditions;
- theory morphisms generate or test structural translations;
- conceptual-combination systems construct new representations.

The challenge is whether these can be placed under one useful meta-interface without pretending they share one universal primitive operator basis.

The candidate-generation interface was subsequently stress-tested against CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR automated theory formation, and computational conceptual blending. All five fit a revised typed regime without a new top-level coordinate:

\[
\mathcal G_R=(\mathcal A_R,\mathcal L_R,\mathcal D_R,B_R,\mathcal O_R,\to_R,V_R).
\]

A generation episode is separated as \(E_G=(R,\mathcal G_R,d_0)\), and changes to the generative regime itself are modeled separately as \(\mu:\mathcal G_R\rightharpoonup\mathcal G'_R\). The mapping also shows that transformationality is representation-relative: generating a fresh predicate may remain an ordinary transition if the existing meta-language already permits predicate invention.

The central open questions are:

- what is generated?
- how does the representation vocabulary itself change?
- when does construction become substantive concept invention?
- can generative completeness be defined relative to a representation language?
- how should operator invention be represented?
- how should search bias itself be warranted?
- can different generative spaces be compared structurally?

## 21. Open problem: warrant composition

The framework can represent multiple warrants but does not yet give a universal composition rule.

Suppose a target action has:

- testimonial evidence;
- a probabilistic support grade;
- a statistical guarantee;
- a defeasible argument;
- a deductive conditional derivation.

These supports may be mutually reinforcing, redundant, incomparable, or in conflict.

The correct combination rule may itself depend on a meta-regime.

A future theory of warrant composition should therefore preserve typed guarantees rather than immediately scalarizing them.

## 22. Open problem: context semantics

The foundational license condition is:

\[
C\models A.
\]

Current executable regimes approximate this with set inclusion.

A richer implementation should eventually support:

- logical entailment;
- defeasible assumptions;
- theory morphisms;
- graded applicability;
- temporal validity;
- provenance-sensitive context.

## 23. Open problem: epistemic action algebras

The generic action representation is broad but does not establish a canonical primitive basis.

A future research direction is to study action equivalence and representation theorems.

One question is whether familiar actions such as expansion, contraction, revision, acceptance, and retraction can be generated from a smaller basis relative to an explicit state representation.

Another is whether no representation-independent primitive basis exists.

## 24. Open problem: warrant of warrant

Any warrant depends on assumptions, certificate semantics, and checking rules.

These can themselves be epistemic targets.

The framework intentionally leaves the regress open.

This is not a defect to be hidden.

Possible stopping conditions include:

- axiomatic assumptions;
- formal proof;
- empirical calibration;
- defeasible coherence;
- pragmatic resource limits;
- unresolved assumptions.

## 25. Relationship to inquiry representation

The foundational meta-model and the inquiry-representation project are distinct.

The inquiry graph represents what was expressed and how the inquiry evolved.

The meta-model provides a language for interpreting the epistemic structure of those moves.

The inquiry graph can therefore become an empirical substrate for testing the meta-model.

Conversely, the meta-model can guide higher-level annotations such as:

- support environment;
- warrant type;
- strategy episode;
- candidate-generation operation;
- defeat;
- reflective relation.

## 26. Limitations

The proposal has several important limitations.

First, candidate generation remains underdeveloped.

Second, the model currently contains a set of interfaces rather than one representation theorem proving their necessity or minimality.

Third, the executable warrant regimes are deliberately small benchmark fragments.

Fourth, context satisfaction is simplified.

Fifth, the architecture has not yet been empirically shown to improve reasoning or inquiry navigation.

Sixth, the comparison with existing integrated cognitive and epistemic architectures is not yet exhaustive.

Seventh, the current model is partly descriptive and partly normative; each warrant regime must state which role it is playing.

## 27. Research methodology

The model was developed through repeated primitive-factorization analysis.

The working pattern was:

\[
\text{candidate formalization}
\to
\text{counterexample}
\to
\text{hidden assumption}
\to
\text{refactor}.
\]

Typical diagnostics were:

- underfactored;
- overfactored;
- misfactored;
- representation-dependent;
- incomplete;
- noncanonical.

The methodological target was:

\[
\boxed{
\text{minimal, complete, compositional, nonredundant, and preferably canonical factorization}
}
\]

relative to an explicit representation contract.

## 28. Conclusion

The main conclusion is not that one new universal epistemic logic has been discovered.

It is that several recurring confusions in reasoning theory arise from conflating distinct architectural functions.

A more promising representation separates:

\[
\boxed{
\text{generation}
\neq
\text{support}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{action}
\neq
\text{control}.
}
\]

This permits deductive, defeasible, probabilistic, statistical, testimonial, measurement, and metareasoning guarantees to coexist without pretending they have the same semantics.

The architecture is mature enough to support reference implementations and benchmark cases.

Its largest foundational gap is candidate generation.

Its largest integrative gap is warrant composition.

Its next scientific test is empirical: whether this factorization actually improves the representation, audit, navigation, or control of real reasoning processes.

## References

A submission-ready bibliography should be generated from the repository reference list. Core works include:

- Alchourrón, Gärdenfors, and Makinson on belief revision.
- de Kleer on Assumption-Based Truth Maintenance Systems.
- Dung on abstract argumentation.
- Bondarenko, Dung, Kowalski, and Toni on Assumption-Based Argumentation.
- Modgil and Prakken on ASPIC+.
- Čyras and Toni on ABA+.
- Green, Karvounarakis, and Tannen on provenance semirings.
- Artemov on Justification Logic.
- Baltag, Moss, van Benthem and related work on Dynamic Epistemic Logic.
- Shalev-Shwartz and Ben-David on statistical learning theory.
- Lieder and Griffiths on strategy selection as rational metareasoning.
- Harper, Honsell, and Plotkin on LF.
- Rabe on MMT/theory graphs.
- JCGM GUM and VIM on measurement and uncertainty.
- Bovens and Hartmann on Bayesian epistemology and testimony.
- Merdes, von Sydow, and Hahn on source reliability.
- Gulwani, Polozov, and Singh on program synthesis.
- Kakas, Kowalski, and Toni on abductive logic programming.

See docs/references.md for the working bibliography.
