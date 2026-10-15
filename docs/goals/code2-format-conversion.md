# Goal: inquiry-graph follows the code2 repository format

- Profile: continuous-light (one writer, reversible, branch plus PR)
- Approved: Brian, 2026-10-15: "yes" to converting inquiry-graph as the first active repository
- Format rule and checker: `~/code2/workspace/docs/index.md`, `~/code2/code2-template`

## Roadmap (code2 documentation system)

| # | Goal | Depends on | Why here | Status |
| --- | --- | --- | --- | --- |
| 1 | Template plus `code2check` (code2-template) | none | everything else is made from it | done 2026-10-15 |
| 2 | Greenfield trial (hooks-autoapply) | 1 | shows the loop works on new code | done 2026-10-15 |
| 3 | Convert one active repository: inquiry-graph (this goal) | 1, 2 | shows the format fits real, existing code | active |
| 4 | Other repositories convert when next changed | 3 | decision 0002 in code2-workspace | open |

## Mission and canonical example

Brian, 2026-10-15: "start refactoring an active repo into that format". Done looks like this:

`python3 ~/code2/workspace/scripts/repo_format.py ~/code2/inquiry-graph` prints
`RESULT repo-format compliant=1 of=1 exit=0`, and `make check` in inquiry-graph exits 0 with
`RESULT trace findings=0`, `RESULT sources ... missing=0`, `Contracts: N kept, 0 broken`, and the
existing test suite passing. The OpenSpec specs describe what inquiry-graph actually does today
(at least the extraction, linking and rendering paths a reader would ask about), each requirement has
an `Implements:` line in the module that does it, and each scenario a real test.

Forbidden substitutes: placeholder specs (`core` starter, "Reports its version") or specs that
describe nothing the code does; tests that only assert `True`; an architecture diagram with one box
or arrows that allow everything; deleting, skipping or weakening existing tests to get green; marking
tests for new behavior `existing=True`; `Source:` lines that claim Brian's words without a quote.

## Boundaries

- In scope: inquiry-graph only, on a branch in `worktrees/`, merged by PR after `make check` exits 0.
- Existing documents move into the format (`docs/index.md` reading order; older pages linked or
  archived in place), never deleted.
- Out of scope: behavior changes, the nightly jobs' schedules, data under `private/`.
- `code2check` bugs found here are fixed in code2-template (test first), not worked around locally.
- New requirements an agent writes are `Source: inferred by agent (<basis>)`; they appear on the
  oversight page's Requirements tab for Brian.

## Increments

1. Add the format's files (copier `--trust` update or by hand from the template), `Makefile`,
   `lefthook.yml`, `[tool.code2check] source = ["src"]`; `make check` runs.
2. Diagram the real modules in `docs/architecture/model.c4`; `code2check arch gen`; `lint-imports`
   passes or the diagram is corrected to the true imports.
3. Write specs for existing behavior, one capability at a time; mark existing tests
   `req(..., existing=True)` and add `Implements:` lines.
4. `docs/index.md` and arc42 link the existing design, decision and goal documents.

## Acceptance checks and traces

Report, from the final run on the merged commit: the `repo_format.py` RESULT line, the full
`make check` output's RESULT lines and pytest summary with exit status, the PR URL and merge commit.
Read a sample of `Implements:` lines and spec scenarios against the code they name.

## Stops

- No progress after three attempts on the same reproduced blocker: report it, the owner and the
  resume event.
- Revalidate after three increments or about four hours: report outcome versus process progress.
- Not gating: Brian reviewing the inferred requirements; converting any other repository.
