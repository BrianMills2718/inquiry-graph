# Preregistered balanced replay: 2026-09-30

## Claim and decision

**Claim:** On the fixed 13-question key from the same 30-chat corpus, per-question
answers from archive search/read (A), extracted positions plus typed links (B),
and extracted positions without links (C) can be compared descriptively for
key-point coverage when each question is answered in its own call.

**Decision:** Determine whether this corrected, bounded sample supports keeping
archive search/read as the answer-retrieval fallback and whether typed links add
observable answer value over positions alone. It cannot establish broad
generalization or product readiness.

**Unit and population:** One cross-chat question; the same 13 retained key
questions across agreement, tension, recurring open questions, change over time,
and position summaries. The key was generated from the full corpus, so the
seven source-heldout questions are not an independent question-set holdout.

## Fairness correction and systems

The previous run answered A's questions in 13 separate calls, but put all 13
questions into one call for B and one for C. This replay makes each B and C call
contain exactly one question, matching A's batching. Each route uses the same
answer model (`codex/gpt-5.6-luna`), answer instructions and schema, question
wording, subscription transport, and corpus revision. The retrieval material is
the intended route difference: A's question-specific archive results, B's full
positions-plus-links export, and C's full positions-only export.

Reuse the already saved A answers because they were made one question per call
with the same model and prompt. Generate 13 fresh B calls, 13 fresh C calls,
then blindly regrade all three routes together once per question with
`codex/gpt-5.6-sol`. Preserve the old campaign and all its outputs.

## Metrics, controls, and readout

- Primary: per-question and mean covered-key-point fraction, computed as
  `min(points_covered, key_points) / key_points`.
- Secondary: contradiction, attribution-error, unsupported-claim, and
  cannot-answer counts; literal citation/quote audit; calls, token totals,
  recorded billing, and failures.
- Report all 13 rows and five category aggregates. With 13 questions, treat
  differences as descriptive; do not make a statistical or general superiority
  claim. Do not select a route from a small mean difference alone.
- Before answer generation, run a fresh grader positive/negative control: one
  obvious two-point correct answer and one contradictory answer. Required
  outcome: 2/2 with no contradiction for the correct answer; 0/2 and a
  contradiction flag for the wrong answer. A failed control invalidates grading.
- Build adequacy: validate all 30 source graphs; require all 13 questions and
  all three answers per question; any missing, malformed, or failed call leaves
  the replay incomplete. The saved reference-key quote audit remains the source
  integrity evidence.

## Budget, artifacts, and stop rule

Expected new calls: 26 route answers, 13 blind graders, and one paired control.
Using the prior aggregate telemetry as a rough estimate, B/C replay plus grading
and control is about 4.05 million total tokens; actual usage must come from the
metadata-only trace database. Calls use the authorized Codex subscription route
with no output-token cap or request timeout. Stop on authentication, quota, or
provider errors, retain completed per-question files, and resume only from the
same campaign after inspecting the error.

Private inputs and outputs remain under
`private/xconv/scale_run_codex_balanced_20260930/`. Public records contain
aggregate outcomes and trace IDs only. The runner writes one private file per
completed answer/grade, so an interrupted run resumes without repeating
successful calls. After execution, independently rerun score/source checks and
obtain a fresh adversarial C5 signoff before changing the retrieval decision.

Reproduction entrypoint:
`python evaluation/cross_conversation_scale/balanced_replay.py --codex-subscription`
