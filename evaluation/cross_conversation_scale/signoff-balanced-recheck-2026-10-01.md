# Independent C5 balanced replay signoff

**Verdict: SIGNED-OFF for the bounded disposition.** The balanced replay supports keeping the typed linker as a bounded research/topic-map source, while making no general-scale claim that B beats search or that links improve key-point coverage over positions alone. It does not support productizing an answer route under the observed source-citation and quote performance.

This verdict is about the evidence-based disposition. The goal's separate C5 delivery criterion also calls for a comment on inquiry-graph issue #38 (`docs/goals/cross-conversation-linker.md:74`). Posting was outside this reviewer's assigned scope; parent-goal delivery remains pending.

## Highest-impact findings

1. **The answer route still fails the sourced-answer bar.** Direct literal checks reproduced only 3/13 B and 2/13 C questions with at least two expected title/date pairs; expected-source quote spans matched only 3/45 B and 4/40 C. All three routes had unsupported claims flagged on 12/13 answers. This is consistent with the published evidence and rules out productizing an answer route on this replay (`results.md:90-115`).
2. **The evidence does not show an advantage from typed links over positions alone.** I independently recomputed all 39 route/question coverage fractions. Means were A 0.647436, B 0.685897, C 0.685897: B−A = +0.038462 and B−C = 0. The shared 13-question set came from the full corpus; seven source-heldout questions are not an independent question-set holdout (`balanced-replay-2026-09-30.md:15-18, 42-44`). Do not generalize B's small descriptive difference over A to scale.
3. **“Fully right” is narrower than full answer correctness.** The saved aggregate calls an answer fully right when it has full key-point coverage and no contradiction; the summarizer does not require clean attribution or no unsupported-claim flag (`summarize_balanced_replay.py:224-230`). In q12, B and C each cover all four key points with no contradiction, yet both also carry attribution-error and unsupported-claim flags. Use the separate citation and unsupported-claim evidence when judging answer suitability.
4. **The archived observability database does not contain the campaign call bodies.** All 39 answer calls and 13 blind graders use `metadata_only` persistence with empty body fields. This is not the same as having no inspectable body at all: I independently inspected the named local C q13 Codex session at `/home/brian/.codex/sessions/2026/09/30/rollout-2026-09-30T20-38-06-01a0f4e5-a65c-7ba0-aa14-2d5268febffe.jsonl`. It contains a full user input and assistant output; the saved C q13 answer is present as a substring of that output. Session metadata identifies the linker worktree, Codex CLI, and `gpt-5.6-luna`; the local JSONL does not contain the campaign trace ID. I therefore count one directly inspectable local model body, not 39 persisted bodies and not a trace-ID-linked database body. The goal's “inspect at least one full trace” evidence gate is met by that direct session inspection (`results.md:138-143`; `docs/goals/cross-conversation-linker.md:76`).

## Recomputed score evidence

I read the private reference key, A source campaign, all B/C answer files, all blind grade files, and the saved summary. I recomputed each score as `min(points_covered, key_points) / key_points`; all 39 scores below match the saved per-question table (`results.md:52-84`). No question, answer, transcript, or quote text is reproduced here.

| Q | Category | Key points | A | B | C |
|---:|---|---:|---:|---:|---:|
| 1 | Agreement | 4 | 1.000 | 1.000 | 1.000 |
| 2 | Agreement | 3 | 0.667 | 0.667 | 0.667 |
| 3 | Agreement | 4 | 0.750 | 0.750 | 0.750 |
| 4 | Conflict/tension | 4 | 1.000 | 0.750 | 0.750 |
| 5 | Conflict/tension | 4 | 0.750 | 0.500 | 0.500 |
| 6 | Conflict/tension | 4 | 0.750 | 0.500 | 0.750 |
| 7 | Recurring open | 4 | 0.000 | 0.500 | 0.250 |
| 8 | Recurring open | 4 | 0.500 | 0.500 | 0.500 |
| 9 | Recurring open | 4 | 0.500 | 0.500 | 0.500 |
| 10 | Change over time | 4 | 0.500 | 0.500 | 0.750 |
| 11 | Change over time | 4 | 1.000 | 0.750 | 0.750 |
| 12 | Position summary | 4 | 0.000 | 1.000 | 1.000 |
| 13 | Position summary | 4 | 1.000 | 1.000 | 0.750 |
| **Mean** | **All 13** | — | **0.647436** | **0.685897** | **0.685897** |

Recomputed category means (A/B/C): Agreement 0.805556/0.805556/0.805556; Conflict/tension 0.833333/0.583333/0.666667; Recurring open 0.333333/0.500000/0.416667; Change over time 0.750000/0.625000/0.750000; Position summary 0.500000/1.000000/0.875000.

The saved flags also reproduce: full coverage with no contradiction 4/13, 3/13, 2/13; contradictions 5/13, 3/13, 5/13; attribution errors 2/13, 4/13, 4/13; unsupported claims 12/13 for each route; cannot-answer 0/13 for each. The first row is the summarizer's narrow “fully right” proxy noted above, not full answer correctness.

## Identity, completeness, controls, and provenance

- **Question/key/label identity:** 13 retained questions, 2 dropped; categories are 3 agreement, 3 conflict/tension, 3 recurring-open, 2 change-over-time, and 2 position-summary. The 51 key points and all 78 question-position references (65 unique) resolve among the 30 per-chat key-position files. I checked the saved answer trace IDs for q01–q13 on each route, all 13 grade IDs, route identities, and blind-label mapping. Replaying the recorded seed (59) reproduced all 13 label assignments; every X/Y/Z grade maps back to its recorded route.
- **Graph validation:** Re-ran the validator for all 30 keyed source graphs: 30 valid, 0 errors; command loop exit status 0. The source key contains 581 retained position quotes; all 620 nonempty B-export position quotes match contiguous spans in their source messages (620/620), consistent with the separate extraction-provenance check.
- **Answer, grade, and call counts:** 39 scored answers (13 each A/B/C), 13 blind graders, and one original paired grader control. A's 13 reused answer calls were in the source campaign database. B/C/J/control have 40 corresponding rows in the balanced campaign DB. The fresh signoff control below is a separate call. All answer rows used `codex/gpt-5.6-luna`; graders and controls used `codex/gpt-5.6-sol`. Combined recorded totals across A, B, C, graders, original control, and fresh signoff control were 6,011,616 tokens, $0 separately billed API cost, `subscription_included` billing, zero call errors, and `stop` finish reason for all 54 call rows.
- **Fresh control:** I ran the preregistered two-point known-correct/known-wrong grader shape with unique trace `inquiry-graph/c5-balanced-signoff-20261001/grader-positive-control`. Readback from its private artifact and call/lifecycle DB: `codex/gpt-5.6-sol` over `codex-cli`, 25,228 tokens, $0 recorded cost, `subscription_included`, zero errors, `stop`; correct case 2/2 with no contradiction; wrong case 0/2 with contradiction; `passed=true`. The request supplied no `max_tokens`, `max_output_tokens`, or explicit timeout. Lifecycle recorded `requested_timeout_s=0`, `provider_timeout_s=NULL`, `timeout_policy=ban`. The control's observability row is `metadata_only` with no body persisted. Readback check: passed 1, failed 0, total 1, exit status 0. The campaign's original control also passed 2/2 and 0/2 with the expected contradiction outcomes (`results.md:132-136`).
- **Source availability:** The key's 33 expected source-chat references were available 22/33 in A's question-specific inputs and 33/33 in each B/C full export. This is input presence, not proof a model used a source (`results.md:96-98`).
- **Literal citation/quote recomputation:** At least two expected chat titles: A 7/13, B 12/13, C 12/13. At least two expected title/date pairs: A 7/13, B 3/13, C 2/13. Answer quote spans found in expected source messages: A 9/33, B 3/45, C 4/40. These literal checks are not semantic citation judgments (`results.md:100-115`).
- **Five direct answer/grade/key/source checks:** I independently hand-checked q02 (agreement), q05 (conflict/tension), q07 (recurring open), q10 (change over time), and q12 (position summary). In each I traced a selected key position ID to its source message, checked that the saved quote matched the source span, and compared the saved answer and blinded grade/label record to the key. The q12 check exposed the metric limitation above: B/C had full point coverage while both retained attribution and unsupported-claim flags. No raw content was copied.

## Timeout interpretation and gate result

The runner passes no `timeout` option (`balanced_replay.py:149-150`; `scale.py:149-175`), so the plan's “no request timeout” condition was met in the caller-explicit sense. The lifecycle database nevertheless records `provider_timeout_s=300` and `timeout_policy=ban` across the historical campaign. In the shared client, this 300-second value is the runtime safety ceiling, distinct from `requested_timeout_s`; it is independent of the caller timeout policy (`llm_client/execution/call_lifecycle.py:127-145`; `llm_client/execution/timeout_policy.py:157-179`). It is therefore accurate to say “no explicit request timeout was passed,” but not “the runtime had no finite timeout metadata or safety behavior.”

No campaign call was observably interrupted by 300 seconds: all 13 A calls and all 40 balanced-campaign calls ended with `stop`, no call errors, and a recorded result. Two balanced calls had latency above 300 seconds (305.031s and 996.640s) and corresponding `stalled` lifecycle events before their later completion. This demonstrates that the metadata value did not cut off those Codex CLI calls; it does not prove how every transport/backend behaves at the ceiling. I treat this as a disclosed runtime-policy ambiguity, not an observed truncation or failed scoring/completeness gate. The fresh signoff control explicitly disabled the shared safety ceiling (`LLM_CLIENT_SAFETY_TIMEOUT=0`) in its isolated process.

**Material gate result:** the preregistered completeness, grader-control, score-reproduction, source-integrity, and one-full-trace gates pass. No evidence shows a 300-second timeout interrupted or truncated a scored call. If “no request timeout” is interpreted to prohibit even shared runtime safety metadata, that wording was not satisfied literally; the no-explicit-caller-timeout reading is satisfied, and no observed result gate fails. The sample/key construction prevents a scale claim regardless.

## Representation disposition

The reviewer use case is to decide whether the replay supports the bounded disposition and trace each material claim to evidence. The router recommended a requirements-traceability matrix, with a data table as an alternative. I used a static, labeled A/B/C per-question table as the primary comparison and kept the verdict first, followed by limitations, category outcomes, and gate evidence. This fits the exact 39-value comparison and read-only one-off deliverable; an interactive map would add no needed operation. The use case has 54 items against the router's 40-object one-screen budget, so the report is intentionally multi-section; one-screen fit and a cold-reader timing claim are not asserted. The existing `results.usecase.json`, `results.recommendation.json`, and `results.disposition.json` cover the C4 comparison report, not this signoff's control, timeout, and full-trace gates, so I recorded a content-free signoff disposition at [signoff-balanced-recheck-2026-10-01.disposition.json](signoff-balanced-recheck-2026-10-01.disposition.json). Its router disposition check accounted for 79 entries: 10 satisfied, 54 not applicable, and 15 skipped; exit status 0.

## Signoff limits

This is one 13-question evaluation over a question set generated from the full corpus, and the five hand checks do not turn it into a representative sample. Source-chat presence and quote provenance do not prove model use or answer attribution. The balanced call database is metadata-only; the separate q13 local session proves direct body availability for one case only. No tests were used as a proxy for evaluation. The issue #38 comment remains outside this reviewer's assigned scope; parent-goal delivery is pending.

**Disposition:** continue the typed linker only as a bounded research/topic-map source. Do not claim B beats search at scale or that links improve key-point coverage over positions only. Do not productize an answer route under the current citation/quote performance.
