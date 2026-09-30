# For Brian: does linking extracted positions improve cross-chat answers? (30-chat results)

**Run:** corrected Codex subscription campaign, 2026-09-30 · **Report:** v1.0

**C5 decision (independently signed off 2026-09-30):** Use archive-search-then-read
(A) as the default retrieval route for this measured workload. B scored 0.019
above positions only (C) overall, tied C on the seven source-heldout questions,
and scored 0.038 below A. Keep the linker data for the separate future topic-map
phase. Defer productizing any answer route for the full sourced-answer contract
until source citations and verbatim answer quotes pass direct checks. This is a
bounded decision from one 30-chat corpus and 13 valid questions; it does not
establish broad generalization or evaluate the future topic map.

The comparison measures key-point coverage, not the complete answer contract.
The required source citations and verbatim quotes were not part of the blind
judge's score. A separate literal-string audit below finds weak source evidence
in all three routes, with no answer route meeting the citation/quote contract.
The action is limited to retrieval direction; no route is ready for the complete
sourced-answer contract.

## Scope and method

The fixed corpus contains 30 chats and 4,229,221 visible characters. All 30
extracted graphs validated. The independent reference key retained 581 quoted
positions, dropped 43, and retained 13 cross-chat questions across the five
required categories. A source audit verified all retained quotes against
Brian-authored messages. Two proposed questions were dropped because their
position IDs were invalid.

- **A:** archive search, then read the selected source chats within the measured
  per-question read budget.
- **B:** extracted positions with typed links, question status and chat dates.
- **C:** the same positions without links.

The B input contains 620 positions and 233 typed cross-chat links (437,686
characters); C contains the same 620 positions without links (330,267
characters). For A, archive search selected 2–7 chats per question and read
580,835–598,750 characters. The corpus-wide estimate is about 1,057,305 tokens
against the runner's 1,050,000-token single-call context setting, a narrow
overrun based on the runner's character-to-token estimate.

Answers were graded blind against the independent key on normalized key-point
coverage from 0 to 1: **1.0 means every key point was covered; 0 means none
were covered**. Fractional scores are the covered share. There were 13 graded
questions in each route. The result rows below expose only anonymous question
numbers, categories and scores; they contain no question wording, answer text,
transcript text or quotes.

The corrected campaign used 15 answer-generation calls and 13 judge calls.
Those calls produced 13 answers per route. Answer calls used
`codex/gpt-5.6-luna`; judging used `codex/gpt-5.6-sol`. Telemetry records
subscription-included billing, $0 API cost and zero errors for all 28 calls.
Reported token totals were A 1,980,739, B 157,932, C 125,665, and judging
335,531.
The first answer/grade run used metered OpenRouter by mistake and is excluded.
The runtime fix is commit `ce7b8b7`.

## Per-question coverage

| Q | Category | A: search/read | B: positions + links | C: positions |
|---:|---|---:|---:|---:|
| 1 | Agreement | 1.00 | 0.75 | 0.75 |
| 2 | Agreement | 0.67 | 0.67 | 0.67 |
| 3 | Agreement | 0.75 | 0.50 | 0.50 |
| 4 | Conflict/tension | 1.00 | 0.75 | 0.75 |
| 5 | Conflict/tension | 0.75 | 0.50 | 0.25 |
| 6 | Conflict/tension | 0.75 | 0.50 | 0.50 |
| 7 | Recurring open question | 0.25 | 0.25 | 0.25 |
| 8 | Recurring open question | 0.50 | 0.75 | 0.75 |
| 9 | Recurring open question | 0.25 | 0.50 | 0.50 |
| 10 | Change over time | 0.50 | 0.75 | 0.75 |
| 11 | Change over time | 1.00 | 0.50 | 0.50 |
| 12 | Position summary | 0.25 | 1.00 | 0.75 |
| 13 | Position summary | 1.00 | 0.75 | 1.00 |
| **Mean** | **All 13** | **0.67** | **0.63** | **0.61** |

### Category means

| Category | Questions | A | B | C |
|---|---:|---:|---:|---:|
| Agreement | 3 | 0.81 | 0.64 | 0.64 |
| Conflict/tension | 3 | 0.83 | 0.58 | 0.50 |
| Recurring open question | 3 | 0.33 | 0.50 | 0.50 |
| Change over time | 2 | 0.75 | 0.62 | 0.62 |
| Position summary | 2 | 0.62 | 0.88 | 0.88 |

## Error and completeness counts

| Judged outcome | A | B | C |
|---|---:|---:|---:|
| Fully right | 4/13 | 1/13 | 1/13 |
| Contradicts key | 5/13 | 5/13 | 5/13 |
| Attribution errors | 3 | 4 | 3 |
| Unsupported claims flagged | 13 | 11 | 11 |
| Cannot answer | 0 | 0 | 0 |
| Recorded API cost | $0 | $0 | $0 |

## Held-out and limitations

Seven questions use only chats outside the five used during linker prompt
revisions (Q2, Q3, Q5, Q8, Q9, Q11, Q13). They cover all five categories.
On this source-held-out subset, mean coverage is A 0.702, B 0.595, C 0.595;
B−C is 0 and B−A is −0.107. A is fully right on 2/7, B on 0/7, and C on
1/7. The calculation is recorded in
[`heldout_summary.json`](heldout_summary.json). This is a small source holdout,
not an independently generated question set: the reference questions were
generated using the full corpus, and the key and answer routes used the same
model. It supports a limited check against the five-chat prompt-development
source set, not broad generalization.

## Source citation and quote audit

The blind judge scored key-point agreement but did not score the answer
instruction to name supporting chats/dates or the goal's verbatim-quote
requirement. The content-free audit in
[`answer_evidence_audit.json`](answer_evidence_audit.json) checks exact title
and date strings from each question's reference chats, plus double-quoted answer
spans against those source messages. It is a literal-string screen, not a
semantic citation judgment.

| Literal evidence check | A | B | C |
|---|---:|---:|---:|
| Questions with at least two expected chat titles | 7/13 | 13/13 | 11/13 |
| Questions with at least two expected title/date pairs | 7/13 | 4/13 | 4/13 |
| Double-quoted answer spans found verbatim in expected source chats | 9/33 | 0/27 | 0/28 |

The 620 position quotes in B's graph export were all nonempty and matched a
contiguous span in their source message after Unicode and whitespace
normalization (620/620). The answer routes' lower quote-match counts therefore
point to answer-generation fidelity as a separate weakness; the blind score
does not account for it.

The observed differences are small and descriptive. A's advantage is consistent
with the archive-search route being the better default for this workload; B's
0.02 overall gain over C does not establish useful typed-link value for answer
quality. The three routes also share a low fully-right count, so the result does
not imply that any route answers this task reliably.

## Trace and signoff record

- Scored answer traces: 15 synthesis calls under
  `inquiry-graph/xconv-scale-codex/answer-*`; judges:
  `inquiry-graph/xconv-scale-codex/judge-q01` through `judge-q13`. The scored
  database retains lifecycle metadata only, not their prompt/response bodies.
- Supplemental full-trace reproduction:
  `inquiry-graph/xconv-scale-codex/trace-inspection-C`. Its mapped Codex session
  contains the route-C positions-only prompt and 13 structured answers; this
  one-call replay is not part of the scored comparison.
- Grader positive control: `inquiry-graph/xconv-scale-codex/grader-positive-control/q01`.
  The known-correct answer received 4/4 key points and no contradiction; the
  known-wrong answer received 0/4 and was marked contradictory. The call used
  `codex/gpt-5.6-sol`, subscription-included, $0. This checks the grader's
  ability to distinguish an obvious positive and negative, not the full rubric;
  it is a separate calibration call and is not included in C4 scores or token
  totals. Aggregate evidence is in
  [`grader_positive_control.json`](grader_positive_control.json).
- Fresh independent signoff control: `inquiry-graph/c5-signoff/grader-positive-control`.
  The known-correct answer received 4/4; the known-wrong answer received 0/4
  and was marked contradictory. It used `codex/gpt-5.6-sol` over the authenticated
  Codex CLI, with subscription-included billing, 25,112 tokens, $0 cost, no call
  error, and exit 0. It is excluded from C4 totals; aggregate evidence is in
  [`grader_positive_control.json`](grader_positive_control.json).
- Independent hand-check: four answer/grade/key/source rows across agreement,
  conflict, recurring-question, and position-summary categories all aligned
  (4/4). Only anonymous row IDs and counts were reported; no private content is
  reproduced here.
- Independent C5 disposition: **SIGNED-OFF**, with the seven-question subset
  explicitly limited to source-heldout references rather than broad
  generalization. The bounded decision is recorded on
  [inquiry-graph issue #38](https://github.com/BrianMills2718/inquiry-graph/issues/38).

The private inputs and outputs remain under
`private/xconv/scale_run_codex_rerun_20260930/`. The first, metered OpenRouter
answer and grade set remains preserved separately and excluded from all figures
above.
