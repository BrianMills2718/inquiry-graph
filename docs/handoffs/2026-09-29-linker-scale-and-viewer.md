# Handoff 2026-09-29: linker scale run + graph viewer

Written for a fresh agent. No transcripts or quotes here; private data stays under
`~/code/inquiry-graph/private/xconv/` (never commit it).

## Long-term goal (Brian)
An AI understands everything Brian is interested in and his positions across all his
ChatGPT conversations, and finds gaps, open questions and conflicts. Brian does not read
the graphs; the AI does. He also wants to *see* a map: each inquiry alone and all together,
clustered by topic. inquiry-graph = per-chat producer; onto-canon6 = cross-source kernel
(read-only for these goals).

## State
- Merged: inquiry-graph PRs #44, #45, #49-#59 (goal 1 cross-chat positions proof done; goal 2
  step C1, the relation-typed linker v1.2, done, 10/11 hand-checked). Router PR #44 merged.
- Worktree `~/code/inquiry-graph/worktrees/linker`, branch `goal/linker-scale`:
  - includes the parameterized `build_key`, the `live_extract` supersession-cycle fix + test,
    and `evaluation/cross_conversation_scale/scale.py`.
  - UNTRACKED and to be deleted once a shared viewer exists: `tools/build_inquiry_map.py`,
    `tools/inquiry_map_template.html` (hand-rolled D3; Brian rejected this approach).
- Goal docs: `docs/goals/cross-conversation-linker.md` (C2-C5 remain).

## Scale-run provider status (2026-09-29)
The 30-chat scale run (`scale.py`) exited in the "key" stage: OpenRouter refused
`build_key.per_chat` with "requires more credits ... can only afford 29639" tokens.
Corpus (30 chats, ~4.2M chars, all graphs valid) and linker outputs are already cached under
`private/xconv/scale_run/`. Do NOT cap max_tokens to dodge it (AGENTS.md rule).

A bounded Codex-subscription probe succeeded on chat `6a7bd3db` through
`codex/gpt-5.6-luna` using the installed Codex CLI and metadata-only observability. It returned
20 positions; all 20 quotes matched Brian-authored messages. The client reported
`billing_mode=subscription_included`, `$0`, and no token usage counts. Trace:
`inquiry-graph/xconv-key/codex-subscription-probe/6a7bd3db-20260929-attempt2`.
Codex `/status` showed Pro, 84% of the weekly limit and 48% of Luna Reserve remaining at the
time checked. This proves the route works for one chat, not that the remaining 30-chat workload
fits the available allowance. The scale run has not been resumed; its original OpenRouter cache
is unchanged.

For a consistent Codex reference-key set, use a separate run directory and regenerate all 30
per-chat keys rather than mixing the eight existing OpenRouter keys with Codex output. The
cross-key, route-answer and grading stages also remain outstanding. Do not buy OpenRouter credits
or infer full-run capacity from the single probe.

At this handoff, all 30 corpus IDs have valid graphs; 8 of 30 per-chat key JSONs exist, and
their IDs all belong to the corpus. The other 22 key calls and the cross-key call are still
needed in the original run. Linker exports exist; route answer files and `grades.json` do not,
so completing the evaluation also needs route A (15 calls), B/C (one call each), and judging
(15 calls). These counts come from the current cache and the stage loops in `scale.py`. Do not
resume the original mixed-provider cache as a completed evaluation.

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
the reference-key generator. Do not infer extraction precision from these results.

## Next steps
1. Add a Codex CLI subscription route to the scale-run entrypoint, keep its output in a separate
   campaign directory, and regenerate all 30 reference keys consistently. Check usage while
   running; the one-call trace has no token counts. Then finish the scale evaluation, hand-check
   >= 4 grades, write
   `evaluation/cross_conversation_scale/results.md`, comment on issue #38, open the PR.
   Report counts and exit status.
2. Graph viewer (Brian: "every time i ask for a graph ... my coding agents try to recreate the
   wheel"; typedb-style typed graphs, hierarchies, hyperedges). Do not build a new viewer.
   A subagent found (unverified by me, verify first):
   - best fit: Scientific Hypergraph viewer
     `scientific-hypergraph/wiki/reference/metamodel/hypergraph-viewer.html` (zero-build,
     typed n-ary diamonds with role spokes, layers, type hierarchy, inspector);
   - best home/pattern: shared_ui WorkGraph (project-meta Plan #280; Pydantic -> JSON Schema
     -> web component);
   - others: O2A explorer, onto-canon6 GraphCanvas, OrgChart groups.
   - root cause: the `ui` skill's graph guide points at a copy-paste React Flow template;
     the capability index has no "render a graph" entry; the router catalog lists only
     outside libraries.
   Verify these claims, then: make one shared viewer (domain-free format, a plain graph =
   a relation with two roles) in `shared_ui`, add one routing pointer in
   `project-meta/wiki/tool_and_capability_index.md`, the `ui` skill graph guide and the router
   catalog, retire the copy-paste default, and have inquiry-graph only export to its format.
   Cross-project shared skill/index edits: claim per AGENTS.md; skills are authored only in
   `~/projects/.agents/skills/`.
3. Render the 30-chat map through that viewer (topics = Louvain communities over position
   embeddings, k=6, floor 0.5; typed cross-chat links as edges). Design via representation-router;
   reuse `topics()`/`name_topics()`/`chat_views()` logic from `tools/build_inquiry_map.py` as the
   data producer only. Output contains quotes -> write under `private/`.
4. Cleanup: router worktree `~/code/representation-router/worktrees/quality-fallback` (branch
   merged as PR #44) can be removed via the sanctioned worktree-remove path. Memory
   `reuse-shared-graph-viewer.md` still needs Codex parity once the shared viewer exists.

## Constraints in force
Never commit transcripts/quote-bearing outputs. ChatGPT bridge is read/search only (no
ask_chatgpt, rename, move, tag, reload). onto-canon6 and epistemic-warrant read-only. No
deploy/publish. Ask before WSL restart. Outbound content needs approval. brianmills-spec/*
repos use `gh-insidesuccess` and its credential helper for git push.
