# Verification Record — Inquiry Graph

## 2026-09-30 current-main verification

Verified on native Windows against current `main` after the latest operational-games continuation was merged.

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

- **67 tests passed**
- founding seed rebuild: **250 nodes / 250 relations / 204 moves**
- operational-games continuation rebuild: **103 nodes / 80 relations / 84 moves / 61 stance events / 33 question events**
- both graphs: **0 validation errors / 0 warnings**
- generated founding artifacts: **8 checked**
- **no broken requirements**

The operational-games trajectory contains **109 selected visible excerpts**. It remains a curated, proposed annotation rather than a full-export reconciliation or semantic gold set.

The 30-chat cross-conversation campaign is separately documented in `evaluation/cross_conversation_scale/`; its independent signoff supports only the bounded retrieval-direction decision stated there.

## Earlier 2026-09-30 conversation-continuation verification

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
- operational-games continuation rebuild: **58 nodes / 41 relations / 45 moves / 27 stance events / 13 question events**
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

GitHub-hosted jobs had historically failed/cancelled before useful test execution. On PR #67, the ordinary workflow was corrected to install `.[dev]` rather than the private optional `llm_client` dependency; both Python 3.11 and 3.13 jobs then completed the rebuild, tests, both graph validations, artifact drift check, and dependency check successfully.

The optional live-LLM adapter remains outside hosted CI because it depends on a separately authorized private package/provider path.

## Explicitly not verified

- no live paid extraction run;
- no independent human adjudication of the 798 proposed annotations;
- no full conversation-export reconciliation;
- the first single-conversation pilot favored raw transcript over the graph report (0.81 vs 0.65 key-point coverage);
- the later 30-chat campaign is now tested, but only for its measured retrieval workload: archive-search-then-read averaged 0.67 coverage versus 0.63 for positions + typed links and 0.61 for positions only; no route met the complete source-citation/verbatim-quote contract, and broad generalization was not evaluated;
- no production deployment.

These are product/research questions, not schema-validation guarantees.
