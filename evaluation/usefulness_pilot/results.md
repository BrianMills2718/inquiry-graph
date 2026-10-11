# Usefulness pilot (issue #38): model reader, 2026-09-29

**Question:** when a model has to recover the state and history of an inquiry, does the inquiry graph help it more than the raw transcript or the curated excerpts the graph was built from?

**Result:** no, not for a long-context model reader. The raw transcript gave the best answers. The graph report did a little better than the plain excerpts it was built from, but with this few questions that gap is within noise.

| Condition | Material given | Size | Mean key points covered | Fully right (of 12) | Contradicts key | Said "can't answer" |
|---|---|---|---|---|---|---|
| A | Real transcript, visible text, same span as the graph | 367k chars | **0.81** | **7** | 1 | 0 |
| B | The 219 curated excerpts | 32k chars | 0.59 | 4 | 2 | 2 |
| C | The graph's readable report (`examples/seed/report.md`) | 79k chars | 0.65 | 5 | 0 | 1 |

No condition made attribution errors (Brian vs assistant) or treated an open question as settled.

## Where the graph lost

- **Reasons behind decisions.** For "why was Bronstein removed?" and "why was 'reframe' dropped?", the graph answers gave plausible but generic reasons, not the ones in the conversation. The graph records *that* something was rejected better than *why*.
- **What happened to side lines.** For "what happened to Hoel's coarse-graining line?", the graph answer said the material records no outcome. The transcript answer found it.
- **Where it held its own.** Attribution questions, deferred work, the order of revisions, and the open agenda: the graph matched the transcript on most of these.

## Method

1. **Aligning the conversation.** `prepare.py` cut the real ChatGPT thread ("Inference Beyond Observation") to the graph's span: 159 visible messages, 2026-09-26 23:35 to 2026-09-27 21:17. Each excerpt was matched to the first message containing it. Excerpts shorter than 30 characters were ignored, because lines like "Okay, do that." recur later in the chat.
2. **Questions.** `run.py` had the model write 14 questions with answer keys from the **transcript only**, two for each task type in issue #38. The 2 keys whose supporting quote was not verbatim in the cited message were dropped, leaving 12. Q1/Q11 and Q2/Q12 are near-duplicates, so there are about 10 independent questions.
3. **Answers.** The same model answered all 12 questions under each condition, using only that condition's material.
4. **Grading.** Grading was blind: the three answers were shuffled and labelled X/Y/Z before a judge scored them against the key's points. The answer model and the judge are the same model (`openrouter/openai/gpt-5.6-luna`), because llm_client allows only that one for synthesis and judging. That risk is limited by blinding, and by a hand check of Q3, Q4, Q8 and Q11, where the grades matched my own reading. On Q8 the judge was slightly harsh on the transcript answer.
5. **Cost.** The three answering calls cost $0.035. The question and judge calls were not totalled.

## What this does not test

- **Bias toward the transcript.** The questions were written from the transcript, so their wording and key points follow its specific reasoning. That is realistic ("why did we drop X?"), but it favours condition A.
- **Human readers.** Nobody reads 367k characters to resume work. The graph's likeliest value is for a person scanning the open agenda, which this pilot did not measure.
- **Size and speed.** The graph gave 80% of the transcript's score at about a fifth of the size. That matters only if the transcript doesn't fit in the model's context, or reading it costs too much.
- **Sample size.** About 10 independent questions, from one conversation that is also the tool's own design dialogue.

## What it means for the project

- **For AI-assisted resumption, give the model the transcript.** The graph doesn't earn its complexity there.
- **For the graph to justify itself,** it has to win on one of two things:
  - human navigation: time to find the open questions or the reason for a decision, with a person reading;
  - histories too long for the context window, e.g. many conversations combined.
- **It should keep reasons and outcomes, not just labels.** That was its clearest weakness here, and it's a cheap schema or annotation fix to test next.

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
