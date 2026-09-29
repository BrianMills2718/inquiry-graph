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
