# C5 independent signoff

**Campaign:** `scale_run_codex_rerun_20260930`

**Signoff date:** 2026-09-30

**Verdict:** **SIGNED-OFF**, for a bounded retrieval-direction decision.

## Gate results

| Gate | Status | Evidence and limit |
|---|---|---|
| Validity, positive control, and build adequacy | **Pass** | The independent reviewer recomputed all 39 route/item scores and aggregate/category means. The source audit matched 620/620 graph-position quotes to source messages. A fresh Codex subscription control scored the known-correct answer 4/4 and the known-wrong answer 0/4 with a contradiction flag. All three answer routes produced 13 items over 30 validated chats. |
| Representativeness and held-out coverage | **Pass, limited** | Seven of 13 questions cite only chats outside the five used for linker prompt revisions and represent all five categories. Mean coverage there was A 0.702381, B 0.595238, C 0.595238. The subset is a source-reference check, not an independent question set; the five prompt-development chats remained in the available corpus. |
| Class-level diagnosis | **Pass** | A led overall and in agreement, conflict, and change; B/C led in recurring questions and position summaries. B−C was +0.019 overall and 0 on the source-heldout subset. A/B/C were fully right on 4/13, 1/13, and 1/13. All routes had five contradictions. Literal answer-evidence checks show that no route met the full source-citation and quote contract. |
| Broad generalization | **Not evaluated** | This is one 30-chat corpus and 13 valid questions. It does not establish general superiority. |
| Bounded decision | **Pass** | Use archive-search-then-read as the answer-retrieval default for this measured workload. Retain the linker data for the separate topic-map phase. Defer productizing any answer route for the complete sourced-answer contract. |

## Reproduction and calibration evidence

- A fresh blinded Codex CLI control used `codex/gpt-5.6-sol`,
  `subscription_included`, 25,112 tokens, $0 recorded cost, no call error, and
  exit status 0. Trace:
  `inquiry-graph/c5-signoff/grader-positive-control`.
- The reviewer independently hand-checked Q1/A, Q4/B, Q7/C, and Q13/A against
  their key and source records. All four cached grades aligned; no private
  question, answer, transcript, or quote is reproduced here.
- The seven-item source-heldout aggregates were recomputed from the reference
  key and the five prompt-development chat IDs. Category counts were 2
  agreement, 1 conflict, 2 recurring, 1 change, and 1 position.
- The supplemental route-C Codex session was checked for prompt/response
  structure: 5/5 completeness checks passed. This replay is not part of scored
  C4 results.
- The scored campaign telemetry records 15 synthesis calls and 13 judging calls,
  subscription-included billing, $0 recorded cost, and no provider-call errors.
  Scored prompts and responses remain metadata-only in that database.

The reviewer initially rejected an earlier C5 package that lacked the grader
positive control and citation/quote audit. Those controls and bounded-scope
limitations were added before this fresh review. The final verdict does not
convert the small source-heldout subset into a generalization claim.
