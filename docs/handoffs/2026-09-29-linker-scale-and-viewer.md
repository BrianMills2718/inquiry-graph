# Handoff 2026-09-29: linker scale run + graph viewer

Written for a fresh agent. No transcripts or quotes here; private data stays under
`~/code/inquiry-graph/private/xconv/` (never commit it).

## Current status (2026-10-01)

This note's original provider and viewer sections describe the state on 2026-09-29. The
30-chat campaign completed through the Codex subscription route. The balanced replay and
independent C5 signoff support keeping the linker as a bounded research/topic-map source; the
decision is posted to [issue #38](https://github.com/BrianMills2718/inquiry-graph/issues/38#issuecomment-5923619199).
No scale-superiority or product answer-route claim was made.

The private topic map uses the committed builder in `tools/topic_map.py`, template in
`tools/topic_map_template.html`, and representation record in `docs/ui/topic-map/README.md`.
The canonical output is `private/xconv/scale_run/map/verified/index.html`: 30 conversations,
620 positions, 27 interpretive topic groups, 233 typed links, 750 unrelated pairs hidden, and
48 aggregated cross-topic links. The prior generated page is preserved under
`private/xconv/scale_run/map/verified/previous-shared-ui-2026-10-01/`. Keep both pages and all
screenshots under gitignored `private/xconv/`; do not publish or commit them.

The shared `relation-graph-view/v1` bundle is merged in
[shared_ui PR #11](https://github.com/BrianMills2718/shared_ui/pull/11). Its export manifest
records source commit `3bd114e1f9cc61561d2ff98fd7177d37fc6984a5` and bundle SHA-256
`9a2fabf95f1823f70a4f00fc8c9d8c89a922e3c8826536de6fec474f6cf152af`. The Inquiry Graph
consumer refresh is merged in [PR #80](https://github.com/BrianMills2718/inquiry-graph/pull/80)
(commit `4b9f0c14acb07f8712adddd23ad0bbe964d44dd3`). Regeneration from the committed builder
uses the shared export; there is no active shared_ui worktree dependency.

The new page loaded and was visually captured at 1440×1000 and 390×844. These checks confirmed
the map and responsive overview loaded; they did not verify page interactions or console errors.
Regeneration reused matching topic and name caches and made no model call. The output remains a
30-chat prototype, not evidence of full-archive coverage or map usefulness across all chats.
The next goal authority is `docs/goals/cross-chat-position-memory.md`; its first step reconciles
the local archive against a complete, dated snapshot. The bounded Jev/Laya disposition remains
in `docs/goals/cross-conversation-linker.md`.

## Long-term goal (Brian)
“An AI that knows all your positions across your chats, plus a map you can look at.” It should
find gaps, open questions, conflicts, and changes over time, and show each inquiry on its own
and all inquiries together by topic. `inquiry-graph` is the per-chat producer; `onto-canon6`
remains read-only for this goal. The active goal authority is
`docs/goals/cross-chat-position-memory.md`.

## State at the original handoff (2026-09-29)
- Merged: inquiry-graph PRs #44, #45, #49-#59 (goal 1 cross-chat positions proof done; goal 2
  step C1, the relation-typed linker v1.2, done, 10/11 hand-checked). Router PR #44 merged.
- Worktree `~/code/inquiry-graph/worktrees/linker`, branch `goal/linker-scale`:
  - includes the parameterized `build_key`, the `live_extract` supersession-cycle fix + test,
    and `evaluation/cross_conversation_scale/scale.py`.
  - The hand-rolled D3 prototype was scratch work and was superseded by the shared-component
    topic map. Its two scratch files are absent from this worktree.
- Goal docs: `docs/goals/cross-conversation-linker.md` records C2-C5 evidence, the bounded
  C5 disposition, and the remaining map, archive-coverage, and Jev/Laya questions.

## Original OpenRouter attempt (2026-09-29; historical)
The first 30-chat scale run stopped during `build_key.per_chat`: OpenRouter refused a request
because the account lacked enough credits. The corpus and linker output were cached under
`private/xconv/scale_run/`. That mixed-provider attempt was not treated as a completed evaluation;
the balanced replay and C5 decision were later completed through separate Codex-subscription
runs, described above and in `docs/goals/cross-conversation-linker.md`.

## Jev/Laya extraction check (2026-09-29)

Local prior art in OntoCanon6 is a Jev predicate-ranking spike, not a conversational
position extractor: `~/code/onto-canon6/worktrees/jev-ontology-adjudication-20260921/docs/experiments/jev_extraction_spike_results_20260920.md`
reports 5,995 predicates, Recall@1 31.25%, Recall@16 93.75%, and a mean 19.94 predicates
scoring at least 0.5. Its follow-up
`docs/experiments/jev_text_to_graph_usage_20260922.md` demonstrates LangExtract followed by
Jev predicate/type selection on short text examples.

Verified online prior art:
- [jev-mcp](https://github.com/jkudish/jev-mcp) has `jev_extract`: regexes propose candidate
  spans, Jev selects among them, and accepted values are returned verbatim. This is a useful
  grounding pattern, not a complete conversation-position pipeline.
- [zero-shot-ie-bench](https://github.com/umstek/zero-shot-ie-bench) compares extractors and
  typed-decision systems, including Jev and Laya. It is an evaluation harness, not a personal
  chat extractor.
- [Laya](https://github.com/NandhaKishorM/laya) is an open-source typed decision engine that
  can run locally. Its choice/score/yes-no decisions can filter candidate text, but it does
  not generate self-contained position statements.

Larger-chat Jev probe: chat `6a988a7a`, 235 Brian-authored sentence candidates in eight
  batches, using `openrouter/typesafe/jev-1.13` (resolved to
  `typesafe/jev-1.13-20260917`). It labeled 181 position, 16 question, and 38 other. Against
  the independently generated, quote-verified reference key, it labeled all 10 of 10
  sentence-covered positions as positions and 4 of 5 covered open questions as questions;
  all 3 synthetic controls passed. Stance matched the key on 6 of 15 covered excerpts. Total
  reported cost was $0.001558326, with 37,103 input tokens, 9,969 output tokens, and 2.87
  seconds across nine calls. This is recall evidence only: the key is model-generated, not
  human ground truth, and the 181 predicted positions leave precision unmeasured. The stance
  agreement is weak. The calls used OpenRouter, so Jev here does not remove that account
  dependency. Trace `inquiry-graph/xconv-system1-pilot/jev-6a988a7a-batched-20260929` has
  nine metadata-only records; prompts, outputs, and per-candidate labels were not persisted.

Earlier one-chat Laya probe on `698975ae` labeled 4 of 16 quote-verified position controls as
positions and matched stance on 2 of 16. That probe has no durable trace, so treat it as
exploratory and not replayable. Neither System 1 probe establishes a drop-in replacement for
the reference-key generator. Do not infer extraction precision from these results. This section
is the historical 2026-09-29 check; the newer Jev-Mem review and current adoption condition are
recorded in `docs/goals/cross-conversation-linker.md`.

## Next steps (current)
1. Follow `docs/goals/cross-chat-position-memory.md`. The local inventory is internally reconciled:
   1,728 catalog records match the embedded IDs in 1,728 valid transcript files, with one filename
   whose basename differs from its embedded ID. All 30 map-corpus chats are in the catalog. The
   account snapshot is still unresolved: the last successful paginated sync listed 1,246 unique
   IDs, the catalog has 1,728, and the next sync attempt failed with HTTP 429. Compare against a
   fresh complete dated account snapshot before calling the local catalog complete.
2. Use the reconciled snapshot to extend position extraction and the map. Keep the structured-output
   extractor; the Jev/Laya disposition changes only if its recorded reopening condition is met.

The shared viewer is already merged and integrated. There is no remaining bundle wait.

## Constraints in force
Never commit transcripts/quote-bearing outputs. ChatGPT bridge is read/search only (no
ask_chatgpt, rename, move, tag, reload). onto-canon6 and epistemic-warrant read-only. No
deploy/publish. Ask before WSL restart. Outbound content needs approval. brianmills-spec/*
repos use `gh-insidesuccess` and its credential helper for git push.
