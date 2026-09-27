# Warrant, support, license, and epistemic action

> **Status:** current research draft. This document revisits the earlier warrant certificate after the representation, candidate-generation, strategy, and reflection layers were made more precise. It does not claim a universal philosophical analysis of warrant. It defines the project's operational use of the term.

## 1. Why revisit warrant

The earlier dialogue proposed:

\[
\operatorname{Cert}(\tau)=(A_W,G_W,\pi)
\]

where \(A_W\) are assumptions, \(G_W\) is a claimed guarantee, and \(\pi\) is support for that conditional guarantee.

That core idea survives.

What changed is that the target \(\tau\) is now much better factored. The system distinguishes:

- draft generation;
- formal elaboration;
- evaluator feedback;
- support state;
- epistemic updates;
- operator/strategy selection.

The warrant layer should therefore be refactored against those explicit targets rather than replaced.

## 2. Literature alignment

Several mature formalisms illuminate different parts of the problem.

### 2.1 Justification Logic: explicit reasons

Justification Logic introduces formulas of the form

\[
t:F
\]

read as “\(t\) is a justification for \(F\).”

This is important because it makes reasons/evidence explicit objects rather than hiding them inside a modal “known/believed” operator. Justification terms can also have composition operations.

For this project, Justification Logic is closest to the **support/certificate** side of warrant.

It does not by itself determine every epistemic action that should follow from a justification assertion.

### 2.2 Structured argumentation: defeasible support and defeat

Dung-style argumentation and structured frameworks such as ASPIC+ distinguish the construction of arguments from their dialectical acceptability. ASPIC+ distinguishes strict rules from defeasible rules and permits attacks on premises, defeasible inferences, and conclusions.

This matters because epistemic support can be **defeasible**:

\[
\text{support present}
\not\Rightarrow
\text{unconditionally licensed}.
\]

A warrant system therefore cannot assume that every certificate is monotonic or proof-like.

### 2.3 Hoare logic and assume-guarantee contracts: conditional transition guarantees

A Hoare triple has the form

\[
\{P\}\;a\;\{Q\}
\]

and states a conditional correctness claim about an action/program: if the precondition holds and execution terminates under the relevant semantics, the postcondition holds.

Assume-guarantee contracts similarly separate:

\[
(A,G)
\]

where assumptions constrain the environment and guarantees specify what the component promises under those assumptions.

This is a strong formal analogue of the earlier warrant shape

\[
(A_W,G_W,\pi).
\]

It also suggests that **scope is usually encoded by the assumptions and quantified guarantee**, rather than requiring an independent primitive coordinate.

### 2.4 Formal learning theory: method-level performance guarantees

PAC and identification-in-the-limit results show how an inductive method can receive a precise conditional guarantee once the problem class, sampling conditions, hypothesis class, error tolerance, confidence, or convergence criterion are stated.

This is the right precedent for warranting a **method or strategy**, rather than only a proposition.

### 2.5 Rational metareasoning: strategy selection is itself evaluable

Rational-metareasoning work evaluates strategy choice relative to expected benefits, computational costs, task conditions, and learned performance.

That does not force the base model to be expected-utility based. It does show that the choice of a reasoning strategy can itself be the target of a higher-order warrant.

## 3. Support, warrant, license, and update are different

The main factorization is:

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

### Support

A reason, evidence item, proof object, argument, report, or dependency supports some represented content.

Schematic forms include:

\[
t:F
\]

or an ATMS-style dependency environment supporting node \(F\).

Support records **why a claim is connected to reasons**.

### Warrant

A warrant is a conditional adequacy judgment saying that specified support is sufficient, under specified assumptions and a warrant regime, for a specified epistemic action with a specified guarantee/entitlement.

### License

A license is the derived normative/operational status:

> this epistemic action is permitted by this warrant regime under the current conditions.

“License” is therefore not used as a synonym for “warrant.”

### Update

An update is what the agent actually does to its persistent state.

A licensed action may not be executed, and an executed action may later turn out to have lacked an adequate warrant.

## 4. Normalize the warrant target to an epistemic action

Earlier discussion distinguished candidate warrant, transition warrant, and strategy warrant.

That distinction is useful descriptively but need not create three primitive warrant types.

Normalize the target to a typed **epistemic action**:

\[
a\in\mathcal A_E.
\]

Examples include:

\[
\operatorname{derive}(h),
\]

\[
\operatorname{retainCandidate}(h),
\]

\[
\operatorname{raiseSupport}(h,\delta),
\]

\[
\operatorname{accept}(h),
\]

\[
\operatorname{retract}(h),
\]

\[
\operatorname{useReport}(e),
\]

\[
\operatorname{selectOperator}(o),
\]

\[
\operatorname{selectStrategy}(\pi_s).
\]

Then “candidate warrant,” “transition warrant,” and “strategy warrant” become instances of one polymorphic action-targeted schema.

## 5. Warrant regime

Different standards of adequacy should not be silently collapsed.

Let

\[
\mathfrak W
\]

denote a **warrant regime**: the formal rules, semantics, acceptance standard, and checking procedure relevant to a class of warrant judgments.

Examples:

- deductive proof regime;
- defeasible argumentation regime;
- statistical/PAC regime;
- causal-identification regime;
- measurement/reliability regime;
- strategy-performance regime.

The same support object may license different actions under different regimes.

## 6. Core warrant judgment

The current proposed judgment is:

\[
\boxed{
\mathfrak W\,;\,A
\;\vdash_{\pi}\;
a:G
}
\]

read:

> under warrant regime \(\mathfrak W\) and assumptions \(A\), certificate/support object \(\pi\) warrants epistemic action \(a\) with guarantee or entitlement \(G\).

Components:

- \(\mathfrak W\): warrant regime/standard;
- \(A\): explicit applicability assumptions;
- \(\pi\): proof, evidence object, argument, theorem, calibration certificate, performance result, etc.;
- \(a\): epistemic action being licensed;
- \(G\): typed guarantee/entitlement claimed for that action.

This replaces the earlier tuple

\[
(\text{target},A,G,\pi,\text{scope})
\]

with a cleaner judgment.

Two corrections are important:

1. **target** is normalized to action \(a\);
2. **scope** is normally represented inside \(A\) and the quantification/type of \(G\), rather than as a separate primitive.

## 7. License as derived status

Given current context \(C\), define schematically:

\[
C\models A
\]

and

\[
\mathfrak W\,;\,A\vdash_{\pi}a:G.
\]

Then:

\[
\boxed{
\operatorname{Licensed}_{\mathfrak W,C}(a:G).
}
\]

The license is relative to:

- a warrant regime;
- current conditions;
- a particular guarantee/entitlement.

There is no context-free predicate saying an epistemic action is simply “licensed.”

## 8. Guarantee is typed, not scalar

The guarantee \(G\) is not one universal number.

Examples include:

### Deductive

\[
G=\text{truth preservation relative to premises}.
\]

### Hoare/transition style

\[
G=\text{postcondition }Q\text{ after action }a\text{ when }P\text{ holds}.
\]

### Defeasible

\[
G=\text{argument/conclusion acceptable under semantics }S
\]

until defeated by specified attack/preference structure.

### Statistical

\[
G=
\Pr(L(h)\le\epsilon)\ge 1-\delta
\]

under stated sampling/hypothesis assumptions.

### Formal learning

\[
G=\text{identification/convergence over problem class }\mathcal C.
\]

### Strategy

\[
G=\text{performance/cost/regret bound over task/resource class }\mathcal T.
\]

### Measurement/report

\[
G=\text{reliability, calibration, error, or likelihood condition}.
\]

The project should not force these into one confidence scalar unless an explicit aggregation semantics is later supplied.

## 9. Defeaters and nonmonotonic warrant

A warrant may be defeasible.

The core judgment should therefore coexist with explicit challenge/defeat relations.

Rather than put a fixed “defeater set” inside every warrant tuple, represent defeaters in the support/argument graph:

\[
d \dashv \pi
\]

or as attacks on:

- a premise;
- an inference;
- a certificate;
- an applicability assumption;
- a guarantee claim.

This is closer to structured argumentation and keeps the base warrant judgment small.

A previously licensed action can become unlicensed when the warrant regime is nonmonotonic and new defeat information arrives.

## 10. Relationship to the ATMS-style support state

Recall:

\[
K_{\mathcal F}=(N,A,J,\lambda,\rho).
\]

The ATMS-style layer records **dependency provenance**:

\[
\lambda(h)=\{\Gamma_1,\ldots,\Gamma_k\}.
\]

That answers:

> under which minimal assumption environments can \(h\) be derived/supported?

It does not by itself answer:

> is that support sufficient to perform this epistemic action?

The warrant layer consumes those support structures.

For example:

\[
\Gamma\in\lambda(h)
\]

may contribute to certificate \(\pi\), while the warrant regime determines whether that certificate licenses:

\[
\operatorname{derive}(h),
\quad
\operatorname{raiseSupport}(h,\delta),
\quad
\text{or }
\operatorname{accept}(h).
\]

Those need not have the same threshold.

## 11. Relationship to the candidate-generation pipeline

The current candidate pipeline is:

\[
R_t
\xrightarrow[\pi_s]{\mathcal G}
d_t
\xrightarrow{\operatorname{Elab}}
c_t
\xrightarrow{V}
f_t.
\]

Add warrant only after keeping the earlier distinctions explicit.

### Draft generation

Generating or entertaining a draft does not itself warrant its content.

There may be a separate **control warrant** for spending resources on a search operator or strategy.

### Formal elaboration

Successful elaboration yields a formal admissibility result:

\[
\operatorname{Elab}(d)=c.
\]

That may warrant an action such as “treat \(c\) as well formed,” but not “believe \(c\).”

### Evaluator feedback

Evaluator outputs become support/certificate ingredients.

Examples:

- counterexample;
- proof;
- data fit;
- calibration result;
- source report;
- violated invariant.

### Warrant judgment

A warrant regime assesses whether the available support is sufficient for a particular epistemic action.

### State update

Only then may the action be executed against:

\[
K_{\mathcal F}.
\]

## 12. Worked cases

### 12.1 Deductive readout

Suppose:

\[
\Gamma\vdash h
\]

with proof \(\pi_d\).

A deductive regime may establish:

\[
\mathfrak W_{\mathrm{ded}};\Gamma
\vdash_{\pi_d}
\operatorname{derive}(h):
\text{truth-preserving-relative-to-}\Gamma.
\]

This licenses explicit derivation under the assumptions.

It does **not** license unconditional acceptance of the assumptions.

### 12.2 Statistical generalization

A learning theorem may establish, under assumptions \(A_{\mathrm{PAC}}\):

\[
\mathfrak W_{\mathrm{PAC}};A_{\mathrm{PAC}}
\vdash_{\pi_{\mathrm{PAC}}}
\operatorname{usePredictor}(h):
\Pr(L(h)\le\epsilon)\ge1-\delta.
\]

The guarantee is statistical and scoped.

It is not deductive truth preservation.

### 12.3 Defeasible explanation

An abductive argument may support explanation \(h\).

A structured-argumentation regime can license tentative support:

\[
\mathfrak W_{\mathrm{def}};A
\vdash_{\pi_a}
\operatorname{raiseSupport}(h,\delta):
\text{acceptable-under-semantics }S.
\]

A later defeater may withdraw the license without implying that the earlier argument never existed.

### 12.4 Epistemic transition

For an update action \(\tau\), a Hoare-like warrant can be written:

\[
\mathfrak W_{\mathrm{upd}};P
\vdash_{\pi}
\tau:Q,
\]

meaning that under precondition \(P\), the update satisfies postcondition/guarantee \(Q\).

### 12.5 Strategy selection

For strategy \(\pi_s\):

\[
\mathfrak W_{\mathrm{strat}};A_{\mathcal T}
\vdash_{\pi_p}
\operatorname{selectStrategy}(\pi_s):
G_{\mathcal T}.
\]

Here the certificate may be a theorem, benchmark, learned performance model, or empirical evaluation, and \(G_{\mathcal T}\) may contain cost/performance conditions.

## 13. Warrant of warrant

The regress remains explicit.

If:

\[
\mathfrak W;A
\vdash_{\pi}
a:G
\]

depends on assumptions \(A=\{a_1,\ldots,a_n\}\), those assumptions are themselves representable nodes and may have support/warrant judgments.

Likewise the reliability of the checker or warrant regime may itself become a target of reflective analysis.

The framework does not force termination.

It permits:

- axiomatic stopping points;
- empirical reliability chains;
- formal proof chains;
- defeasible/coherent support;
- unresolved assumptions.

The engineering objective is inspectability, not a fake foundational closure.

## 14. Where “entitlement” fits

Epistemology uses “entitlement” in several technical ways, including views that distinguish entitlement from justification.

Because that terminology is theory-dependent, this project should **not** make “entitlement” a primitive synonym for warrant.

Instead, \(G\) may state an entitlement if a chosen warrant regime uses that concept.

The project term **license** is intentionally operational:

> the warrant regime says a specified epistemic action is permitted under the stated conditions.

## 15. Current factorization

The current end-to-end flow is:

\[
\boxed{
\begin{array}{c}
\text{draft generation}\\
\mathcal G_R
\\[3pt]
\downarrow\\
\text{formal elaboration}\\
\operatorname{Elab}_{\mathcal F}
\\[3pt]
\downarrow\\
\text{evaluation / support production}\\
V,\;J,\;\lambda
\\[3pt]
\downarrow\\
\text{warrant judgment}\\
\mathfrak W;A\vdash_{\pi}a:G
\\[3pt]
\downarrow\\
\text{license}\\
\operatorname{Licensed}_{\mathfrak W,C}(a:G)
\\[3pt]
\downarrow\\
\text{executed epistemic update}\\
K_{\mathcal F}\to K'_{\mathcal F}
\end{array}
}
\]

This makes the relationship between the old warrant work and the newer meta-model explicit.

## 16. What is now resolved versus still open

### Clarified

- warrant was not discarded by the later meta-model;
- support and warrant are different;
- warrant and license are different;
- license is relative rather than absolute;
- candidate/transition/strategy warrant need not be primitive warrant types;
- epistemic action provides a common target type;
- scope is usually carried by assumptions and guarantee semantics;
- formal validity is one possible warrant ingredient, not generic epistemic warrant;
- defeasible warrant requires attack/defeat structure.

### Still open

1. the exact type system for epistemic actions \(\mathcal A_E\);
2. which warrant regimes should be first-class in an executable implementation;
3. how graded support updates \(\rho\) are licensed and calibrated;
4. how multiple independent warrants combine;
5. how conflicting warrant regimes are compared;
6. how source/reliability warrants compose through testimony and measurement;
7. how strategy-performance warrants transfer across task distributions;
8. which parts of the warrant judgment should be encoded directly in the inquiry graph versus a separate formal layer.
