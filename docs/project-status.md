# Research project status

> **Purpose:** durable "forest" view of the foundational reasoning formalism. This page is the short project-management summary; detailed arguments live in the linked research notes and ADRs.

## Current objective

Build a source-grounded inquiry system whose research layer can represent:

\[
\text{candidate generation}
\to
\text{support/evaluation}
\to
\text{defeasible warrant}
\to
\text{license}
\to
\text{epistemic action/update}
\]

without collapsing unlike notions into one confidence score or one universal inference taxonomy.

## Stable architecture

### Formal representation

Use an MMT-like theory-graph view for theories, declarations, formal objects/proofs and morphisms.

### Persistent support

ATMS-style support keeps multiple assumption environments rather than one globally committed theory.

Positive support is represented as finite antichains of minimal assumption environments:

\[
\mathsf{Supp}(X)
=
\operatorname{Antichain}(\mathcal P_{\mathrm{fin}}(X)).
\]

### Candidate generation

Candidate generation is a constrained-search interface:

\[
\mathcal G_R=
(\mathcal D_R,d_0,\mathcal O_R,\to_R)
\]

controlled by a strategy rather than one universal creativity operator.

### Warrant

The current warrant judgment is:

\[
\mathfrak W;A\vdash_\pi a:G.
\]

Support, warrant, derived license and executed update remain separate.

### Defeasible conflict

Positive support is not numerically negated.

The dialectical pipeline is:

\[
\text{support}
\to
\text{ABA attack}
\to
\text{preference resolution}
\to
\text{binary defeat}
\to
\text{Dung acceptability}.
\]

### Argument identity

For the current ABA/ABA+ style layer, dialectical argument identity is quotiented by:

\[
(\text{conclusion},\text{supporting assumption environment}).
\]

Formal proof/derivation identity remains a richer separate layer.

## Current preference regime

The executable binary layer uses **normal-attack preference filtering**.

A basic ABA attack on assumption \(\beta\) succeeds only when the attacking support contains no \(\alpha\) with:

\[
\alpha<\beta.
\]

Blocked attacks remain auditable.

This is deliberately **not called full ABA+**.

Full ABA+ can reverse set-to-set attacks and does not generally reduce faithfully to the current binary Dung graph.

## Deliberate escalation paths

### Issue #17 — first-class derivation/subargument structure

Escalate if ASPIC+-style subargument attack, last-link/weakest-link preference, proof-sensitive warrant or exact proof explanation becomes necessary.

### Issue #18 — full ABA+ / hyperargumentation

Escalate if reverse attacks, collective set-to-set attacks or faithful ABA+ semantics become necessary.

These are preserved future branches, not forgotten work.

## What is settled enough to stop expanding

The project should not currently add more foundational argumentation formalisms merely because they are adjacent.

The following separations are stable enough for integration testing:

\[
\boxed{
\begin{array}{c}
\text{formal representation}\\
\neq\\
\text{support provenance}\\
\neq\\
\text{candidate generation}\\
\neq\\
\text{argument/defeat}\\
\neq\\
\text{warrant}\\
\neq\\
\text{license}\\
\neq\\
\text{executed update}
\end{array}
}
\]

## Immediate path

The project now has executable warrant regimes for defeasible grounded acceptability, exact graded-support reporting, checked strict-Horn deduction, measurement-result recording with uncertainty/calibration provenance, testimony-posterior recording under an explicit reference-class-relative source model, finite-class statistical generalization bounds under explicit sampling assumptions, and strategy-selection warrants based on positive lower confidence bounds for paired normalized utility.

The integrated verification gate is now cleared. The next milestone is benchmark-driven validation rather than ontology expansion:

1. maintain and expand the benchmark only from concrete failures;
2. run adversarial/failure analysis across the existing warrant regimes;
3. reconcile the full conversation export and test source completeness;
4. evaluate empirical usefulness for inquiry navigation/auditability;
5. add any new formal layer only when a benchmark/use case requires it;
6. candidate-generation framework mapping and cross-framework glue surveys are now complete. Existing blackboard systems, multistrategy learning, algorithm selection, hyper-heuristics, configuration, reflection, PRODIGY and Soar cover most orchestration needs. Further foundational work should focus only on typed adapter semantics and warrant/guarantee transport across generator composition if a concrete case requires it.

## Verification status

The current integrated native-Windows suite is green: **138 tests passed**, the seed fixture rebuilt, all **8 generated artifacts** matched, canonical graph validation returned **0 errors / 0 warnings**, and `pip check` reported no broken requirements. The verification run covers the current defeat, ABA, preference, warrant/license, graded-support, deductive, measurement/testimony, statistical/PAC, and strategy-performance code.

Hosted GitHub Actions remains a separate infrastructure problem: repeated hosted runs fail or cancel before runner steps/logs. Do not treat that hosted pre-run failure as an application-level failure.

## Source-grounding debt

The curated founding-dialogue graph is still a first-pass reconstruction rather than a full export reconciliation.

Eventually import the full conversation export and reconcile curated excerpts to actual message IDs/branches before treating the inquiry history as source-complete.

## Canonical entry points

- [Formal Epistemic Reasoning Meta-Model closeout](formal-epistemic-reasoning-metamodel.md)
- [ArXiv-style paper draft](paper-formal-epistemic-reasoning-metamodel.md)
- [Formalism](formalism.md)
- [Warrant/license](warrant-license-interface.md)
- [End-to-end warrant benchmark](end-to-end-warrant-benchmark.md)
- [Candidate-generation cross-framework glue](candidate-generation-cross-framework-glue.md)
- [Candidate generation framework mappings](candidate-generation-framework-mappings.md)
- [Candidate generation landscape](candidate-generation-landscape.md)
- [Candidate generation interface](candidate-generation-interface.md)
- [Positive support](support-antichain-probability.md)
- [Defeat integration](defeat-argumentation-integration.md)
- [ABA vs ASPIC+ benchmark](aba-aspic-benchmark.md)
- [Argument identity boundary](argument-identity-boundary.md)
- [Preference regimes](preference-regimes.md)
- [Architectural decisions](decisions/index.md)
- [Architecture reassessment](architecture-reassessment.md)
- [Research log](research-log-post-v1.md)
