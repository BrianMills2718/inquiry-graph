# Inquiry Graph

**A source-grounded map of how an inquiry develops—not just what topics it contains.**

V1 turns normalized conversations or ChatGPT exports into a typed graph of content, questions, relations, inquiry moves, and actor-relative stance/status histories. It records a challenge, clarification, retraction, or reframing as its own object, with source anchors. Questions remain navigable even when the conversation moves elsewhere.

The curated founding example extends through the late-session meta-model closeout and adoption/handoff work: **250 content nodes, 250 relations, 204 moves, 68 stance events, and 86 question-status events over 247 curated excerpts**. It includes **59 distinct questions** and 858 proposed annotations. A separate [2026-09-30 operational-games continuation](examples/operational-games-2026-09-30/README.md) records the later trajectory from factorization analysis through megamodeling, uncertain game structure, unawareness, white-box simulation, computational opacity, compositional game theory, deliberate universalization of the game concept, perspectival goals, replacement-first infrastructure reasoning, the compositional-executable-world reframing, game/decision coupling, the candidate-generation reuse correction, and the authentic local execution of the truck/logistics fixture: **124 selected excerpts, 116 nodes, 91 relations, 93 moves, 74 stance events, and 33 question events**. The nine excerpts for that authentic execution step quote the owner's 2026-10-02 curation request, not the original dialogue; the [fixture README](examples/operational-games-2026-09-30/README.md#authentic-trucklogistics-execution-recorded-2026-10-02) states this limit. The operational-games continuation also includes a [substantive-turn coverage audit](examples/operational-games-2026-09-30/coverage-audit.md) covering the visible 2026-09-30 inquiry arcs through the compositional-executable-world synthesis. The founding example remains all-proposed; in the operational-games example 59 claim/hypothesis nodes are `confirmed` (wording matches the quoted source; not endorsement or truth; basis: [review note](examples/operational-games-2026-09-30/review-2026-10-02.md)). Neither is an independently reviewed gold dataset or a complete transcript export.

## Start here

[New-agent handoff](docs/new-agent-handoff.md) · [Project status](docs/project-status.md) · [Walk through the dialogue](docs/conversation-walkthrough.md) · [Evaluation plan](docs/evaluation.md) · [Roadmap](docs/roadmap.md) · [Founding graph](examples/seed/graph.json) · [Operational-games continuation](examples/operational-games-2026-09-30/graph.json) · [Open agenda and grounded move report](examples/seed/report.md) · [Inquiry diagram](examples/seed/inquiry-map.md) · [Source excerpts](examples/seed/source-excerpts.json)

The formal theory of support, defeat, warrant and license, its reference code and the paper draft moved to **[epistemic-warrant](https://github.com/BrianMills2718/epistemic-warrant)** on 2026-09-29, with full history. The two shared no code.

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

Pass one imported source to `prepare`, then supply a candidate JSON from an LLM to `extract --response-file`. Candidate schema: [schemas/candidates.schema.json](schemas/candidates.schema.json). For live extraction install `pip install -e '.[llm]'` (Brian's shared `llm_client`) and run `extract SOURCE OUTPUT --llm --report REPORT.json`; `--model` overrides `llm_client`'s `extraction` route. A chat read through the chatgpt-bridge can be normalized with `import-bridge TRANSCRIPT.md SOURCE.json`; it keeps only visible user/assistant text.

## Let conversations improve Inquiry Graph

For substantive conversations, capture the inquiry and then review how well the
representation served its purpose. The proposed workflow is documented in
[conversation-to-graph self-improvement loop](docs/design/conversation-self-improvement-loop.md).

A conversation may carry a sibling `fit-review.json` that records
representation, extraction, workflow, and factorization friction plus an
explicit promotion gate. Validate it with:

```bash
python tools/check_fit_review.py examples/conversations/2026-10-05-semantic-modeling/fit-review.json
```

The fit review is **evidence about the model, not authority to mutate it**.
Core semantic changes should be promoted only after the documented reuse,
independent-case, approval, and regression gates. See the
[2026-10-05 semantic-modeling fixture](examples/conversations/2026-10-05-semantic-modeling/README.md).

## What is guaranteed—and what is not

The validator checks schema, identity, reference resolution, exact quotes and Unicode offsets, relation-role signatures, actor/source consistency, and restricted temporal ordering. Rejected interpretations remain in the audit trail. Conceptual cycles are allowed; dependency cycles are warnings.

It does **not** certify truth, detect every bad paraphrase, know a person's private beliefs, prove the deduction/induction/abduction taxonomy exhaustive, or select the best next thought. Structured output provides a contract; semantic fidelity still needs review. A valid graph may contain a false claim and its later rejection.

## Trust judgments (optional)

`tools/warrant_adapter.py` feeds a graph into the external `epistemic-warrant` package and returns an accepted/defeated judgment per claim with its source excerpt ids. See [docs/warrant-adapter.md](docs/warrant-adapter.md).

## Project documents

[New-agent handoff](docs/new-agent-handoff.md) · [Project status](docs/project-status.md) · [Requirements](docs/requirements.md) · [Implementation brief](docs/implementation-brief.md) · [Formalism](docs/formalism.md) · [Ontology](docs/ontology.md) · [Architecture](docs/architecture.md) · [Annotation guide](docs/annotation-guide.md) · [Seed review](docs/seed-review.md) · [Conversation walkthrough](docs/conversation-walkthrough.md) · [Evaluation](docs/evaluation.md) · [Verification](docs/verification.md) · [Decisions](docs/decisions/index.md) · [Roadmap](docs/roadmap.md) · [Security](docs/security.md) · [References](docs/references.md)

Rebuild checked-in artifacts with `python examples/build_seed.py && python tools/build_artifacts.py && python examples/build_operational_games.py`. Check drift with `python tools/build_artifacts.py --check` plus `git diff --exit-code -- examples/operational-games-2026-09-30`. Canonical JSON and curation stay in Git; there is no required graph database, vector store, web application, or custom agent runtime.

Code and conversation data remain private. No public redistribution license has been selected. Keep the repository private unless the source conversation and all derived artifacts have been reviewed for release.
