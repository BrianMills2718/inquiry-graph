"""Capture contract: decide, before an expensive run, which schema fields the run will and will not capture.

Why: `moves` was left out of the live extractor for one goal and a later goal needed it; the gap was found only by a count after the money was spent
(see docs/design/capture-contract.md). Rule (Brian approved 2026-10-05): capture an extra field now if  f*C < p*R
  C = expected cost of the pass (USD)       f = extra cost of capturing the field, as a fraction of C
  R = cost of redoing later = C + redo_extra_cost_usd (time/attention converted to USD, default 0)
  p = probability a later use needs the field
Ranges are used for f and p. Verdicts: 'capture' if f_hi*C < p_lo*R; 'skip' if f_lo*C >= p_hi*R; otherwise 'uncertain'.
A field may be left out only when the verdict is 'skip' or `approved_by` is set; missing estimates fail the check.

Usage: capture_contract.py init OUT.json --cost-usd C [--redo-extra-usd X]   (writes a skeleton from the schema)
       capture_contract.py check CONTRACT.json                               (exit 0 ok, 1 not ok; prints every problem and each field's verdict)
Contract JSON: {"run": {"description", "expected_cost_usd", "redo_extra_cost_usd"},
 "fields": {"<collection>": {"captured": bool, "requires_env": {VAR: value} (optional; checked at run time), "reason": str, "marginal_cost_fraction": [lo, hi], "p_later_need": [lo, hi],
                            "blocks_later_uses": [str], "approved_by": str|null, "approved_at": str|null}}}
"""
import argparse
import json
import os
import sys
from pathlib import Path

try:
    from inquiry_graph.model import COLLECTIONS
except ImportError:   # run as a script without the package installed
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
    from inquiry_graph.model import COLLECTIONS


def verdict(f, p, cost, redo_extra):
    redo = cost + redo_extra
    if f[1] * cost < p[0] * redo:
        return "capture"
    if f[0] * cost >= p[1] * redo:
        return "skip"
    return "uncertain"


def _range(v):
    return isinstance(v, (list, tuple)) and len(v) == 2 and all(isinstance(x, (int, float)) for x in v) and v[0] <= v[1]


def check(contract):
    """Return (problems, verdicts)."""
    problems, verdicts = [], {}
    run, fields = contract.get("run", {}), contract.get("fields", {})
    cost, redo_extra = run.get("expected_cost_usd"), run.get("redo_extra_cost_usd", 0)
    if not isinstance(cost, (int, float)) or cost <= 0:
        problems.append("run.expected_cost_usd must be a positive number")
        return problems, verdicts
    for name in COLLECTIONS:
        f = fields.get(name)
        if f is None:
            problems.append(f"{name}: missing from contract (every schema collection must be listed)")
            continue
        if f.get("captured") is True:
            verdicts[name] = "captured"
            for var, want in (f.get("requires_env") or {}).items():   # a field is only captured if the run is actually set up to capture it
                if os.environ.get(var) != want:
                    problems.append(f"{name}: marked captured but the run needs {var}={want} (currently {os.environ.get(var)!r})")
            continue
        if not f.get("reason"):
            problems.append(f"{name}: not captured but no reason given")
        if not f.get("blocks_later_uses") and f.get("blocks_later_uses") != []:
            problems.append(f"{name}: list the later uses a skip would block (use [] if none)")
        fr, pr = f.get("marginal_cost_fraction"), f.get("p_later_need")
        if not (_range(fr) and _range(pr)):
            problems.append(f"{name}: not captured and estimates missing: marginal_cost_fraction and p_later_need must each be [low, high] numbers")
            verdicts[name] = "unestimated"
            continue
        v = verdict(fr, pr, cost, redo_extra)
        verdicts[name] = v
        if v != "skip" and not f.get("approved_by"):
            problems.append(f"{name}: verdict is '{v}' (capturing looks worth it or is unclear); capture it, or set approved_by to the person who approved skipping it")
    extra = set(fields) - set(COLLECTIONS)
    if extra:
        problems.append(f"unknown fields (not schema collections): {sorted(extra)}")
    return problems, verdicts


def init(out, cost, redo_extra):
    fields = {n: {"captured": True, "reason": "", "marginal_cost_fraction": None, "p_later_need": None, "blocks_later_uses": [], "approved_by": None, "approved_at": None}
              for n in COLLECTIONS}
    out.write_text(json.dumps({"run": {"description": "", "expected_cost_usd": cost, "redo_extra_cost_usd": redo_extra}, "fields": fields}, indent=1))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("init"); i.add_argument("out", type=Path); i.add_argument("--cost-usd", type=float, required=True); i.add_argument("--redo-extra-usd", type=float, default=0.0)
    c = sub.add_parser("check"); c.add_argument("contract", type=Path)
    a = ap.parse_args(argv)
    if a.cmd == "init":
        init(a.out, a.cost_usd, a.redo_extra_usd)
        print(f"wrote {a.out}")
        return 0
    problems, verdicts = check(json.loads(a.contract.read_text()))
    print("verdicts:", verdicts)
    for p in problems:
        print("PROBLEM:", p)
    print(f"capture contract {'OK' if not problems else 'NOT OK'} ({len(problems)} problems)")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
