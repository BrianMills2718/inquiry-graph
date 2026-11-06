# Usefulness pilot (issue #38): model reader, 2026-09-29

> **Interpretation updated after strategic review, 2026-09-29.** Measurements and the recorded method below are unchanged; this update did not rerun the experiment. The current product reader is an AI model, not a person navigating a graph. Earlier human-navigation recommendations are superseded by the [roadmap](../../docs/roadmap.md): improve rationale/outcome representation, rerun the AI-reader pilot, then test multi-conversation histories beyond one context window.

**Question:** when a model has to recover the state and history of an inquiry, does the inquiry graph help it more than the raw transcript or the curated excerpts the graph was built from?

**Result:** not in this pilot. The raw transcript gave the best answers. The graph report scored a little better than the plain excerpts it was built from, but this small sample does not establish a reliable advantage. This is a diagnostic result for one model, conversation and evaluation setup, not a general finding that structured inquiry memory cannot help AI readers.

| Condition | Material given | Size | Mean key points covered | Fully right (of 12) | Contradicts key | Said "can't answer" |
|---|---|---|---|---|---|---|
| A | Real transcript, visible text, same span as the graph | 367k chars | **0.81** | **7** | 1 | 0 |
| B | The 219 curated excerpts | 32k chars | 0.59 | 4 | 2 | 2 |
| C | The graph's readable report (`examples/seed/report.md`) | 79k chars | 0.65 | 5 | 0 | 1 |

No condition made attribution errors (Brian vs assistant) or treated an open question as settled in the scored sample. That absence does not establish an error-free attribution or closure mechanism.

## Where the graph lost

- **Reasons behind decisions.** For "why was Bronstein removed?" and "why was 'reframe' dropped?", the graph answers gave plausible but generic reasons, not the ones in the conversation. The graph records *that* something was rejected better than *why*.
- **What happened to side lines.** For "what happened to Hoel's coarse-graining line?", the graph answer said the material records no outcome. The transcript answer found it.
- **Where it held its own.** Attribution questions, deferred work, the order of revisions, and the open agenda: the graph matched the transcript on most of these.

## Method

1. **Aligning the conversation.** `prepare.py` cut the real ChatGPT thread ("Inference Beyond Observation") to the graph's span: 159 visible messages, 2026-09-26 23:35 to 2026-09-27 21:17. Each excerpt was matched to the first message containing it. Excerpts shorter than 30 characters were ignored, because lines like "Okay, do that." recur later in the chat.
2. **Questions.** `run.py` had the model write 14 questions with answer keys from the **transcript only**, two for each task type in issue #38. The 2 keys whose supporting quote was not verbatim in the cited message were dropped, leaving 12. Q1/Q11 and Q2/Q12 are near-duplicates, so there are about 10 independent questions.
3. **Answers.** The same model answered all 12 questions under each condition, using only that condition's material.
4. **Grading.** Grading was blind: the three answers were shuffled and labelled X/Y/Z before a judge scored them against the key's points. The answer model and the judge were the same model (`openrouter/openai/gpt-5.6-luna`), because the pilot's llm_client setup allowed only that one for synthesis and judging. The original pilot recorded a hand check of Q3, Q4, Q8 and Q11 that agreed with the grading overall, with the judge slightly harsh on the transcript answer for Q8. Blinding and this spot check mitigate some risks; they do not establish independent or unbiased adjudication. This strategic review did not repeat the hand check.
5. **Cost.** The three answering calls cost $0.035. The question and judge calls were not totalled.

## What this does not establish

- **General usefulness or lack of usefulness.** There were about 10 independent questions from one conversation that is also the tool's own design dialogue. No held-out multi-conversation evaluation was performed.
- **A budget-matched retrieval comparison.** The conditions had different sizes and information coverage. The graph gave approximately 80% of the transcript's score at roughly a fifth of the character count. Character count is not a measured token-cost, latency or end-to-end efficiency advantage. The pilot did not compare budget-matched transcript retrieval, compact summaries and graph-assisted retrieval.
- **Independent question selection and judging.** Questions were generated from the transcript, so their wording and keys follow its specific reasoning. That is realistic for rationale questions but may favor condition A. Answer and judge models were also the same.
- **Source completeness or adjudicated graph truth.** Matching an excerpt to the first containing message is a pilot alignment procedure, not final source reconciliation. Exact quotations do not prove every graph interpretation correct. The canonical seed's proposed review status is not changed by this experiment.

Human-reader navigation was not tested and is not a pending product success criterion. Human review of annotations and evaluation keys remains compatible with the AI-reader goal.

## What it means for the project

For this tested setting, use the transcript as the quality baseline rather than assuming the graph should replace it. The experiment identifies a representation/extraction/projection weakness in rationale and side-line outcomes; it does not isolate which stage caused the loss, and it does not demonstrate a failure of the foundational epistemic meta-model.

The next sequence under issue #38 is:

1. **Preserve reasons and outcomes explicitly.** Test annotations and report/query projection using the existing schema first. Add a schema primitive only if a concrete case cannot be represented faithfully. Do not infer a user's endorsement or closure merely from an assistant answer.
2. **Rerun and add held-out tests.** Keep the original questions as diagnostic regressions, not independent evidence after tuning against them. Add new conversations/questions, assess rationale, attribution, dependencies, open/deferred branches, false closure and source support, and separate answer generation from adjudication where practical. Report sample limitations and all relevant costs.
3. **Test the actual long-history use case.** Compare graph-assisted context assembly with transcript retrieval and compact-summary baselines under comparable context budgets across conversations exceeding one window. Preserve source/actor/context distinctions. Cross-source identity/alignment and governed tensions belong in the downstream `onto-canon6` direction specified by the roadmap, not a second canonical store inside Inquiry Graph.

A useful outcome may be a hybrid retrieval design or continued use of transcripts. The graph must earn its extra complexity; human navigation is not an alternative success target. Source reconciliation in issue #3 improves validity but need not block clearly labelled exploratory experiments.

## Reproduce

```bash
# needs llm_client (Brian's shared LLM client, OPENROUTER_API_KEY) and the thread
# transcript at private/usefulness/founding-chat.md (not committed)
python evaluation/usefulness_pilot/prepare.py
python evaluation/usefulness_pilot/run.py   # stages are cached in private/usefulness/
```

The questions, answers and grades are in `data/`.

## Follow-up 2026-10-11: report with reasons as text

**Question.** The pilot named "keep reasons and outcomes, not just labels" as the graph report's clearest weakness. Before this change, `report()` printed motivates/supersedes relations and move inputs/outputs as node IDs. It now prints them as sentences with the node text: "Y — because: X", "B — was replaced by: A", move inputs and outputs as clipped text, all under a "Decisions and reasons" section. Does that close the gap to the transcript?

**Method.**
- **What changed.** Only condition C was re-run. The pilot-era graph (commit `45b1e82`, the graph the original C report came from; the old renderer reproduces that report byte for byte) was rendered with the new `report()`, giving condition C2 (146k characters, against 79k before).
- **What was reused.** The saved 12 questions and answer keys, and the saved A and B answers. No questions were regenerated.
- **Answering.** The same answer prompt, with model `codex/gpt-5.6-luna` through Brian's Codex subscription, not OpenRouter.
- **Grading.** The same blind three-answer judge prompt and shuffle seed, run twice through the same Codex route: once over (A, B, C2) and once over (A, B, old C). Old and new C were therefore graded by the same judge.
- **Comparability.** The model is the one the pilot used, but the route differs, so the Codex grades are not strictly comparable with the saved OpenRouter grades. The like-for-like comparison is between the two Codex runs.

**Result.** Mean key-point coverage, with fully-right answers out of 12 in brackets:

| Judge run | A transcript | B notes | C graph report |
|---|---|---|---|
| Saved pilot (OpenRouter judge) | 0.81 (7) | 0.59 (4) | old C 0.65 (5) |
| Codex judge, old C | 0.79 (6) | 0.56 (3) | old C 0.63 (3) |
| Codex judge, new C2 | 0.78 (6) | 0.53 (4) | **C2 0.62 (3)** |

Rendering reasons as text did not improve answers: C2 scored 0.62 against old C's 0.63 under the same judge, a tie within the judge's own run-to-run noise. A's identical answers moved by 0.01 between the two Codex runs, and B's by 0.03. Per question, C2 gained on q4 (0.33 to 0.67) and q10 (0.5 to 1.0), and lost on q2 (1.0 to 0.33) and q8 (0.67 to 0.33). The transcript still leads, by about 0.16.

**Every C2 miss, read against the answer, the grade and the C2 report text.** The judge's output has no rationale field, so each classification below comes from comparing the key points with the answer and the report:

| Q | C2 | Classification | Evidence |
|---|---|---|---|
| q3 Bronstein removed | 0/3 | mostly **not in report** | The report keeps "not part of the foundational spine merely because it was suggested earlier" (the answer used it). It lacks "assumes known geometric structure" and any link saying Pattern Theory was closer. |
| q8 Hoel line | 1/3 | **not in report** | The report says only "raised as related work". The deferral and the "revisit later" were never extracted. |
| q6 assumed vs known | 2/3 | **not in report** | The report has the correction and its distinction. Its use in the white-box/black-box formalization is absent. |
| q11 next step on primitive actions | 1/3 | **not in report** | The report has no candidate action list (accept, select strategy); the answer used the ones it had (derive, retain, raise support). |
| q1 open primitive actions | 2/3 | **in report, unused** | The warrant/license question is in the report, but the answer did not tie the open issue to that refactor. |
| q2 combining warrants | 1/3 | **in report, unused** | The open-agenda question is present in both reports. Old C's answer linked it to graded rho; C2's did not. "Hard acceptance" is in neither report. |
| q4 reframe removed | 2/3 | **key/grade questionable** | The answer says "dialogue-level macro … decomposed", which matches the key's third point; the judge did not credit it. |
| q5 factorization uniqueness | 3/4 | **key/grade questionable** | "Not absolute … for a fixed representation" paraphrases "not representation-independent". |
| q7 meta-strategy | 2/3 | **key/grade questionable** | The answer covers the proposal, its layer and Brian's recursive-modeling response. |

In total, 4 misses are reasons the graph never extracted, 2 are reasons the report holds but the answer did not use, and 3 are borderline grades. The remaining gap therefore lies mainly in **extraction** (what the annotation records as a reason or a disposition), not in how the report prints relations.

**Limits (unchanged).** This is one conversation and about 10 independent questions. The questions were written from the transcript, which favours A. The same model answers and judges. One run per condition.

**Reproduce:** `USEFULNESS_PRIVATE_DIR=<private/usefulness> python evaluation/usefulness_pilot/followup.py` (stages cached; results in `data/followup_summary.json`, `data/answers_C2.json`, `data/grades_followup_*.json`).
