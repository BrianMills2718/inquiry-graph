---
schema_version: "1.0"
artifact_type: design_plan
id: coding-sessions
plan_id: coding-sessions
status: proposed
planning_path: requested
method_conformance_receipt: docs/plans/coding-sessions.receipt.json
conflict_surfaces:
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "src/inquiry_graph/coding_session.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "src/inquiry_graph/model.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "src/inquiry_graph/validate.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "src/inquiry_graph/views.py", access: write}
  - {kind: repository_path, repository: "BrianMills2718/inquiry-graph", target: "src/inquiry_graph/cli.py", access: write}
trace_review_criteria:
  - criterion_id: outcome
    expected_outcome: pass
goal:
  outcome: "inquiry-graph import-session turns a Claude Code or Codex session record into a validated graph of goals, tasks, requests and work, and inquiry-graph sessions lists what is open, unknown, closed, shipped and waiting on Brian. This is one more importer and view inside inquiry-graph, used only by inquiry-graph's own CLI; no other repository, hook or skill calls it in this plan (wiring start/where-are-we/work-review to it is a later, separate plan), so it is not a shared mechanism"
  canonical_example: "This session's record e86f4df8 yields 5 open items at the last listing, 1 superseded closure, and 20 items with unknown status."
  forbidden_substitutes: "claiming success from a check's last line or exit status alone; a change outside the listed files; a commit without the saved check output"
  boundaries: "only these files: src/inquiry_graph/coding_session.py, src/inquiry_graph/model.py, src/inquiry_graph/validate.py, src/inquiry_graph/views.py, src/inquiry_graph/cli.py; no irreversible action and no spend; Brian's request as quoted is the scope"
  done_when: "tests/test_coding_session.py asserts: injected/sidechain text is excluded and one assistant message per turn; closure words map to resolved/dropped/superseded with the replacement node; an item absent from the last listing is unknown, not open; Codex records parse; status events on non-question/non-task nodes are still refused. A run over this week's 285 real session records imports all but malformed ones and validates. The check's full output on the parent commit and on the change commit is committed as docs/plans/coding-sessions.check.txt, and the commit is tagged [Goal coding-sessions] with an Asked: line quoting the request. python3 \"$SESSION_PLUGIN_ROOT/scripts/durable_docs_check.py\" --repo . --plan docs/plans/coding-sessions.md --range 34017196115149540ee111e8926b2f48a3e30c01..HEAD exits 0 and its output is in the same file."
  do_not_gate_on: "Brian's review of the plan page; work outside the listed files"
---

# Coding-agent sessions become resumable inquiry graphs

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

**Request (verbatim):** Brian 2026-10-13 "i want somethign similar for my coding agent sessions" and "yes" / "i approve" to building the importer

**Desired result:** inquiry-graph import-session turns a Claude Code or Codex session record into a validated graph of goals, tasks, requests and work, and inquiry-graph sessions lists what is open, unknown, closed, shipped and waiting on Brian. This is one more importer and view inside inquiry-graph, used only by inquiry-graph's own CLI; no other repository, hook or skill calls it in this plan (wiring start/where-are-we/work-review to it is a later, separate plan), so it is not a shared mechanism.

**Stable example:** This session's record e86f4df8 yields 5 open items at the last listing, 1 superseded closure, and 20 items with unknown status.

## Authority and non-goals

**Authority:** Brian asked for this change in his own repository; one agent makes it.

**Non-goals:** nothing outside the files listed under Vertical and reset. No irreversible action and no spend.

## Requirements

| Id | Requirement | Source | Check | Status |
| --- | --- | --- | --- | --- |
| R1 | inquiry-graph import-session turns a Claude Code or Codex session record into a validated graph of goals, tasks, requests and work, and inquiry-graph sessions lists what is open, unknown, closed, shipped and waiting on Brian. This is one more importer and view inside inquiry-graph, used only by inquiry-graph's own CLI; no other repository, hook or skill calls it in this plan (wiring start/where-are-we/work-review to it is a later, separate plan), so it is not a shared mechanism. | asked: Brian 2026-10-13 "i want somethign similar for my coding agent sessions" and "yes" / "i approve" to building the importer | the success check under Success and disproof, its output saved as `docs/plans/coding-sessions.check.txt` | planned, not yet run |

Requirements the change's own claims imply: none beyond R1; the change presents nothing as following a standard, schema or contract.

## Durable documents

This repository declares durable documents (`durable_documents` in `.agentic/repo.yaml`); its declared roles are `goal`, `requirements`, `system_model`, `decisions`, `plans`. Each role named below is one of them (checked by quick-adopt).

Durable documents: requirements#REQ-16, system_model#RULE-SESSION-FIELDS

At completion, `python3 "$SESSION_PLUGIN_ROOT/scripts/durable_docs_check.py" --repo . --plan docs/plans/coding-sessions.md --range 34017196115149540ee111e8926b2f48a3e30c01..HEAD` must exit 0; its full output is appended to `docs/plans/coding-sessions.check.txt` (the durable-documents check, Plan #61; `durable_docs_check.py` ships in the Company Planning plugin).

## Success and disproof

**Success evidence:** tests/test_coding_session.py asserts: injected/sidechain text is excluded and one assistant message per turn; closure words map to resolved/dropped/superseded with the replacement node; an item absent from the last listing is unknown, not open; Codex records parse; status events on non-question/non-task nodes are still refused. A run over this week's 285 real session records imports all but malformed ones and validates.

**Trace review:** two runs of the success check above are judged from their full output: one on the parent commit before the change (the disproof run: it must show the defect or the check failing, which proves the check can fail) and one on the commit that makes the change (the success run); no model, agent or LLM pipeline runs under this plan. Where the trace lives: the check's complete output, with the exact command and its exit status, is saved as `docs/plans/coding-sessions.check.txt` and committed with the change. What must be seen in it beyond the final result: the command ran against the files listed under Vertical and reset at that commit, each check or test it reports appears by name with its result and none is skipped, and the exit status matches; for each model element listed under System model, the output shows what that line says. Both runs are saved in that one file, each headed by its commit: the disproof condition is judged from both (it holds if the success run still shows the defect, or if the before run already passes, meaning the check cannot detect it), and success from the success run.

**Disproof:** An agent-closed item is reported open, a missing item is reported open, a quote is not in its message, or hook/subagent text appears as Brian's or the assistant's words.

## System model

**System model:** `docs/model/ARCHITECTURE.md`, a file in this repository describing this repository only (not a shared model). Reachable from the documentation entry point `wiki/index.md`, which links `docs/model/ARCHITECTURE.md`.

**Model elements this change adds, changes or relies on, and what the saved check output must show of each:**

- ENT-GRAPH gains node kinds task and work and status dropped; check output: validate passes on imported session graphs
- VIEW-SESSION-DIGEST new view; check output: sessions lists open/unknown_status/closed/work/requests_open

**Views, freshness and reconciliation:** the applicable view is the requirement-to-verification link in the Requirements table (each requirement and the check that shows it, the check being source-linked by its command); no other view applies because the change adds, changes or relies on no entity, process, record, event or view beyond the elements listed above. Freshness: the model's drift test (`tests/test_validation.py`, `tests/test_pipeline.py`, `tests/test_ask_positions.py`) runs inside the success check and its output is in the saved check file. If an element above is added, removed or renamed, the model, its view coverage and the saved check output are reconciled in the same commit, and otherwise the model needs no update because the elements keep their meaning.

## Capability reuse

Checked against the capability catalogue in agentic-capability-architecture-canonical (`reuse_candidates.yml` and `capability_registry.yml`):

- No catalogue entry fits, because capability_registry.yml and reuse_candidates.yml have no session, transcript, memory or conversation entry (grep returned nothing); this extends inquiry-graph's own importer family
- What the work needs that no entry provides: edits to this repository's own files (`src/inquiry_graph/coding_session.py`, `src/inquiry_graph/model.py`, `src/inquiry_graph/validate.py`, `src/inquiry_graph/views.py`, `src/inquiry_graph/cli.py`); catalogue entries are cross-project capabilities, and none edits a repository's own source.

## Uncertainties

Material uncertainties. This one is the complete set; it is material because a file outside the list would
make the change exceed this plan's scope.

| Material uncertainty | Owner or resolving evidence |
| --- | --- |
| Whether the change needs files beyond the list below; if so it is out of scope for this plan | Resolved before editing: git status --short in the worktree lists the files: src/inquiry_graph/{coding_session,cli,model,validate,views}.py, tests/test_coding_session.py, schemas/{graph,candidates}.schema.json, docs/{requirements,ontology}.md, docs/model/{trace.yaml,ARCHITECTURE.md}, README.md, wiki/index.md; all inside inquiry-graph |

## Vertical and reset

One vertical over these files (and the saved check output, `docs/plans/coding-sessions.check.txt`):

- `src/inquiry_graph/coding_session.py`
- `src/inquiry_graph/model.py`
- `src/inquiry_graph/validate.py`
- `src/inquiry_graph/views.py`
- `src/inquiry_graph/cli.py`

The vertical delivers: inquiry-graph import-session turns a Claude Code or Codex session record into a validated graph of goals, tasks, requests and work, and inquiry-graph sessions lists what is open, unknown, closed, shipped and waiting on Brian. This is one more importer and view inside inquiry-graph, used only by inquiry-graph's own CLI; no other repository, hook or skill calls it in this plan (wiring start/where-are-we/work-review to it is a later, separate plan), so it is not a shared mechanism. It is done when this holds: tests/test_coding_session.py asserts: injected/sidechain text is excluded and one assistant message per turn; closure words map to resolved/dropped/superseded with the replacement node; an item absent from the last listing is unknown, not open; Codex records parse; status events on non-question/non-task nodes are still refused. A run over this week's 285 real session records imports all but malformed ones and validates.

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
