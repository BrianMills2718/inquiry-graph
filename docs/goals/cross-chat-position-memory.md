# Cross-chat Position Memory and Map

## Goal

**Mission:** Build a private AI that knows Brian's positions across a reconciled snapshot of his chat conversations (ChatGPT, plus Claude and Gemini via Kept or official exports), finds gaps, open questions, conflicts, and changes over time, and provides a map Brian can open by inquiry or across topics.

**Execution profile:** `continuous-light`

**Stage and investment boundary:** Private research prototype over one dated archive snapshot. The accessible local catalog currently has 1,728 threads, but its completeness and extraction cost have not yet been established. Estimate cost after validating corpus membership and a small representative extraction slice; do not infer it from the 30-chat run.

**Canonical example:** Given the reconciled archive snapshot and the question, “Where have my views on X changed or pulled against each other, and which questions do I keep leaving open?”, the AI returns source-grounded positions with exact quotes, chat titles, and dates, notes supported changes/conflicts/open questions, and opens a map built from that same snapshot with individual inquiries and a combined topic view.

**Forbidden substitutes:** Presenting the 30-chat sample or the 1,728-row local catalog as a complete account archive without reconciling it; treating assistant text as Brian's position; unsupported summaries without source quotes and chat/date; hand-authored positions or reference keys; a map that omits archive records silently; a component demo without the archive-backed map and answer example.

**Repository / working scope:** `BrianMills2718/inquiry-graph` produces and validates per-chat graphs, the cross-chat position store, and the private map. The merged `shared_ui` relation viewer is a read-only dependency. `onto-canon6` and `epistemic-warrant` remain read-only.

## Boundaries

- **In scope:** Reconcile a dated archive snapshot; extract and validate source-grounded positions and open questions; build a combined map with per-inquiry views; deliver one real archive-grounded answer path for the canonical question; report source coverage, known gaps, and actual cost.
- **Out of scope:** Continuous syncing of future chats, a production answer route, public or ungated release, changing `onto-canon6`, and broad A/B/C benchmarking beyond a decision-changing uncertainty.
- **Writes allowed:** Inquiry Graph branches and PRs; quote-bearing source data and generated pages only under gitignored `private/`.
- **Read-only or externally owned:** ChatGPT bridge is read/search only. Do not send messages, rename, move, tag, reload, or reorganize chats. Use `shared_ui` exports as a dependency; do not modify that repository under this goal.
- **Private hosting (added 2026-10-03, Brian):** quote-bearing pages may be served only from the single-password-gated hosts `maps.brianmills.dev` and `browser.brianmills.dev` (personal-vps repo, apps/maps and apps/jupyter). yFiles runs only inside JupyterLab or Voila (Voila is Brian's call; see personal-vps apps/jupyter/README.md).
- **Irreversible actions requiring authorization:** None expected. Never commit transcripts or quote-bearing outputs; never publish ungated.

## Acceptance Checks

| ID | Criterion | Evidence to report |
| --- | --- | --- |
| C1 | Archive snapshot reconciled | A dated source inventory identifies every conversation as processed, no-position, failed, or explicitly excluded; totals reconcile with the authoritative snapshot count. Do not report full coverage from a retrieval sample or local catalog count alone. |
| C2 | Position memory preserves evidence | Every surfaced position/question has Brian attribution, exact source quote, conversation identity, title, and date; graph validators pass; report completeness warnings and source checks on a sample spanning conversations and dates. |
| C3 | Map covers the reconciled snapshot | Per-inquiry and combined-topic views derive from the same snapshot; membership and counts reconcile to C1; desktop and mobile browser renders load from the private generated page. |
| C4 | The AI answers the canonical example | One authentic traced run answers from the position memory, cites the original conversations, and identifies only supported changes/conflicts/open questions; resolve every citation against source and hand-check the answer's material claims. Inspect the full trace directly. |
| C5 | The completion report names limits | Report the exact snapshot, included/excluded/failed counts, costs, validators, browser evidence, and any unprocessed or uncertain source class. An unresolved archive discrepancy is a blocker, not full success. |

For every LLM behavior claim, include the trace identifier and inspect at least one complete trace. Do not cap model output or use a different provider as a workaround for a billing/capacity error.

## Increments

1. **Reconcile the archive snapshot:** inspect the existing 1,728-thread catalog, raw transcript inventory, project coverage, completeness warnings, and sync state. The catalog IDs now match embedded IDs in all raw transcript files; one filename differs from its embedded ID. Compare that reconciled local inventory to an authoritative export or exhaustive account count. This retires the remaining uncertainty about what “all chats” means for this run.
2. **Validate extraction readiness:** choose a small source-diverse set from the reconciled archive, validate graph provenance and current extractor behavior, inspect the full LLM trace, and estimate actual full-run cost before scaling.
3. **Extract the reconciled snapshot:** process all included conversations through the current structured-output extractor, preserving explicit empty/failure dispositions and quote provenance.
4. **Generate the archive-wide map:** build the combined topic overview and per-inquiry views from the extracted snapshot using the merged relation viewer.
5. **Deliver the AI answer example:** retrieve relevant positions, answer the canonical question, resolve citations, and inspect the complete trace.
6. **Report disposition:** summarize coverage, remaining known gaps, costs, map location, and whether a new extraction or answer-route decision is justified.

## Loop Bounds

- **No-progress stop:** 3 attempts on the same reproduced archive-access, extraction, or validation blocker with no new evidence or safe next action.
- **Finite bound:** 6 substantive increments; if the archive reconciliation or source format requires another phase, revalidate the outcome before adding it.
- **Strategy revalidation:** after 3 substantive increments, roughly 4 hours, twice the stage estimate, or an outcome reset.
- **Revalidation readout:** compare user-visible archive-backed answers/map coverage with enabling work and process work; recommend `retain`, `replace`, or `clear`.
- **Exact blocked resume event:** reconcile the local catalog and transcript files with an authoritative archive snapshot; if Brian must download an export, state the exact steps in the session closeout.

## Non-Gating Next Actions

- Ingest conversations created after the dated snapshot or add continuous sync.
- Asking yWorks to allow-list the domain.
- Adopt Jev or Laya as an open-ended extractor. The bounded disposition in `docs/goals/cross-conversation-linker.md` keeps the structured-output extractor; reopen only under its recorded same-input evidence condition.
- Make a product answer-route or general superiority claim from the one-corpus C5 result.

## Current State

- **Demonstrated:** The 30-chat linker evaluation is complete; the private map is generated and visually loaded with the merged shared viewer. The page has 30 conversations, 620 positions, 27 interpretive topics, and 233 typed links; it is not an archive-wide result.
- **Local archive inventory (2026-10-01):** The catalog at `chatgpt-conversation-manager-v0.2/data/metadata/catalog.json` records 1,728 threads and there are 1,728 valid raw transcript JSON files. The embedded `thread_id` values form an exact one-to-one match with catalog records; one filename differs from its embedded ID. All 30 map-corpus chat IDs are present in the catalog. It contains 153 project-associated threads and 22 completeness warnings (1,718 API captures and 10 DOM captures). This reconciles the local catalog to its transcript files, not to a complete account snapshot.
- **Access and sync:** The live recent-chat tool returned 100 non-Project chats at its maximum. Project-inclusive listing failed twice with HTTP 422 from the Projects sidebar path. The connector repo has a paginated bulk-sync path for `/backend-api/conversations` (50 per page, deduplicated by thread ID). Its last successful run on 2026-09-29 listed 1,246 unique threads, while the current local catalog has 1,728; the next recorded attempt on 2026-09-30 failed with HTTP 429. Project inclusion and the 1,728-thread catalog have not been reconciled to a complete account snapshot.
- **Model route:** The 30-chat OpenRouter run stopped at insufficient account credits. A separate Codex CLI 0.159.3 campaign completed over the same 30-chat sample using `codex/gpt-5.6-luna` for position extraction and `codex/gpt-5.6-sol` for answer judging; its local readout records 581 verified positions and 13 cross-chat questions. This remains a sample result, not archive-wide coverage. The campaign used the CLI's read-only sandbox; a separate synthetic probe now confirms a custom deny-by-default profile can expose one allowed directory and block an adjacent directory, but that stricter profile was not used for the completed campaign. The full trace inspection required by C4 remains open. Inquiry Graph still records `provider="openrouter"` unconditionally, and its Codex route uses an agent runtime.
- **Export/import readiness:** No OpenAI-issued ZIP is present, but Brian's existing ChatGPT Conversation Manager exporter has already produced the local 1,728-thread catalog and per-thread JSON, Markdown, and history files. Do not rebuild the exporter or wait for an OpenAI ZIP. `inquiry-graph import` accepts OpenAI's `conversations.json`; `import-bridge` accepts the separate bridge Markdown format with timestamped role headers. Conversation Manager Markdown uses a different format, so normalize its per-thread JSON (`thread_id` and `messages` with message IDs, roles, text, and timestamps) into the Inquiry Graph `Conversation` model instead of passing its Markdown to `import-bridge`. The local archive still needs reconciliation against a fresh exporter inventory, including Project coverage.
- **Technical execution status:** The map builder reused matching topic/name caches and made no model call. Visual checks covered desktop and mobile only; interaction and console checks were not run.
- **Stakeholder observation status:** The page is locally available for Brian to inspect; no usefulness or comprehension claim is made.
- **Outcome / enabling / process progress:** Outcome: 30-chat position map delivered. Enabling: stable viewer and builder are merged. Process: long-term goal is defined; archive coverage is the next unresolved increment.
- **Current increment:** Compare the locally reconciled 1,728-thread inventory against a fresh, complete dated account snapshot; then resolve any missing or incomplete records before estimating the full extraction run.
- **Blockers:** Full account membership, freshness, and Project inclusion remain unverified. The bridge listing concern is tracked in Project Meta issue #2263; the built exporter's last successful paginated account listing contained 1,246 IDs, while its next recorded attempt failed with HTTP 429. That listing has not been reconciled with the 1,728 local records.
- **Resume event:** Use the existing ChatGPT Conversation Manager exporter to obtain a fresh paginated ID inventory when its recorded rate-limit backoff permits. Preserve the dated inventory under gitignored `private/`, reconcile every listed ID and Project record against the local catalog and raw transcripts, and record missing, extra, and incomplete cases. Then normalize the exporter's per-thread JSON into `Conversation` records and validate one source-grounded extraction. Do not pass its Markdown to `import-bridge`, request or wait for an OpenAI ZIP, or call the local catalog a complete account snapshot until the membership discrepancy is resolved.

## Evaluator-Facing Objective

Set via `/goal` on 2026-10-03 (Brian). The launcher widens sources to Claude and Gemini via Kept or official exports and requires the map to open at maps.brianmills.dev behind the single-password gate; Done-when is C1-C5 for one reconciled snapshot covering every conversation source. The full text lives in the session that set it; this document's Boundaries and Acceptance Checks are the authority.

## 2026-10-03 state additions

- Private gated hosting is live: `https://maps.brianmills.dev/` (menu, interests map, per-chat Cytoscape+ELK view `inquiry-one-chat-elk.html`) and `https://browser.brianmills.dev/` (yFiles via Voila, 4 chats). The per-chat viewer code is merged (inquiry-graph PRs #110, #111).
- Interests map (not positions): 2,900 normalized conversations; filter and meaningful cluster names built; Kept chats and ~99 new ChatGPT chats not yet merged in.
- Next increment: 10-chat extraction test slice via Codex, then full-snapshot decision. Kept Markdown to Conversation converter, and Claude/Gemini scheduled export, remain open.

## 2026-10-03 extraction test slice (increment 2 evidence)

- 10 chats (2023-06 to 2026-09, spread by date, 4k-25k chars of Brian text), `codex/gpt-5.6-luna`, $0 (subscription), all 10 validate with no errors, 551 ideas, 2 to 61 relations each; per-chat runtime 3 to 19 minutes.
- Independent check (not the extractor's own): all 551 node quotes and all 589 stance/question quotes appear verbatim in the source message, and every stance/question actor equals that message's speaker. 210 events are attributed to Brian with his own words. Nodes are often anchored in assistant text by design (the idea's origin); Brian's position is the stance/question event.
- Private outputs: `private/extract_test_20261003/` (graphs, per-chat reports, run.sh); gated per-chat views at maps.brianmills.dev/chats/.
- Kept: `tools/normalize_kept.py` (PR #113) turned 1,053 vault files into 833 new Conversations (724 gemini, 58 claude, 51 chatgpt) plus 220 duplicates of exporter chats; 0 failed.
- Not yet done: C1 reconciliation across all sources, full extraction, combined map, answer route.

## 2026-10-03 later state (C3/C4 tooling, preview only)

- Tools merged: `tools/extract_queue.py` (resumable, dispositions), `tools/ask_positions.py` (cross-chat answer, code-checked citations), `tools/position_records.py` + `tools/position_topics.py` + `tools/name_topics.py` (combined map with generated topic names).
- Full extraction running on Codex only (Brian: "keep using codex"): ChatGPT queue 743 chats, Kept queue 570 chats; at last check 61 and 13 done, all extracted, 0 failed. Dispositions: `private/extract_full_20261003/dispositions.jsonl` and `kept/dispositions.jsonl`; exclusions listed in `kept/skipped_too_short.json` and the interest-filter outputs.
- Preview map (213 events, 21 chats, 11 named topics, membership reconciles) is at maps.brianmills.dev/positions/, rendered at desktop and phone width through the gate. It is a preview of a subset, not C3.
- Remaining: finish extraction (C1), rebuild map and rerun the answer over everything (C3, C4), write the report (C5). Resume: `tools/extract_queue.py <queue.json> <workdir> --workers N` skips finished chats.

## 2026-10-03 handoff: how the run continues without a chat session

- Extraction runs as systemd user services `extract-chatgpt`, `extract-kept-fwd`, `extract-kept-rev`, `extract-new108` (private/extract_full_20261003). They must be started with `--setenv=PATH="$PATH"` from a normal shell: a bare service picks `/snap/bin/codex` (0.114.0), which cannot refresh the shared login (project-meta issue #2354). `loginctl` linger is on, so they survive logout; they do NOT survive `wsl --shutdown` or a reboot. Resume: rerun `tools/extract_queue.py <queue.json> <workdir> --workers N` (skips finished chats).
- `tools/finish_pipeline.sh` (service `finish-pipeline`) waits for those services, retries failures once, reconciles, rebuilds the combined map with generated names, publishes it to maps.brianmills.dev/positions/, and runs the cross-chat answer into private/answer_full.json; log in private/finish_report.txt.
- Still needs a person or fresh agent: hand-check private/answer_full.json (C4), confirm map desktop/mobile from the gated URL (C3), write the completion report with costs and limits (C5), decide the Claude/Gemini official-export check, and run the low-confidence-interest queue (private/extract_full_20261003/lowconf).

## 2026-10-04 Claude official export (completeness check result)

- Claude data export (requested 2026-10-04, downloaded, private/official_exports/claude_20261004): 848 conversations, 2023-12 to 2026-09. Kept's vault had 58 Claude chats; 45 are in the export, 13 only in Kept, **803 export chats were not in Kept (about 95%)**. Kept is therefore NOT a reliable Claude backup; use the official export (tools/normalize_claude_export.py; 819 normalized, 29 without visible text).
- Interest filter on the 819: 643 included; 453 queued after dropping 178 too short and 12 already extracted via Kept (service `extract-claude-export`, private/extract_full_20261003/claude_export).
- Reconciliation now has three sources (ChatGPT exporter 3,020; Kept 1,053; Claude export 848 = 4,921 conversations, each with one disposition, exit 0).
- Open: Gemini official export (Takeout, created Oct 2, downloadable until Oct 10; size unchecked) not yet compared with Kept's 725 Gemini chats; ChatGPT official export requested, awaiting the emailed link; therakorski and montaguecantsin accounts not yet checked.

## 2026-10-04 handoff: extraction moved to OpenRouter gpt-6-luna (read this first)

- **Running:** user service `extract-or-run` (enabled, starts at boot) extracts the 1,442 chats not yet done, 8 at a time, with `openrouter/openai/gpt-6-luna` at medium effort (`INQUIRY_REASONING_EFFORT`), spend cap `--budget 25` that survives restarts (sums `cost_usd` in `private/extract_full_20261003/or_run/dispositions.jsonl`). Expected cost about 11 USD. Output: `private/extract_full_20261003/or_run/out`. Hard-kill test passed: finished graphs and per-chunk cache survive, service restarts itself.
- **Codex services** (`extract-chatgpt`, `extract-kept-fwd`, `extract-kept-rev`, `extract-new108`, `extract-claude-export`) are disabled, not deleted; their graphs are kept. Re-enable only as a fallback. Codex runs use the shell's `codex` (0.160) via the PATH in the unit files, never `/snap/bin/codex` (project-meta issue #2354).
- **Evidence for the model choice** (private/qwen_test): 10-chat slice, gpt-6-luna medium 10/10 valid, 0 of 1,159 quotes not verbatim, 0.114 USD; low effort is cheaper (0.076) but finds about a quarter fewer ideas. Spot-check of 20 Codex-finished chats: 20/20 valid, 0 not verbatim, 0.077 USD. Qwen: qwen3.7-flash has no endpoint for forced tool_choice; qwen3.7-plus works only with thinking off and ignored the schema enums on 4 of 10 chats. K2 Horizon 375B A23B is not on OpenRouter.
- **When it finishes:** `finish-pipeline` (enabled) reconciles, builds the full map, publishes maps.brianmills.dev/positions/, runs the cross-chat answer into private/answer_full.json; log private/finish_report.txt. Then a person or fresh session must: hand-check the answer (C4), view the map on phone and desktop from the gated URL (C3), write the cost and limits report (C5).
- **Completeness checks still open:** Claude official export ingested (848 conversations; Kept had 58). Gemini Takeout (created 2026-10-02, downloadable until 2026-10-10, size unchecked) not yet compared with Kept's 725 Gemini chats. ChatGPT official export requested 2026-10-04, link pending by email. therakorski and montaguecantsin accounts not checked. Robot Chrome (Windows, port 9333, profile %LOCALAPPDATA%\robot-browser\a) is signed in to ChatGPT, Claude and Google for brianmills2718; drive it with C:\Users\thela\robot\cdp.js (per-tab CDP), not Playwright connectOverCDP (refused by this browser).
- **Residue to clean:** `~/code/llm_client` main checkout has two staged Qwen-route edits (and a stash `brian-qwen-routes-abandoned-20261004`), plus an unpushed worktree branch `brian/add-qwen37-flash-plus` blocked by another session's Plan 378 write claim. Qwen routes proved unusable here, so discard them once the checkout is writable.
- The goal was cleared on 2026-10-04 because its Stop hook looped on a multi-hour wait (learning lrn-20261004T161147050430Z-059e0f67b9). Set a narrower goal for the session that finishes the pipeline.

## 2026-10-05 exporter scheduled sync disabled (tab pile-up)

- Brian reported ~220 ChatGPT tabs piling up in his montaguecantsin Chrome profile, one new every few minutes. Cause: the exporter's scheduled sync (my 2026-10-02 drop-in `91-backup-all-accounts.conf`) re-ran SYNC_OPEN_CHATGPT_CMD on every failed connect and for every account while the extension had 0 connections. Fixed in the exporter (chatgpt-conversation-manager PR #101: at most one open per account per 30 min; npm test 469 passed).
- **The scheduled backup is now OFF** (drop-in moved to `~/.config/systemd/user/disabled/`; `90-throttle-safe.conf` sets interval 0). To resume: connect the browser extension to the exporter first (`curl localhost:8787/health` must show extension_connections > 0), then move the drop-in back and restart `chatgpt-bridge.service`. Until then ChatGPT backup is manual, so new chats are not being captured; the 2026-10-05 official export request is the safety net.

## Topic digests and agent lookup (2026-10-05)

Brian reset the goal to "useful, not just complete". Narrow topic questions answer well from own-words positions; one broad "everything" question returns vague answers.

- **Digests:** 100 topics (layer 25, chore topics skipped by `tools/run_topic_digests.py`) answered with `tools/ask_positions.py` (own-words only via `--authorship`/`--records`). 1,000 claims: 494 position, 409 open_question, 56 change, 41 conflict. 2 claims cited a record that did not exist and were dropped. Rebuild: `run_topic_digests.py --n 100` then `build_topic_site.py private/topic_digests private/topic_site`, then copy to the gated host (`/srv/apps/chat-atlas/site/`, pages `positions-by-topic.html`, `topics/<id>.html`, `open-questions.html`). Rendered at 1200 px and 390 px, no horizontal overflow, quotes expand; unauthenticated requests get 303.
- **Hand-check (10 claims, 6 topics):** 6 supported, 3 over-read (a "change" whose quotes all share one day; a question read as a shift; "has a transcript" read as "supports using it"), 1 weak (single unclear quote behind "recursively nested"). Treat the "changed over time" label as a lead to verify against the dated quotes. The index page says so.
- **Agent lookup:** `tools/brian_positions.py "<topic>"` (keyword match over 15,291 own-words records, no model call, about 1.3 s warm; index at `private/positions_index.json`, `--rebuild` after re-extraction). Skill `brian-positions` merged to agent-skills (PR #438, commit 469fc48). No MCP server: the MCP Tooling Policy says CLI plus skill. The agent-skills canonical checkout is locked read-only while another lane (`brain-now-headlines`) is open, so `~/.claude/skills/brian-positions` resolves only after that lane closes and the canonical checkout pulls main. Backup copy: `private/skill_backup/brian-positions`. A fresh `claude -p` session ran the CLI by path and returned four dated quotes.
- **Cost:** 100 topic answers plus 5 earlier ones = $0.32 of the $15 allowance approved Oct 5 (project month total $10.58).
- **Limits:** retrieval is keyword-only, so synonyms miss (the "hypergraph knowledge graph" query returned 4 records from one day); authorship labels are about 7-13% wrong in mixed spans; completeness is unproven until the official exports (ChatGPT x3, Gemini) are compared.
