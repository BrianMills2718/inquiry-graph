# Verification record

## Build environment checks

Latest integrated native-Windows verification: **138 tests passed** on Python 3.14.7; fixture rebuilding succeeded; all **8 generated artifacts** matched; canonical graph validation returned zero errors and warnings; and `pip check` reported no broken requirements. This run includes the defeat, ABA, preference, warrant/license, graded-support, deductive, measurement/testimony, statistical/PAC, and strategy-performance research layers.

The offline suite passed in the isolated conversation build environment with Python 3.13, Pydantic 2.13.4 and NetworkX 3.6.1. The editable package built using preinstalled dependencies; this environment had no package-index DNS access.

The current verified environment uses Python 3.14.7, Pydantic 2.13.5 and NetworkX 3.7. An earlier fresh Windows virtual environment had independently installed `.[dev,llm]` from the package index and passed the then-current suite as well. Together these checks cover native Windows packaging plus the current integrated research-layer code without relying on WSL.

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

The repository CI is configured to install the package with development and optional provider dependencies on Python 3.11 and 3.13, rebuild the fixture and artifacts, run tests, validate the graph, and check generated-file drift and dependency consistency.

**Hosted CI is still not verified as passing.** Repeated hosted runs have failed or been cancelled before runner steps were recorded and exposed no useful job logs. The cause has not been verified. Do not confuse those pre-execution failures with application-test failures. The native-Windows integrated run above is the current full-repository execution record.

## Explicitly not verified

The integrated research-layer code has now been exercised by a full repository pytest/artifact/graph-validation run. Remaining unverified areas are: no live paid API extraction, no model comparison, no full conversation-export reconciliation, no independent human adjudication of the 798 proposed annotations, and no evidence yet that the tool improves downstream reasoning. The provider boundary is tested with fake clients for normal output, refusal, truncation and transport error. The HTML is a static linked-record inspector, not a deployed application.

## Recovery

Remote WSL failed its guarded health check during implementation. The task process was stopped, no WSL restart was attempted, and unknown local changes were not discarded. The durable implementation was recovered into the separate native Windows checkout `C:\Users\thela\code\inquiry-graph-portable`, using existing Git authentication and a checksummed source bundle already stored in the private repository. The bundle was expanded into ordinary source files and the temporary delivery workflow/parts were removed in a normal commit. Git configuration changes were repository-local only. Any old WSL `feat/v1` work must be inspected before reuse; it was not reset, cleaned, or assumed synchronized.
