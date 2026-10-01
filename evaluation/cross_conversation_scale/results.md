# Cross-chat linker: balanced 30-chat results

> **C5 status: signed off for a bounded disposition (2026-10-01).** This
> balanced replay fixes the earlier comparison's different question batching.
> The independent review supports keeping the typed linker as a bounded
> research/topic-map source, without a broad answer-route superiority claim.
> See [`signoff-balanced-recheck-2026-10-01.md`](signoff-balanced-recheck-2026-10-01.md).

## What the replay shows

On the same 13 questions, average key-point coverage was **A 0.647, B 0.686,
C 0.686**. B's coverage was 0.038 above archive search/read (A), but it tied
positions alone (C). B had fewer key contradictions than either route, while
having more attribution errors than A. All three routes flagged unsupported
claims on 12/13 answers, and none met the requested sourced-answer contract on
the literal evidence screen. The sample is too small and narrow to establish
that B beats search at scale. It shows no coverage lift from adding typed links
to this answer route.

**Signed-off bounded disposition:** keep the linker as a research artifact for
the later topic-map phase. B tied positions alone on key-point coverage and its
small descriptive lead over search/read does not establish a scale advantage.
Do not productize an answer route under the observed citation and quote
performance.

## Scope and method

This replay compares three ways to answer cross-chat questions from the same
30-chat corpus:

- **A — archive search/read:** use the saved per-question search results and
  read the selected source chats.
- **B — positions plus links:** give the answer model the full export of 620
  extracted positions, 233 typed cross-chat links, question status, and dates.
- **C — positions only:** give it the same 620 positions and metadata without
  links.

Each route answered one question per call, with the same answer model,
instructions, schema, question wording, and subscription transport. A's 13
previously saved one-question answers were reused; B and C each ran 13 fresh
calls. A fresh blind grader scored all three answers against the independent
reference key once per question. A positive/negative grader control ran before
the answers.

The corpus has 30 validated graphs and 4,229,221 visible characters. The
independent key retained 13 questions across agreement, conflict/tension,
recurring open questions, change over time, and position summary; 2 invalid
candidate questions were dropped. The key's 581 retained position quotes were
verified against Brian-authored source messages. Seven questions cite only
chats outside the five used in linker prompt revisions, but the questions were
still generated from the full corpus, so this is not an independent
question-set holdout.

The exact grade metric is `min(covered key points, key points) / key points`.
It ranges from 0 to 1. Full correctness also requires no contradiction flag.
The 13-question differences are descriptive; no significance or broad
generalization claim is made.

## Per-question coverage

| Q | Category | Key points | A: search/read | B: positions + links | C: positions |
|---:|---|---:|---:|---:|---:|
| 1 | Agreement | 4 | 1.000 | 1.000 | 1.000 |
| 2 | Agreement | 3 | 0.667 | 0.667 | 0.667 |
| 3 | Agreement | 4 | 0.750 | 0.750 | 0.750 |
| 4 | Conflict/tension | 4 | 1.000 | 0.750 | 0.750 |
| 5 | Conflict/tension | 4 | 0.750 | 0.500 | 0.500 |
| 6 | Conflict/tension | 4 | 0.750 | 0.500 | 0.750 |
| 7 | Recurring open question | 4 | 0.000 | 0.500 | 0.250 |
| 8 | Recurring open question | 4 | 0.500 | 0.500 | 0.500 |
| 9 | Recurring open question | 4 | 0.500 | 0.500 | 0.500 |
| 10 | Change over time | 4 | 0.500 | 0.500 | 0.750 |
| 11 | Change over time | 4 | 1.000 | 0.750 | 0.750 |
| 12 | Position summary | 4 | 0.000 | 1.000 | 1.000 |
| 13 | Position summary | 4 | 1.000 | 1.000 | 0.750 |
| **Mean** | **All 13** | — | **0.647** | **0.686** | **0.686** |

## Category means

| Category | Questions | A | B | C |
|---|---:|---:|---:|---:|
| Agreement | 3 | 0.806 | 0.806 | 0.806 |
| Conflict/tension | 3 | 0.833 | 0.583 | 0.667 |
| Recurring open question | 3 | 0.333 | 0.500 | 0.417 |
| Change over time | 2 | 0.750 | 0.625 | 0.750 |
| Position summary | 2 | 0.500 | 1.000 | 0.875 |

## Other outcomes

| Blind-graded outcome | A | B | C |
|---|---:|---:|---:|
| Full key coverage, no contradiction (narrow proxy) | 4/13 | 3/13 | 2/13 |
| Contradicts the key | 5/13 | 3/13 | 5/13 |
| Attribution error | 2/13 | 4/13 | 4/13 |
| Unsupported claim flagged | 12/13 | 12/13 | 12/13 |
| Cannot answer | 0/13 | 0/13 | 0/13 |

The narrow full-key-coverage row does not require clean attribution or the
absence of unsupported-claim flags; it is not full sourced-answer correctness.

The route inputs contained 22/33 key-question source-chat references for A and
33/33 for both B and C. This is source-chat presence in the supplied material;
it does not prove that the answer model used a particular position.

## Citation and quote evidence

The blind grader scored key-point agreement, not the full requirement to cite
source chats and dates or reproduce exact quotes. The following checks use
literal title/date strings and Unicode-normalized quote substring matching.
They are not semantic citation judgments.

| Literal check | A | B | C |
|---|---:|---:|---:|
| Questions with at least two expected chat titles | 7/13 | 12/13 | 12/13 |
| Questions with at least two expected title/date pairs | 7/13 | 3/13 | 2/13 |
| Quoted answer spans found in expected source messages | 9/33 | 3/45 | 4/40 |

All 620 nonempty position quotes in the B export match contiguous spans in their
source messages (620/620). This supports extraction provenance; it does not
repair the answer routes' weak literal quote fidelity.

## Calls, token totals, and trace IDs

All calls finished without provider errors and recorded subscription-included
billing with $0 separately billed API cost. The scored comparison used 39 answer
calls and 13 judge calls. Two separate one-call grader controls are excluded
from scores: the preregistered campaign control and the independent C5 signoff
control.

| Group | Calls | Model | Total tokens | Recorded API cost | Trace IDs |
|---|---:|---|---:|---:|---|
| A answers (reused) | 13 | `codex/gpt-5.6-luna` | 1,980,739 | $0 | `inquiry-graph/xconv-scale-codex/answer-A/q01`–`q13` |
| B answers | 13 | `codex/gpt-5.6-luna` | 2,031,408 | $0 | `inquiry-graph/xconv-scale-codex-balanced-20260930/answer-B/q01`–`q13` |
| C answers | 13 | `codex/gpt-5.6-luna` | 1,612,072 | $0 | `inquiry-graph/xconv-scale-codex-balanced-20260930/answer-C/q01`–`q13` |
| Blind graders | 13 | `codex/gpt-5.6-sol` | 337,150 | $0 | `inquiry-graph/xconv-scale-codex-balanced-20260930/judge-q01`–`q13` |
| Positive/negative control | 1 | `codex/gpt-5.6-sol` | 25,019 | $0 | `inquiry-graph/xconv-scale-codex-balanced-20260930/grader-positive-control` |
| Fresh independent C5 control | 1 | `codex/gpt-5.6-sol` | 25,228 | $0 | `inquiry-graph/c5-balanced-signoff-20261001/grader-positive-control` |

Both controls gave the known-correct answer 2/2 with no contradiction and the
known-wrong answer 0/2 with a contradiction flag. The fresh signoff control
used the same subscription route and completed with no recorded error. The
trace database is metadata-only for these subscription calls.
`balanced_replay_summary.json` records aggregate totals and
`summarize_balanced_replay.py` recomputes them from the private per-question
files and metadata database.

The independent reviewer directly inspected the full Codex CLI trace for
`inquiry-graph/xconv-scale-codex-balanced-20260930/answer-C/q13` in the local
session store. Its input contains the matching q13 prompt and the full
positions-only export; its final structured answer matches the saved q13
answer, and it contains no tool calls. The raw trace stays in the local private
session store; its observability database row stores metadata only.

The runner supplied no explicit request timeout. Historical campaign lifecycle
rows nevertheless record a 300-second runtime safety value. Two calls exceeded
that value (305.031s and 996.640s), emitted `stalled` lifecycle events, and
later completed with `stop` and no call error. No scored call was observably
interrupted by that value; other transports' behavior at the ceiling was not
tested.

The summarizer's “fully right” count means full key-point coverage with no
contradiction. It does not require clean attribution or no unsupported-claim
flag, so it is not a measure of full sourced-answer correctness.

## Limits and final signoff

This replay uses one 30-chat corpus and 13 questions. The reference key was
generated using the full corpus, the grader shares the answer model family,
and the literal evidence audit cannot establish semantic source correctness.
The earlier comparison, in which B and C received all questions in one call,
is superseded for route choice because it confounded retrieval with batching;
see [`signoff-recheck-2026-09-30.md`](signoff-recheck-2026-09-30.md).

The independent C5 reviewer recomputed all 39 coverage scores and category
means, revalidated all 30 graphs, reran a fresh positive/negative control, and
hand-checked five grade/source cases across the five categories. Its bounded
decision is that typed links add 0 key-point coverage over positions alone
(B−C = 0.000) and the observed +0.038 B−A difference does not show that the
graph route beats search at scale. The required issue #38 comment is the final
C5 delivery step; the previous comment remains historical until the signed-off
result is posted.

Private transcripts, questions, answers, and quote-bearing outputs remain
under `private/xconv/scale_run_codex_balanced_20260930/` and the earlier A
source campaign. They are not reproduced in this report.
