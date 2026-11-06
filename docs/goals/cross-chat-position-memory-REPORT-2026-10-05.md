# Cross-chat position memory: cost and limits report (2026-10-05)

Counts and costs only; no quotes (quote-bearing data stays under gitignored `private/`).

## What exists

| Surface (behind the single-password gate) | Content |
|---|---|
| maps.brianmills.dev/interests-map.html | 2,264 chats from ChatGPT, Claude, Gemini; 5 zoom levels; 387 generated names; provider tag on hover |
| maps.brianmills.dev/positions/ | 19,587 quoted positions/questions from 1,719 chats; 3 zoom levels (22/54/127 named topics) |
| maps.brianmills.dev/chats/ | 1,999 chats as searchable idea graphs; stance tags (own words / pasted / unclear); dashed lines = second-pass links |
| browser.brianmills.dev | yFiles in JupyterLab through Voila (licence is Brian's call; see personal-vps apps/jupyter/README.md) |

## Snapshot reconciliation (C1)

`tools/reconcile_snapshot.py`, exit 0: 3,020 ChatGPT exporter files + 1,053 Kept files + 848 Claude export conversations = **4,921**, each with exactly one disposition:
extracted with Brian events 1,452; extracted without 338; excluded by interest filter 1,747 (admin/tool chores 699, INTEREST below 0.7 or legal 532, unclear 215, everyday 197, sensitive 104); agent-sent 467; too short (<200 chars of Brian text) 572; duplicates 303 (258 exporter, 45 Kept); no visible text 41; pending 1.

## Positions are source-grounded (C2)

Every quote is verified verbatim in a message Brian sent (10-chat slice: 0 of 1,353 anchors failed; 20-chat spot-check on a second model: 0 of 586). Authorship check (own words vs pasted) over all 19,587 events: 15,171 own words, 4,296 pasted or quoted, 120 unclear. Hand check of 30 labels: 26 right, 2 wrong or doubtful, 2 borderline (error roughly 7-13%, small sample).

## Answer (C4)

`tools/ask_positions.py`, question on build-versus-reuse, run on 15,291 own-words events: 6 claims, all citations resolve and quotes verbatim (code-checked); hand-read against the quoted evidence. It found a real change (2025 building own KG-RAG and agent coordination; Aug-Sept 2026 reuse-first) and says what the evidence cannot establish. A broad first question returned mostly "no strong change", which was honest but weak (retrieval is word-based). Known weaknesses: authorship labels miss mixed spans; retrieval is lexical.

## Costs

- OpenRouter this month (shared client log): extraction 8.19, second-pass linking 0.85, authorship check 0.54, map-label naming 0.30, topic naming 0.09, interest filter 0.06; **total about 10.05 USD**. Model for extraction/linking/authorship: `openrouter/openai/gpt-6-luna`.
- Codex subscription (0 USD API): about 700 chats extracted before the move to OpenRouter.
- Free rebuild of 2,100 graphs from cached model answers (link fix): 0 USD.

## Limits (read before relying on any number)

1. **Completeness is unproven for ChatGPT, Gemini and the two other ChatGPT accounts.** Official ChatGPT exports were requested 2026-10-05 for all three accounts; the main account's started 13:04, links not yet received. Gemini official export not downloaded (Takeout is 16 parts; a Gemini-only export is needed). Kept captured only about 7% of Claude (58 of 848) so its Gemini coverage (725 chats) is suspect.
2. The scheduled ChatGPT backup is **off** (tab pile-up, fixed in the exporter, extension must be reconnected first), so chats created after the last sync are not captured.
3. Interest filter judged titles only; 532 chats rated INTEREST were left out for confidence below 0.7 or legal topics.
4. Links: 45% of ideas had no link; now 3% after a second model pass, but those links are inferred and marked proposed.
5. Authorship error rate about 7-13%; mixed spans are the main failure.
6. Extraction model was only compared on a 10-chat and a 20-chat slice; the new model finds about 80% as many ideas as the earlier one but more of Brian's own positions.
7. No usefulness or comprehension claim: Brian has not reviewed the answer or the pages.

## Resume

`docs/goals/cross-chat-position-memory.md` has the handoff sections. Timer `chatgpt-export-watch` downloads the main account's export when it arrives; therakorski and montaguecantsin downloads need Brian to click the email link.
