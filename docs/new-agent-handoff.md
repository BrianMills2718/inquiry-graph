# New Agent Handoff — Inquiry Graph + Formal Epistemic Reasoning Meta-Model

> **Split, 2026-09-29.** The formal theory (support, defeat, ABA, warrant/license regimes and their certificates), its research docs, ADRs 007–018, the paper draft and `project-status.md` moved to [epistemic-warrant](https://github.com/BrianMills2718/epistemic-warrant) with full history. Theory items below are tracked there. Issues #34, #46, #17, #18 and #40 were transferred and are now epistemic-warrant #1–#5 in that order; the old numbers here redirect. This repository is the inquiry-graph tool: import, extraction, validation, query and render, plus the seed. Its product priorities are issue #38 (usefulness) and issue #3 (source reconciliation).


> **Prepared:** 2026-09-29  
> **Repository:** \`BrianMills2718/inquiry-graph\` (private)  
> **Current main:** \`81f136fa73c843a97267e5d04a01c9be885beb8c\`  
> **Purpose:** allow a new agent to continue without reconstructing the long founding conversation.
>
> **Immediate warning:** start with GitHub issue **#46** before extending the formal layer. The integration suite is green, but an independent semantic audit reproduced three correctness defects that remain in current code.

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

Last independently executed integrated native-Windows baseline (post-PR-#36 code at `4ad3942`, 2026-09-29):

- **142 tests passed**
- seed fixture rebuilt successfully
- **8 generated artifacts** matched
- graph validation: **0 errors / 0 warnings**
- dependency check: clean

An independent Linux/Python 3.10 run of the same tree reproduced these results. Details: `docs/verification.md`.

Environment used:

- Python 3.14.7
- Pydantic 2.13.5
- NetworkX 3.7

At handoff review, changes after verified code commit `4ad3942` were documentation-only; the execution record therefore still covered the executable tree. Check current `main` before resuming work rather than relying on a frozen branch SHA in this document.

**But:** issue #46 is a semantic-audit failure on that same executable layer. Passing tests do not establish the correctness of the binary preference semantics, flat-ABA precondition, or grounded-warrant target binding.

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

## 10. Immediate correctness gate and main research frontier

The next agent should **first resolve issue #46** before extending acceptance semantics.

Issue #46 reports three reproduced defects that still apply to current code because only documentation changed after the audited commit:

1. the binary preference-removal filter can make an assumption and its contrary both grounded-IN;
2. flat ABA is claimed but not enforced when an assumption is also a rule head;
3. grounded-dialectical warrant can ignore an unrelated action target.

The first defect is especially important because it turns issue #18 from a purely hypothetical escalation path into an active design question: either implement a faithful preference semantics with the needed rationality properties, or explicitly remove/demote the current filter from warrant-bearing use.

After #46 is resolved, the main foundational/integrative open problem is:

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

Current preference layer is deliberately binary, but issue #46 has now demonstrated a concrete consistency failure caused by attack removal without reversal.

Treat #18 as **conditionally activated for review**, not automatically as a mandate to implement the entire HYPAF/full-ABA+ stack. The new agent should first decide whether a faithful preference semantics is needed in the warrant-bearing reference layer or whether the current filter should be explicitly demoted/removed.

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

- **#46** — formal-layer semantic defects; **immediate correctness priority**.
- **#34** — acceptance licensing and warrant composition; next foundational priority after #46.
- **#38** — empirical usefulness of the inquiry representation / Inquiry System.
- **#3** — full conversation export reconciliation and review of 798 proposed annotations.
- **#40** — systematic comparison against the closest integrated frameworks, with adoption/alignment rather than novelty as the goal.
- **#18** — full ABA+ / set-to-set hyperargumentation; now conditionally activated for review by #46's preference counterexample.
- **#17** — escalation path for first-class derivation/subargument structure; still dormant.
- **#2** — hosted CI Python 3.11/3.13 matrix; low-priority infrastructure debt because local execution verification is green.

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

### Track A — formal correctness, then foundational research

Start with issue #46. Fix/enforce the clear local defects first, and make the preference-semantics decision together with issue #18. Then proceed to issue #34: acceptance licensing + warrant composition.

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

1. **Issue #46 — formal-layer semantic defects.** Resolve before extending the warrant/acceptance layer.
2. **Issue #34 — acceptance licensing + warrant composition** after #46.
3. **Useful Inquiry System/product track** may proceed independently; do not block it on philosophical closure.
4. **Issue #38 — empirical usefulness** for the inquiry representation/product.
5. **Issue #3 — source reconciliation** when the full export is available.
6. **Issue #40 — systematic integrated-framework comparison** for adoption/positioning and paper cleanup.
7. **Issue #18** is now conditionally activated for preference-semantics review by #46; **issue #17** remains escalation-only.
8. **PR #36** completed the bounded strategy-performance multiple-comparison/optional-stopping correction; the post-merge integrated rerun passed (142 tests, native Windows and Linux).
9. **Issue #2** remains low-priority hosted-CI infrastructure debt.
10. **PR #8/#15** remain intentionally separate and must not be merged casually.

If a future document conflicts with this handoff, prefer the canonical closeout and current ADRs, then update this handoff rather than inferring intent from historical notes.

## 22. One-sentence handoff

The foundational architecture is broadly mapped to mature prior work and execution-verified, but **issue #46 is the immediate semantic-correctness gate**; fix that before acceptance/warrant composition, while the product track can independently test whether the inquiry representation is actually useful.
