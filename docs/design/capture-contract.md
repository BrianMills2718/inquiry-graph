# Capture contract: decide what an expensive run will not capture before it runs

Status: adopted by Brian 2026-10-05 ("i approve your recommendation").

## Why
`moves` was left out of the live extractor for one goal (commit `9c8d431`, 2026-09-29; the only record was a code comment) and a later goal, how Brian reasons, needed it. A count after the run (`tools/schema_census.py`) found 0 of 2,176 graphs had any. Redoing costs real money (the full OpenRouter pass cost $7.69, plus earlier runs) and time. The check belongs before the run.

## Rule
Before any run with no `--budget` or `--budget >= 2` USD, write a contract (`tools/capture_contract.py init`, example `docs/capture_contracts/extraction-position-memory.json`) listing every schema collection as captured or not. For each field left out: the reason, the later uses the skip blocks, and two ranges: `f`, the extra cost of capturing it in the same pass as a fraction of the pass cost `C`; and `p`, the probability a later use needs it.

Capture the field if `f*C < p*R`, where `R = C + redo_extra_cost_usd` (time and attention to redo, converted to USD). Money only: capture if `f < p`. With ranges, the verdict is `capture` if `f_hi*C < p_lo*R`, `skip` if `f_lo*C >= p_hi*R`, else `uncertain`. Leaving a field out needs a `skip` verdict or an `approved_by` naming who approved it. Missing estimates fail the check. `tools/extract_queue.py` refuses to start an expensive run without a passing contract. After the run, `tools/schema_census.py` confirms the contract was kept.

Worked example (from the prior-art survey): `C = 7.69`, `p = 0.3` gives break-even extra cost `$2.31`; `f = 0.10` captures ($0.77), `f = 0.40` skips ($3.08), and ten minutes of attention valued at $10 flips the second to capture (`R = 17.69`, threshold `$5.31`).

## Updating the estimates
`tools/decision_ledger.py` (built 2026-10-05): one append-only ledger, JSONL per day (`private/ledger/decisions-YYYY-MM-DD.jsonl`, gitignored), with `decision` and `resolution` events. `update` gives `p` a Beta(3,7) prior updated by resolved needed yes/no outcomes, and `f` and cost estimates a mean of log(actual/estimate) shrunk toward 0 with prior weight 3; `rule` applies this contract's verdict (it imports `capture_contract.verdict`). About ten decisive outcomes per decision type are needed before an updated value beats the prior; until then `update` says so. Exchange rates for time and attention are placeholders ($60 and $120 per hour) until Brian gives his. Backfill of five past decisions (hindsight estimates, real outcomes): `examples/decision-ledger-backfill/`.

## Wrong when
This decision is wrong if (a) the contract step is skipped or rubber-stamped in more than one of the next five expensive runs, or (b) a field marked `skip` with a clear verdict is later needed in a run that costs more than its estimated `f*C` to redo. Check at the next five runs and when ten ledger outcomes exist.

## First contract, resolved (2026-10-06)
The first contract failed on purpose: `moves` had no estimates. A 34-chat pilot (PR #175, `INQUIRY_EXTRACT_MOVES=1`) measured the extra cost of capturing moves at f = 0.11 of the pass (bootstrap 95% interval 0.06 to 0.18). With p in [0.5, 0.9] the rule says capture, so the contract now marks `moves` captured and lists `requires_env: INQUIRY_EXTRACT_MOVES=1`, which the check verifies at run time (a contract cannot claim a field the run is not set up to capture). `tools/finish_pipeline.sh` sets it.

Not done: the 2,176 existing graphs still have zero moves. Backfilling re-runs every chat (about $8.5 at today's cost) and is a separate decision. The move prompt also under-produces test, deduce, generalize and retract (ask is over a third of all moves); tune it before any backfill.
