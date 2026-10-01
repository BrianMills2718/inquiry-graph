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
- The renderer uses the shared `relation-graph-view/v1` contract and offline bundle from
  `shared_ui`. The generated HTML embeds the component bundle and source data, so the private
  page can be viewed without fetching a runtime dependency. The builder needs an exported bundle
  when regenerating the page; the shared component work is active but is not yet a merged,
  versioned dependency. The old D3 prototype files are absent from this checkout.
- The exact generated page was opened both through localhost and directly as a `file://` page.
  At 1440×1000 the overview showed all 27 topic groups and 48 aggregated links. The selected
  48-position topic detail has 8 typed links in a vertically scrollable canvas; the last node was
  visible after scrolling to the bottom. Selecting a source conversation opened its full
  105-position, 40-relation graph, within the shared viewer's 120/400 bounds; the last node was
  reachable by scrolling, and the selected position remained selected. Twelve interaction
  assertions passed, including topic search, view switching, source selection, and evidence
  inspection; the browser recorded zero page errors and zero failed requests. Screenshots and the
  machine-readable check record are in the private `verified/evidence/` directory.
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
`private/xconv/` tree. To regenerate after obtaining the exported relation-graph-view bundle:

```bash
python tools/topic_map.py \
  --component-bundle /path/to/relation-graph-view.v1.js \
  --output private/xconv/scale_run/map/index.html
```

## Known limits

The topic overview aggregates only cross-topic links; links within one topic appear in that
topic's detail graph. The underlying cached linker judgments are not changed or revalidated by
this viewer. The map is private, locally generated, and not a publication surface.
