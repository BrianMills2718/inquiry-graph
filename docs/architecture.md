# Architecture

```text
Visible export / normalized source
  → deterministic active-branch importer
  → immutable source snapshot
  → prepare(prompt + schema + role signatures)
  → structured-output provider OR response-file
  → Pydantic candidate parsing
  → exact-quote grounding + source injection + reset review state to proposed
  → semantic validator
  → canonical graph JSON
  → exact-identity merge
  → agenda / trace / dependencies / conflict views
  → Mermaid / DOT / Markdown / offline HTML
```

Failures in extraction go to a separate private quarantine record. Canonical JSON writes are atomic and exclusive by default. No source text is executed. No database or persistent service runs.

## Modules

`model.py` is the executable ontology and anchor helper. `validate.py` checks cross-record invariants. `io.py` normalizes source, writes atomically, ingests candidates, and merges. `extract.py` contains one provider-independent prompt and a thin official SDK adapter. `views.py` projects agenda and traced histories with NetworkX for graph structure. `render.py` exports escaped views. `cli.py` wires these together using argparse.

The only runtime dependencies for offline operation are Pydantic and NetworkX. The optional provider dependency is OpenAI's SDK. Tests add pytest and jsonschema. These are deliberately ordinary components. We do not introduce an orchestration framework merely to make one schema-constrained request.

## Boundaries and data ownership

**Source boundary:** imported text and source identifiers are input records, never LLM-generated fields. The selected export branch is explicit. Source scope is not the whole account.

**Provider boundary:** only `extract --llm` sends source text externally, through Brian's shared `llm_client` (OpenRouter route, traced per chunk as `inquiry-graph/live-extract/<conversation>/chunkNN`). `prepare`, `import-bridge`, response-file extraction, validation, merge, query and rendering are local. The live extractor works in message chunks. The model returns quotes, not offsets; `live_extract.locate` finds each quote in the source with formatting ignored and anchors the exact source text. Items that cannot be grounded or fail validation are dropped and counted in the `--report`. Model outputs are cached under `--cache-dir` by prompt version and chunk hash.

**Validation boundary:** provider schemas are not trusted as referentially complete. A successful parse can still fail source/ref/type/time checks. Inferred relationships remain proposed. An LLM cannot self-certify its output as human-confirmed because ingestion resets review metadata. Unique quotes have their offsets recomputed deterministically; repeated quotes require an exact supplied position, not fuzzy matching.

**Persistence boundary:** canonical JSON is versioned by Git. Source text, graph, and reports contain private material. Public hosting is not configured. The offline HTML contains copies of source-derived records and is just as sensitive as the JSON.

## Recovery and replay

The founding annotation is stored twice for different purposes: compact curator instructions in `curation.json`, and explicit generated candidate/graph JSON. `examples/build_seed.py` deterministically grounds the curated records. `tools/build_artifacts.py` creates schemas and review views. `--check` detects drift.

The production extraction path consumes a structured response rather than the seed curation format. Replaying a response file is deterministic; a new live model call need not be. Store the response, source snapshot, prompt version, model identifier and graph commit when conducting experiments. The current extraction metadata records source hash and method; full billing/token telemetry is not implemented.

## Scaling boundary

One source conversation per extraction is the V1 unit. There is no undocumented chunking or stitching algorithm. Very long exports should be partitioned into explicitly scoped normalized sources with source IDs preserved, then reconciled manually; a generic automatic long-context merger is out of scope. The full cross-conversation graph is assembled by explicit exact-identity union. Similarity-based identity suggestions, reviewed alias maps, database indexing, and incremental subgraph extraction belong in later versions.

## Machine failure during implementation

The initial project checkpoint was pushed from Brian's machine. Its guarded WSL health probe subsequently failed; the launched task process was stopped without restarting WSL or deleting local work. Development continued in an isolated build environment on `feat/v1-portable`. Any local-only files left on `feat/v1` must be inspected before reuse. GitHub's completed branch/main is the durable deliverable, not an assumption that the inaccessible local worktree is synchronized.
