# Cross-conversation positions proof: results (2026-09-29)

**Goal:** `docs/goals/cross-conversation-positions.md`.

**Question:** can an AI find Brian's positions, open questions and conflicts across his conversations better through inquiry-graph + onto-canon6 than by reading the conversations?

**Answer:**
- **inquiry-graph's extraction pays for itself.** Brian's extracted positions (each with a verbatim quote) answered cross-chat questions as well as reading all five chats in full, at about 1/20 of the cost and 1/14 of the tokens.
- **onto-canon6 added nothing measurable.** It found no cross-chat identity and no conflict. Its notion of identity (the same claim restated) and of conflict (the same claim held with different stances) doesn't match how Brian's views relate across chats: they are related, extended and reworded, rarely restated.

**Decision: replace.**
- Keep inquiry-graph as the per-conversation producer.
- Replace "same claim" alignment with a relation-typed cross-chat linker (related / agrees / pulls against / evolves). Carry question status and chat dates into the export.
- Test next at a scale where reading everything does not fit.

## The five chats

| Chat | Dates | Visible chars | Brian stances extracted |
|---|---|---|---|
| Inference Beyond Observation (`6ab8563b`) | 26–29 Sep | 466k | 52 |
| Conceptualizing Inference Models (`6ab96260`) | 27–29 Sep | 223k | 23 |
| Conspiratorial Ideation Factors (`69c07755`) | 22 Mar | 46k | 13 |
| algorithmic ingress (`6a988a7a`) | 2–3 Sep | 378k | 29 |
| Polemologist Peircean Metis Enthusiast (`6a171ac3`) | 27–28 May | 320k | 31 |

The chats were chosen by a subagent through archive search, to overlap the founding chat's topics and contain Brian's own substantive messages. They were read through the chatgpt-bridge. Transcripts stay in gitignored `private/`.

## C1 — live extraction

- **Code:** `extract --llm` through `llm_client`, prompt `live-2.2.0`.
- **Cost and size:** $0.23 for all five chats (55 chunks). Every graph validates with 0 errors.
- **Traces:** `inquiry-graph/live-extract/<chat>/chunkNN`. The founding chat's 17 traces all show `finish_reason=stop` with 0 errors.
- **Spot check** of 12 random Brian stances per prompt round:
  - v2.0: 9/12 right;
  - v2.1: 0 wrong, 4 procedural;
  - v2.2: 11/12 right, 0 procedural.
- **Grounding:** speaker attribution is enforced by code. Formatting-insensitive quote realignment raised node grounding from 43% to about 80%.

## C2 — reference key, independent of the system

- **How it was built:** `build_key.py` has a model read each whole chat and list Brian's positions and open questions, each quoting one of his own messages. Code verified every quote.
- **Positions:** 103 kept, 12 dropped because the quote was not in a Brian message.
- **Questions:** a second pass wrote 12 cross-chat questions. Each cites verified positions from at least 2 chats (position summaries may use one); 12 kept, 0 dropped. Categories:
  - 3 agreement;
  - 3 conflict or tension;
  - 2 recurring open question;
  - 2 change over time;
  - 2 position summary.
- **Cost:** $0.14. Traces: `inquiry-graph/xconv-key/…`.

## C3 — export into onto-canon6 (pinned `6864aa16c2f38270b0812302c2154391866a4f11`)

- **Route:** `export_oc6.py` uses only the public API. Each Brian stance becomes `ig:holds_stance(holder=brian, stance, proposition)`, with the proposition as an entity whose id is its alignment cluster.
- **Result:** all 148 stances were accepted as valid under `general_purpose_open`, then auto-accepted and promoted (labelled `inquiry-graph:auto-accept`; **not human review**). 0 rejected.
- **Carried:**
  - speaker;
  - stance;
  - proposition identity;
  - the exact evidence span (verified by onto-canon6 against the source text);
  - source message text and id;
  - chat and stance id.
- **Lost by this export:**
  - question-status events (open, deferred, resolved);
  - relations between nodes;
  - assistant stances;
  - chat dates.
- **Packaging defect:** a GitHub install of onto-canon6 cannot find its own `profiles/`, `ontology_packs/` or `config/`. The export ran with `ONTO_CANON6_HOME` pointing at those folders extracted with `git archive` from the pinned commit.

## C4 — cross-chat identity and conflict

- **Alignment:** the alignment extension's embedding recall plus its typed restatement judge. 146 propositions produced 122 recalled pairs, of which the judge accepted 3.
- **Clusters:** 3 multi-member clusters, all within a single chat. **0 cross-chat propositions.**
- **Tensions:** the epistemic extension reported 2, both within one chat, differing only in stance, and neither opposed (posits vs rejects). **0 cross-chat conflicts.**
- **Why:** the closest cross-chat pairs (cosine 0.56–0.59) are related positions, not restatements. For example, "inference may form a ladder from regularities to mechanisms" against "inference should be modelled as a multidimensional framework". The judge was right to call them different.
- **What the tension engine does:** it is a role-filler conflict test (same predicate, shared entity anchor, differing fillers). It can only find the *same* proposition held with different stances.

## C5 — head-to-head (12 key questions, blind-graded)

| Route | Material | Key points covered | Fully right | Contradicts | Attribution errors | Unsupported cross-chat claims | Answer cost |
|---|---|---|---|---|---|---|---|
| A: all 5 full transcripts (best case for "search, then read") | 1.43M chars, 335k tokens | 0.56 | 2 | 1 | 1 | 5 | $0.170 |
| B: onto-canon6 export of Brian's positions | 80k chars, 24k tokens | 0.58 | 1 | 1 | 1 | 6 | $0.008 |

**By category** (A vs B, mean points):

| Category | A | B |
|---|---|---|
| Agreement | 0.89 | 0.81 |
| Conflict | 0.64 | 0.64 |
| Recurring open question | 0.25 | 0.25 |
| Change over time | 0.29 | 0.58 |
| Position summary | 0.50 | 0.50 |

**Hand check:** Q2, Q6, Q7 and Q9 were read against their answers, and the grades are fair. Neither route found the "wet sidewalk" example or the agentic-deduction point in Q7. B caught the shift toward extending OntoCanon in Q9, which A missed.

## Caveats

- **Shape bias toward B.** The key was built from per-chat *position lists*, and route B *is* a position list, so the similar shape may favour B. Route A saw the raw text the positions came from.
- **One model does everything.** It writes the key, answers and grades, because `llm_client` allows only one synthesis/judging model (`openrouter/openai/gpt-5.6-luna`). Grading was blind (routes shuffled, labelled X/Y).
- **Small sample.** 12 questions over 5 chats. The tie between A and B is within noise; the cost difference is not.
- **A is a best case for search.** It could read every chat in full. At archive scale (hundreds of chats) that route no longer fits a context window, while B's size grows only with the number of positions.

## Reproduce

```bash
# chats: chatgpt-bridge read_chatgpt_chat → private/xconv/<id8>.md
inquiry-graph import-bridge private/xconv/<id8>.md private/xconv/<id8>.conv.json
inquiry-graph extract private/xconv/<id8>.conv.json private/xconv/<id8>.graph.json --llm --report private/xconv/<id8>.report.json
python evaluation/cross_conversation/build_key.py
ONTO_CANON6_HOME=<git archive of pinned onto-canon6: config profiles ontology_packs> \
  <onto-canon6[authoring] env>/python evaluation/cross_conversation/export_oc6.py
python evaluation/cross_conversation/compare.py
```

`data/` holds the non-quoting outputs: `summary.json` (per-question scores) and `loss.json` (the export loss report and counts).
