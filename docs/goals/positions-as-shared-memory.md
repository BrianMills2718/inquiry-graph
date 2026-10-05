# Goal: Brian's recorded positions as working memory for agents

Status: active (set 2026-10-05). Authority for this goal; update the "Current state" section, not a separate diary.

## Goal

**Mission:** make Brian's verified positions (19,587 quoted positions and questions from his chats, `tools/ask_positions.py`) do real work outside this repository, in three places he approved on 2026-10-05 ("all those"):

- **A. Check before asking or deciding.** A shared skill any agent (Claude Code and Codex) uses to ask "what has Brian already said about X?" and get verified quotes back, so agents stop asking him to restate and plans cite his own reasons.
- **B. Vision register.** Step 3 of the AES vision-coverage plan: vision-related positions and open questions become rows in `vision/wiki/synthesis/hypotheses-and-evidence-register.md`, each tied to its conversation.
- **C. Meeting transcripts.** An importer that turns a multi-person meeting transcript (the AI Astronauts Zoom transcripts) into an inquiry graph with each person's positions attributed to that person.

Why: the 30-chat evaluation showed the graph is not better general retrieval than search-then-read; its distinct value is attributed, verbatim-checked positions and how they change. That value is unproven until something outside this repository consumes it. This goal supplies the first consumers.

**Execution profile:** continuous-coordinated

One coordinator; writes in `inquiry-graph`, the shared skills source, `plan-code-wiki`, and `vision`.

**Stage and investment boundary:** PoC per lane: one authentic run each. Model spend uses the existing OpenRouter route; no full re-extraction of the archive.

**Canonical examples:**

- A: replay the plan-drafting session of `plan-code-wiki` (`make lifecycle-run`, real Claude Code) with the skill installed; the draft plan's rationale cites at least one verbatim Brian quote with its chat id, returned by the skill and verified by its code check, and the quote is relevant to a choice the draft makes. The same skill invoked from a real Codex session returns verified quotes for one question.
- B: open the register; vision-related rows each show a Brian position or open question, a verbatim quote, the conversation it came from, and a link into the topic atlas; a code check confirms every quote is verbatim in a message Brian sent.
- C: import `ai-astronauts` `brian/raw/2026-10-02-zoom-sd-ai-astronaut-transcript.md` (279 turns, four speakers); extraction yields stance and question events attributed to each speaker (`participant:<name>`), every quote verbatim at its turn, and an `ask_positions`-style query restricted to one person returns only that person's quotes.

**Forbidden substitutes:** hand-written or paraphrased positions; quotes not passed through the verbatim check; a skill that exists but no recorded consumer run used it; a plan whose cited quote the agent typed itself; a transcript test that uses a synthetic or edited transcript instead of the real one; register rows without a conversation id; per-person output where any quote belongs to another speaker.

**Repository / working scope:** this repository's `AGENTS.md`; the shared skills source `~/projects/.agents/skills/` (client copies derived; Claude–Codex parity required); `~/code/plan-code-wiki`; `~/code/vision`; `agentic-engineering-system-canonical` only to update the vision-coverage plan page/README on its shaping branch.

## Boundaries

- In scope: a `positions` skill wrapping `ask_positions.py` (question in, verified quotes out, refusal when evidence is weak); one replay of the plan-code-wiki planning session using it; vision register rows from existing extraction output; a Zoom-transcript normalizer plus extraction on the real Oct 2 transcript.
- Out of scope: re-running the archive extraction; ontology expansion (repo stop rule); new graph tooling (vision plan "Not building"); human-facing UI polish; better-than-lexical retrieval (record as next action if it blocks A).
- Writes allowed: new files and focused edits in the named repositories, through branches and PRs merged after each repo's local checks.
- Read-only or externally owned: the untracked `tools/run_topic_digests.py` and `uv.lock` in this repository's main checkout (another lane); `Inside-Success/*` repositories; onto-canon6.
- Privacy: quote-bearing data stays in gitignored `private/` or private repositories; meeting-transcript positions (Inside Success content) never go onto a public surface; anything served goes behind the existing sign-in.
- Irreversible actions requiring authorization: none expected. No messages to the AI Astronauts group or anyone else.

## Acceptance Checks

| ID | Criterion | Evidence to report |
| --- | --- | --- |
| A1 | Skill returns verified quotes for a real question and refuses when evidence is weak | Command output for one answered question (claims with chat ids, verify step passed) and one out-of-scope question (refusal) |
| A2 | Authentic Claude consumer | `plan-code-wiki` lifecycle replay trace: the skill call, its output, and the draft plan line citing the returned quote |
| A3 | Codex parity | A real Codex session invoking the skill, with its output; skill present in Codex's skill listing |
| B1 | Register rows from real positions | Row count added; code check output: every quote verbatim, every row has a conversation id and atlas link |
| B2 | Plan updated | Vision-coverage step 3 marked done with counts on its shaping branch |
| C1 | Importer on the real transcript | Normalizer output: 279 turns, 4 speakers, offsets preserved |
| C2 | Attributed extraction | Events per speaker; verbatim check passes; one per-person query returns only that person's quotes |
| G1 | Repos clean and merged | Each PR merged after local checks with counts and exit codes; no uncommitted residue from this goal |

For every LLM behavior claim (A1, A2, A3, C2), report the exact trace or log ids and inspect the full trace, not a summary.

## Increments

1. A: skill wrapper over `ask_positions.py` with refusal on weak evidence (A1).
2. A: lifecycle replay with the skill (A2); Codex invocation (A3).
3. B: register rows from vision-related atlas clusters with the verbatim check (B1, B2).
4. C: Zoom normalizer on the real transcript (C1); extraction and per-person query (C2).

If lexical retrieval makes A2's quote irrelevant, record that as the finding (it is the decision the repo needs) and add better retrieval as a next action; do not hand-pick a quote.

## Profile Additions

- One progress authority: this document's "Current state" section.
- Lanes (owner: the goal's coordinator session for all three; no worker sessions unless spawned explicitly):
  - A positions skill: next event "A1 command output recorded"; deadline 1 working session.
  - B vision register: next event "B1 check output recorded"; deadline 1 working session after A1.
  - C transcript importer: next event "C1 normalizer output recorded"; deadline 1 working session after B1.
  - On a missed event: one fresh claim/runtime probe, then recover the lane in place or record a blocker with its resume event.
- Authority transfer/reversion: the block below; claim state never transfers authority.
- Pinned dependencies: inquiry-graph `e6732d8`; plan-code-wiki `297407d`; AES vision-coverage on `shaping/vision-coverage`.
- Dependency-sensitive stop points: if another session holds a live claim on `vision/wiki/synthesis/` or this repository's `tools/`, message it before writing there.

<!-- goal-authority-reversion:v1:start -->
```yaml
schema_version: "1.1"
owner: "coordinator:positions-goal"
receiver: "coordinator:recovery"
transfer:
  trigger: "owner_runtime_absent_after_missed_event_and_probe"
reporting:
  event: "lane acceptance-check output recorded in Current state"
  deadline: "PT8H"
  one_probe_transition: "recover"
non_gating_utility_review:
  broad_cycle_limit: 2
  on_limit: "compare_direct_route_and_merge_or_defer"
  later_review: "exact_counterexample_only_unless_scope_expands"
```
<!-- goal-authority-reversion:v1:end -->

## Stops

- No progress: three attempts on the same reproduced blocker with no new evidence or safe next action → record the blocker, owner and resume event, and stop that lane (continue the others).
- Strategic revalidation: after three increments or roughly four hours, report outcome versus enabling/process progress and whether to retain, replace, or clear this goal.

## Non-Gating Next Actions

- Brian reads the register rows and the per-person meeting positions.
- Semantic (non-lexical) retrieval for `ask_positions` if A2 shows lexical retrieval misses.
- Importing the Sep 30 and Oct 1 meetings once their transcripts are captured.

## Current state

- 2026-10-05: goal set; no lane started.
