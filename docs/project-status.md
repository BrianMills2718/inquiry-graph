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

Candidate generation is now treated as a typed generative regime rather than a universal creativity operator:

\[
\mathcal G_R=
(\mathcal A_R,\mathcal L_R,\mathcal D_R,B_R,\mathcal O_R,\to_R,V_R)
\]

with a concrete episode:

\[
E_G=(R,\mathcal G_R,d_0)
\]

and representation-level transformations modeled separately as:

\[
\mu:\mathcal G_R\rightharpoonup\mathcal G'_R.
\]

CEGIS, Meta-Interpretive Learning, anti-unification, HR theory formation, and conceptual blending have all been mapped into this interface. Cross-framework orchestration is treated as typed blackboard/portfolio control using mature work in blackboard systems, multistrategy learning, algorithm selection, hyper-heuristics, configuration, reflection, PRODIGY and Soar.

### Warrant

The current warrant judgment is:

\[
\mathfrak W;\Phi\vdash_\kappa a:G.
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

The foundational architecture is now in **handoff / selective-research mode**, not expansion mode.

Priority order:

1. **Acceptance licensing + warrant composition** — issue #34. This is the main remaining foundational/integrative problem: when heterogeneous typed warrants are sufficient for stronger actions such as acceptance, commitment, use-for-action, retraction or revision.
2. **Source reconciliation** — issue #3. Reconcile the 219 curated excerpts / 798 proposed annotations against a full export when available.
3. **Empirical usefulness** — test whether the factorization and inquiry representation actually improve auditability, navigation, reasoning quality or strategy selection. Treat the useful Inquiry System as a separate product project if desired.
4. **Documentation/paper normalization** — the paper's high-level priorities and canonical warrant notation are now synchronized. Remaining work is systematic related-work/bibliography normalization, optional migration of historical docs to canonical notation, and review of strategy-performance multiple-comparison/optional-stopping conditions.
5. **Hosted CI** — issue #2 is infrastructure debt only; local integrated verification is green.
6. **Escalation-only branches** — issues #17 and #18 remain dormant unless concrete benchmark cases require richer derivation/subargument or full ABA+ set-to-set semantics.

Candidate generation itself is no longer a broad open mystery: mature frameworks cover fixed-space generation, representation/vocabulary extension, orchestration, operator/heuristic generation and guarantee transport. Formal adapter transport should reuse institution/DOL/Hets, MMT morphisms, abstract interpretation and contract/refinement machinery; unverified translations carry artifacts/provenance only and require target-side re-warrant.

## Verification status

The current integrated native-Windows suite is green: **138 tests passed**, the seed fixture rebuilt, all **8 generated artifacts** matched, canonical graph validation returned **0 errors / 0 warnings**, and `pip check` reported no broken requirements. The verification run covers the current defeat, ABA, preference, warrant/license, graded-support, deductive, measurement/testimony, statistical/PAC, and strategy-performance code.

Hosted GitHub Actions remains a separate infrastructure problem: repeated hosted runs fail or cancel before runner steps/logs. Do not treat that hosted pre-run failure as an application-level failure.

## Source-grounding debt

The curated founding-dialogue graph is still a first-pass reconstruction rather than a full export reconciliation.

Eventually import the full conversation export and reconcile curated excerpts to actual message IDs/branches before treating the inquiry history as source-complete.

## Canonical entry points

- [New-agent handoff](new-agent-handoff.md)
- [Formal Epistemic Reasoning Meta-Model closeout](formal-epistemic-reasoning-metamodel.md)
- [ArXiv-style paper draft](paper-formal-epistemic-reasoning-metamodel.md)
- [Formalism](formalism.md)
- [Warrant/license](warrant-license-interface.md)
- [End-to-end warrant benchmark](end-to-end-warrant-benchmark.md)
- [Warrant/guarantee transport](warrant-guarantee-transport.md)
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
