# Inquiry Graph topic map: representation and disposition

## Use case

Brian wants to see which positions recur or connect across 30 conversations, open one
bounded topic to inspect its member positions and exact quotes, and switch to the extracted
graph for any one conversation.

## Representation decision

The representation-router review recommends a linked map with a topic overview, per-topic
detail graphs, and a conversation graph view. The overview shows 27 communities rather than
620 positions at once. Topic membership and names are explicitly interpretive; extracted
positions and source quotes remain inspectable; typed cross-conversation relations are
explicitly inferred and undirected. Aggregated overview edges expose their relation counts in
the inspector. Conversation graphs preserve source relation roles and use a relation node for
multi-role records.

The router's initial `primary: null` result was caused by passing plain-English requirements
where catalog capability IDs were required. The corrected call declared the supported
capabilities (`provenance`, `linked-views`, `persistent-selection`, `shared-filters`,
`details-on-demand`, and `evidence-inspector`) and the `source-derived` and `interpretive`
semantic lenses. Its recommendation was `composite-linked-view`, form `map`, renderer
`native-web`, with semantic zoom through a topic overview and bounded topic/conversation
detail views.

## Evidence and disposition

- The cached source has 620 extracted positions, 983 judged cross-chat pairs, and 30 valid
  per-chat graphs.
- The map excludes the 750 pairs judged `unrelated`; the remaining 233 typed links are shown
  inside topic detail views and aggregated between topics where applicable.
- Conversation views focus on Brian's linked positions. A source relation appears only when
  every role binding is represented in that position view; this keeps hidden assistant/context
  items from changing the relation's apparent meaning.
- The largest topic has 48 positions, within the shared component's 120-node and 400-relation
  rendering limits. Larger undirected views use four columns; sparse directed views switch to a
  compact role-preserving grid when Dagre would exceed the available width.
- The renderer uses the merged `relation-graph-view/v1` contract and offline export from
  [`shared_ui` PR #11](https://github.com/BrianMills2718/shared_ui/pull/11). The bundle embedded
  in the regenerated page matches the export manifest: source commit
  `3bd114e1f9cc61561d2ff98fd7177d37fc6984a5`, SHA-256
  `9a2fabf95f1823f70a4f00fc8c9d8c89a922e3c8826536de6fec474f6cf152af`. The generated HTML embeds
  both the component and source data, so it works offline without a runtime dependency.
- Regeneration reused matching topic-group and topic-name caches; it made no model call. The
  builder reported 30 conversations, 620 positions, 27 topics, 233 typed links, 750 hidden
  unrelated pairs, and 48 aggregated cross-topic links.
- The regenerated page rendered at 1440×1000 and 390×844. Playwright screenshots show the topic
  overview, its counts, and the responsive one-column mobile graph. These are visual-render
  checks only; this pass did not rerun page-level interaction or console-error assertions.
  Screenshots and the machine-readable render record are in the private `verified/evidence/`
  directory.
- Topic names are generated with Brian's Codex subscription route and marked interpretive.
  Private positions, rationales, and exact quotes stay in `private/xconv/scale_run/map/`.
- The balanced replay and fresh C5 signoff are complete. On one 30-chat corpus and 13 questions,
  positions plus links tied positions alone on mean key-point coverage; the small descriptive lead
  over archive search does not establish scale superiority. The bounded decision is posted to
  [issue #38](https://github.com/BrianMills2718/inquiry-graph/issues/38#issuecomment-5923619199).
  This map visualizes the cached linker output; it does not resolve answer quality or validate
  full-archive coverage.

## Local artifact

The quote-bearing standalone HTML is generated at
`private/xconv/scale_run/map/verified/index.html`. It opens directly in a browser and works
offline. Keep the HTML, its screenshots, and its source cache under the gitignored
`private/xconv/` tree. Regenerate it with the merged shared UI export:

```bash
python tools/topic_map.py \
  --component-bundle /path/to/shared_ui/exports/relation-graph-view.v1/relation-graph-view.js \
  --output private/xconv/scale_run/map/verified/index.html
```

## Known limits

The topic overview aggregates only cross-topic links; links within one topic appear in that
topic's detail graph. The underlying cached linker judgments are not changed or revalidated by
this viewer. The map is private, locally generated, and not a publication surface.
