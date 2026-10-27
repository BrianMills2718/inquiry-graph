---
description: Cold review of the inquiry-graph planning package by the planning-compliance-reviewer subagent, three rounds, final verdict pass at 8fe79ca
---

# Cold review

Three rounds were run by the planning-compliance-reviewer (run through `claude -p` with read-only tools).

| Round | Revision read | Verdict | Blocking findings |
| --- | --- | --- | --- |
| 1 | 4a8bba0 | revise | 7: Q9 wrong about moves; Q6 and plan step 2 missed `finish_pipeline.sh` and the existing capture contract; no question about the live checkout lagging main; Q7, Q2, Q3, Q4 marked open although answered; FitReview, episode and frame profiles and the capture contract missing from the system model; capture contract missing from the domain graph and `relies_on`; context view hid the pipeline's network dependencies. All fixed in dcae8c7. |
| 2 | dcae8c7 | revise | 1: Q14 and plan step 0 claimed a plain fast-forward works, but the live checkout's untracked `uv.lock` differs from the tracked one, so git refuses it. Fixed in 8fe79ca with notes N1 to N3 (other environments, line 15 alone, waits-for edge). |
| 3 | 8fe79ca | pass | none |

The report of the last round follows unchanged. Its note N4 (this file said "pending") is fixed by this file; N5, N6 and N7 remain notes.

## Round 3 report: inquiry-graph planning package

**Verdict: pass.** The one blocking finding from round 2 (B1) is fixed, and the claim the fix rests on is true in the live checkout. N1, N2 and N3 are also fixed. N4 to N6 remain as notes. I found no new blocking finding.

I read subject revision 8fe79ca. HEAD fc39718 differs from it only in `planning-package.json` and the page's `data.js`. I edited nothing and read nothing under `private/`.

## 1. Validator

I ran `validate_planning_package.py --repo . docs/planning/planning-package.json`. It exited **1**.

- **Parts:** 7 of 8 pass.
  - Checks: 8 results, 3 of them with findings.
  - Open questions: 19 (13 open, 6 resolved).
  - Domain model: 37 concepts, 41 relations.
  - Diagrams: 4.
- **Substance checks:** 4 of 5 pass, 0 pending.
  - 59 file citations and 13 other sources resolve.
  - Concepts: 34 implemented, 3 dashed.
  - `relies_on` names 11 concepts.
  - "No typed rules."
- **Freshness:** passes, 0 commits since 8fe79ca.
- **The two failures** are the slots this review fills: the cold-review verdict is still `revise`, and `reviewed_revision` is still `PLACEHOLDER`.

## 2. Checks reproduce

- **Rerun:** `doc_reachability.py .` exited 0 with 103 reachable, 0 unreachable, 103 tracked. That matches the manifest.
- **Unchanged:** this round changed nothing outside `docs/planning/` and the page. So the four counts I reproduced in round 2 still hold.
- **Worktree:** still clean after the run.

## Previous findings

| # | Finding | Status | Evidence |
| --- | --- | --- | --- |
| B1 | Q14 and step 0 claimed a plain fast-forward works | **fixed** | **Live checkout:** HEAD is 8672a4e, `HEAD..origin/main` = 15, `origin/main..HEAD` = 0, and the only status line is `?? uv.lock`. **The two lock files:** the untracked `uv.lock` has 2,559 lines; `origin/main:uv.lock` has 2,745. **The fix:** Q14 and step 0 now state that git refuses the fast-forward. They compare the two files, move the untracked one aside, then pull and sync. The repeated update raises a keyed concern when the fast-forward is refused. Q14 still claims only "argument, no test", and that is accurate. |
| N1 | Other virtual environments | **fixed** | `git diff 8672a4e origin/main -- pyproject.toml` adds `[dependency-groups] dev`, `[tool.uv.sources] code2check` and `[tool.code2check]`, and no runtime dependency. So the claim that `~/.venvs/inquiry-maps` and `~/.venvs/inquiry-or` need no sync holds. New citations: `nightly_sessions.py:29` (MAPS_PY), `finish_pipeline.sh:15` (inquiry-or python) and `SKILL.md:18` (inquiry-maps) all say what they are cited for. `pyproject.toml:17` is `[dependency-groups]`. |
| N2 | Plan step 2 ran the whole finish script | **fixed** | Step 2 and Q6 now pick "line 15 alone" and say why: the whole script renames every topic through Codex and publishes to personal-vps. |
| N3 | Diagram did not show the wait on extract units | **fixed** | The diagram (`system-model.md:66`) now has a dashed edge from finish to the queue: "waits until every extract-* unit stops". The page's `context_diagrams` carries it. |
| N4 | Cold-review record says pending | **not fixed** (note) | `docs/planning/cold-review.md:7` still says "Pending: the first review has not run yet." |
| N5 | Domain kinds of the two profiles | **not fixed** (note) | No change. |
| N6 | Carried notes | **not fixed** (note) | No change. |

## Findings

### Blocking

None.

### Notes

- **N4. Cold-review record** (`docs/planning/cold-review.md:7`, which the page's cold-review tab shows). It still says "Pending: the first review has not run yet." Three reviews have now run. When `cold_review.verdict` and `reviewed_revision` are filled in, record all three rounds there: verdicts, findings and their status.
- **N5. Domain kinds.** `episode-profile` and `frame-profile` are kind `Review`, but they are derived projections. There is also no edge from `episode-profile` to the dashed `strategy-episode`.
- **N6. Carried notes:**
  - The `task` concept says "plus dropped", but `model.py:101` applies `dropped` to questions too.
  - Q8 is phrased as a task.
  - The page's evidence links point to `blob/main/docs/planning/*`, which only exists after the merge.
  - mermaid and marked load from a CDN.
  - The repository is public, so run publish-checker before deploying `/plans/`.
- **N7 (new, minor). Stale count in Q6.** Q6 still says `NRestarts 2537`; round 2 saw 2552. It is a dated observation, so it does not change any conclusion.

## Missing material questions

None found beyond those already in the ledger.

## Page

Checked statically. I did not re-render.

- `data.js` manifest == `planning-package.json`: True.
- Questions == `open-questions.json`: True (19).
- `next_plan` == `next-plan.md`, apart from the frontmatter and links rewritten to `blob/main`. It includes the new step 0 and step 2 text.
- The Q14, Q6 and diagram changes are present.

## Where I was unsure

- **The `[tool.uv.sources]` entry.** It points `code2check` at a git branch. I counted it as "no runtime dependency" because only the dev group uses it. If either job's environment were ever built with dev groups, that would change, but neither is today.
- **N4's weight.** I kept it a note because the manifest's `cold_review` fields are the ones the validator and the page status read. Still, a reader who opens the cold-review tab would see a false "pending". Fix it in the same commit that fills the verdict.

Reviewed revision: 8fe79caccad09601220d5ac713ee76228ace9aa6

Verdict: pass
