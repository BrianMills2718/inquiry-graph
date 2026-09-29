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
E_G=(R,\mathcal G_R,d_0),\;\Pi
\\[4pt]
\downarrow
\\[4pt]
\textbf{argument / attack / defeat}\\
\text{ABA-like construction + typed attacks + preferences}
\\[4pt]
\downarrow
\\[4pt]
\textbf{regime-specific warrant}\\
\mathfrak W;\Phi\vdash_\kappa a:G
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

### Formal-layer semantic audit — immediate correctness priority

Issue #46 has exposed three reproduced defects in the executable reference layer: preference attack-removal can violate consistency, flat ABA is not enforced, and grounded-dialectical warrant can ignore its action target. These defects do not overturn the high-level factorization, but they do invalidate the assumption that all current reference regimes are semantically safe merely because the integration suite is green.

Resolve issue #46 before extending stronger acceptance semantics. In particular, the preference counterexample supplies a concrete trigger for revisiting issue #18's ABA+/attack-reversal boundary.

### Acceptance licensing and warrant composition — next foundational priority

The main unresolved foundational/integrative problem is no longer candidate generation. It is the transition from typed warrants to stronger epistemic actions such as:

- accept;
- commit;
- use-for-action;
- revise;
- retract.

The current executable regimes mostly license recording, derivation, defeasible use, or strategy selection. There is no general rule for composing heterogeneous guarantees or deciding when they are sufficient for stronger actions.

This is tracked in GitHub issue #34.

Current stance:

\[
\boxed{
\text{do not collapse heterogeneous guarantees into one scalar threshold by default.}
}
\]

Acceptance/composition policies should be explicit, typed, action-relative, and themselves warrantable.

### Candidate generation — substantially mapped

Candidate generation is no longer a broad foundational gap.

The current typed interface is:

\[
\mathcal G_R=
(\mathcal A_R,\mathcal L_R,\mathcal D_R,B_R,\mathcal O_R,\to_R,V_R)
\]

with generation episode:

\[
E_G=(R,\mathcal G_R,d_0)
\]

and regime transformation:

\[
\mu:\mathcal G_R\rightharpoonup\mathcal G'_R.
\]

This has been mapped against CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR theory formation, and conceptual blending. Cross-framework orchestration and guarantee transport have also been mapped to mature work in blackboard systems, multistrategy learning, algorithm selection, hyper-heuristics, reflection, Hets/DOL/institutions, MMT, abstract interpretation, and contract/refinement theory.

Further candidate-generation theory should be pursued only if a concrete integration case exposes a failure.

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

Issue #46 now supplies a concrete preference-semantics failure in the current attack-removal filter. Treat #18 as conditionally activated for design review: either adopt a faithful preference semantics that restores the required rationality properties, or explicitly demote/remove the current filter from warrant-bearing use.

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

### Track A — execution verification — completed

The complete repository suite has now been run in the native Windows environment. Result: **138 tests passed**, seed fixture rebuilding succeeded, **8 artifacts** matched, canonical graph validation returned **0 errors / 0 warnings**, and `pip check` found no broken requirements.

The run exposed and fixed three Windows portability problems: subprocess stdout encoding, locale-default seed-file decoding, and pytest collection of imported `Testimony*` dataclasses. Track A is therefore no longer blocking the research-layer architecture.

### Track B — semantic correctness, then selective foundational research

Begin with issue #46. Only after the reference-layer defects are resolved should foundational research continue with issue #34: acceptance licensing and warrant composition. Compare existing proof-standard, acceptance/commitment, decision-theoretic, structured-argumentation, and belief-revision work before inventing a new policy calculus.

Do not reopen candidate generation, derivation DAGs, or full ABA+ unless a concrete case triggers their documented escalation conditions.

### Track C — benchmark expansion and empirical evaluation — issue #38

Turn the current examples into a maintained benchmark corpus and test:

- annotation discrimination;
- end-to-end warrant behavior;
- failure cases;
- strategy episodes;
- robustness to changed assumptions/defeaters/preferences.

### Track D — source reconciliation/product usefulness — issue #3

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
