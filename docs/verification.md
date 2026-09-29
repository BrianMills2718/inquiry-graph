# Verification record

## Build environment checks

**Current: post-PR-#36 native-Windows rerun of `main` at `4ad3942` (2026-09-29).** In a fresh Windows virtual environment (Python 3.14.7, Pydantic 2.13.5, NetworkX 3.7, jsonschema 4.26.0, pytest 9.1.1) with `.[dev]` installed from the package index: **142 tests passed**; the seed fixture rebuilt to 229 nodes, 250 relations and 185 moves; `tools/build_artifacts.py` generated **8 artifacts** and `--check` passed (8 checked); canonical graph validation returned zero errors and warnings; `query ... stats` reported 798 proposed and 0 confirmed annotations; and `pip check` reported no broken requirements. The rebuilt `examples/seed/*` and `schemas/*` files matched `main` except for Windows CRLF line endings (`git diff --ignore-cr-at-eol` empty). Graphviz is not installed on that Windows host, so the `dot` step was not run there.

An independent Linux rerun on a tree byte-identical to the same `main` (Python 3.10.12, Pydantic 2.13.5, NetworkX 3.4.2, jsonschema 4.26.0) also produced **142 passed**, the same fixture counts, 8 artifacts with `--check` passing, 0 validation errors/warnings, and byte-identical rebuilt `examples/seed/*`; `dot -Tsvg examples/seed/inquiry.dot` exited 0 there. Its `pip check` flagged only an unrelated system pipx/argcomplete conflict.

These two runs cover PR #36's strategy-performance multiple-comparison/optional-stopping correction. At the handoff review, the commits after verified code commit `4ad3942` were documentation-only, so this execution record still covered the executable tree. Check the current branch diff before assuming that remains true. The previous integrated native-Windows record, before PR #36, was **138 tests passed** with the same fixture, artifact, validation and dependency results.

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

**Hosted CI is still not verified as passing.** Repeated hosted runs have failed or been cancelled before runner steps were recorded and exposed no useful job logs. The cause has not been verified. Do not confuse those pre-execution failures with application-test failures. The post-PR-#36 142-test native-Windows and Linux reruns above are the current independently repeated integrated execution records.

## Semantic-audit caveat

A later independent formal-layer audit opened **issue #46** against code ancestor `024201f`. A comparison from that commit to current `main` shows only documentation changes, so the reported defects still apply to the current executable tree until fixed. The audit reproduced: (1) a preference-removal counterexample in which an assumption and its contrary can both become grounded-IN; (2) failure to enforce flat ABA when an assumption is also a rule head; and (3) a grounded-dialectical warrant that can ignore a mismatched action target. These are semantic/rationality defects that the 142-test suite does not currently catch.

Therefore a green integration run must not be described as proof that the formal reference regimes are semantically correct. Issue #46 is the immediate correctness gate before stronger acceptance/warrant work.

## Explicitly not verified

The integrated research-layer code has now been exercised by a full repository pytest/artifact/graph-validation run. Remaining unverified areas are: no live paid API extraction, no model comparison, no full conversation-export reconciliation, no independent human adjudication of the 798 proposed annotations, and no evidence yet that the tool improves downstream reasoning. The provider boundary is tested with fake clients for normal output, refusal, truncation and transport error. The HTML is a static linked-record inspector, not a deployed application.

## Recovery

Remote WSL failed its guarded health check during implementation. The task process was stopped, no WSL restart was attempted, and unknown local changes were not discarded. The durable implementation was recovered into the separate native Windows checkout `C:\Users\thela\code\inquiry-graph-portable`, using existing Git authentication and a checksummed source bundle already stored in the private repository. The bundle was expanded into ordinary source files and the temporary delivery workflow/parts were removed in a normal commit. Git configuration changes were repository-local only. Any old WSL `feat/v1` work must be inspected before reuse; it was not reset, cleaned, or assumed synchronized.
