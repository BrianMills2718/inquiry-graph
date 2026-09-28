# Verification record

## Build environment checks

Last fully executed local repository result: **67 tests passed**; graph validation returned zero errors and warnings. That run predates the newest defeat, ABA, argument-preference, and preference-filtering modules. Those newer modules are present in GitHub with unit tests, but the full repository suite has not yet been re-executed against them because the remote local agent became unavailable.

The offline suite passed in the isolated conversation build environment with Python 3.13, Pydantic 2.13.4 and NetworkX 3.6.1. The editable package built using preinstalled dependencies; this environment had no package-index DNS access.

An independent **fresh Windows virtual environment** then installed `.[dev,llm]` from the package index successfully and passed **all 59 tests** on Python 3.14.7, Pydantic 2.13.5, NetworkX 3.7 and OpenAI SDK 2.54.0. Fixture rebuilding, all eight generated-artifact checks, canonical graph validation and `pip check` passed. This independently checks packaging, newer dependencies and native Windows without relying on WSL.

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

**Hosted CI is not verified as passing.** Repeated hosted runs, including later research-layer branches, have failed or been cancelled before runner steps were recorded and have exposed no useful job logs. The cause has not been verified. Do not confuse those pre-execution failures with application-test failures, and do not infer CI success from the workflow file. The executed local suites remain the last full-repository verification record; newer research-layer code is explicitly execution-pending.

## Explicitly not verified

The newest defeat/ABA/preference, warrant/license integration, graded-support warrant, strict-Horn deductive warrant, measurement/testimony reliability, statistical/PAC warrant, and strategy-performance warrant code has not yet been exercised by a full repository pytest/artifact/graph-validation run. Unit and end-to-end test files are committed as executable specifications, but no new passing full-suite count is claimed. No live paid API extraction, no model comparison, no full conversation-export reconciliation, no independent human adjudication of the 798 proposed annotations, and no evidence that the tool improves downstream reasoning yet. The provider boundary is tested with fake clients for normal output, refusal, truncation and transport error. The HTML is a static linked-record inspector, not a deployed application.

## Recovery

Remote WSL failed its guarded health check during implementation. The task process was stopped, no WSL restart was attempted, and unknown local changes were not discarded. The durable implementation was recovered into the separate native Windows checkout `C:\Users\thela\code\inquiry-graph-portable`, using existing Git authentication and a checksummed source bundle already stored in the private repository. The bundle was expanded into ordinary source files and the temporary delivery workflow/parts were removed in a normal commit. Git configuration changes were repository-local only. Any old WSL `feat/v1` work must be inspected before reuse; it was not reset, cleaned, or assumed synchronized.
