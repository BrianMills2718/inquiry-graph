# New Agent Handoff — Inquiry Graph

> **Prepared:** 2026-09-29  
> **Repository:** `BrianMills2718/inquiry-graph` (private)  
> **Current main:** verify live before making changes; do not rely on a frozen SHA in this handoff.  
> **Purpose:** source-grounded inquiry representation and the future useful Inquiry System.

## 1. Repository split

The foundational theory was split into a separate repository:

- **Theory:** `BrianMills2718/epistemic-warrant`
- **Product/inquiry representation:** this repository

Do not copy the theory code back here.

If the product later uses the theory, add an explicit package dependency so the relationship is visible in code.

The theory repository has its own handoff, roadmap and verification record.

## 2. What Inquiry Graph is

Inquiry Graph represents **how an inquiry develops**, not merely its topics.

It records:

- source utterances/excerpts;
- content nodes;
- questions;
- typed relations;
- inquiry moves;
- actor-relative stance;
- question-status history;
- exact source grounding/provenance;
- review status.

It is intentionally not a truth engine and does not infer private/user beliefs from assistant statements.

## 3. Current founding dataset

Current curated seed:

- 219 source excerpts/messages
- 229 content nodes
- 250 relations
- 185 inquiry moves
- 58 stance events
- 76 question events
- 54 distinct questions
- 798 proposed annotations
- 0 confirmed / 0 rejected

This is a curated reconstruction, **not** a reconciled full ChatGPT export.

## 4. Immediate product priority — issue #38

The main product/scientific question is:

> Does the representation help an AI recover Brian's attributed positions, rationale, open questions, dependencies and tensions when the relevant history cannot all fit in context?

Issue #38 is the primary active product track.

**Status 2026-09-29:** a first pilot with an AI model as the reader is done ([results](../evaluation/usefulness_pilot/results.md)). The raw transcript beat the graph report (0.81 vs 0.65 key points covered; the plain excerpts scored 0.59). The graph lost mainly on reasons behind decisions and what happened to side lines. Next: record decision reasons/outcomes and deferred-branch rationale, rerun the AI-reader pilot, then test multi-conversation histories too large for one context window. **The intended reader is always AI; do not create a human-reader evaluation track.**

Start with the smallest useful test, not a polished UI.

Suggested tasks:

- identify unresolved questions;
- recover why a proposal was rejected;
- identify live assumptions/dependencies;
- distinguish user commitments from assistant proposals;
- recover abandoned/deferred branches;
- reconstruct revisions that produced the current view;
- resume the inquiry after interruption.

Prefer measurable outcomes:

- answer accuracy;
- missed branches/dependencies;
- attribution errors;
- false question closure;
- time/steps to recover context.

## 5. Cross-conversation architecture boundary

`inquiry-graph` is the per-conversation producer. Cross-source identity/alignment, governed assertions and tension/conflict detection belong in the separate `onto-canon6` direction already identified in project status. Do not turn inquiry-graph into a second cross-conversation canonical store.

The useful-system target is therefore a pipeline: per-conversation attributed inquiry structure from inquiry-graph, then cross-conversation identity/tension integration downstream.

## 6. Source-integrity priority — issue #3

When the full conversation export is available:

1. import the active branch;
2. reconcile the 219 curated excerpts against exact source message IDs/offsets;
3. preserve previous mappings/review history;
4. identify omitted transitions/branches;
5. adjudicate interpretation separately from quote validity;
6. audit actor attribution;
7. review question closure.

Do not fabricate original message IDs or timestamps.

## 7. Hosted CI — issue #2

Hosted GitHub Actions still fails/cancels before runner steps/logs.

Treat this as infrastructure debt, not an application failure.

Current local post-split verification is green; see `docs/verification.md`.

## 8. Fresh post-split verification

Verified from a fresh native-Windows clone of current reviewed `main`:

- Python 3.14.7
- editable `.[dev]` install succeeded
- **60 tests passed**
- seed rebuild succeeded: 229 nodes / 250 relations / 185 moves
- **8 generated artifacts** checked
- graph validation: **0 errors / 0 warnings**
- `pip check`: clean

This is the authoritative verification for the current product-only repository after the theory split.

## 9. Open PRs that are separate trajectories

### PR #8 — formal-inquiry-substrate

A second deliberately separate inquiry trajectory/handoff.

### PR #15 — inquiry-hypergraph-crosswalk

Stacked on #8; includes the Scientific Hypergraph / OntoCanon crosswalk.

**Do not merge either automatically.**

They predate the current main line and require a deliberate architecture/integration decision.

## 10. Theory status

The theory repository is `BrianMills2718/epistemic-warrant`.

At current handoff, its default next step is its issue #2 semantic-correctness audit, then issue #1 acceptance licensing/warrant composition.

If you are assigned theory work, switch repositories and follow that repository's handoff.

Do not use the stale duplicated theory issues formerly present in this repository as the source of truth.

## 11. Stop rules

Do not:

- infer user stance from assistant output;
- silently merge semantically similar nodes;
- treat the curated seed as source-complete;
- build a polished UI before testing usefulness;
- make product work depend on philosophical closure;
- copy epistemic-warrant theory code back into this repo;
- merge PR #8/#15 casually;
- claim hosted CI passed when no runner executed.

## 12. Recommended next-agent tracks

Choose one:

### Track A — usefulness pilot
Work issue #38. This is the default product recommendation.

### Track B — source reconciliation
Work issue #3 when the full export is available.

### Track C — machine-consumable product workflow
Only after the AI-reader usefulness pilot identifies which retrieval/representation workflows matter. Do not optimize for a human-facing UI.

### Track D — old formal/hypergraph trajectory
Review PR #8 and stacked #15 only if explicitly requested.

### Track E — theory
Switch to `epistemic-warrant`; do not continue theory in this repository.

## 13. Canonical product documents

1. `docs/new-agent-handoff.md`
2. `docs/project-status.md`
3. `docs/roadmap.md`
4. `docs/verification.md`
5. `docs/formalism.md`
6. `docs/requirements.md`
7. `docs/annotation-guide.md`
8. `docs/evaluation.md`
9. `docs/architecture.md`
10. `docs/decisions/index.md`

Historical theory documents were moved to `epistemic-warrant`.

## 14. One-sentence handoff

**Inquiry Graph is the per-conversation, source-grounded producer for an AI-facing inquiry system: improve rationale/outcome capture, rerun issue #38 with an AI reader, then test multi-conversation histories beyond one context window; keep foundational theory in `epistemic-warrant` and cross-source canonicalization downstream.**
