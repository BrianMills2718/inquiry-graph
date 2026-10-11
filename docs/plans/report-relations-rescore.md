---
schema_version: "1.0"
artifact_type: design_plan
id: report-relations-rescore
status: proposed
planning_path: requested
method_conformance_receipt: docs/plans/report-relations-rescore.receipt.json
trace_review_criteria:
  - criterion_id: outcome
    expected_outcome: pass
goal:
  outcome: "An AI reading examples/seed/report.md sees why decisions were made: every motivates, supersedes, reframes and challenges relation appears as a sentence with both nodes' text, and the usefulness pilot's condition C is re-scored on that report with the result recorded"
  canonical_example: "grep -c 'because:' examples/seed/report.md prints 26 (was 0); evaluation/usefulness_pilot/results.md has a 2026-10-11 section giving the new condition-C mean key-point coverage and fully-right count next to the saved 0.65 and 5 of 12"
  forbidden_substitutes: "tests passing without the report text containing a motivates relation's reason; a score without reading the judge and answer traces of every miss; re-generated questions or re-run A/B answers; an OpenRouter call"
  boundaries: "files: src/inquiry_graph/render.py, tests/test_report_relations.py, examples/seed/report.md, evaluation/usefulness_pilot/{run.py,followup.py,results.md,data/}, docs/project-status.md, docs/verification.md, this plan and its records; model calls only through Codex (codex/gpt-5.6-luna); no irreversible action, no money spent; private/ never committed"
  done_when: "One traced run of evaluation/usefulness_pilot/followup.py whose llm_client call log rows (trace ids inquiry-graph/usefulness-pilot/answer-C2 and judge-followup-*) are read for every C2 answer that misses key points, each miss classified in results.md; pytest -ra and tools/build_artifacts.py --check output with counts and exit 0 saved as docs/plans/report-relations-rescore.check.txt; durable_docs_check.py --repo . --plan docs/plans/report-relations-rescore.md --range 3dc043727a7b0e0fa4b2685cb918a2ba33baa41d..HEAD exits 0 with output in the same file"
  do_not_gate_on: "Brian reading the report or the results; any improvement in the score (a null or negative result is a valid outcome)"
---

# Report carries reasons as text; re-score pilot condition C

Each section below answers the checklist items quoted in it; the gate judges only that
section's text. Replace every `TODO(answer ...)` line before running `cli.py check`. Quote
values in the front matter: an unquoted ` #` starts a YAML comment and cuts the value.

## Actor and result

> **CORE-ACTOR-RESULT-EXAMPLE** (blocking): The plan names the actor it serves, the desired result, and one stable, concrete, user-visible example of that result.

Actor: an AI agent resuming an inquiry from the graph report (the reader Brian named in docs/project-status.md, 2026-09-29), and Brian, who decides whether the report earns its place. Result: the report carries reasons and replacements as readable sentences, and the pilot score shows whether that closed the "why" gap. Example: the report line "- <result text> — *because:* <reason text>" for each of the 26 motivates relations; `grep -c because: examples/seed/report.md` prints 26 where the old report printed 0.

## Requirements

> **CORE-REQUIREMENTS-TRACED** (blocking): The plan lists its requirements: what was asked for, and what the delivered work's own claims imply. A claim here is what the work is presented as being or doing to its users, for example work presented as following a standard, schema or contract (which implies conformance to it) or an output labelled as showing something (which implies it shows it correctly); the plan's own format and front matter are not such claims, and the details a check examines (what a trace must show) belong to that check rather than being separate requirements. Each requirement names the check that verifies it (a test, script, gate step, or named review of a run) and its status: passing, failing, planned and not yet run, or deferred with a stated reason; deferred requirements are carried onto every release or completion record the plan names. A plan fails this item if it has no requirements list, if any requirement has neither a check nor an explicit deferral with its reason, or if the plan presents the work as following a named standard, schema or contract, or as having another property its users rely on, that its requirements list omits.

| Id | Requirement | Check | Status |
|---|---|---|---|
| R1 | (asked) Report renders relations as sentences with node text, decisions/reasons grouped, existing sections kept | tests/test_report_relations.py (fails on the old renderer, passes on the new) | planned |
| R2 | (asked) Move inputs/outputs shown as text, truncated | tests/test_report_relations.py::test_move_inputs_and_outputs_show_node_text_not_ids | planned |
| R3 | (asked) Seed report regenerated | tools/build_artifacts.py --check exits 0 | planned |
| R4 | (asked) Condition C re-scored with saved questions/keys, A/B answers not re-run, Codex route only | followup.py run; llm_client call log shows only codex/ models for these trace ids | planned |
| R5 | (asked) Every C miss classified from its trace | named review of the followup run's answer and judge traces, recorded in results.md | planned |
| R6 | (asked) results.md, project-status.md:19, verification.md:133 state the pilot's limits and the new result without overclaiming | named review of the diff against the summary json | planned |
| R7 | (implied) Old renderer on the pilot graph reproduces the saved C material byte-for-byte, so C vs C2 differs only by the renderer | one-off comparison run, output in check.txt | planned |

## Success and disproof

> **CORE-SUCCESS-DISPROOF** (blocking): The plan defines the evidence that would show success and a concrete condition that would disprove the approach. Each success measure is the property the plan claims, or a check that directly tests that property, not a stand-in for it: a count, a picture, a readability judgment, or the pipeline agreeing with itself (hashes, labels, byte equality) does not show correctness or conformance it does not test. A plan fails this item if it has no disproof condition, or if a success measure is such a stand-in for the claimed property and the plan names no direct check of that property.

> **CORE-TRACE-REVIEW** (blocking): Every success or acceptance criterion in the plan is judged from the full trace of a run, not only its final outcome: it names the run whose full trace is examined (for example the session, its tool and LLM calls, commits, check output, or messages), where that trace lives, and what must be seen in that trace beyond the final outcome. A criterion that names only an outcome, such as tests passing, a PR merged, a test fixture reproducing the journey, or a status reading succeeded, fails this item. A criterion for which no run exists, such as a pure document edit, passes only when the plan states that exemption and its reason explicitly.

Success: the report text contains each motivates relation's reason and result text on one line (tested directly by reading report output, not a count); the followup run produces a C2 score graded by the same judge route as a re-grade of old C, so the comparison is like-for-like. Disproof of the approach: C2's mean key-point coverage is not above the old C's under the same Codex judge, or the "why" questions (rejection_reason category) still miss with the needed reason present in the report — that would show the linearization is not what limits the graph.

Run: one execution of `evaluation/usefulness_pilot/followup.py` (this session). Trace: llm_client call log (`calls_2026-10-11.jsonl`, trace ids `inquiry-graph/usefulness-pilot/answer-C2`, `.../judge-followup-C2-q*`, `.../judge-followup-C-q*`) plus the cached JSON in private/usefulness/. What must be seen beyond the score: for every question where C2 covers fewer than all key points, the full answer and the judge's grade for it, and a search of C2_graph_report.md for the key's reason; each is classified (reason absent from report / present but unused / key questionable). For R1-R3: the pytest -ra and build_artifacts --check output saved in docs/plans/report-relations-rescore.check.txt, showing counts and exit status, plus the failing run of the new tests against the old renderer. That failing run's full pytest output (each test's assertion message, showing the report line that lacked the reason/result text) is also saved in that same check file. Beyond the pass/fail counts, the examined trace must show: for the old-renderer run, each of the three new tests failing on its own assertion (not on an import or collection error); for the new-renderer run, the regenerated examples/seed/report.md containing a "## Decisions and reasons" heading and "because:" lines, and build_artifacts --check reporting no drift.

## When a run fails or surprises us

> **CORE-TRACE-DEBUGGING** (blocking): The plan includes a separate When a run fails or surprises us procedure, distinct from anticipated failure modes. It requires preserving the failed run and its trace id; reading full inputs, prompts, each tool call arguments/results, intermediate stages and final output before selecting a fix; citing the observed divergence; classifying evidence absent, evidence returned but unused or contradicted, invalid expectation, or unresolved; and linking a targeted repair to a new traced verification run while retaining the original failure. Unresolved diagnoses permit investigation but cannot authorize a causal repair. Review completeness is separate from the run verdict.

If a run fails or surprises us: keep the failed output and its trace id (cached JSON is never overwritten; a rerun writes a new file name). Before choosing a fix, read the full prompt, the material given, the structured response and any error for that call; cite the exact divergence; classify it as evidence absent, evidence returned but unused or contradicted, invalid expectation (answer key wrong), or unresolved. An unresolved diagnosis permits more investigation but not a causal fix. This procedure is separate from the anticipated failure modes listed elsewhere: it covers failures nobody predicted. Before a fix, the full trace is read: the inputs, the prompt, each tool call's arguments and results (Codex CLI calls run read-only with no tools expected; any tool call that appears is read), every intermediate stage (render, answer, judge) and the final output. A repair must target the cited divergence only, and is linked to a new traced run while the original failure and its trace id stay recorded. Whether the review covered every miss is reported separately from the score.

## System model

> **CORE-SYSTEM-MODEL** (blocking): The plan links the project's system model (a path such as docs/model/ODD.md) or carries the one-line exemption `System model: exempt -- <reason>`, which fits only a project with no stored state and no user-facing view. Unless exempt, the plan names each system-model element (entity, process, record or event, or view) that the work adds, changes, or relies on, and its trace review names, for each such element, what the examined run must show of it (for example an event of that record type with its id, or the view displaying that entity). A plan with neither a model link nor the exemption line fails this item, as does one that lists model elements without saying what the examined run must show of each, or one that names no element without stating that the work touches none and why. For a maintained repository, the plan also cites the documentation entry point from which the model is reachable; a shared model explicitly identifies this repository's scope. It names applicable source-linked views, explains material omissions without imposing a fixed diagram quota, names concrete model freshness or drift checks, and states how the model, view coverage and verification evidence will be reconciled in the same change (or gives a concrete reason each needs no update). A bare model path without these discovery, view, freshness and reconciliation obligations fails this item. Representation Router may render selected views but does not supply planning authority or prove executed behavior.

System model: docs/model/ARCHITECTURE.md with docs/model/trace.yaml, reachable from wiki/index.md. Element changed: VIEW-RENDER (the Markdown report projection in src/inquiry_graph/render.py); the examined run must show the regenerated examples/seed/report.md containing the "Decisions and reasons" section with because/replaced-by lines. Element relied on: PROC-BUILD-ARTIFACTS; the examined run must show that process regenerating examples/seed/report.md from examples/seed/graph.json (the diff of report.md in this change), and its --check run printing "Checked 8 artifacts" with exit 0, meaning the committed report equals what the process produces. No other element changes; the evaluation script is outside the model. Views: the existing C4 container view already lists views.py / render.py "report"; no diagram change is needed because the report's content changes, not its place in the system. Freshness: build_artifacts --check and durable_docs_check run in the same change; trace.yaml VIEW-RENDER text stays accurate, so no model edit is required. Reconciliation in this same change: (1) model -- no update, because VIEW-RENDER's description (a Markdown report projection of the graph) remains true; (2) view coverage -- no update, because no element is added or moved and the C4 container view still names render.py; (3) verification evidence -- updated in this change: docs/verification.md gains the follow-up result, and the check output is saved beside this plan.

## Capability reuse

> **CORE-CAPABILITY-REUSE** (blocking): The plan answers capability reuse against the capability catalogue in agentic-capability-architecture-canonical, which has two files: `reuse_candidates.yml`, whose entries under `candidates:` are cross-project capabilities with their selected off-the-shelf implementations, each named by its `id` (for example `documents_to_text`) and marked candidate or promoted; and `capability_registry.yml`, whose entries under `capabilities:` are the packages that repository holds, each named by its key (for example `approvals`) with the capability ids it `provides` (for example `approval.resolve`). An entry from either file counts. The plan names each catalogue capability the work reuses, by its id, key or provided id; names each new capability the work adds together with its first consumer (the project, command or workflow in this plan that uses it); and, where no entry covers what the work needs, states `No catalogue entry fits, because <reason>`, the reason saying what the work needs that no entry provides. A plan may give more than one of these answers. A plan fails this item if it gives none of them, if it claims reuse without naming the catalogue entry or id reused (reusing code or a contract that is not a catalogue entry does not count), if it adds a capability without naming its first consumer, or if it says no entry fits without a reason.

No catalogue entry fits, because the work changes one Markdown renderer inside this repository and re-runs an existing pilot's llm_client calls; neither reuse_candidates.yml (approval_action_workflow, twitterapi_io_search_candidates_wrapper, documents_to_text) nor capability_registry.yml (core, approvals, notifications, scheduling) provides report linearization or model calls.

## Authority and non-goals

> **CORE-AUTHORITY-NONGOALS** (blocking): The plan states who holds authority over the work and what it explicitly will not do (non-goals).

Authority: Brian approved this task (2026-10-11) through the coordinating session; this repo is his (BrianMills2718/inquiry-graph). Non-goals: no new questions, no re-run of A/B answers, no OpenRouter, no schema change, no change to extraction, no claim that the graph beats the transcript beyond what the score shows, no publication of private/ material.

## Irreversible actions and spend

> **CORE-IRREVERSIBLE-SPEND** (blocking): For each irreversible action or spend the plan proposes, it names the boundary, who must authorize it, and how it is contained.

No irreversible action and no money spend. The only consumption is Codex subscription usage. Boundary: at most about 25 calls for this re-score plus the planning verifier calls, no paid API. Authorizer: Brian, who authorized it on 2026-10-11 by instructing that this work use his Codex subscription (or Claude subscription) instead of OpenRouter. Model calls go through Brian's Codex subscription (no per-call money); about 25 calls (12 answers in one call, 24 judge calls). Containment: if the Codex route fails twice the same way, stop and report; never fall back to OpenRouter.

## Uncertainties

> **CORE-UNCERTAINTIES** (blocking): The plan lists its material uncertainties, and each one has an owner or the evidence that would resolve it.

U1: whether codex/gpt-5.6-luna grades like the pilot's OpenRouter gpt-5.6-luna — resolved by re-grading A and old C through Codex alongside C2 and comparing with the saved grades. U2: whether the longer report (about 2x) helps or dilutes — resolved by the C2 score and the per-miss trace review. U3: whether answer keys are sound — resolved per miss in the trace review. Owner: this session.

## Activation facts

> **CORE-ACTIVATION-FACTS** (blocking): No activation fact that the plan triggers is declared false. Declaring a fact true when the plan does not strictly need it is acceptable, because it only adds checks; judge only facts declared false. empirical_comparison_proposed is triggered when the plan proposes an A/B test, benchmark, bake-off, or other experiment comparing alternative designs, models, or candidates to choose among them; checking the built result against an expected outcome (an acceptance test, fixture replay, or regression check) is verification and does not trigger it. shared_mechanism is triggered by a new shared mechanism, contract, or algorithm; llm_central by behavior that centrally depends on LLM calls; irreversible_or_spend_action by a proposed irreversible action or spend. claims_external_standard is triggered when the plan claims, or presents its work as, following, implementing or conforming to a standard, schema or contract owned outside the repository being changed (for example a model presented as DM2, or output said to match a published schema); conforming to the repository's own contracts does not trigger it; aes_governed_target when the target repository is governed by an AES target (`.aes/target.yaml`), or the plan creates one (for example by running `aes init`). These two facts are optional: an undeclared one is shown as false and is judged like a declared false.

shared_mechanism=false (one repo-local renderer); empirical_comparison_proposed=true (old vs new report compared on the pilot); llm_central=true (the score depends on model answers and grades); irreversible_or_spend_action=false (subscription calls, revertible commits).

## Evaluation design

> **OV-EVAL-DECISION** (blocking): The plan names the specific decision that the proposed comparison or benchmark could change, and what would be done differently under each possible result.

> **OV-EVAL-IRREDUCIBLE-UNCERTAINTY** (blocking): The plan names the irreducibly empirical uncertainty the comparison resolves and explains why first principles and existing evidence or prior art cannot resolve it.

> **OV-EVAL-PARITY** (blocking): The plan states the minimum capability parity every compared candidate must meet before the comparison is meaningful.

> **OV-EVAL-COST** (blocking): The plan explains why running the comparison costs less than making a reversible choice now and correcting it later.

Decision: whether report() with relation sentences becomes the default linearization handed to model readers, and whether "keep reasons" is the fix the pilot named. If C2 beats old C under the same judge, keep it and record the gap to A that remains; if not, revert to the old compact layout (or keep only the decisions section) and record that the reason gap lies in extraction, not rendering.

Whether a model reader actually uses the added sentences to answer "why" questions cannot be settled from first principles: adding text can help or dilute a 146k-char context, and the pilot itself is the only existing evidence on these questions. That existing evidence cannot settle it, because the pilot only measured the old renderer: its C report printed relations as IDs, so it says nothing about whether a model uses reasons once they are printed as text. Prior art on long-context reading (more relevant text can help, and padding can distract) points both ways, so it gives no decisive prediction for this report.

Both report variants come from the same pilot-era graph (commit 45b1e82; the old renderer reproduces the saved C material byte-for-byte), are answered by the same prompt and model, and are graded by the same blind three-answer judge prompt and route alongside the same saved A and B answers. Minimum capabilities every compared candidate must meet before the comparison counts: (1) it is a rendering of the same pilot-era graph (45b1e82), so only the renderer differs; (2) it fits in one answer call's context, so no candidate is truncated; (3) its answers exist for all 12 saved questions in the same AnswerSet schema; (4) it is graded in the same blind three-answer judge run as the saved A and B answers. A candidate missing any of these is reported but not compared.

The run reuses saved questions and A/B answers and costs about 25 subscription calls and minutes of wall time; making the renderer change without measuring would leave the pilot's headline number stale in project-status and verification docs, which agents read to decide direction. Comparison: the run costs zero money and roughly an hour of unattended wall time. Making the choice now without measuring and correcting it later costs more: every agent reading the stale 0.65 figure would steer the project from it until someone ran the same measurement anyway, and the renderer decision (keep or revert) would have no evidence behind it. So the measurement is the cheaper path.

## LLM call boundary

> **OV-LLM-CALL-BOUNDARY** (blocking): The plan describes the model call graph, the structured result boundary each call returns, and how calls are traced.

> **OV-LLM-AUTHORITY-PROMOTION** (blocking): The plan names the provider and spend authority for model calls and one authentic-run condition that must hold before the behavior is promoted.

Call graph: one answer call (AnswerSet: 12 Answer records with question_number, answer, cannot_answer) for C2; 24 judge calls (GradeSet: three Grade records labelled X/Y/Z with points_covered, contradicts_key, attribution_error, false_closure), 12 for (A,B,C2) and 12 for (A,B,old C). All via llm_client call_llm_structured with Pydantic response models; each call has a trace_id and is logged in llm_client's daily call log; outputs cached as JSON under private/usefulness/.

Provider: Codex CLI on Brian's subscription (codex/gpt-5.6-luna), per Brian's 2026-10-11 instruction not to use OpenRouter; no money spend. Promotion condition: the new report is presented as improving model answers only if one authentic traced followup run shows C2 above old C under the same judge, with every miss read and classified.

## Vertical and reset

> **OV-PROTO-VERTICAL-RESET** (blocking): The plan names the minimal vertical result, the reset boundary, and the non-goals, without adding coordinated-work ceremony.

Minimal vertical: renderer change, its test, regenerated seed report, one re-score run, results recorded. Reset boundary: git revert of the branch restores the old report; cached private JSON is untouched by a revert. Non-goals: no new questions, no re-run of conditions A or B, no OpenRouter calls, no change to extraction or the graph schema; no coordinated work units.

## Durable documents

> **OV-DURABLE-DOCS-DECLARED** (blocking): The adopting repository declares durable documents (a `durable_documents` block in `.agentic/repo.yaml`). The plan carries a `Durable documents:` line that names each durable role it updates, with the system-model rule or element ID where the role is the system model (for example `Durable documents: system_model#RULE-LOAN-OVERDUE, decisions`), or says `The repository declares its durable documents in the `durable_documents` block of `.agentic/repo.yaml` (goal, requirements, system_model, decisions, plans).

Durable documents: none -- no declared durable role changes: the goal, requirements, system model and decisions stay as they are, because VIEW-RENDER's description stays true and the evaluation follow-up is a measurement, not a decision.

Evidence of the declaration: `.agentic/repo.yaml` in this repository has a top-level `durable_documents:` block naming the roles goal, requirements, system_model, decisions and plans. The status and verification pages this work edits are not declared durable roles. Completion runs `durable_docs_check.py --repo . --plan docs/plans/report-relations-rescore.md --range 3dc043727a7b0e0fa4b2685cb918a2ba33baa41d..HEAD` and requires exit 0.
