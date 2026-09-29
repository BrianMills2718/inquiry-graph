# Goal: relation-typed cross-chat linker, tested at a scale where reading everything doesn't fit

## Goal

**Mission:** Brian's long-term aim is an AI that understands his interests and positions across **all** his conversations and finds gaps, open questions and conflicts. Brian never reads the graphs; the reader is always an AI.

The previous goal (`cross-conversation-positions.md`, results in `evaluation/cross_conversation/results.md`) showed three things:
- extracted positions match reading full transcripts, at about 1/20 of the cost;
- onto-canon6's same-claim alignment finds no links across chats;
- both routes are weak on recurring open questions.

This goal builds the missing piece. A linker labels how Brian's positions in *different* chats relate:
- `same`
- `agrees`
- `extends`
- `pulls_against`
- `evolves`
- `unrelated`

The export also carries question status and chat dates. The test then runs at a scale where reading everything no longer fits one model call.

**Execution profile:** `continuous-light`

Why this profile: one repository (inquiry-graph), reversible, no deployment. Another writer sometimes merges docs PRs to inquiry-graph, so sync to `origin/main` before each PR.

**Stage and investment boundary:** proof of concept. Estimate: 1–2 working sessions. LLM spend is expected to be a few dollars; the previous 5-chat goal cost under $1.

**Canonical example:** Input is 30 of Brian's ChatGPT conversations from different months and topics, each with substantive messages from Brian: the 5 from the previous goal plus 25 selected by archive search. Their combined visible text is far beyond one call's context. An AI is asked, for example, "Where have my views on X changed or pulled against each other across chats, and which questions do I keep raising without settling?" The observable result has three parts:
- an answer built from Brian-attributed positions, each with chat title, date and verbatim quote;
- typed cross-chat links (e.g. `pulls_against` between a May position and a September one), with at least one cross-chat link that the answer uses;
- blind-graded scores for three routes on the same questions.

**Forbidden substitutes:**
- the curated seed graph, or hand-authored positions, links or keys;
- assistant proposals counted as Brian's positions;
- mocked or fake LLM clients;
- links produced only by embedding similarity without a typed judgment;
- counts of links or conflicts without the linked members and quotes;
- results on fewer than 20 chats presented as a scale result;
- a reference key produced by the system under test;
- a "can't fit" claim for route A without measured sizes.

**Repository / working scope:** `BrianMills2718/inquiry-graph`: the linker in `src/`, and the evaluation in `evaluation/cross_conversation_scale/`.

## Boundaries

- **In scope:**
  - adding question status and chat dates to the per-chat positions export;
  - a typed cross-chat linker: embedding recall, then an LLM relation judgment, restricted to pairs from different chats;
  - selecting and extracting 25 more chats;
  - an independent reference key;
  - a three-route comparison.
- **Out of scope:**
  - UI or human-reader views;
  - epistemic-warrant theory;
  - onto-canon6 changes (it is not used in this goal);
  - scaling past 50 chats.
- **Writes allowed:**
  - inquiry-graph, through branches and PRs, merged when checks pass;
  - gitignored `private/` for transcripts and quote-bearing outputs.
- **Read-only or externally owned:**
  - the ChatGPT bridge: read and archive search only; never send into, rename, move, tag or reload chats;
  - onto-canon6 and epistemic-warrant.
- **Irreversible actions requiring authorization:** none expected. Never commit transcripts or quote-bearing outputs. Never publish or deploy.

## Acceptance Checks

| ID | Criterion | Evidence to report |
|---|---|---|
| C1 | Linker exists and is tested | Tests pass. One live run on the previous goal's 5 chats: link counts by type, a hand check of 10 or more cross-chat links with the number judged correct, and trace ids |
| C2 | 30 or more chats extracted with question status and dates | Per-chat validate output (0 errors), total cost, and the chat list with dates and visible character counts. The combined visible text is measured and shown to exceed one call's context |
| C3 | Independent reference key | Per-chat positions with quotes verified by code (not using inquiry-graph extraction), and 12–15 cross-chat questions covering agreement, pulls-against, recurring open question, change over time and position summary. Kept and dropped counts |
| C4 | Three-route comparison, blind-graded | Route A: archive-search-then-read (lexical retrieval over the transcripts, reading the top chats up to a fixed context budget). Route B: positions plus typed links plus question status and dates. Route C: positions only (ablation). Per-question table, category means, cost, and a hand check of 4 or more grades |
| C5 | Decision recorded | `evaluation/cross_conversation_scale/results.md` plus a comment on inquiry-graph issue #38 stating continue/replace/shelve. It must say whether the links add value (B vs C) and whether the graph route beats search at scale (B vs A) |

For every LLM behaviour claim, report trace ids and inspect at least one full trace directly.

## Increments

1. **Linker and export fields (C1):** build the linker and add question status and dates to the export, then run it on the previous 5 chats (data is in `private/xconv/`). Retires the unknown "does a typed judgment find real cross-chat relations?".
2. **Scale corpus (C2):** select 25 more chats by archive search, then import and extract them.
3. **Reference key (C3).**
4. **Comparison and decision (C4, C5).**

## Loop Bounds

- **No-progress stop:** 3 attempts on the same reproduced blocker with no new evidence.
- **Finite bound:** 6 increments in total.
- **Strategy revalidation:** after 3 increments, about 4 hours, or an outcome reset. Report outcome, enabling and process progress, and recommend retain, replace or clear.
- **Linker gate:** if the linker's hand check in increment 1 finds fewer than 6 of 10 cross-chat links correct after 2 prompt revisions, stop. Report it as a finding (typed linking is not reliable enough); do not scale up a broken linker.
- **Exact blocked resume event:** named per blocker in Current State.

## Non-Gating Next Actions

- Brian's ChatGPT data export, for voice-mode messages (inquiry-graph issue #3).
- onto-canon6 #505 (packaging): not needed here.
- Scaling to the whole archive, only after C5 says continue.
- Hosted CI (#2).

## Current State

- **Demonstrated:** the previous goal's C1–C6 (`evaluation/cross_conversation/results.md`).
- **C1 (2026-09-29):** the linker (`src/inquiry_graph/linker.py`, v`linker-1.2.0`) and tests (`tests/test_linker.py`) are in place.
  - **Run on the previous 5 chats:** 146 Brian positions and 180 recalled cross-chat pairs. After judging: 146 unrelated, 15 extends, 14 agrees, 3 evolves, 2 pulls_against. Judge cost $0.032. Traces: `inquiry-graph/xconv-linker/linker5/judge-000`…`011`.
  - **Hand checks, per prompt round:**
    - v1.0: about 5/12 correct (below the gate).
    - v1.1: 7–9/12 correct (all 6 pulls_against and evolves right). A strict count was just under the gate.
    - v1.2: 10/11 correct, 9/11 strict. The only clear error is a thematic stretch between Peircean categories and the question of whether inference types are exhaustive. **Gate passed.**
- **C2 (2026-09-29):** 30 chats are imported and all 30 extracted graphs validate. The corpus
  records 4,229,221 visible characters, per-chat dates and sizes, and extraction costs in
  `private/xconv/scale_run/corpus.json`.
- **Current increment:** 3 (independent reference key).
- **C3 state:** 8 of 30 per-chat key files exist in the original OpenRouter run; the cross-key,
  route answers and grades are absent. OpenRouter rejected the next key request because the
  account could afford only 29,639 tokens. A separate Codex CLI subscription probe on one chat
  returned 20 positions with all 20 quotes matching Brian-authored messages; the client reported
  `subscription_included` and `$0`, but no token counts. This proves one-chat route compatibility,
  not full-run capacity. Keep any Codex campaign separate and regenerate all 30 keys consistently.
- **Blocker:** the original OpenRouter route cannot continue at the current balance; capacity for
  the full Codex campaign is not established.
- **Resume event:** prepare a separate Codex-backed campaign, then monitor Codex usage while
  generating the full reference key and running the comparison stages.

## Evaluator-Facing Objective

```text
Goal: build a relation-typed cross-chat linker for Brian's extracted positions and test, on 30+ real ChatGPT chats (too large to read in one call), whether positions+links beat archive-search-then-read and positions-only at answering cross-chat questions about his positions, conflicts, changes and recurring open questions. Read and follow docs/goals/cross-conversation-linker.md in BrianMills2718/inquiry-graph.
Profile: continuous-light.
Canonical example: 30 chats (the previous 5 + 25 by archive search) -> AI answers "where have my views changed or pulled against each other, and what do I keep leaving open?" with Brian-attributed positions + chat title + date + verbatim quote, using at least one typed cross-chat link, plus blind-graded scores for routes A (search-then-read), B (positions+links+status+dates) and C (positions only).
Forbidden substitutes: seed graph or hand-authored positions/links/keys; assistant proposals counted as Brian's; mocked LLMs; embedding-only links without typed judgment; counts without listed members and quotes; fewer than 20 chats presented as scale; keys made by the system under test; unmeasured "doesn't fit" claims.
Boundaries: write only to inquiry-graph via PRs merged when checks pass, and gitignored private/; ChatGPT bridge read/search only; onto-canon6 and epistemic-warrant read-only; never commit transcripts or quote-bearing outputs; no deploy or publish.
Done when: C1-C5 in the goal doc are reported with evidence: linker tests + 10-link hand check + trace ids; 30+ chats validated with dates, costs and measured combined size; quote-verified independent key; per-question A/B/C table with category means, costs and 4+ hand-checked grades; results.md plus an inquiry-graph #38 comment stating continue/replace/shelve and whether links add value (B vs C) and beat search (B vs A).
Stop as blocked only after 3 attempts on the same reproduced blocker produce no new evidence or safe next action; report the blocker, owner and resume event. If the linker scores under 6/10 on its hand check after 2 prompt revisions, stop and report that as the finding instead of scaling.
Do not gate on: Brian reading anything, the ChatGPT data export, onto-canon6 changes, hosted CI, or scaling beyond 50 chats.
Revalidate after: 3 increments, ~4 hours, or an outcome reset. Report outcome/enabling/process progress and recommend retain, replace or clear. If misaligned, stop and return control; do not call misalignment a technical blocker.
```
