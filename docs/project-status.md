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

The next milestone is composition, not ontology expansion:

1. finish the preference-sensitive binary defeat implementation;
2. connect dialectical acceptability explicitly to warrant/license;
3. define what graded support values license under typed regimes rather than global thresholds;
4. build a small end-to-end benchmark across deductive, defeasible, statistical, testimonial/measurement and conflicting-evidence cases;
5. reassess the architecture from benchmark failures;
6. only then return to deeper candidate-generation theory.

## Verification debt

The last fully executed local repository suite predates some of the newest defeat/ABA/preference code.

Hosted GitHub Actions repeatedly fails before runner steps and has not supplied application-level verification.

Therefore code merged after the last local run should be treated as **implementation present, full-suite execution pending** until an executable environment is available.

This verification debt is operational, not a reason to stop preserving research and code in GitHub.

## Source-grounding debt

The curated founding-dialogue graph is still a first-pass reconstruction rather than a full export reconciliation.

Eventually import the full conversation export and reconcile curated excerpts to actual message IDs/branches before treating the inquiry history as source-complete.

## Canonical entry points

- [Formalism](formalism.md)
- [Warrant/license](warrant-license-interface.md)
- [Candidate generation](candidate-generation-interface.md)
- [Positive support](support-antichain-probability.md)
- [Defeat integration](defeat-argumentation-integration.md)
- [ABA vs ASPIC+ benchmark](aba-aspic-benchmark.md)
- [Argument identity boundary](argument-identity-boundary.md)
- [Preference regimes](preference-regimes.md)
- [Architectural decisions](decisions/index.md)
- [Research log](research-log-post-v1.md)
