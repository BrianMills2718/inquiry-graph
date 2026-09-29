# Goal: prove an AI can find Brian's positions, open questions and conflicts across conversations

## Goal

**Mission:** Brian's long-term aim (2026-09-29) is that an AI understands everything he is interested in and his positions across **all** his conversations, and identifies gaps, open questions and conflicts. Brian never reads the graphs; the reader is always an AI. This goal is the first finite proving step. Run the full chain on 5 real conversations and find out whether it beats the obvious alternative: an agent searching the ChatGPT archive and reading the chats it finds. The chain is:

1. inquiry-graph extracts attributed positions and questions from each chat;
2. onto-canon6 matches identical ideas and finds conflicts across chats;
3. an AI answers questions from the result.

**Execution profile:** `continuous-coordinated`

Why this profile: two repositories are involved, and onto-canon6 has other agents holding live claims.

**Stage and investment boundary:** proof of concept. Estimate: 1–2 working sessions. LLM spend is small; the 2026-09-29 single-chat pilot cost under $0.10. Nothing is deployed or published.

**Canonical example:** Input: 5 of Brian's ChatGPT conversations on overlapping topics, starting with "Inference Beyond Observation" (`6ab8563b-cbfc-83ea-81ed-a0acdea0ea9c`) and "Conceptualizing Inference Models" (`6ab96260-eb14-83ea-ae11-f964811b3b4f`). Action: an AI is asked, "Across these chats, what are my positions on X, where do they agree or conflict, and what did I leave open?" Observable result:
- an answer listing Brian-attributed positions, each with chat id and verbatim quote;
- at least one cross-chat agreement or conflict found through onto-canon6 identity or tension output;
- scores for this route and the archive-search route on the same question set, graded blind against a reference key.

**Forbidden substitutes:**
- the curated seed graph (`examples/seed/`) or any hand-authored stances, positions or keys standing in for live extraction;
- assistant proposals counted as Brian's positions;
- mocked or fake LLM clients;
- fixture-only onto-canon6 imports;
- a count of positions or conflicts without the listed members and quotes;
- a single-chat result presented as a cross-conversation result;
- a reference key produced by the system under test.

**Repository / working scope:** `BrianMills2718/inquiry-graph` (this document, the producer, the exporter and the evaluation). onto-canon6 is consumed read-only at a pinned revision.

## Boundaries

- **In scope:**
  - migrating inquiry-graph's extraction to Brian's shared `llm_client`;
  - live extraction of 5 chats;
  - an inquiry-graph-side exporter to onto-canon6's public lifecycle API (`AuthoringService`, `AssertionService`, `GovernanceService`, `resolve_identities`, `export_foundation_bundle`);
  - a reference key and comparison harness under `evaluation/cross_conversation/`.
- **Out of scope:**
  - UI or human-reader views;
  - new theory (epistemic-warrant);
  - scaling past 5 chats;
  - changing onto-canon6's kernel.
- **Writes allowed:**
  - inquiry-graph, through branches and PRs, merged when checks pass;
  - `private/` (gitignored) for transcripts.
- **Read-only or externally owned:**
  - onto-canon6. Other agents hold live claims there, including the stance plumbing lane `jev-stance-identity`. Do not write there.
  - epistemic-warrant.
  - The ChatGPT bridge: read and archive search only; never send into a chat.
- **Irreversible actions requiring authorization:** none expected. Never commit full transcripts. Never publish or deploy.

## Acceptance Checks

| ID | Criterion | Evidence to report |
| --- | --- | --- |
| C1 | Extraction runs live through `llm_client` on a real chat and produces Brian-attributed stances with verbatim anchors | trace ids; `inquiry-graph validate` shows 0 errors; stance precision spot-check of 10 or more Brian stances against the transcript, with counts |
| C2 | Reference key for the 5 chats is built independently of the system | a key built by exhaustive reading (a separate model pass over full transcripts, with no graph input); every key quote verified verbatim by script; count of dropped items |
| C3 | Positions reach onto-canon6 without losing who said what | the exporter run against onto-canon6 at a pinned SHA; a report of speaker/stance fields that were preserved or lost |
| C4 | Cross-chat identity or conflict output exists | onto-canon6 identity or tension records listing the member positions and their chats, or an explicit statement that the pinned revision produces none |
| C5 | Head-to-head comparison | 8–15 cross-chat questions from the key, answered by (A) an agent with archive search and chat reads and (B) an agent over the onto-canon6 export; blind grading; per-question table; hand check of 4 or more grades |
| C6 | Decision recorded | `evaluation/cross_conversation/results.md` plus a comment on issue #38 giving continue/replace/shelve and the reasons |

For every LLM behaviour claim, report trace ids and inspect the full trace directly.

## Increments

1. **Live producer (C1):** switch `extract` to `llm_client` and run it on "Inference Beyond Observation". Retires the unknown "does extraction work live?".
2. **Chats and reference key (C2):** select the other 3 chats by archive search on overlapping topics, and build the key.
3. **Extract all 5 chats.**
4. **Export to onto-canon6 (C3, C4).** If the pinned revision cannot carry speaker/stance, record the exact loss. Then run C5 route B over the inquiry-graph output directly, labelled "without kernel", and list the onto-canon6 gap under Non-Gating Next Actions.
5. **Comparison and decision (C5, C6).**

## Profile Additions

### Continuous-Coordinated

- **One progress authority:** this document's Current State section.
- **Active owners/claims (lane registry):**
  - *inquiry-graph lane* — owner: the goal-running session. Next event: an increment PR merged. Deadline: PT4H per increment. Missing-event transition: block.
  - *onto-canon6 stance lane* (`jev-stance-identity`) — owned by a ChatGPT agent, not this goal. This goal only reads its landed result at the pinned revision and never waits on it.
- **Authority transfer/reversion:** see the block below. A claim's state never transfers authority.
- **Worker reporting/status:** subagents report completion receipts. Keep at most one bounded wait per expected event. If an event is missing, make one fresh probe, then block. No repeated short polling.
- **Pinned cross-repository dependencies:**
  - onto-canon6: record the SHA used (it was `edfc34ad7` on 2026-09-29).
  - `llm_client`: the installed revision.
  - chatgpt-bridge: read and archive search.
- **Dependency-sensitive stop points:** onto-canon6's public API changed or broken at the pinned SHA; the ChatGPT bridge unable to read.

<!-- goal-authority-reversion:v1:start -->
```yaml
schema_version: "1.1"
owner: "coordinator:goal-running-session"
receiver: "coordinator:next-brian-session"
transfer:
  trigger: "explicit_handoff"
reporting:
  event: "increment PR merged with acceptance evidence"
  deadline: "PT4H"
  one_probe_transition: "block"
non_gating_utility_review:
  broad_cycle_limit: 2
  on_limit: "compare_direct_route_and_merge_or_defer"
  later_review: "exact_counterexample_only_unless_scope_expands"
```
<!-- goal-authority-reversion:v1:end -->

## Loop Bounds

- **No-progress stop:** 3 attempts on the same reproduced blocker with no new evidence.
- **Finite bound:** 8 increments in total.
- **Strategy revalidation:** after 3 increments, about 4 hours, or an outcome reset. Report outcome, enabling and process progress, and recommend retain, replace or clear.
- **Exact blocked resume event:** named per blocker in Current State.

## Non-Gating Next Actions

- The onto-canon6 stance lane landing speaker/stance support, if C3 shows the loss.
- The voice-mode excerpts of the founding chat, which need Brian's ChatGPT data export (issue #3).
- Scaling to Brian's whole archive, after C6 says continue.
- Hosted CI (#2).

## Current State

- **Demonstrated:**
  - The single-chat model-reader pilot (`evaluation/usefulness_pilot/results.md`).
  - **C1 (2026-09-29):** live extraction of "Inference Beyond Observation" through `llm_client`.
    - Input: 211 visible messages in 17 chunks, 2 minutes, $0.072, prompt `live-2.2.0`.
    - Output: 174 nodes, 153 stances (52 by Brian), 25 question events and 57 relations. `validate`: valid, 0 errors.
    - Traces: `inquiry-graph/live-extract/chatgpt:6ab8563b-…/chunk00`–`chunk16`. All 17 show 1 call, 0 errors, `finish_reason=stop`.
    - Spot checks of 12 random Brian stances per prompt round:
      - v2.0: 9/12 right; 2 wrong target or type; 1 arguable.
      - v2.1: 0 wrong, but 4/12 procedural noise.
      - v2.2: 11/12 right; 1 wrong target (a question attached to the assistant's answer); 0 procedural.
    - Speaker attribution is enforced by code. In v2.2 all 12 sampled stances quote Brian's own messages.
    - Quote realignment (formatting-insensitive matching, anchored to exact source text) raised node grounding from 43% to about 80%.
- **Current increment:** 2 (select the other 4 chats and build the reference key).
- **Blockers:** none.
- **Resume event:** n/a.

## Evaluator-Facing Objective

```text
Goal: prove whether an AI can find Brian's positions, open questions and conflicts across 5 real ChatGPT conversations better via inquiry-graph + onto-canon6 than via archive search. Read and follow docs/goals/cross-conversation-positions.md in BrianMills2718/inquiry-graph.
Profile: continuous-coordinated.
Canonical example: 5 real chats (incl. "Inference Beyond Observation") -> AI answers "where do my positions agree/conflict and what is open?" with Brian-attributed positions + chat id + verbatim quote, at least one cross-chat identity/conflict from onto-canon6 output, and blind-graded scores vs an archive-search agent on the same questions.
Forbidden substitutes: the curated seed graph or hand-authored stances/keys; assistant proposals counted as Brian's; mocked LLMs; fixture-only imports; counts without listed members; single-chat results; keys made by the system under test.
Boundaries: write only to inquiry-graph (PRs merged when checks pass) and gitignored private/; onto-canon6 and epistemic-warrant are read-only; never send into a ChatGPT chat; never commit transcripts; no deploy or publish.
Done when: C1-C6 in the goal doc are reported with evidence: trace ids, validate output, stance spot-check counts, verbatim-checked reference key, exporter loss report at a pinned onto-canon6 SHA, per-question comparison table with hand-checked grades, and results.md plus an issue #38 comment stating continue/replace/shelve.
Stop as blocked only after 3 attempts on the same reproduced blocker produce no new evidence or safe next action; report the blocker, owner and resume event. If onto-canon6 cannot carry speaker/stance, record the loss, run the comparison without the kernel, and finish.
Do not gate on: onto-canon6's stance lane landing, Brian reading anything, the ChatGPT data export, hosted CI, or scaling beyond 5 chats.
Revalidate after: 3 increments, ~4 hours, or an outcome reset. Report outcome/enabling/process progress and recommend retain, replace or clear. If misaligned, stop and return control; do not call misalignment a technical blocker.
```
