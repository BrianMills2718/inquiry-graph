---
schema_version: "1.0"
artifact_type: design_plan
id: session-launch-kind
plan_id: session-launch-kind
status: proposed
planning_path: requested
method_conformance_receipt: docs/plans/session-launch-kind.receipt.json
conflict_surfaces:
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "src/inquiry_graph/coding_session.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "tools/brian_positions.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "tests/test_coding_session.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "docs/model/trace.yaml", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "wiki/index.md", access: write}
trace_review_criteria:
  - criterion_id: outcome
    expected_outcome: pass
goal:
  outcome: "Prompts typed by a program in headless Claude Code/Codex runs are no longer attributed to Brian, and tools/brian_positions.py --sessions returns what Brian typed in coding sessions alongside his chat positions"
  canonical_example: "Before: 160 copies of 'These records come from AI coding agents feedback...' (a codex exec grading prompt) counted as Brian's messages and swamped session search; after re-import, 443 headless sessions carry an 'Automated prompt' participant and a --sessions query for 'periodic AI review of my commits should read the session transcripts' returns his 2026-10-13 prompts from session e86f4df8."
  forbidden_substitutes: "claiming success from a check's last line or exit status alone; a change outside the listed files; a commit without the saved check output"
  boundaries: "only these files: src/inquiry_graph/coding_session.py, tools/brian_positions.py, tests/test_coding_session.py, docs/model/trace.yaml, wiki/index.md; no irreversible action and no spend; Brian's request as quoted is the scope"
  done_when: "tests/test_coding_session.py::test_prompts_from_headless_launches_are_not_brians asserts, for 7 launch cases, that sdk-cli/sdk-py/codex_exec/Codex-subagent prompts carry participant:automation and cli/no-entrypoint/codex-tui prompts carry participant:brian; ::test_position_search_reads_only_brians_typed_session_prompts asserts session_records returns the typed prompt once (same session imported twice) and drops the headless prompt and the one-word reply; both fail on the parent for the headless cases; ::test_claude_record_keeps_typed_text_turns_and_work_only and ::test_codex_record still pass, showing interactive records parse as before; a live --sessions query over the re-imported private sessions returns his session prompts with no automated prompt. The check's full output on the parent commit and on the change commit is committed as docs/plans/session-launch-kind.check.txt, and the commit is tagged [Goal session-launch-kind] with an Asked: line quoting the request. python3 \"$SESSION_PLUGIN_ROOT/scripts/durable_docs_check.py\" --repo . --plan docs/plans/session-launch-kind.md --range d2690113ddcd64d6442c23c5c14840b80895943e..HEAD exits 0 and its output is in the same file."
  do_not_gate_on: "Brian's review of the plan page; work outside the listed files"
---

# Label headless-session prompts as automated; search Brian's session prompts

## When a run fails or surprises us

This procedure is separate from the anticipated failure named in the disproof
under Success and disproof: it applies to any run that fails or surprises us.
Preserve the failed run itself: keep its complete output (command, every
line, exit status) and its execution trace id, never overwritten by a rerun.
Before selecting a fix,
read the complete inputs, prompts, tool arguments/results, intermediate stages
and final output, including the full check command/output and the changed files.
Cite the observed divergence and classify evidence absent, returned but unused
or contradicted, invalid expectation, or unresolved. An unresolved diagnosis
cannot authorize a causal repair; it permits only further investigation. Bind the targeted repair to a new
traced verification run; retain the failed original. Review every failing or
surprising item and a sample of passes. A complete review is distinct from a
passing run. Criterion `outcome` covers the entire requested success check.

## Actor and result

**Actor:** Brian, who asked for this change.

**Request (verbatim):** Brian 2026-10-13 "i approve." (the recommended next step: a committed session search that filters automated prompts)

**Desired result:** Prompts typed by a program in headless Claude Code/Codex runs are no longer attributed to Brian, and tools/brian_positions.py --sessions returns what Brian typed in coding sessions alongside his chat positions.

**Stable example:** Before: 160 copies of 'These records come from AI coding agents feedback...' (a codex exec grading prompt) counted as Brian's messages and swamped session search; after re-import, 443 headless sessions carry an 'Automated prompt' participant and a --sessions query for 'periodic AI review of my commits should read the session transcripts' returns his 2026-10-13 prompts from session e86f4df8.

## Authority and non-goals

**Authority:** Brian asked for this change in his own repository; one agent makes it.

**Non-goals:** nothing outside the files listed under Vertical and reset. No irreversible action and no spend.

## Requirements

| Id | Requirement | Source | Check | Status |
| --- | --- | --- | --- | --- |
| R1 | Prompts typed by a program in headless Claude Code/Codex runs are no longer attributed to Brian, and tools/brian_positions.py --sessions returns what Brian typed in coding sessions alongside his chat positions. | asked: Brian 2026-10-13 "i approve." (the recommended next step: a committed session search that filters automated prompts) | the success check under Success and disproof, its output saved as `docs/plans/session-launch-kind.check.txt` | planned, not yet run |
| R2 | No model is called by this change, so llm_central is false | stated with the request | git diff shows no LLM client import or call | planned, not yet run |

Requirements the change's own claims imply are listed above as R2 onward.

## Durable documents

This repository declares durable documents (`durable_documents` in `.agentic/repo.yaml`); its declared roles are `goal`, `requirements`, `system_model`, `decisions`, `plans`. Each role named below is one of them (checked by quick-adopt).

Durable documents: system_model#RULE-SESSION-FIELDS

At completion, `python3 "$SESSION_PLUGIN_ROOT/scripts/durable_docs_check.py" --repo . --plan docs/plans/session-launch-kind.md --range d2690113ddcd64d6442c23c5c14840b80895943e..HEAD` must exit 0; its full output is appended to `docs/plans/session-launch-kind.check.txt` (the durable-documents check, Plan #61; `durable_docs_check.py` ships in the Company Planning plugin).

## Success and disproof

**Success evidence:** tests/test_coding_session.py::test_prompts_from_headless_launches_are_not_brians asserts, for 7 launch cases, that sdk-cli/sdk-py/codex_exec/Codex-subagent prompts carry participant:automation and cli/no-entrypoint/codex-tui prompts carry participant:brian; ::test_position_search_reads_only_brians_typed_session_prompts asserts session_records returns the typed prompt once (same session imported twice) and drops the headless prompt and the one-word reply; both fail on the parent for the headless cases; ::test_claude_record_keeps_typed_text_turns_and_work_only and ::test_codex_record still pass, showing interactive records parse as before; a live --sessions query over the re-imported private sessions returns his session prompts with no automated prompt.

**Trace review:** two runs of the success check above are judged from their full output: one on the parent commit before the change (the disproof run: it must show the defect or the check failing, which proves the check can fail) and one on the commit that makes the change (the success run); no model, agent or LLM pipeline runs under this plan. Where the trace lives: the check's complete output, with the exact command and its exit status, is saved as `docs/plans/session-launch-kind.check.txt` and committed with the change. What must be seen in it beyond the final result: the command ran against the files listed under Vertical and reset at that commit, each check or test it reports appears by name with its result and none is skipped, and the exit status matches; for each model element listed under System model, the output shows what that line says. Both runs are saved in that one file, each headed by its commit: the disproof condition is judged from both (it holds if the success run still shows the defect, or if the before run already passes, meaning the check cannot detect it), and success from the success run.

**Disproof:** The headless cases already pass on the parent (the test cannot detect the defect), an interactive cli/codex-tui session is labelled automated, or the live query returns a headless grading prompt as Brian's words.

## System model

**System model:** `docs/model/ARCHITECTURE.md`, a file in this repository describing this repository only (not a shared model). Reachable from the documentation entry point `wiki/index.md`, which links `docs/model/ARCHITECTURE.md`.

**Model elements this change adds, changes or relies on, and what the saved check output must show of each:**

- PROC-IMPORT-SESSION (docs/model/trace.yaml): a headless record's prompts carry participant:automation
- RULE-SESSION-FIELDS (docs/model/trace.yaml): statement names headless launches; checks list the two new tests

**Views, freshness and reconciliation:** the applicable view is the requirement-to-verification link in the Requirements table (each requirement and the check that shows it, the check being source-linked by its command); no other view applies because the change adds, changes or relies on no entity, process, record, event or view beyond the elements listed above. Freshness: the model's drift test (`tests/test_validation.py`, `tests/test_pipeline.py`, `tests/test_ask_positions.py`) runs inside the success check and its output is in the saved check file. If an element above is added, removed or renamed, the model, its view coverage and the saved check output are reconciled in the same commit, and otherwise the model needs no update because the elements keep their meaning.

## Capability reuse

Checked against the capability catalogue in agentic-capability-architecture-canonical (`reuse_candidates.yml` and `capability_registry.yml`):

- No catalogue entry fits, because this extends the existing brian-positions search (tools/brian_positions.py, skill brian-positions) with one more source instead of adding a search tool
- What the work needs that no entry provides: edits to this repository's own files (`src/inquiry_graph/coding_session.py`, `tools/brian_positions.py`, `tests/test_coding_session.py`, `docs/model/trace.yaml`, `wiki/index.md`); catalogue entries are cross-project capabilities, and none edits a repository's own source.

## Uncertainties

Material uncertainties. This one is the complete set; it is material because a file outside the list would
make the change exceed this plan's scope.

| Material uncertainty | Owner or resolving evidence |
| --- | --- |
| Whether the change needs files beyond the list below; if so it is out of scope for this plan | Resolved before editing: git diff --stat: 5 files (coding_session.py, brian_positions.py, test_coding_session.py, docs/model/trace.yaml, wiki/index.md) |

## Vertical and reset

One vertical over these files (and the saved check output, `docs/plans/session-launch-kind.check.txt`):

- `src/inquiry_graph/coding_session.py`
- `tools/brian_positions.py`
- `tests/test_coding_session.py`
- `docs/model/trace.yaml`
- `wiki/index.md`

The vertical delivers: Prompts typed by a program in headless Claude Code/Codex runs are no longer attributed to Brian, and tools/brian_positions.py --sessions returns what Brian typed in coding sessions alongside his chat positions. It is done when this holds: tests/test_coding_session.py::test_prompts_from_headless_launches_are_not_brians asserts, for 7 launch cases, that sdk-cli/sdk-py/codex_exec/Codex-subagent prompts carry participant:automation and cli/no-entrypoint/codex-tui prompts carry participant:brian; ::test_position_search_reads_only_brians_typed_session_prompts asserts session_records returns the typed prompt once (same session imported twice) and drops the headless prompt and the one-word reply; both fail on the parent for the headless cases; ::test_claude_record_keeps_typed_text_turns_and_work_only and ::test_codex_record still pass, showing interactive records parse as before; a live --sessions query over the re-imported private sessions returns his session prompts with no automated prompt.

Make the change, run the success check before and after it, commit. Reset: `git revert` of the commit. Not pursued: anything outside these files. This plan adds no coordinated-work ceremony: no work-unit graph, no review or release contract, no claim beyond the repository's own rules.

## Activation facts

Each fact, with its value and why:

- `shared_mechanism`: false -- the change edits only the listed files and adds no contract, algorithm or mechanism other code uses.
- `empirical_comparison_proposed`: false -- no alternatives are compared; the success check verifies the one change.
- `llm_central`: false -- the change makes no model call.
- `irreversible_or_spend_action`: false -- the change is reverted by `git revert` and spends nothing.
- `claims_external_standard`: false -- the work claims no external standard, schema or contract.
- `aes_governed_target`: false -- this repository has no `.aes/target.yaml` (checked by quick-adopt).
- `durable_documents_declared`: true -- derived, `.agentic/repo.yaml` has `durable_documents`; see Durable documents.
