# New-Agent Handoff — Formal Epistemic Reasoning / Inquiry Graph

> **Prepared:** 2026-09-29  
> **Reviewed base:** main at bbe34abfb699d23f9afc15d49cf227c4d5b0342d  
> **Purpose:** compact operational handoff for a new agent. Read this before extending the theory or product.

## 1. Three related projects

### Project 1 — Formal Epistemic Reasoning Meta-Model
Canonical handoff: docs/formal-epistemic-reasoning-metamodel.md

### Project 2 — Inquiry Representation Model
Source-grounded graph for claims, questions, moves, alternatives, objections, revisions, strategies, actor-relative stance, question status, and provenance.

### Project 3 — Inquiry System
Future useful product built on the first two. The user is most interested in this long term, but this session deliberately did not build the full product.

Do not collapse these three projects into one roadmap.

## 2. Stable meta-model

The stable factorization is:

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
\text{strategy/control}
}
\]

The current warrant judgment is:

\[
\boxed{
\mathfrak W;\Phi\vdash_\kappa a:G
}
\]

The crucial distinction is:

\[
\boxed{
\text{support}
\neq
\text{warrant}
\neq
\text{current license}
\neq
\text{execution}
}
\]

Treat the central factorization as a research hypothesis supported by successful reference mappings, not as a proved theorem.

## 3. Implemented and verified reference layers

Executable layers include:

- positive support antichain algebra;
- independent-Bernoulli support interpretation;
- ABA-style assumption/contrary argument construction;
- typed rebut/undercut/undermine origins;
- binary preference filtering;
- Dung grounded semantics;
- grounded dialectical warrant;
- graded-support warrant;
- checked strict-Horn deductive warrant;
- measurement-result warrant;
- testimony-posterior warrant;
- finite-class statistical/PAC warrant;
- strategy-performance warrant.

Latest integrated native-Windows verification:

- **138 tests passed**;
- seed fixture rebuilt;
- **8 generated artifacts** matched;
- graph validation: **0 errors / 0 warnings**;
- dependency check clean.

Hosted GitHub Actions is still an infrastructure-only issue; do not infer application failure from jobs that never reach runner steps.

## 4. Candidate generation is largely mapped

Canonical docs:

- docs/candidate-generation-landscape.md
- docs/candidate-generation-framework-mappings.md
- docs/candidate-generation-cross-framework-glue.md
- ADRs 015–017

Current typed generative regime:

\[
\mathcal G_R=
(
\mathcal A_R,
\mathcal L_R,
\mathcal D_R,
B_R,
\mathcal O_R,
\to_R,
V_R
)
\]

Concrete generation episode:

\[
E_G=(R,\mathcal G_R,d_0)
\]

Generative-system transformation:

\[
\mu:\mathcal G_R\rightharpoonup\mathcal G'_R.
\]

The interface was mapped successfully to CEGIS/program synthesis, Meta-Interpretive Learning, anti-unification, HR automated theory formation, and computational conceptual blending.

Cross-framework orchestration was mapped to blackboard systems, blackboard control, multistrategy learning, algorithm selection/portfolios, hyper-heuristics, algorithm configuration, PRODIGY, Soar, and computational reflection.

Current adoption stance:

\[
\boxed{
\text{typed blackboard}
+
\text{generator portfolio}
+
\text{explicit controller}
+
\text{reflection}
+
\text{warrant}
}
\]

Do not restart a search for universal primitive creativity operators.

## 5. Guarantee transport is largely mapped too

Canonical docs:

- docs/warrant-guarantee-transport.md
- ADR 018

For formal transport, prefer institution theory, DOL/Hets, and MMT/LF theory morphisms.

For sound lossy transport, prefer abstract interpretation, simulation/refinement, and assume-guarantee/contract theory.

Default rule:

\[
\boxed{
\text{artifact translation}
\not\Rightarrow
\text{guarantee transport}
}
\]

If an adapter lacks a typed preservation certificate for the relevant guarantee, translate the artifact/provenance and re-warrant in the target regime.

## 6. Main foundational frontier

The main unresolved theoretical/integrative problem is:

# **Acceptance licensing and warrant composition**

Tracked in GitHub issue #34.

The implemented regimes deliberately avoid silently jumping from evidence/support to unconditional proposition acceptance.

Open questions include:

- what exactly is accept(h)?
- is acceptance task/stakes-relative?
- how should acceptance differ from belief, credence, commitment, and use-for-action?
- how may heterogeneous warrants compose without one universal scalar?
- how should lottery/preface-style closure problems be handled?
- what licenses retraction/revision?
- can an acceptance policy itself be a warranted meta-policy?

Before inventing anything, compare belief-vs-acceptance literature, decision-theoretic acceptance, Carneades/proof standards, structured argumentation acceptance, belief revision/nonmonotonic consequence, and decision-rule/contract formalisms.

Do not add a universal probability threshold.

## 7. Other current open work

### Source completeness / annotation review
Tracked in issue #3.

Current seed:
- 219 curated source excerpts;
- 229 content nodes;
- 250 relations;
- 185 inquiry moves;
- 58 stance events;
- 76 question events;
- 54 distinct questions;
- 798 proposed annotations;
- 0 confirmed / 0 rejected.

### Deferred argumentation escalation paths
- issue #17 — first-class derivation/subargument DAGs;
- issue #18 — full ABA+ / set-to-set hyperargumentation.

Keep these open unless a concrete benchmark triggers them.

### Hosted CI
- issue #2.

Low priority because the integrated local suite is green.

### Empirical usefulness
Tracked in issue #38.

Still untested:
- whether the graph improves navigation;
- whether it improves auditability;
- whether unresolved assumptions/branches are easier to recover;
- whether strategy annotations help;
- whether the meta-model improves reasoning rather than merely describing it.

### Strategy-performance statistical caveat
Tracked in issue #39.

The closeout flags multiple comparisons and optional stopping. Audit this before interpreting the current benchmark as a general adaptive strategy-selection guarantee.

### Documentation consistency
The canonical notation in §5.1 of docs/formal-epistemic-reasoning-metamodel.md is newer than several historical research docs. Do not rewrite historical logs just for notation uniformity. Update only active normative docs when needed.

## 8. Priority order for a new meta-model agent

1. **Acceptance licensing / warrant composition** — issue #34.
2. **Update the paper to match the current closeout** — acceptance, hypothesis framing, current candidate-generation/transport literature.
3. **Audit strategy-performance statistical assumptions** — multiple comparison / optional stopping.
4. Only then consider further foundational theory, and only if a benchmark exposes a real gap.

Do not reopen candidate generation broadly unless a concrete use case breaks ADRs 015–018.

## 9. Priority order for an Inquiry Representation / product agent

1. source reconciliation — issue #3;
2. independent review/adjudication of proposed annotations;
3. define one concrete usefulness test;
4. build the smallest human-readable inquiry view that supports that test;
5. compare that view against reading the transcript directly;
6. only then invest in richer UI/storage/automation.

The useful-system project should be judged by usefulness, not formal elegance.

## 10. Current-state corrections to older plans

Treat these older statements as historical, not current:

- candidate generation is the largest unresolved foundational area;
- next step is integrated verification;
- preference-sensitive defeat is the next step;
- warrant integration is still pending.

Current state:

- integrated verification is complete;
- candidate-generation landscape/mappings/orchestration are complete enough to freeze;
- formal guarantee transport is mapped to prior art;
- acceptance licensing / warrant composition is the main meta-model frontier;
- source reconciliation and empirical usefulness are the main inquiry-system frontiers.

## 11. Canonical documents to read first

Read in this order:

1. docs/new-agent-handoff.md
2. docs/formal-epistemic-reasoning-metamodel.md
3. docs/project-status.md
4. docs/architecture-reassessment.md
5. docs/warrant-license-interface.md
6. docs/warrant-guarantee-transport.md
7. docs/candidate-generation-landscape.md
8. docs/candidate-generation-framework-mappings.md
9. docs/candidate-generation-cross-framework-glue.md
10. docs/end-to-end-warrant-benchmark.md
11. docs/decisions/index.md
12. docs/research-log-post-v1.md only when historical reasoning is needed.

For product/inquiry-graph work also read:
- docs/formalism.md
- docs/ontology.md
- docs/annotation-guide.md
- docs/roadmap.md
- docs/evaluation.md

## 12. Things the next agent should not redo

Do not:

- rebuild the support algebra;
- invent a new argumentation framework;
- implement full ABA+ unless issue #18 triggers;
- add derivation DAGs unless issue #17 triggers;
- search again for a universal candidate-generation operator basis;
- invent a generic orchestration runtime before using blackboard/portfolio precedents;
- invent a new formal guarantee-transport calculus before Hets/DOL/MMT/refinement machinery is exhausted;
- conflate support with truth;
- conflate grounded acceptability with proposition acceptance;
- combine heterogeneous guarantees into one confidence score by default;
- treat assistant claims as user beliefs;
- claim hosted CI passes.

## 13. When to reopen architecture

Reopen foundational architecture only if:

- a benchmark cannot be represented without distortion;
- two current layers collapse distinctions that change outcomes;
- a required action/guarantee has no faithful type;
- an adapter cannot state the preservation property it needs;
- empirical annotation repeatedly fails because categories are not distinguishable;
- a concrete useful-system workflow exposes a missing semantic operation.

Otherwise prefer existing-framework adoption, implementation, validation, and empirical evaluation.

## 14. Open issues that matter

- #2 hosted CI infrastructure;
- #3 full export/source reconciliation;
- #17 derivation/subargument escalation;
- #18 full ABA+/hyperargumentation escalation;
- #34 acceptance licensing / warrant composition;
- #38 empirical usefulness of the inquiry representation/system;
- #39 strategy-performance adaptive-statistics audit.

Latest architectural decisions:
- ADR 015 typed generative systems;
- ADR 016 five-framework candidate-generation mapping survived;
- ADR 017 blackboard-style cross-framework orchestration;
- ADR 018 certified guarantee transport.

The repository is private.

The native Windows checkout used for verification has historically been:
C:\Users\thela\code\inquiry-graph-portable

Do not assume another local checkout is synchronized without checking Git state first.

## 15. Handoff bottom line

The foundational architecture is no longer in discovery mode.

It is in:

\[
\boxed{
\text{targeted open-problem work}
+
\text{empirical validation}
+
\text{product usefulness testing}
}
\]

The biggest meta-model question is acceptance/warrant composition.

The biggest inquiry-representation question is source completeness and annotation validity.

The biggest product question is whether the representation is actually useful.

That is where a new agent should start.
