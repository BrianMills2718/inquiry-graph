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
