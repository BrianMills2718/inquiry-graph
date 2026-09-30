# Verification Record — Inquiry Graph

## 2026-09-30 conversation-continuation verification

Verified on the native-Windows execution device against the
`record-operational-games-conversation` working tree after rebuilding both
source-grounded fixtures.

Environment:

- Python 3.14.7
- editable install with `.[dev]`

Executed:

```powershell
python examples/build_seed.py
python tools/build_artifacts.py
python examples/build_operational_games.py
python -m pytest -q
python -m inquiry_graph.cli validate examples/seed/graph.json
python -m inquiry_graph.cli validate examples/operational-games-2026-09-30/graph.json
python tools/build_artifacts.py --check
python -m pip check
```

Result:

- **62 tests passed**
- founding seed rebuild: **250 nodes / 250 relations / 204 moves**
- operational-games continuation rebuild: **38 nodes / 24 relations / 26 moves / 16 stance events / 10 question events**
- both graphs: **0 validation errors / 0 warnings**
- generated founding artifacts: **8 checked**
- **no broken requirements**

The run also exposed two provisional continuation move labels in the founding
curation that were outside the executable V1 move vocabulary. They were
normalized without widening the ontology:

- `name` -> `clarify`
- `refine` -> `reframe`

The operational-games trajectory remains selected excerpts with proposed
annotations; structural validity is not semantic adjudication or full-export
coverage.

## Historical post-split verification

Verified 2026-09-29 from a fresh native-Windows clone of reviewed `main` at:

`fd85714a77e807a7b064426978ca4c0d5dcec332`

Environment:

- Python 3.14.7
- fresh virtual environment
- editable install with `.[dev]`

Executed:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e '.[dev]'
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe examples\build_seed.py
.\.venv\Scripts\python.exe tools\build_artifacts.py --check
.\.venv\Scripts\python.exe -m inquiry_graph validate examples\seed\graph.json
.\.venv\Scripts\python.exe -m pip check
```

Result:

- **60 tests passed**
- seed rebuild: **229 nodes, 250 relations, 185 moves**
- **8 artifacts checked**
- graph validation: **0 errors / 0 warnings**
- **no broken requirements**

This is the authoritative **executed** product-repository verification after the theory split. A later 2026-09-30 curated-seed continuation updates the checked-in dataset to 247 excerpts / 250 nodes / 204 moves / 68 stance events / 86 question events / 59 questions / 858 proposed annotations. That continuation was structurally cross-reference checked during the GitHub update but has not yet had the canonical build/artifact/test commands rerun because the execution device was unavailable.

## Scope

The product repository no longer contains the formal epistemic-warrant reference modules/tests.

Those moved to `BrianMills2718/epistemic-warrant`, which has its own verification record.

## Hosted CI

GitHub-hosted jobs have historically failed/cancelled before runner steps/logs.

Issue #2 tracks that infrastructure problem.

Do not treat pre-run hosted failures as application-test failures.

## Explicitly not verified

- no live paid extraction run;
- no independent human adjudication of the 798 proposed annotations;
- no full conversation-export reconciliation;
- the first AI-reader usefulness pilot did **not** show improvement over the raw transcript on the single-conversation case (raw transcript 0.81 vs graph report 0.65 key-point coverage); multi-conversation usefulness remains untested;
- no production deployment.

These are product/research questions, not schema-validation guarantees.
