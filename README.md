# Inquiry Graph

**A source-grounded map of how an inquiry develops—not just what topics it contains.**

V1 turns normalized conversations or ChatGPT exports into a typed graph of content, questions, relations, inquiry moves, and actor-relative stance/status histories. It records a challenge, clarification, retraction, or reframing as its own object, with source anchors. Questions remain navigable even when the conversation moves elsewhere.

The first-pass example now covers the original V1 arc, the epistemic-transition and assumption-context refinements, the strategy/reflection and candidate-generation passes, and the warrant/license refactoring: **229 content nodes, 250 relations, 185 moves, 58 stance events, and 76 question-status events over 219 curated excerpts**. It includes **54 distinct questions**. This is a proposed annotation, not an independently reviewed gold dataset or a complete transcript export.

## Start here

[Walk through the dialogue](docs/conversation-walkthrough.md) · [Current epistemic-actions/support algebra](docs/epistemic-actions-support-algebra.md) · [Warrant/license interface](docs/warrant-license-interface.md) · [Candidate-generation interface](docs/candidate-generation-interface.md) · [Metareasoning/strategy/reflection extension](docs/metareasoning-strategy-reflection.md) · [Assumption-context stage](docs/assumption-context-meta-model.md) · [Earlier epistemic-transition stage](docs/epistemic-transition-calculus.md) · [Post-V1 research log](docs/research-log-post-v1.md) · [Open agenda and grounded move report](examples/seed/report.md) · [Inquiry diagram](examples/seed/inquiry-map.md) · [Canonical graph](examples/seed/graph.json) · [Source excerpts](examples/seed/source-excerpts.json)

The [offline linked-record inspector](examples/seed/inspector.html) works by opening the file locally after cloning. It has no external scripts, CDN, telemetry, or server. It is a searchable/linkable record inspector, **not** an interactive force-directed canvas. GitHub displays the Mermaid diagrams directly.

## Run locally—no API key required

Requires Python 3.11 or later. From the repository root:

```bash
python -m venv .venv
. .venv/bin/activate                 # PowerShell: .venv\Scripts\Activate.ps1
python -m pip install -e '.[dev]'
python -m pytest -q
inquiry-graph validate examples/seed/graph.json
inquiry-graph query examples/seed/graph.json open
inquiry-graph query examples/seed/graph.json trace \
  --id dialogue-2026-09-27:n:imagination
inquiry-graph render examples/seed/graph.json /tmp/inquiry.html --format html
```

Create a new validated graph through the same boundary used for LLM responses:

```bash
inquiry-graph prepare examples/seed/source-excerpts.json /tmp/extraction-request.json
inquiry-graph extract examples/seed/source-excerpts.json /tmp/my-graph.json \
  --response-file examples/seed/candidates.json
inquiry-graph merge /tmp/my-graph.json /tmp/my-graph.json --output /tmp/merged.json
inquiry-graph render /tmp/my-graph.json /tmp/my-map.md --format mermaid --view inquiry
```

Paths above are examples for Unix-like systems; use another writable path on Windows. Outputs are not overwritten unless `--force` is supplied. Invalid extraction outputs are quarantined under `private/quarantine`, never substituted for a good graph.

## Bring another conversation

```bash
inquiry-graph import /path/to/conversations.json private/imported --conversation-id EXPORTED_ID
```

The importer follows each export's `current_node` parent chain: **only the active branch**, not an accidental mixture of alternative replies. Without `--conversation-id`, all conversations are imported into distinct hash-named JSON files. Only visible user/assistant text is imported; skipped parts are counted. This is an export adapter, not access to all your ChatGPT conversations. Review exports before sharing them.

Pass one imported source to `prepare`, then supply a candidate JSON from an LLM to `extract --response-file`. Candidate schema: [schemas/candidates.schema.json](schemas/candidates.schema.json). An optional official OpenAI SDK adapter is available with `pip install -e '.[llm]'` and `extract SOURCE OUTPUT --openai --model MODEL_ID`; choose a structured-output-compatible model explicitly and use securely provisioned credentials. No key is stored in this repository. **The provider protocol is mock-tested; no live paid extraction was run for this release.**

## What is guaranteed—and what is not

The validator checks schema, identity, reference resolution, exact quotes and Unicode offsets, relation-role signatures, actor/source consistency, and restricted temporal ordering. Rejected interpretations remain in the audit trail. Conceptual cycles are allowed; dependency cycles are warnings.

It does **not** certify truth, detect every bad paraphrase, know a person's private beliefs, prove the deduction/induction/abduction taxonomy exhaustive, or select the best next thought. Structured output provides a contract; semantic fidelity still needs review. A valid graph may contain a false claim and its later rejection.

## Project documents

[Requirements](docs/requirements.md) · [Formalism](docs/formalism.md) · [Current epistemic-actions/support algebra](docs/epistemic-actions-support-algebra.md) · [Warrant/license interface](docs/warrant-license-interface.md) · [Candidate-generation interface](docs/candidate-generation-interface.md) · [Metareasoning/strategy/reflection extension](docs/metareasoning-strategy-reflection.md) · [Assumption-context stage](docs/assumption-context-meta-model.md) · [Earlier epistemic-transition stage](docs/epistemic-transition-calculus.md) · [Post-V1 research log](docs/research-log-post-v1.md) · [Ontology](docs/ontology.md) · [Architecture](docs/architecture.md) · [Annotation guide](docs/annotation-guide.md) · [Seed review](docs/seed-review.md) · [Evaluation](docs/evaluation.md) · [Decisions](docs/decisions/index.md) · [Roadmap](docs/roadmap.md) · [Security](docs/security.md) · [Research references](docs/references.md)

Rebuild checked-in artifacts with `python examples/build_seed.py && python tools/build_artifacts.py`. Check drift with `python tools/build_artifacts.py --check`. Canonical JSON and curation stay in Git; there is no required graph database, vector store, web application, or custom agent runtime.

Code and conversation data remain private. No public redistribution license has been selected. Keep the repository private unless the source conversation and all derived artifacts have been reviewed for release.
