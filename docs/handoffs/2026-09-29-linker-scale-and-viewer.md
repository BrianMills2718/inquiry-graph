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
  - commit 4ac5994 (WIP, parameterizes `build_key`)
  - committed with this handoff: `live_extract` supersession-cycle fix + test (63 tests pass)
    and `evaluation/cross_conversation_scale/scale.py`.
  - UNTRACKED and to be deleted once a shared viewer exists: `tools/build_inquiry_map.py`,
    `tools/inquiry_map_template.html` (hand-rolled D3; Brian rejected this approach).
- Goal docs: `docs/goals/cross-conversation-linker.md` (C2-C5 remain).

## BLOCKER: OpenRouter credits (needs Brian)
The 30-chat scale run (`scale.py`) exited in the "key" stage: OpenRouter refused
`build_key.per_chat` with "requires more credits ... can only afford 29639" tokens.
Corpus (30 chats, ~4.2M chars, all graphs valid) and linker outputs are already cached under
`private/xconv/scale_run/`. Do NOT cap max_tokens to dodge it (AGENTS.md rule). After credits
are topped up, rerun: `cd worktrees/linker && .venv/bin/python evaluation/cross_conversation_scale/scale.py > private/xconv/scale_run.log 2>&1`
(expect cached stages to skip). Check the log with `grep -v TIMEOUT`.

## Next steps
1. Finish goal 2: after the rerun, hand-check >= 4 grades, write
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
