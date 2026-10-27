---
description: Next plan for Inquiry Graph — make the private positions pipeline run green again (nightly topic naming, the extract-or-run restart loop, the ChatGPT export watcher) so agents' brian-positions answers stay current
status: proposed
---

# Next plan: keep the positions memory current

Planning package: docs/planning/planning-package.json

Answers open questions: Q5, Q6, Q12

Status: proposed on 2026-10-27 by the planning-package agent. It is ordinary agent-owned repair work
(open questions Q5, Q6 and Q12 are all `owner: agent`); in `~/code2` a change this size needs no
adopted design plan, the pull request is the record (`~/code2/AGENTS.md`). If the work grows beyond
the three steps below, adopt it first under `bounded-design`.

## Why this is next

The one capability of this repository that has a consumer outside it is the positions memory:
the `brian-positions` skill runs `tools/brian_positions.py` over Brian's verbatim positions and,
with `--sessions`, over what he typed in coding sessions (open question R1). That memory is only as
current as the private pipeline that feeds it, and on 2026-10-27 that pipeline is red in three
places:

1. `inquiry-graph-nightly.service` has failed since 2026-10-26 08:35. Session import worked (1,133
   imported) and both map builds exited 0, but 149 of 867 topic names failed with
   `CODEX_CLI_ERROR` and the naming step alone took 18,690 s (5.2 h). More than 20 failed names
   fails the step (`tools/nightly_sessions.py:86`). Issues #227 and #229.
2. `extract-or-run.service` restarts every few seconds: `tools/extract_queue.py` refuses a run with
   `--budget 25` and no `--contract` (`tools/extract_queue.py:71`), and the unit predates that rule.
   Issue #191, open since 2026-10-07.
3. The ChatGPT export watcher scrapes Gmail through a robot browser that is often down; it missed a
   ready export for 8 days and the link went stale (issue #205). New chats stop reaching the
   positions memory without anyone being told.

The other open questions are either Brian's priority calls (Q10, Q11, Q13) or small documentation
repairs (Q1 to Q4, Q7, Q8) that any session can do; none blocks this plan.

## Steps

1. **Topic naming.** Reproduce one failing `name_topics.py` call with the full Codex CLI stderr
   (the concern keeps only its first line). Fix the cause where it originates (llm_client's Codex
   transport, or the naming call's working directory and sandbox options,
   `tools/name_topics.py:31`-`:33`). Then find out why 867 topics needed names on one night although names
   are carried over from the previous build when a topic barely changed (`tools/name_topics.py:51`,
   threshold 0.5); if the carry-over is not matching, fix it so a nightly run names only new topics. Record per-call traces through llm_client as today (`trace_id="inquiry-graph/name-topics"`).
2. **extract-or-run.** Read `private/extract_full_20261003/or_run` to learn whether that run is
   finished. If finished, disable the unit and say so on #191; if not, write its capture contract
   (`tools/capture_contract.py`) and add `--contract` to the unit.
3. **Export watcher.** Replace the browser scrape with a Gmail read through an API or connector that
   does not depend on the robot browser, and alert (keyed concern) when the check itself cannot run.

## Done when

- Two consecutive nightly runs end with `systemctl --user is-failed inquiry-graph-nightly.service`
  printing `inactive` (not `failed`), each log under `private/logs/` showing fewer than 20 failed
  names, and a sample of five named topics read against their records (names match the quotes).
- `systemctl --user status extract-or-run.service` shows the unit disabled or running under a
  contract, not `auto-restart`.
- The watcher's log shows a successful check that did not use the robot browser.
- Issues #227, #229, #191 and #205 are closed with that evidence, and the planning package is
  rebuilt at the merge revision.

## Domain concepts it relies on

`coding-session`, `launch-kind`, `reply-fields`, `resume-digest`, `brian-position`, `topic-map`,
`topic-name`, `extraction`, `quarantine`, `conversation` (see [DOMAIN.md](DOMAIN.md)). All are
implemented; the plan changes how they are produced on schedule, not what they are.

## Not in scope

No schema change, no new evaluation, and no change to what the map shows. The five-condition reader
benchmark (#225) is Brian's call (Q11).
