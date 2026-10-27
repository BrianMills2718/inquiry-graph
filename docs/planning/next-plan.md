---
description: Next plan for Inquiry Graph — make the private positions pipeline run green again (live checkout on main, nightly topic naming, the extract-or-run restart loop, the ChatGPT export watcher) so agents' brian-positions answers stay current
status: proposed
---

# Next plan: keep the positions memory current

Planning package: docs/planning/planning-package.json

Answers open questions: Q5, Q6, Q12, Q14

Status: proposed on 2026-10-27 by the planning-package agent. It is ordinary agent-owned repair work
(open questions Q5, Q6, Q12 and Q14 are all `owner: agent`); in `~/code2` a change this size needs no
adopted design plan, the pull request is the record (`~/code2/AGENTS.md`). If the work grows beyond
the steps below, adopt it first under `bounded-design`.

## Why this is next

The one capability of this repository that has a consumer outside it is the positions memory:
the `brian-positions` skill runs `tools/brian_positions.py` over Brian's verbatim positions and,
with `--sessions`, over what he typed in coding sessions (open question R1). That memory is only as
current as the private pipeline that feeds it. On 2026-10-27 that pipeline is red in three places,
and the code it runs is behind main:

1. `inquiry-graph-nightly.service` has failed since 2026-10-26 08:35. Session import worked (1,133
   imported) and both map builds exited 0, but 149 of 867 topics failed to get a name with
   `CODEX_CLI_ERROR` (555 of 988 on 2026-10-25, 442 of 844 on 2026-10-22), and the naming step alone
   took 18,690 s (5.2 h). More than 20 failed names fails the step (`tools/nightly_sessions.py:86`).
   Issues #227 and #229.
2. `extract-or-run.service` restarts every few seconds (2,537 restarts by 2026-10-27):
   `tools/extract_queue.py` refuses a run with `--budget 25` and no `--contract`
   (`tools/extract_queue.py:71`), and the unit is the older invocation that predates that rule. The
   same queue is already rerun under the contract by `tools/finish_pipeline.sh:15`, which first waits
   for every `extract-*` unit to stop (`tools/finish_pipeline.sh:12`), so the loop also holds that
   pipeline back. Issue #191, open since 2026-10-07.
3. The ChatGPT export watcher scrapes Gmail through a robot browser that is often down; it missed a
   ready export for 8 days and the link went stale (issue #205). New chats stop reaching the
   positions memory without anyone being told.
4. Every job above, and the `brian-positions` skill, runs from `~/code/inquiry-graph`, a symlink to
   the main checkout, which sat at 8672a4e (2026-10-15), 15 commits behind `origin/main`, with its own
   `.venv` (`tools/systemd/inquiry-graph-nightly.service:6`-`:7`). Fixes merged to main do not reach
   the jobs until that checkout moves (Q14).

The other open questions are either Brian's priority calls (Q9, Q10, Q11, Q13) or small
documentation repairs (Q1 to Q4, Q8) that any session can do; none blocks this plan.

## Steps

0. **Live checkout.** `~/code2/inquiry-graph` has nothing of its own (`rev-list origin/main..HEAD`
   is 0) except an untracked `uv.lock` that differs from the one `origin/main` tracks since 8b063a0,
   so git refuses a fast-forward. Compare the two files, move the untracked one aside (not delete),
   then `git pull --ff-only` and `uv sync`. Then make it repeatable: after each merge to main the
   same two commands run, from `ship`'s post-merge step or at the start of the nightly unit, and a
   refused fast-forward raises a keyed concern instead of failing quietly. The jobs' other
   environments (`~/.venvs/inquiry-maps`, `~/.venvs/inquiry-or`) need no sync for these 15 commits:
   the only `pyproject.toml` change adds a dev dependency group. Do this first and again after each
   later step merges.
1. **Topic naming.** Reproduce one failing `name_topics.py` call with the full Codex CLI stderr
   (the concern keeps only its first line). Fix the cause where it originates (llm_client's Codex
   transport, or the naming call's working directory and sandbox options,
   `tools/name_topics.py:31`-`:33`). Failures compound: a failed topic is never written to the names
   file (`tools/name_topics.py:79`-`:87`), the nightly run deletes that file before naming
   (`tools/nightly_sessions.py:81`), and only written names carry over (`tools/name_topics.py:51`),
   so a topic that failed once is retried every night. Log the carried count in the nightly log so a
   run shows how many calls it made. Record per-call traces through llm_client as today
   (`trace_id="inquiry-graph/name-topics"`).
2. **extract-or-run.** Disable the unit (`systemctl --user disable --now extract-or-run.service`): it
   is the pre-contract invocation of a queue that `tools/finish_pipeline.sh:15` already reruns under
   the existing contract `docs/capture_contracts/extraction-position-memory.json`. Read the queue's
   output folder; if anything is unfinished, run line 15 of `finish_pipeline.sh` alone (the whole
   script also renames every topic through the failing Codex route and publishes the map to
   personal-vps). Say which on #191.
3. **Export watcher.** Replace the browser scrape with a Gmail read through an API or connector that
   does not depend on the robot browser, and alert (keyed concern) when the check itself cannot run.

## Done when

- `git -C ~/code2/inquiry-graph rev-list --count HEAD..origin/main` prints `0` after each merge of
  this plan, and the post-merge update is written down where it runs.
- Two consecutive nightly runs end with `systemctl --user is-failed inquiry-graph-nightly.service`
  printing `inactive` (not `failed`), each log under `private/logs/` showing fewer than 20 failed
  names, and a sample of five named topics read against their records (names match the quotes).
- `systemctl --user status extract-or-run.service` shows the unit disabled, not `auto-restart`.
- The watcher's log shows a successful check that did not use the robot browser.
- Issues #227, #229, #191 and #205 are closed with that evidence, and the planning package is
  rebuilt at the merge revision.

## Domain concepts it relies on

`coding-session`, `launch-kind`, `reply-fields`, `resume-digest`, `brian-position`, `topic-map`,
`topic-name`, `extraction`, `capture-contract`, `quarantine`, `conversation` (see
[DOMAIN.md](DOMAIN.md)). All are implemented; the plan changes how they are produced on schedule,
not what they are.

## Not in scope

No schema change, no new evaluation, and no change to what the map shows. The five-condition reader
benchmark (#225) is Brian's call (Q11); the moves backfill is Brian's call (Q9).
