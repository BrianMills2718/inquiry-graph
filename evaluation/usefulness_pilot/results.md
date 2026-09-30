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
