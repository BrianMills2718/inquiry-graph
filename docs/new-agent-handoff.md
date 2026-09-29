# New Agent Handoff — Inquiry Graph + Formal Epistemic Reasoning Meta-Model

> **Prepared:** 2026-09-29  
> **Repository:** \`BrianMills2718/inquiry-graph\` (private)  
> **Purpose:** allow a new agent to continue without reconstructing the long founding conversation.

## 1. Read this first

There are **three related but distinct projects** in this repository/conversation:

1. **Formal Epistemic Reasoning Meta-Model** — the foundational research model.
2. **Inquiry Representation Model** — the source-grounded graph of how an inquiry develops.
3. **Inquiry System** — the future useful product for navigating, resuming, auditing, and improving inquiry.

Do not collapse them into one project.

The user is most interested in the useful system, but the current session focused heavily on getting project 1 into a coherent, documented, literature-aligned state.

The canonical high-level research document is:

- \`docs/formal-epistemic-reasoning-metamodel.md\`

The compact project-management summary is:

- \`docs/project-status.md\`

The current roadmap is:

- \`docs/roadmap.md\`

The paper draft is:

- \`docs/paper-formal-epistemic-reasoning-metamodel.md\`

## 2. Core result of the foundational work

The project moved away from trying to make deduction / induction / abduction a primitive MECE taxonomy.

The current central hypothesis is that epistemic reasoning is better modeled by a factorized architecture:

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
\text{epistemic action/update}
\neq
\text{strategy/control}
}
\]

This is a **working architectural hypothesis**, not a proven universal theorem.

## 3. Canonical state and notation

A reasoning state is:

\[
s=(\mathcal F,K_{\mathcal F},\Gamma,Q,\Pi)\in\mathcal S
\]

with:

- \(\mathcal F\): formal representation substrate;
- \(K_{\mathcal F}\): persistent support/provenance state;
- \(\Gamma\): temporary assumption context;
- \(Q\): current question/task;
- \(\Pi\): strategy/control state.

Persistent support state:

\[
K_{\mathcal F}=(N,A,J,\lambda,\rho)
\]

where \(\lambda(n)\) is the set of minimal assumption environments supporting \(n\).

Positive support uses finite antichains:

\[
\mathsf{Supp}(X)=\operatorname{Antichain}(\mathcal P_{\mathrm{fin}}(X)).
\]

Canonical notation is defined in §5.1 of the closeout. Older docs still use some legacy notation.

## 4. Warrant model

The central warrant judgment is:

\[
\boxed{
\mathfrak W;\Phi\vdash_\kappa a:G
}
\]

meaning:

> under warrant regime \(\mathfrak W\) and applicability assumptions \(\Phi\), certificate/support object \(\kappa\) warrants epistemic action \(a\) with typed guarantee \(G\).

Keep these distinct:

\[
\boxed{
\text{support}
\neq
\text{warrant}
\neq
\text{current license}
\neq
\text{executed update}
}
\]

Current license requires:

\[
C\models\Phi.
\]

Executable benchmark regimes currently approximate this with explicit set inclusion; that is not the foundational semantics.

## 5. Candidate generation status

Candidate generation is **not** a blank-slate open problem anymore.

After a landscape survey and mappings, the current typed generative regime is:

\[
\mathcal G_R=
(\mathcal A_R,\mathcal L_R,\mathcal D_R,B_R,\mathcal O_R,\to_R,V_R)
\]

where:

- \(\mathcal A_R\): artifact/candidate ontology;
- \(\mathcal L_R\): generative/representation language;
- \(\mathcal D_R\): draft state space;
- \(B_R\): admissibility/search bias;
- \(\mathcal O_R\): operators;
- \(\to_R\): ordinary candidate transitions;
- \(V_R\): evaluators.

A concrete generation episode is:

\[
E_G=(R,\mathcal G_R,d_0).
\]

A true change to the represented generative regime is:

\[
\mu:\mathcal G_R\rightharpoonup\mathcal G'_R.
\]

Important result:

\[
\boxed{
\text{new predicate/concept}
\not\Rightarrow
\text{new generative meta-language}
}
\]

Transformationality is representation-relative.

Frameworks already mapped successfully:

- CEGIS / program synthesis;
- Meta-Interpretive Learning;
- anti-unification;
- HR automated theory formation;
- computational conceptual blending.

Cross-framework orchestration is also mostly established prior art:

- blackboard systems;
- Hayes-Roth blackboard control;
- Michalski multistrategy learning;
- algorithm selection / portfolios;
- hyper-heuristics;
- algorithm configuration;
- PRODIGY;
- Soar;
- computational reflection.

The adopted architecture is effectively:

\[
\boxed{
\text{typed blackboard}
+
\text{generator/evaluator portfolio}
+
\text{explicit controller}
+
\text{reflection}
+
\text{warrant}
}
\]

See ADRs 015–017.

## 6. Guarantee transport status

The remaining cross-framework formal-transport problem has also been mapped to mature work.

Rule:

\[
\boxed{
\text{artifact translation}
\not\Rightarrow
\text{guarantee transport}
}
\]

Use a typed preservation relation:

\[
\operatorname{Preserves}_\tau(G_S,G_T).
\]

Transport classes:

- **T0** — syntactic/opaque; no semantic warrant transport;
- **T1** — provenance/structural correspondence only;
- **T2** — sound one-way/weakened guarantee transport;
- **T3** — exact satisfaction/judgment preservation;
- **T4** — compositional preservation for the actual pipeline operators.

Adopt existing machinery before building anything new:

- institutions / morphisms / comorphisms;
- DOL / Hets;
- MMT/LF theory morphisms;
- abstract interpretation;
- refinement / assume-guarantee / contract theories.

If no preservation certificate exists, translate artifact/provenance only and **re-warrant in the target regime**.

See ADR 018 and \`docs/warrant-guarantee-transport.md\`.

## 7. Implemented reference regimes

The repository has executable reference instances for:

- positive support antichain algebra;
- independent-Bernoulli support interpretation;
- ABA assumptions/contraries and minimal-support arguments;
- typed attack origins;
- binary preference filtering;
- Dung grounded semantics;
- grounded dialectical warrant;
- graded-support recording;
- strict-Horn deductive warrant;
- measurement result + uncertainty/calibration;
- testimony posterior + reference-class-relative source reliability;
- finite-class statistical generalization bound;
- strategy-performance warrant.

These are benchmark/reference regimes, not claims of universal adequacy.

## 8. Verification status

Last independently executed integrated native-Windows baseline:

- **138 tests passed**
- seed fixture rebuilt successfully
- **8 generated artifacts** matched
- graph validation: **0 errors / 0 warnings**
- dependency check: clean

PR #36 subsequently merged a strategy-performance multiple-comparison/optional-stopping correction and records **142 tests passed** on its tested branch. The current handoff agent reviewed the patch but could not independently rerun current main because the Windows execution channel was degraded. Treat a fresh integrated rerun as a small verification follow-up, not a foundational blocker.

Environment used:

- Python 3.14.7
- Pydantic 2.13.5
- NetworkX 3.7

Hosted GitHub Actions remains broken before runner execution. That is issue #2 and should be treated as infrastructure debt, not application failure.

Local checkout:

\`C:\Users\thela\code\inquiry-graph-portable\`

When syncing a stale local checkout, inspect status before changing branches. The previously verified sequence was:

\`\`\`powershell
git status -sb
git fetch origin main
git switch main
git merge --ff-only origin/main
git status -sb
\`\`\`

Full verification commands:

\`\`\`powershell
python -m pytest -q
python examples/build_seed.py
python tools/build_artifacts.py --check
python -m inquiry_graph validate examples/seed/graph.json
python -m pip check
\`\`\`

Do not claim a passing run unless those commands (or equivalent checked-in workflow steps) actually execute.

## 9. Current graph/source state

Founding-dialogue curated source:

- 219 source excerpts/messages
- 229 content nodes
- 250 relations
- 185 inquiry moves
- 58 stance events
- 76 question events
- 54 distinct questions
- 798 proposed annotations
- 0 confirmed / 0 rejected

This is **not** a fully reconciled conversation export.

Issue #3 tracks reconciliation against the full export.

## 10. Main research frontier

The current main foundational/integrative open problem is:

# **Acceptance licensing + warrant composition**

Tracked in issue #34.

The existing regimes mostly license recording, derivation, defeasible use, or strategy selection under stated guarantees.

There is no general rule yet for when heterogeneous typed warrants license stronger actions such as:

- accept;
- commit;
- use-for-action;
- revise;
- retract.

Important questions:

- Is acceptance a single action or stakes/task-relative family?
- Can one regime license acceptance or is composition required?
- How should deductive, defeasible, probabilistic, testimonial, measurement and statistical guarantees combine?
- What guarantee attaches to acceptance?
- How are lottery/preface closure failures handled?
- What licenses retraction/revision?
- Can acceptance/composition policies themselves be warranted?

Before inventing machinery, compare Carneades proof standards, belief-versus-acceptance literature, decision-theoretic acceptance, structured argumentation, belief revision and explicit policy/contract formalisms.

Do **not** introduce a universal scalar confidence threshold by default.

## 11. Other open research

Secondary open questions:

- warrant-of-warrant / backing / regress;
- richer context entailment \(C\models\Phi\);
- epistemic action algebra / representation theorems;
- reflective self-application and trust;
- empirical adequacy of the factorization;
- generative-regime equivalence/composition, only if needed;
- operator/bias invention, only if mature meta-learning/hyper-heuristic machinery proves insufficient.

## 12. Deliberate escalation issues

### Issue #17 — derivation/subargument structure

Current ABA dialectical identity is:

\[
(\text{conclusion},\text{supporting assumption environment}).
\]

Escalate only if:

- ASPIC+-style subargument attacks;
- proof-structure-sensitive preferences;
- proof-sensitive warrant;
- exact derivation explanation

become necessary.

Do not preemptively add derivation DAGs.

### Issue #18 — full ABA+ / hyperargumentation

Current preference layer is deliberately binary and Dung-compatible.

Escalate only if:

- attack reversal;
- collective set-to-set attacks;
- faithful full ABA+ semantics

materially affect a benchmark/use case.

## 13. Product / Inquiry System track

The user regards the useful Inquiry System as especially important, but it can be assigned to a separate agent.

Do not require every foundational question to be solved first.

Potential product goals:

- show what the inquiry is trying to resolve;
- show candidate answers and why they were rejected/retained;
- show live assumptions;
- show genuinely unresolved questions;
- show revisions/retractions and provenance;
- show productive reasoning strategies;
- help resume a long inquiry;
- eventually suggest what to inspect next.

The central empirical question is:

> Does the representation give users something valuable that reading the raw transcript does not?

Issue #3/source reconciliation is a prerequisite for treating the founding inquiry as source-complete, but product prototypes can be explored before philosophical closure.

## 14. Open GitHub issues

At handoff:

- **#2** — hosted CI Python 3.11/3.13 matrix; low-priority infrastructure debt because local verification is green.
- **#3** — full conversation export reconciliation and review of 798 proposed annotations.
- **#17** — escalation path for first-class derivation/subargument structure.
- **#18** — escalation path for full ABA+ / set-to-set hyperargumentation.
- **#34** — acceptance licensing and warrant composition; **main foundational priority**.
- **#38** — evaluate whether the inquiry representation is actually useful; main empirical/product-validation issue.
- **#40** — systematic comparison matrix against the closest integrated frameworks; main research-positioning/adoption issue.

## 15. Open pull requests that are separate from current main

Two older PRs remain intentionally open:

### PR #8 — Add formal inquiry substrate handoff

Branch: \`formal-inquiry-substrate\`

This contains a second, deliberately separate inquiry trajectory and formal-inquiry handoff. It was not merged into the founding seed because cross-graph identity/integration had not been defined.

### PR #15 — Crosswalk Inquiry Graph with Hypergraph kernel and OntoCanon

Branch: \`inquiry-hypergraph-crosswalk\`

This is stacked on PR #8 and includes a Scientific Hypergraph / OntoCanon crosswalk.

**Do not merge either automatically.**

They predate the current main research line and should be rebased/reviewed as a separate architecture decision if that trajectory is resumed.

## 16. Documentation hierarchy

When documents disagree, prefer this order:

1. \`docs/new-agent-handoff.md\` — current handoff/priorities.
2. \`docs/formal-epistemic-reasoning-metamodel.md\` — canonical foundational model + notation.
3. \`docs/project-status.md\` — compact current status.
4. ADRs in \`docs/decisions/\` — durable architecture decisions.
5. specialized current docs:
   - \`warrant-license-interface.md\`
   - \`warrant-guarantee-transport.md\`
   - \`candidate-generation-landscape.md\`
   - \`candidate-generation-framework-mappings.md\`
   - \`candidate-generation-cross-framework-glue.md\`
   - \`end-to-end-warrant-benchmark.md\`
6. \`docs/research-log-post-v1.md\` — chronological history, not canonical current semantics.
7. older stage documents — useful history but may use superseded notation/claims.

## 17. Documentation debt

The final handoff review synchronized the canonical project status, architecture reassessment, closeout checklist, and paper draft with the current priority: acceptance licensing + warrant composition. The paper now reflects the narrowing of candidate generation and uses the canonical warrant notation in its top-level statement.

Known cleanup work that remains:

- older stage documents still use pre-closeout notation and should be treated as historical unless explicitly migrated;
- the paper draft is still not submission-ready: it needs a systematic related-work pass, bibliography normalization, and a stronger formal/empirical evaluation story;
- PR #36 now handles declared multiple comparisons and optional stopping for the strategy-performance reference regime; benchmark reuse/adaptive-selection assumptions still need to be stated truthfully by callers;
- full comparison to adjacent integrated meta-models/cognitive architectures is not exhaustive;
- source reconciliation and empirical usefulness remain undone.

Do not spend time normalizing every historical document unless that work directly serves the next chosen track.

## 18. Research methodology / user preference

The user explicitly prefers:

- mature literature/frameworks before invention;
- compact, information-dense communication;
- corrections/pushback rather than reflexive agreement;
- formal/descriptive questions separated from normative “good reasoning” questions;
- representation-relative claims rather than fake universality;
- durable decisions recorded in GitHub;
- no reliance on hosted CI as proof when jobs never executed.

A recurring project method is **primitive-factorization analysis**:

\[
\text{candidate formalization}
\to
\text{counterexample}
\to
\text{hidden assumption}
\to
\text{refactor}.
\]

Diagnostics include:

- underfactored;
- overfactored;
- misfactored;
- representation-dependent;
- incomplete;
- noncanonical.

## 19. Stop rules for the new agent

Do not:

- add formal systems because they are merely adjacent;
- claim novelty as a goal;
- invent candidate-generation machinery already covered by mature work;
- collapse heterogeneous guarantees into one scalar without an explicit warranted policy;
- treat translation as guarantee preservation without a certificate;
- infer user belief from assistant statements or conversational acknowledgment;
- merge PR #8/#15 casually;
- implement issues #17/#18 unless their trigger conditions are actually met.

## 20. Recommended next-agent choices

Choose **one** track instead of continuing everything at once.

### Track A — foundational research

Start with issue #34: acceptance licensing + warrant composition.

### Track B — useful system/product

Work issue #38. Treat the Inquiry System as a separate project. Prototype the smallest human-readable inquiry view needed to test whether the representation earns the graph/meta-model complexity.

### Track C — source integrity

Work issue #3 when the full export is available.

### Track D — paper/research communication

Work issue #40. Build the systematic comparison matrix against the closest integrated frameworks, replace project terminology with established terminology where appropriate, and use that result to normalize the paper. Present the architecture as synthesis/interface work rather than a novelty claim.

### Track E — old formal-inquiry/hypergraph branch

Review/rebase PR #8 and stacked PR #15 only if the user explicitly wants that trajectory resumed.

## 21. Final handoff review

The roadmap, project status, architecture reassessment, canonical closeout, paper draft, open-issue list, and deliberately separate PR #8/#15 stack were reviewed together before handoff.

Current priority order is authoritative as follows:

1. **Issue #34 — acceptance licensing + warrant composition** if continuing foundational research.
2. **Useful Inquiry System/product track** may proceed independently; do not block it on philosophical closure.
3. **Issue #38 — empirical usefulness** for the inquiry representation/product.
4. **Issue #3 — source reconciliation** when the full export is available.
5. **Issue #40 — systematic integrated-framework comparison** for adoption/positioning and paper cleanup.
6. **Issues #17/#18** remain escalation-only, not active implementation plans.
6. **PR #36** completed the bounded strategy-performance multiple-comparison/optional-stopping correction; only a fresh independent integrated rerun remains.
7. **Issue #2** remains low-priority hosted-CI infrastructure debt.
8. **PR #8/#15** remain intentionally separate and must not be merged casually.

If a future document conflicts with this handoff, prefer the canonical closeout and current ADRs, then update this handoff rather than inferring intent from historical notes.

## 22. One-sentence handoff

The foundational architecture is now broadly mapped to mature prior work and internally verified; **do not keep expanding it by default**—the main research frontier is acceptance/warrant composition, while the most important product question is whether the inquiry representation is actually useful.
