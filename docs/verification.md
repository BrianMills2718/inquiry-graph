# Verification record

## Build environment checks

Latest local result: **59 tests passed**; graph validation returned zero errors and warnings.

The offline suite ran in an isolated conversation build environment with Python 3.13, Pydantic 2.13.4 and NetworkX 3.6.1. The editable package built successfully using the environment's preinstalled dependencies. This sandbox had no package-index DNS access, so fresh network dependency installation is delegated to the GitHub CI workflow rather than claimed as a local clean-room check.

Commands exercised:

```bash
python -m pytest -q
PYTHONPATH=src python examples/build_seed.py
PYTHONPATH=src python tools/build_artifacts.py
PYTHONPATH=src python tools/build_artifacts.py --check
PYTHONPATH=src python -m inquiry_graph validate examples/seed/graph.json
PYTHONPATH=src python -m inquiry_graph query examples/seed/graph.json stats
dot -Tsvg examples/seed/inquiry.dot -o /tmp/inquiry.svg
```

The integrated tests exercise import, prepare, response-file extraction, validation, query, render, exact merge, no-overwrite and quarantine paths. The generated graph has zero structural errors or warnings. Deterministic rendering is checked across different Python hash seeds; the initial non-deterministic NetworkX view ordering was found and corrected before release.

## GitHub checks

The repository CI installs the package with development and optional provider dependencies on Python 3.11 and 3.13, rebuilds the fixture and artifacts, runs tests, validates the graph, checks generated-file drift and dependency consistency. The PR/Actions checks are the authoritative hosted execution record; do not infer success from the existence of the workflow file alone.

## Explicitly not verified

No live paid API extraction, no model comparison, no full conversation-export reconciliation, no independent human adjudication of the 267 proposed annotations, and no evidence that the tool improves downstream reasoning yet. The provider boundary is tested with fake clients for normal output, refusal, truncation and transport error. The HTML is a static linked-record inspector, not a deployed application.

## Recovery

Remote WSL failed its guarded health check during implementation. The task process was stopped, no WSL restart was attempted, and unknown local changes were not discarded. The durable implementation is on the GitHub portable branch/main after review; any local `feat/v1` work must be inspected before reuse.
