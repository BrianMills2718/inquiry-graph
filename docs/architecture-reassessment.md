# Architecture reassessment after warrant benchmark coverage

> **Status:** current project-management checkpoint.

## 1. Question

After adding executable warrant regimes for defeasible argumentation, graded support, deduction, measurement, testimony, statistical generalization, and strategy performance, should the project keep expanding the foundational ontology?

Current answer:

\[
\boxed{
\textbf{no, not by default.}
}
\]

The architecture is now broad enough to test composition across genuinely different guarantee types.

Further formal expansion should be driven by benchmark failure, not adjacency to another literature.

## 2. Stable research spine

The current research architecture is:

\[
\boxed{
\begin{array}{c}
\textbf{formal representation}\\
\mathcal F
\\[4pt]
\downarrow
\\[4pt]
\textbf{persistent support/provenance}\\
J,\lambda,\rho_\eta
\\[4pt]
\downarrow
\\[4pt]
\textbf{candidate generation}\\
\mathcal G_R,\pi_s
\\[4pt]
\downarrow
\\[4pt]
\textbf{argument / attack / defeat}\\
\text{ABA-like construction + typed attacks + preferences}
\\[4pt]
\downarrow
\\[4pt]
\textbf{regime-specific warrant}\\
\mathfrak W;A\vdash_\pi a:G
\\[4pt]
\downarrow
\\[4pt]
\textbf{current license}\\
\operatorname{Licensed}_{\mathfrak W,C}(a:G)
\\[4pt]
\downarrow
\\[4pt]
\textbf{optional epistemic action/update}
\end{array}
}
\]

Reflection/metareasoning can target any of these objects rather than requiring a separate permanent meta-level ontology.

## 3. Benchmark coverage now spans distinct guarantee families

Executable benchmark regimes now cover:

- **defeasible argumentation:** grounded acceptability under attack/defeat;
- **preference-sensitive conflict:** binary preference-filtered defeat;
- **graded support:** exact support-event probability under an explicit model;
- **deduction:** checked strict-Horn derivability relative to premises;
- **measurement:** result + uncertainty + calibration provenance;
- **testimony:** Bayesian posterior under a reference-class-relative source model;
- **statistical learning:** finite-class uniform-convergence bound;
- **strategy selection:** positive lower confidence bound on paired benchmark utility advantage.

These are intentionally heterogeneous.

The fact that they all fit the same action-targeted warrant interface is evidence that the interface is carrying useful structure rather than merely renaming one specific formalism.

## 4. What remains genuinely open

The following are still research questions, but they do not currently justify another top-level layer.

### Acceptance licensing and warrant composition

This is now the main foundational/integrative frontier.

The executable regimes deliberately distinguish support, warrant, current license and execution, but they mostly license recording, deriving or typed defeasible-use actions rather than unconditional proposition acceptance.

Open questions include:

- what acceptance/commitment/use-for-action means;
- whether acceptance is task/stakes-relative;
- how heterogeneous typed guarantees compose;
- how closure problems such as lottery/preface cases are handled;
- what licenses retraction/revision;
- whether acceptance policies are themselves warrantable meta-policies.

This is tracked in issue #34.

### Candidate generation

Candidate generation is no longer the deepest general unknown.

The project has mapped CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR theory formation and conceptual blending into a typed generative-system interface, and has mapped cross-framework orchestration to blackboards, multistrategy learning, algorithm selection, hyper-heuristics, configuration, PRODIGY, Soar and reflection.

Formal guarantee transport is likewise mapped to institutions/DOL/Hets, MMT theory morphisms, abstract interpretation and contract/refinement theory.

Reopen candidate-generation foundations only if a concrete case breaks those mappings.

### Context entailment

Executable license currently approximates:

\[
C\models A
\]

with explicit set inclusion in the benchmark implementations.

A richer logical/context checker can be added when a concrete case requires it.

### Action algebra

Epistemic actions are modeled as typed partial state transducers, but a minimal composition basis has not been proven.

This remains a representation-theorem question, not a blocker for benchmark use.

### Full transcript/source reconciliation

The research history still needs reconciliation against the full conversation export if the inquiry graph is to become source-complete.

### Empirical usefulness

The largest empirical question remains:

> does using this representation actually improve inquiry navigation, reasoning quality, auditability, or strategy selection?

That requires experiments, not more ontology.

## 5. Explicitly deferred richer branches

These are intentionally preserved rather than forgotten.

### Issue #17

First-class derivation/subargument structure.

Trigger only if proof-sensitive or ASPIC+-level semantics distinguish arguments currently quotiented together.

### Issue #18

Full ABA+ / set-to-set hyperargumentation.

Trigger only if reverse or collective attacks matter to benchmark outcomes.

## 6. Project-management stop rule

From this point:

\[
\boxed{
\text{new formal layer}
\Rightarrow
\text{must be motivated by a failing benchmark or concrete use case}.
}
\]

“Relevant literature exists” is no longer sufficient reason to import another framework.

## 7. Next workstreams

The next project work should split into three tracks rather than continue one foundational chain.

### Track A — verification — completed

The complete repository suite has now been run in the native Windows environment. Result: **138 tests passed**, seed fixture rebuilding succeeded, **8 artifacts** matched, canonical graph validation returned **0 errors / 0 warnings**, and `pip check` found no broken requirements.

The run exposed and fixed three Windows portability problems: subprocess stdout encoding, locale-default seed-file decoding, and pytest collection of imported `Testimony*` dataclasses. Track A is therefore no longer blocking the research-layer architecture.

### Track B — targeted benchmark and empirical evaluation

Acceptance/warrant-composition research is tracked in issue #34. Empirical usefulness evaluation is tracked separately in issue #38, and the adaptive-statistics audit for strategy-performance warrant is issue #39.

The first targeted meta-model benchmark should now focus on acceptance/warrant composition rather than adding more warrant-regime examples.

In parallel, turn the current examples into a maintained benchmark corpus and test:

- annotation discrimination;
- end-to-end warrant behavior;
- failure cases;
- strategy episodes;
- robustness to changed assumptions/defeaters/preferences.

### Track C — source reconciliation/product usefulness

Reconcile the full conversation export, then evaluate whether the inquiry graph materially helps users navigate open questions, provenance, revisions, and reasoning strategies.

## 8. Re-entry to foundational research

Return to foundational formalization when one of these happens:

- a benchmark cannot express a case without distortion;
- two existing layers collapse distinctions that affect observable outcomes;
- the executable system requires an unsupported semantic operation;
- empirical evaluation exposes systematic ambiguity or annotation failure.

Otherwise, prefer implementation, verification, and evaluation.

## 9. Bottom line

The project has crossed from:

\[
\text{architecture discovery}
\]

into:

\[
\boxed{
\text{architecture testing and empirical validation}.
}
\]

The foundational formalism is not complete in any absolute philosophical sense.

It is now complete enough that further progress is more likely to come from **using it and trying to break it** than from importing additional formal machinery.
