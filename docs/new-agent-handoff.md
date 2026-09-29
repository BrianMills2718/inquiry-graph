# New Agent Handoff — Inquiry Graph

> **Prepared:** 2026-09-29  
> **Repository:** `BrianMills2718/inquiry-graph` (private)  
> **Current main at review:** `fd85714a77e807a7b064426978ca4c0d5dcec332`  
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

> Does the representation actually help a person or model navigate, audit, resume, or improve an inquiry better than the transcript alone?

Issue #38 is the primary active product track.

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

## 5. Source-integrity priority — issue #3

When the full conversation export is available:

1. import the active branch;
2. reconcile the 219 curated excerpts against exact source message IDs/offsets;
3. preserve previous mappings/review history;
4. identify omitted transitions/branches;
5. adjudicate interpretation separately from quote validity;
6. audit actor attribution;
7. review question closure.

Do not fabricate original message IDs or timestamps.

## 6. Hosted CI — issue #2

Hosted GitHub Actions still fails/cancels before runner steps/logs.

Treat this as infrastructure debt, not an application failure.

Current local post-split verification is green; see `docs/verification.md`.

## 7. Fresh post-split verification

Verified from a fresh native-Windows clone of current reviewed `main`:

- Python 3.14.7
- editable `.[dev]` install succeeded
- **60 tests passed**
- seed rebuild succeeded: 229 nodes / 250 relations / 185 moves
- **8 generated artifacts** checked
- graph validation: **0 errors / 0 warnings**
- `pip check`: clean

This is the authoritative verification for the current product-only repository after the theory split.

## 8. Open PRs that are separate trajectories

### PR #8 — formal-inquiry-substrate

A second deliberately separate inquiry trajectory/handoff.

### PR #15 — inquiry-hypergraph-crosswalk

Stacked on #8; includes the Scientific Hypergraph / OntoCanon crosswalk.

**Do not merge either automatically.**

They predate the current main line and require a deliberate architecture/integration decision.

## 9. Theory status

The theory repository is `BrianMills2718/epistemic-warrant`.

At current handoff, its default next step is its issue #2 semantic-correctness audit, then issue #1 acceptance licensing/warrant composition.

If you are assigned theory work, switch repositories and follow that repository's handoff.

Do not use the stale duplicated theory issues formerly present in this repository as the source of truth.

## 10. Stop rules

Do not:

- infer user stance from assistant output;
- silently merge semantically similar nodes;
- treat the curated seed as source-complete;
- build a polished UI before testing usefulness;
- make product work depend on philosophical closure;
- copy epistemic-warrant theory code back into this repo;
- merge PR #8/#15 casually;
- claim hosted CI passed when no runner executed.

## 11. Recommended next-agent tracks

Choose one:

### Track A — usefulness pilot
Work issue #38. This is the default product recommendation.

### Track B — source reconciliation
Work issue #3 when the full export is available.

### Track C — product UI
Only after a usefulness pilot identifies which views/workflows actually matter.

### Track D — old formal/hypergraph trajectory
Review PR #8 and stacked #15 only if explicitly requested.

### Track E — theory
Switch to `epistemic-warrant`; do not continue theory in this repository.

## 12. Canonical product documents

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

## 13. One-sentence handoff

**Inquiry Graph is now a product/inquiry-representation repository: test whether the representation is useful (issue #38), reconcile the source when available (issue #3), and keep foundational theory in `epistemic-warrant`.**
