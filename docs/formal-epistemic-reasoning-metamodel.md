# Formal Epistemic Reasoning Meta-Model — Closeout and Handoff

> **Status:** canonical project-1 handoff.
> **Purpose:** preserve the current state of the formal epistemic reasoning meta-model so a future agent can resume without reconstructing this long conversation.
> **Scope:** this document covers the foundational meta-model, not the product-level inquiry system. It also records the relation to the inquiry-representation project and the main open research directions.
> **Notation:** see §5.1 for the symbol table. Each symbol has one meaning throughout.

## 1. Project identity

The cleanest name for the foundational project is:

**Formal Epistemic Reasoning Meta-Model**

The project is not intended to be one theory of knowledge, one logic, one universal confidence calculus, one list of inference types, one cognitive architecture, or one argumentation formalism.

It is intended to be a **meta-model of epistemic reasoning**: a representation of the major kinds of objects, state, operations, support relations, warrants, actions, and control structures that occur across different reasoning regimes.

The central research question is:

> **What structure is required to represent and evaluate epistemic reasoning moves without collapsing deduction, statistical learning, defeasible reasoning, measurement, testimony, candidate generation, belief/update operations, and strategy selection into one undifferentiated notion of inference?**

A second foundational question motivated much of the work:

> **What warrants a reasoning move, and what warrants that warrant?**

This second question is a descendant of Toulmin's distinction between a *warrant* and its *backing* (see §20).

The inquiry-graph project emerged later as a distinct but related project for representing actual inquiry histories.

## 2. Three related projects

### Project 1 — Formal Epistemic Reasoning Meta-Model

**Goal:** represent the structure of epistemic reasoning itself.

### Project 2 — Inquiry Representation Model

A source-grounded representation of actual inquiry histories: utterances, claims, questions, moves, alternatives, objections, revisions, strategies, stance, provenance, and question status.

**Goal:** represent how an inquiry actually develops.

### Project 3 — Inquiry System

A useful tool built on the first two.

Possible functions include navigating unresolved questions, recovering abandoned branches, inspecting assumptions and dependencies, comparing competing arguments, exposing why a view changed, identifying recurring reasoning strategies, recommending what to inspect next, and helping a person or model resume a long inquiry.

**Goal:** make inquiry easier, more auditable, and potentially better.

These projects are related but should not be conflated.

## 3. Meta-relationship among the projects

The Inquiry Representation Model can represent the historical process by which the Formal Epistemic Reasoning Meta-Model was constructed.

The Formal Epistemic Reasoning Meta-Model can characterize operations represented inside an inquiry graph.

The future Inquiry System can use both models to reason about inquiry and potentially about its own reasoning.

Reflection is represented relationally, as $\operatorname{about}(x,y)$. An object is "meta" relative to another object when it reasons about or controls that target.

## 4. Main substantive result

The original inquiry began with traditional categories such as deduction, induction, and abduction.

The work suggests that these are not an adequate primitive partition of epistemic reasoning.

The central reason is that they mix levels.

Something called "abduction" may include candidate generation, admissibility constraints, explanatory scoring, defeasible support, and a later epistemic update.

Something called "induction" may refer to a learning algorithm, a statistical theorem, a support change, a prediction policy, or an epistemic update.

Deduction is better defined, but even there:

$$
\text{derivation}
\neq
\text{acceptance of premises}
\neq
\text{state update}.
$$

The main replacement is therefore not a new flat taxonomy. It is a **factorized architecture**.

## 5. Canonical factorization

The current stable distinction is:

$$
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
\text{strategy/control}
}
$$

These categories should not be treated as a partition of all objects. They are architectural dimensions/layers.

A reasoning state is described as:

$$
s=(\mathcal F,K_{\mathcal F},\Gamma,Q,\Pi)\in\mathcal S
$$

where:

- $\mathcal F$: formal representation substrate;
- $K_{\mathcal F}$: persistent support/provenance state;
- $\Gamma$: temporary assumption context;
- $Q$: current question/task;
- $\Pi$: strategy/control state;
- $\mathcal S$: the space of reasoning states.

### 5.1 Notation

Earlier drafts reused several letters for unrelated objects. The following conventions are canonical; other documents in `docs/` may still use older symbols.

| Symbol | Meaning | Section |
|---|---|---|
| $s$, $\mathcal S$ | reasoning state, state space | §5, §11 |
| $\mathcal F$ | formal representation substrate | §6 |
| $K_{\mathcal F}=(N,A,J,\lambda,\rho)$ | persistent support state | §7 |
| $N$ | represented nodes | §7 |
| $A\subseteq N$ | assumable nodes (only use of $A$) | §7 |
| $J$ | justification structure | §7 |
| $\lambda(n)$ | label: minimal support environments of $n$ | §7 |
| $\rho_\eta$ | graded interpretation under regime $\eta$ | §9 |
| $\Gamma$ | temporary assumption context | §7 |
| $\operatorname{Cl}_J(\Gamma)$ | closure of a context | §7 |
| $X$ | primitive assumption tokens | §8 |
| $E, F$ | assumption environments (finite subsets of $X$) | §8 |
| $\sigma,\tau$ | support antichains | §8, §9 |
| $R$ | reasoning episode | §10 |
| $\mathcal G_R$ | typed generative regime | §10 |
| $\mathcal A_R,\mathcal L_R,\mathcal D_R,B_R,\mathcal O_R,V_R$ | artifact ontology, language, draft space, bias, operators, evaluators | §10 |
| $E_G,d_0$ | generation episode and initial draft | §10 |
| $\mu$ | generative-regime transformation | §10 |
| $c$ | elaborated candidate in $\mathcal F$ | §10 |
| $\operatorname{Ev}_j$ | evaluator | §10 |
| $\pi$ | strategy (only use of $\pi$) | §10 |
| $\Pi$ | strategy/control state | §5 |
| $a$ | epistemic action | §11 |
| $O_a$ | output of action $a$ | §11 |
| $\mathsf{Act},\ \mathsf B$ | action set, action basis | §11 |
| $\mathfrak W$ | warrant regime | §12 |
| $\Phi$ | applicability assumptions of a warrant | §12 |
| $\kappa$ | certificate/support object | §12 |
| $G$ | typed guarantee | §12, §14 |
| $C$ | current context (for licensing) | §13 |
| $\Delta_i$ | paired utility difference | §18.7 |

## 6. Formal representation layer

The representation layer is best understood through theory-graph/logical-framework ideas.

A compact candidate formal-artifact basis is:

$$
\mathcal F=
\{
\mathsf{Theory},
\mathsf{Declaration},
\mathsf{Object},
\mathsf{Morphism}
\}.
$$

Interpretation:

- formulas, terms, proofs: objects;
- predicates, constants, types, rules: declarations;
- collections/specifications: theories;
- translations/models/structure-preserving mappings: morphisms.

MMT-like theory graphs are the current preferred representation precedent.

LF may be used as a foundation/meta-theory inside such a framework rather than as a competing parallel layer.

Important distinction:

$$
\boxed{
\text{formal object identity}
\neq
\text{epistemic role}
}
$$

An assumption is usually a role played by a proposition/declaration/object in an epistemic context, not necessarily a distinct formal artifact type.

## 7. Persistent support and temporary contexts

The ATMS-inspired persistent support state is:

$$
K_{\mathcal F}
=
(N,A,J,\lambda,\rho)
$$

where:

- $N$: represented propositions/reports/hypotheses/etc.;
- $A\subseteq N$: assumable nodes;
- $J$: justification/dependency structure;
- $\lambda(n)$: minimal assumption environments supporting $n$;
- $\rho$: optional typed graded interpretations.

A temporary reasoning context is $\Gamma\subseteq A$. Its closure under the justifications is $\operatorname{Cl}_J(\Gamma)$.

This supports a black-box/white-box distinction:

- persistent state retains multiple hypothetical alternatives;
- a temporary context can stipulate assumptions and inspect consequences.

Selecting $\Gamma$ does not imply permanent acceptance.

## 8. Positive support algebra

For primitive assumption tokens $X$, positive support is represented by finite antichains of finite assumption environments:

$$
\mathsf{Supp}(X)
=
\operatorname{Antichain}
\big(
\mathcal P_{\mathrm{fin}}(X)
\big).
$$

Normalization, for a set $\sigma$ of environments:

$$
\operatorname{Min}(\sigma)
=
\{
E\in\sigma:
\nexists F\in\sigma,\
F\subsetneq E
\}.
$$

Alternative support:

$$
\sigma\oplus\tau
=
\operatorname{Min}(\sigma\cup\tau).
$$

Joint support:

$$
\sigma\otimes\tau
=
\operatorname{Min}
\{
E\cup F:
E\in\sigma,\
F\in\tau
\}.
$$

Identities:

$$
0=\varnothing,
\qquad
1=\{\varnothing\}.
$$

This is the free bounded distributive lattice over $X$, equivalently monotone Boolean provenance (PosBool) modulo logical equivalence, and an idempotent, absorptive commutative semiring.

The information-loss boundary is explicit: this representation preserves minimal support environments but discards proof multiplicity, proof-tree identity, repeated-use counts, and chronological construction history.

That loss is intentional at the support layer.

## 9. Graded support

Numeric/ordinal support is not primitive.

The general pattern is

$$
\rho_\eta:
\mathsf{Prov}
\to
V_\eta
$$

for an interpretation regime $\eta$ with value space $V_\eta$.

A concrete executable reference regime uses independent Bernoulli assumptions, optionally conditioned on nogoods.

If $\sigma$ is a support antichain:

$$
\rho_{\mathrm{Bern}}(\sigma)
=
P\big(
[\![\sigma]\!]
\mid
\text{consistency}
\big).
$$

Critical distinction:

$$
\boxed{
\rho_{\mathrm{Bern}}(\lambda(h))
\neq
P(h)
\text{ by definition}
}
$$

The value is the probability that the support condition holds under the model.

Turning that into proposition probability requires additional semantics/warrant.

Two further caveats:

- **Independence is a modeling assumption**, not a default truth. Correlated assumptions (shared sources, common causes) will make $\rho_{\mathrm{Bern}}$ miscalibrated.
- **Exact computation is #P-hard in general**, since it subsumes computing the probability of a monotone DNF formula under independent variables. Reference instances are small; realistic sizes will need approximation (e.g., sampling) or knowledge compilation.

## 10. Candidate generation

Candidate generation is separate from warrant and state update and is now treated as a typed generative regime:

$$
\mathcal G_R=
(
\mathcal A_R,
\mathcal L_R,
\mathcal D_R,
B_R,
\mathcal O_R,
\to_R,
V_R
).
$$

Here:

- \(\mathcal A_R\): artifact/candidate ontology;
- \(\mathcal L_R\): representation or generative language;
- \(\mathcal D_R\): draft/candidate state space;
- \(B_R\): admissibility/search bias;
- \(\mathcal O_R\): construction/traversal operators;
- \(\to_R\): ordinary candidate transition;
- \(V_R\): evaluator family.

A concrete generation episode is:

$$
E_G=(R,\mathcal G_R,d_0).
$$

Strategy/control remains separate:

$$
\pi:
\operatorname{Hist}(E_G)
\to
\mathcal P(
\mathcal O_R
\cup
\{\operatorname{stop}\}
).
$$

Formal elaboration maps a draft \(d\) into the formal substrate when possible:

$$
\operatorname{Elab}_{\mathcal F}(d)
=
\begin{cases}
c\in\mathcal F & \text{if formalizable}\\
\bot & \text{otherwise.}
\end{cases}
$$

Evaluation returns typed diagnostic feedback:

$$
\operatorname{Ev}_j(R,c)
\to
(
\operatorname{status},
f_j
).
$$

A change to the represented generative regime itself is distinct from an ordinary candidate transition:

$$
\mu:
\mathcal G_R
\rightharpoonup
\mathcal G'_R.
$$

Transformationality is representation-relative: generating a new predicate or concept is not automatically a \(\mu\)-transition if the existing meta-language already supports such generated declarations.

The interface has been mapped successfully to CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR automated theory formation and computational conceptual blending. Cross-framework orchestration and guarantee transport are largely covered by mature blackboard/multistrategy/algorithm-selection/reflection and Hets/DOL/MMT/refinement traditions.

Core distinction:

$$
\boxed{
\text{generative regime}
\neq
\text{ordinary candidate transition}
\neq
\text{strategy/control}
\neq
\text{evaluation}
\neq
\text{warrant}
}
$$

## 11. Epistemic actions

An epistemic action is modeled schematically as a typed partial state transducer:

$$
a:
\mathcal S
\rightharpoonup
\mathcal S\times O_a.
$$

Candidate state coordinates include $\mathcal F$, $K_{\mathcal F}$, $\Gamma$, $Q$, $\Pi$, and accumulated outputs.

Examples include deriving a consequence, recording a support grade, retaining a candidate, raising support, accepting, retracting, revising, changing temporary context, selecting a reasoning operator, and selecting a strategy.

No universal folk verb list is assumed primitive.

A primitive action basis is representation-relative: the action set $\mathsf{Act}$ is generated as the closure of a basis $\mathsf B$ under the chosen composition operations,

$$
\mathsf{Act}=\langle\mathsf B\rangle.
$$

Whether there is a canonical/minimal basis is still open.

## 12. Warrant

The central warrant judgment is:

$$
\boxed{
\mathfrak W;
\Phi
\vdash_\kappa
a:G
}
$$

read:

> under warrant regime $\mathfrak W$ and applicability assumptions $\Phi$, certificate/support object $\kappa$ warrants epistemic action $a$ with guarantee $G$.

Components:

- $\mathfrak W$: warrant regime;
- $\Phi$: explicit applicability assumptions;
- $\kappa$: certificate/support object;
- $a$: target epistemic action;
- $G$: typed guarantee.

The applicability assumptions $\Phi$ play a role close to the *critical questions* attached to argumentation schemes (§20): they are the conditions under which the certificate is fit for the action.

This preserves:

$$
\boxed{
\text{support}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{update}
}
$$

A support object may exist without being adequate for a given action.

A warrant may be conditionally valid while not currently licensed.

A licensed action may not be executed.

## 13. License

Given current context $C$ with $C\models\Phi$ and $\mathfrak W;\Phi\vdash_\kappa a:G$, derive:

$$
\boxed{
\operatorname{Licensed}_{\mathfrak W,C}(a:G)
}
$$

Current executable benchmark regimes approximate $C\models\Phi$ with explicit set inclusion.

That is an implementation simplification, not the foundational semantics.

## 14. Typed guarantees

Guarantee $G$ is deliberately heterogeneous.

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

$$
\text{positive support}
+
\text{structured attack}
+
\text{attack-to-defeat resolution}
+
\text{acceptability semantics}.
$$

The first executable argumentation bridge is ABA-like.

Assumptions have explicit contraries.

Basic attacks arise when one argument derives the contrary of an assumption used by another.

Attack-origin metadata retains distinctions such as undermine, undercut, and rebut.

The downstream abstract semantics currently uses Dung grounded semantics.

Thus:

$$
\boxed{
\text{argument has support}
\neq
\text{argument is dialectically acceptable}
}
$$

## 16. Preference-sensitive defeat

The current binary preference regime uses a strict relation over assumptions.

If $\alpha<\beta$ means $\alpha$ is less preferred than $\beta$, an attack on $\beta$ is blocked if the attacking support relies on such an $\alpha$.

This is intentionally only the normal-attack filtering part of ABA+-style preference handling.

It is **not** claimed to be full ABA+.

Full ABA+ can require set-to-set attack reversal.

That richer path is explicitly deferred in GitHub issue #18.

## 17. Argument identity boundary

For the current ABA/ABA+-style executable layer, argument identity is quotiented by

$$
(
\text{conclusion},\
\text{minimal supporting assumption environment}
).
$$

This is sufficient for the selected assumption-centered semantics.

It is not a claim that proof objects themselves are identical.

Thus:

$$
\boxed{
\text{formal derivation identity}
\neq
\text{ABA dialectical argument identity}
}
$$

First-class derivation/subargument structure is deferred until a semantics requires it.

That richer path is preserved in GitHub issue #17.

## 18. Executable warrant regimes

The repository contains executable benchmark instances spanning distinct guarantee types.

Note that **none of these regimes licenses unconditional acceptance of a proposition or deployment of a predictor or strategy beyond the stated selection rule.** Each licenses a recording, derivation, or typed defeasible action. How acceptance is licensed is an open problem (§21.1).

### 18.1 Grounded dialectical warrant

A certificate argument must be grounded-IN.

Only typed defeasible actions are warranted.

Grounded acceptability does not automatically license unconditional acceptance.

### 18.2 Graded support warrant

An independent-Bernoulli support certificate can warrant recording a support grade.

Even a grade such as $0.99$ does not automatically warrant acceptance.

### 18.3 Deductive warrant

A checked strict-Horn certificate can warrant $\operatorname{derive}(h)$ relative to explicit premises.

A valid derivation does not warrant accepting the premises.

### 18.4 Measurement warrant

A measurement certificate can warrant recording value, unit, standard uncertainty, and calibration/model provenance.

It does not directly warrant exact proposition acceptance.

### 18.5 Testimony warrant

A source model specifies $P(R^+\mid H)$ and $P(R^+\mid\neg H)$ for a source/reference class, where $R^+$ is a positive report and $H$ the reported proposition.

A certificate can warrant recording the posterior under that model.

It does not make source reliability context-free.

### 18.6 Statistical warrant

A finite-class uniform-convergence certificate computes

$$
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
$$

It can warrant recording that, for every $h\in\mathcal H$,

$$
L_D(h)
\le
L_S(h)+\epsilon
$$

with confidence $1-\delta$.

Applicability assumptions $\Phi$ for this regime:

- the sample $S$ of size $m$ is i.i.d. from distribution $D$;
- the loss is bounded in $[0,1]$;
- $\mathcal H$ is finite and fixed before seeing $S$.

The bound is Hoeffding plus a union bound, holds uniformly over $\mathcal H$, and is two-sided.

It does not warrant predictor deployment.

### 18.7 Strategy-performance warrant

For paired normalized utilities

$$
\Delta_i
=
u_i(\pi)-u_i(\pi_0)
\in[-1,1],
$$

a strategy $\pi$ may be selected over baseline $\pi_0$ only when the lower confidence bound

$$
\bar\Delta
-
\sqrt{
\frac{
2\log(1/\delta)
}{
n
}
}
$$

is strictly positive.

Applicability assumptions $\Phi$ for this regime:

- the $n$ task instances are i.i.d. draws from the target task distribution;
- utilities are normalized so that $\Delta_i\in[-1,1]$;
- the comparison is a single, pre-specified test with fixed $n$.

If several candidate strategies are compared, $\delta$ must be corrected (for example, $\delta/k$ for $k$ candidates by a union bound). If results are inspected repeatedly with the option to stop early, a fixed-$n$ Hoeffding bound is invalid and an anytime-valid bound is required. The implementation should be checked against these conditions.

## 19. Current verification status

The integrated current repository has been executed successfully on native Windows.

Current full result:

- **138 tests passed**;
- seed fixture rebuilt successfully;
- **8 generated artifacts** matched;
- graph validation: **0 errors / 0 warnings**;
- dependency check: no broken requirements.

The verification run includes support algebra, defeat, ABA, preference filtering, warrant/license, graded support, strict-Horn deduction, measurement/testimony, statistical/PAC, and strategy-performance.

These tests verify that the reference implementations behave as specified. They do not test the central hypothesis (§28) that the factorization improves reasoning or inquiry; that is an empirical question (§21.9).

Hosted GitHub Actions remains a separate infrastructure problem: runs have repeatedly failed or cancelled before runner steps/logs.

Do not treat hosted pre-run failure as an application-level failure.

## 20. Comparison to existing work

The current meta-model is best understood as a synthesis/interface, not as a replacement for the mature frameworks it uses.

### Context of discovery vs. context of justification

Reichenbach's distinction (*Experience and Prediction*, 1938) between how hypotheses are arrived at and how they are justified is the direct philosophical ancestor of this project's separation of candidate generation from warrant.

The project does not adopt the stronger positivist conclusion that discovery is outside epistemology. The generation–evaluation feedback loop (§21.7) treats generation as an object of formal study. This aligns with the "friends of discovery" literature (Hanson, Nickles) and with Simon and colleagues' treatment of discovery as heuristic search (Langley, Simon, Bradshaw & Zytkow, *Scientific Discovery*, 1987), which directly supports the constrained-search framing in §21.2.

### Formal epistemology

Formal epistemology uses probability, logic, ranking theory, belief revision, decision theory, and related mathematical tools to analyze epistemic states and norms.

The present project differs mainly in **architectural scope**: instead of choosing one formalism as the core epistemology, it tries to factor the interfaces among heterogeneous epistemic regimes.

### AGM / belief revision

AGM provides postulates and representation theorems for belief-state change.

This project reuses the idea that change operations deserve formal semantics, but does not make belief revision the universal form of reasoning.

The present action model $a:\mathcal S\rightharpoonup\mathcal S\times O_a$ is broader.

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

The current positive-support antichain algebra is essentially a minimal-witness/PosBool instance of this family.

### Structured argumentation

ABA, ABA+, ASPIC+, Pollock, and Dung provide mature machinery for defeasible conflict.

The project uses an ABA-first executable substrate with explicit typed metadata and Dung acceptability.

It does not claim a novel replacement argumentation theory.

### Toulmin's argument model

Toulmin (*The Uses of Argument*, 1958) analyzes arguments into data, claim, **warrant**, **backing**, qualifier, and rebuttal. This project's use of "warrant" and its question "what warrants the warrant?" correspond closely to Toulmin's warrant and backing. The typed guarantee $G$ plays a role related to Toulmin's qualifier, and defeat corresponds loosely to rebuttal.

Differences: Toulmin's warrant licenses an inference from data to claim, and is informal and field-dependent. Here a warrant targets a typed epistemic *action*, carries an explicit applicability set $\Phi$, and in the reference regimes is mechanically checkable. Warrant-of-warrant (§21.4) is Toulmin's backing made into a recursive, representable target.

### Argumentation schemes and critical questions

Walton-style argumentation schemes (Walton, Reed & Macagno, *Argumentation Schemes*, 2008) pair stereotyped patterns (expert opinion, witness testimony, cause to effect, etc.) with critical questions that probe their applicability.

Each executable warrant regime in §18 can be read as a typed, checkable scheme, with its applicability assumptions $\Phi$ playing the role of critical questions promoted to explicit conditions. The testimony regime (§18.5) is close to the scheme for witness testimony, with source reliability made quantitative.

Differences: schemes are usually informal and conclude propositions. This project types the guarantee and targets actions.

### Carneades

Carneades (Gordon, Prakken & Walton, 2007) models argument evaluation with **proof standards** (e.g., preponderance of evidence, clear and convincing evidence, beyond reasonable doubt) assigned per issue, and distinguishes premises, assumptions, and exceptions in how critical questions allocate burden of proof.

This is the closest existing precedent for *action-relative adequacy*: what counts as enough depends on what is being decided. It is directly relevant to the acceptance-licensing problem (§21.1), where proof standards are one candidate mechanism. Carneades' assumption/exception distinction is also a candidate refinement of $\Phi$ (§21.5).

### Justification Logic

Justification Logic supplies a strong precedent for treating reasons/certificates as explicit objects.

The present warrant interface extends the target from "reason for proposition" to "certificate adequate for a typed epistemic action with a typed guarantee."

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

### 21.1 Acceptance licensing

Every implemented warrant regime (§18) licenses a recording, derivation, or typed defeasible action. None licenses $\operatorname{accept}(h)$, deployment of a predictor, or action in the world beyond the strategy-selection rule. The caution is principled, but it means the pipeline currently stops short of the action that most use cases need.

Until this is resolved, the framework functions as an **audit and recording system**, not a decision system.

Acceptance is where heterogeneous guarantees must meet a decision, so this problem is tightly coupled to warrant composition (§21.3). Candidate approaches:

- **Proof standards.** Attach an action-relative adequacy threshold to each acceptance action, as in Carneades (§20).
- **Decision-theoretic acceptance.** License acceptance when expected utility of acting on $h$ exceeds alternatives given stakes, making acceptance stakes-sensitive.
- **Dialectical acceptance.** Add an explicit rule mapping a declared acceptability status (e.g., grounded-IN under stated preferences) to acceptance, with the rule itself as a warranted object.
- **Acceptance as commitment.** Treat acceptance as a policy-level commitment distinct from belief or credence (cf. L. J. Cohen, *An Essay on Belief and Acceptance*, 1992).

Questions include:

- Is acceptance one action type, or a stakes-relative family?
- Can a single regime license acceptance, or does acceptance always require composition?
- What guarantee type does an acceptance carry?
- How are threshold-based acceptance paradoxes handled (lottery and preface: high-probability acceptance is not closed under conjunction)?
- When should acceptance be revocable, and what licenses retraction?

### 21.2 Candidate generation

Candidate generation is no longer the largest broad foundational gap.

A dedicated landscape survey, five-framework mapping, cross-framework orchestration survey, and guarantee-transport survey now show that most of the relevant machinery already exists across program synthesis/CEGIS, ILP/MIL, anti-unification, automated theory formation, conceptual blending, Bayesian program learning, blackboard systems, multistrategy learning, algorithm selection, hyper-heuristics, reflection, Hets/DOL/institutions, MMT and refinement/abstract-interpretation machinery.

The current generative-regime interface is:

$$
\mathcal G_R=
(\mathcal A_R,\mathcal L_R,\mathcal D_R,B_R,\mathcal O_R,\to_R,V_R)
$$

with generation episode:

$$
E_G=(R,\mathcal G_R,d_0)
$$

and regime transformation:

$$
\mu:\mathcal G_R\rightharpoonup\mathcal G'_R.
$$

Remaining questions are narrower and should be pursued only when needed:

- generative-regime equivalence/composition;
- operator or bias invention when existing meta-learning/hyper-heuristic machinery is inadequate;
- semantics of substantive concept invention;
- typed adapter metadata and preservation certificates;
- generator-level warrant.

See the candidate-generation landscape/mapping/glue documents, warrant-guarantee transport document, and ADRs 015–018.

### 21.3 Warrant composition

Multiple warrant regimes may support related actions.

There is currently no universal rule combining $\mathfrak W_1$ and $\mathfrak W_2$ into a joint regime $\mathfrak W_*$.

Questions include:

- when do independent warrants strengthen one another?
- when are guarantees incomparable?
- when should one regime dominate?
- how should conflicts between deductive, statistical, testimonial, and defeasible warrants be represented?
- can a meta-warrant justify an aggregation policy?

Current stance: do not introduce scalar aggregation by default.

### 21.4 Warrant of warrant

The regress remains explicit.

If $\mathfrak W;\Phi\vdash_\kappa a:G$, the assumptions $\Phi$, the certificate checker, the reliability model, or the warrant regime $\mathfrak W$ may themselves become targets of warrant. This is Toulmin's backing (§20) made recursive.

The framework supports axiomatic stopping points, empirical reliability chains, proof chains, defeasible/coherence-based stopping, and unresolved assumptions.

No fake universal closure is assumed.

### 21.5 Context entailment

The foundational license condition is $C\models\Phi$.

Executable benchmark regimes currently use explicit set inclusion.

Open problem: connect the warrant layer to richer theory/context semantics so context satisfaction can use actual logical entailment, morphism-aware entailment, graded assumptions, or defeasible context. Carneades' distinction between assumptions (presumed unless challenged) and exceptions (must be raised to count) is one candidate refinement of $\Phi$.

### 21.6 Epistemic action algebra

We have a generic action type $a:\mathcal S\rightharpoonup\mathcal S\times O_a$.

But we do not have a representation theorem showing a unique/minimal primitive basis $\mathsf B$.

Likely result: primitive action bases are representation-relative.

Open questions include useful normal forms, action equivalence, and compositional generation of revision/update/accept/retract.

### 21.7 Candidate-generation/warrant interaction

Generation and evaluation are separated, but the feedback loop deserves deeper study:

$$
s_t
\xrightarrow[\pi]{\mathcal G}
d_t
\xrightarrow{\operatorname{Elab}}
c_t
\xrightarrow{\operatorname{Ev}}
f_t
\xrightarrow{\operatorname{control/update}}
s_{t+1}.
$$

Open question: what general properties make such a loop effective?

Possible dimensions include completeness, convergence, search bias, cost, information gain, repairability, and representation change.

### 21.8 Reflection and self-application

Strategies, warrants, and the meta-model itself are representable targets, so the framework can **represent** reflection: it can hold objects that are about its own components.

This should not be read as a claim that reflective reasoning within the framework is sound or complete. Self-referential trust has known limits. For example, by Löb's theorem a consistent theory extending arithmetic cannot prove its own reflection principle ("if provable then true") for every sentence. Any regime that warrants trust in its own warrant regimes will need explicit stopping points (§21.4) rather than self-certification.

Open questions include fixed points, self-modifying warrant policies, trust bootstrapping, meta-regress control, and reflective consistency.

### 21.9 Empirical adequacy of the factorization

The architecture is conceptually coherent and executable in reference cases.

It is not yet empirically established that the factorization improves annotation reliability, reasoning quality, auditability, inquiry navigation, or strategy selection.

This is now primarily an empirical question, and it is the test of the central hypothesis (§28).

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
- relational reflection (as representation, not as a soundness claim);
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

- acceptance licensing;
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

(The related-work additions in §20 are comparisons for positioning, not new machinery.)

## 25. Recommended next foundational discussion

The next foundational discussion should be:

**Acceptance licensing and warrant composition** — tracked in GitHub issue #34.

The framework already separates:

$$
\text{support}
\neq
\text{warrant}
\neq
\text{license}
\neq
\text{execution}.
$$

What remains unresolved is when heterogeneous typed warrants are sufficient for stronger epistemic actions such as:

- accept;
- commit;
- use-for-action;
- revise;
- retract.

Questions include:

1. Is acceptance one action type or a stakes/task-relative family?
2. Can a single warrant regime license acceptance, or is composition generally required?
3. How should deductive, defeasible, probabilistic, testimonial, measurement and statistical guarantees combine without being forced into one scalar?
4. What guarantee does an acceptance action carry?
5. How should lottery/preface-style closure failures be handled?
6. What licenses retraction/revision?
7. Can acceptance/composition policies themselves be warranted meta-level objects?

Before inventing machinery, compare Carneades proof standards, belief-versus-acceptance literature, decision-theoretic acceptance, structured argumentation, formal belief revision, and explicit policy/contract formalisms.

Candidate-generation research is now secondary and should resume only if concrete integration/benchmark cases expose a missing distinction.

## 26. Relation to the accompanying paper

The accompanying paper draft:

- states the architecture as a research contribution;
- compares it to adjacent formal traditions;
- frames the main contribution as **factorization and interface synthesis**, not invention of each component;
- identifies candidate generation and warrant composition as the major next research problems.

The paper should be updated to match this document: add acceptance licensing as a major open problem, present the central claim as a hypothesis, and add the related work below.

Future literature review should explicitly compare against Reichenbach's discovery/justification distinction and the discovery-as-search tradition, Toulmin's argument model, argumentation schemes and critical questions, Carneades and proof standards, formal epistemology, AGM and belief-base change, dynamic epistemic logic, ATMS and truth-maintenance, provenance semirings, Justification Logic, Dung/ABA/ASPIC+, probabilistic argumentation, formal learning theory, metareasoning, logical frameworks/theory graphs, the belief/acceptance literature, and cognitive architectures if relevant.

## 27. Repository handoff map

Canonical high-level documents:

- `docs/formal-epistemic-reasoning-metamodel.md` — this document;
- `docs/paper-formal-epistemic-reasoning-metamodel.md` — paper draft;
- `docs/project-status.md` — current project-management status;
- `docs/architecture-reassessment.md` — stop-rule/reassessment;
- `docs/research-log-post-v1.md` — chronological research development;
- `docs/warrant-license-interface.md` — warrant formalism;
- `docs/candidate-generation-interface.md` — candidate-generation work;
- `docs/end-to-end-warrant-benchmark.md` — executable warrant benchmark;
- `docs/epistemic-actions-support-algebra.md` — actions/support;
- `docs/support-antichain-probability.md` — positive support;
- `docs/defeat-argumentation-integration.md` — defeat;
- `docs/preference-regimes.md` — preference boundary;
- `docs/metareasoning-strategy-reflection.md` — strategy/reflection;
- `docs/assumption-context-meta-model.md` — ATMS-style contexts;
- `docs/epistemic-transition-calculus.md` — earlier transition calculus;
- `docs/decisions/` — ADRs.

Other documents may use pre-§5.1 notation (e.g., $A$ for applicability assumptions, $\pi$ for certificates). §5.1 is canonical where they differ.

Open architectural issues:

- issue #17 — derivation/subargument structure;
- issue #18 — full ABA+ / hyperargumentation.

## 28. Final closeout assessment

The meta-model is not "finished" in the sense of a complete philosophy of epistemology.

It is, however, **architecturally mature enough to freeze as a versioned research object**.

Its central **hypothesis** is:

> Epistemic reasoning is better modeled as a composition of distinct generative, support, warrant, action, and control structures than as a flat taxonomy of inference types.

This hypothesis is conceptually motivated and implemented in reference cases. It has not yet been empirically tested (§21.9), and the passing test suite (§19) verifies implementations, not the hypothesis.

The candidate-generation problem is now substantially narrowed: mature frameworks cover fixed-space generation, vocabulary extension, concept formation, generator selection, heuristic generation, orchestration, parameter tuning and reflection. Formal warrant/guarantee transport is also substantially covered by institution theory, DOL/Hets, MMT theory morphisms, abstract interpretation and contract/refinement theory. The remaining work is mainly integration: record typed preservation certificates, preserve residual assumptions/provenance, and re-warrant outputs when no certified transport exists.

The most important unresolved integrative problems are acceptance licensing and warrant composition, which are closely linked.

The most important empirical question is whether the factorization improves actual reasoning/inquiry work.

# Closeout checklist

- [x] Canonical name chosen: **Formal Epistemic Reasoning Meta-Model**
- [x] Core factorization recorded
- [x] Main formal objects recorded
- [x] Canonical notation table recorded (§5.1)
- [x] Warrant interface recorded
- [x] Executable benchmark regimes recorded, with applicability assumptions
- [x] Verification status recorded
- [x] Deferred argumentation branches preserved
- [x] Acceptance licensing marked as major open problem
- [x] Candidate generation historically identified as a major gap and subsequently narrowed through landscape/mapping/orchestration/transport surveys
- [x] Warrant composition marked as major open problem
- [x] Context entailment/action algebra/reflection open questions recorded
- [x] Relation to Inquiry Representation Model recorded
- [x] Relation to future Inquiry System recorded
- [x] Paper draft prepared
- [x] Candidate-generation landscape survey resumed and adoption decision recorded
- [x] Candidate-generation framework mappings completed across CEGIS, MIL, anti-unification, HR, and conceptual blending
- [x] Cross-framework candidate-generation glue compared against blackboards, multistrategy learning, algorithm selection, hyper-heuristics, configuration, PRODIGY, Soar and reflection
- [x] Warrant/guarantee transport compared against Hets/DOL/institutions, MMT morphisms, abstract interpretation and contract/refinement theories
- [ ] Full comparison to adjacent existing meta-models/frameworks deepened beyond the current targeted surveys
- [ ] Empirical usefulness study performed
- [x] Paper draft updated to match this revision (acceptance problem, candidate-generation narrowing, canonical warrant notation)
- [ ] Other `docs/` files migrated to §5.1 notation
- [ ] Strategy-performance implementation checked for multiple-comparison and optional-stopping conditions (§18.7; issue #37)
