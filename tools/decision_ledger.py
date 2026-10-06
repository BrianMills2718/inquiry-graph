"""Decision/estimate ledger: record a decision with its estimates BEFORE acting, record what happened AFTER, learn from the gap.

Append-only JSONL, one file per day: <dir>/decisions-YYYY-MM-DD.jsonl (default dir private/ledger, gitignored). Two event types:
  decision    id, ts, project, decision_type, options, chosen, rule, inputs, reversible, resolve_by, reference_class, made_by
  resolution  decision_id, resolved_at, actual {usd, minutes_wall, minutes_attention}, outcome (needed yes|no|unknown), note,
              optional llm_client query (trace_prefix / task / project / since) whose cost is recorded as actual usd
Estimates are {point, low, high}. Four cost primitives: money (usd), wall-clock (minutes_wall), Brian's attention (minutes_attention),
reversibility (reversible); risk is the low/high range. decision_type: capture_extra | pilot_commit | build_adopt | parallel_sequence | money_for_time.
For capture_extra, inputs mean: usd = cost C of the pass; f = extra cost of capturing as a fraction of C; p = P(a later use needs it);
minutes_wall / minutes_attention / redo_extra_usd = what REDOING later costs beyond C. R = C + redo_extra_usd + converted minutes.
For every other type, `options` carry per-option inputs and `rule` is dominance -> irreversible -> expected USD cost.

PLACEHOLDER EXCHANGE RATES (Brian's real dollars-per-hour is UNKNOWN; replace by editing RATES below or env LEDGER_USD_PER_HOUR_WALL / _ATTENTION):
  wall-clock time $60/hour, Brian's attention $120/hour.

Subcommands: add-decision | resolve | show | update | rule. Unresolved, overdue and unknown outcomes are always listed, never dropped.
Quote-bearing content does not belong in a ledger record; note fields hold numbers and short paraphrase only.
"""
import argparse
import glob
import hashlib
import json
import math
import os
import sys
from datetime import date, datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import capture_contract  # noqa: E402  (verdict() is reused, not copied)

RATES = {"usd_per_hour_wall": 60.0, "usd_per_hour_attention": 120.0, "is_placeholder": True}
PRIOR_BETA = (3, 7)          # Beta(3,7): prior mean p = 0.3
PRIOR_WEIGHT_N0 = 3          # shrinkage of mean log(actual/estimate) toward 0
MIN_RESOLVED_FOR_UPDATE = 10
DECISION_TYPES = ("capture_extra", "pilot_commit", "build_adopt", "parallel_sequence", "money_for_time")
DEFAULT_DIR = Path(__file__).resolve().parents[1] / "private" / "ledger"


def rates():
    r = dict(RATES)
    for key, env in (("usd_per_hour_wall", "LEDGER_USD_PER_HOUR_WALL"), ("usd_per_hour_attention", "LEDGER_USD_PER_HOUR_ATTENTION")):
        if os.environ.get(env):
            r[key] = float(os.environ[env])
            r["is_placeholder"] = False
    return r


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def est(v):
    """Normalise an estimate to {point, low, high}; a bare number or [low, point, high] is accepted; raises on bad input."""
    if isinstance(v, (int, float)) and not isinstance(v, bool):
        v = {"point": v, "low": v, "high": v}
    elif isinstance(v, (list, tuple)) and len(v) == 3:
        v = {"low": v[0], "point": v[1], "high": v[2]}
    if not isinstance(v, dict) or set(v) != {"point", "low", "high"}:
        raise ValueError(f"estimate must be {{point, low, high}}, got {v!r}")
    if not all(isinstance(v[k], (int, float)) and not isinstance(v[k], bool) for k in v):
        raise ValueError(f"estimate values must be numbers: {v!r}")
    if not v["low"] <= v["point"] <= v["high"]:
        raise ValueError(f"need low <= point <= high: {v!r}")
    return {k: v[k] for k in ("point", "low", "high")}


def norm_inputs(inputs):
    return {k: est(v) for k, v in (inputs or {}).items()}


def append(directory, event, day):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"decisions-{day}.jsonl"
    with open(path, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(event, sort_keys=True) + "\n")   # single write: one line per event
    return path


def load_events(directory):
    decisions, resolutions, bad = {}, {}, []
    for path in sorted(glob.glob(str(Path(directory) / "decisions-*.jsonl"))):
        for n, line in enumerate(open(path, encoding="utf-8"), 1):
            if not line.strip():
                continue
            try:
                e = json.loads(line)
            except json.JSONDecodeError as ex:
                bad.append(f"{path}:{n}: {ex}")
                continue
            if e.get("event") == "decision":
                if e["id"] in decisions:
                    bad.append(f"{path}:{n}: duplicate decision id {e['id']}")
                decisions[e["id"]] = e
            elif e.get("event") == "resolution":
                resolutions.setdefault(e["decision_id"], []).append(e)
            else:
                bad.append(f"{path}:{n}: unknown event type {e.get('event')!r}")
    for rs in resolutions.values():
        rs.sort(key=lambda r: r["resolved_at"])   # latest wins in joins; earlier ones stay in the file
    return decisions, resolutions, bad


def make_decision(spec, ts=None):
    for k in ("project", "decision_type", "options", "chosen", "rule", "inputs", "reversible", "resolve_by", "reference_class", "made_by"):
        if k not in spec:
            raise ValueError(f"decision missing field: {k}")
    if spec["decision_type"] not in DECISION_TYPES:
        raise ValueError(f"decision_type must be one of {DECISION_TYPES}")
    opts = []
    for o in spec["options"]:
        o = {"name": o} if isinstance(o, str) else dict(o)
        if "inputs" in o:
            o["inputs"] = norm_inputs(o["inputs"])
        opts.append(o)
    if spec["chosen"] not in [o["name"] for o in opts]:
        raise ValueError("chosen must name one of the options")
    date.fromisoformat(spec["resolve_by"])
    ts = ts or spec.get("ts") or now()
    did = spec.get("id") or "d-" + hashlib.sha256((ts + spec["project"] + spec["chosen"]).encode()).hexdigest()[:8]
    out = {"event": "decision", "id": did, "ts": ts, "project": spec["project"], "decision_type": spec["decision_type"], "options": opts,
           "chosen": spec["chosen"], "rule": spec["rule"], "inputs": norm_inputs(spec["inputs"]), "reversible": bool(spec["reversible"]),
           "resolve_by": spec["resolve_by"], "reference_class": spec["reference_class"], "made_by": spec["made_by"]}
    if spec.get("evidence_note"):
        out["evidence_note"] = spec["evidence_note"]   # how trustworthy the reconstruction is; numbers/paraphrase only
    return out


def query_llm_cost(project, task, trace_prefix, since):
    from llm_client.observability.query import get_cost   # optional dependency; only used when a query is asked for
    return float(get_cost(project=project, task=task, trace_prefix=trace_prefix, since=since))


def make_resolution(decisions, spec):
    if spec["decision_id"] not in decisions:
        raise ValueError(f"unknown decision_id {spec['decision_id']}")
    if spec.get("outcome") not in ("yes", "no", "unknown"):
        raise ValueError("outcome (was the extra capability/information needed) must be yes, no or unknown")
    actual = {k: float(v) for k, v in (spec.get("actual") or {}).items() if v is not None}
    q = spec.get("llm_query")
    if q:
        actual["usd"] = query_llm_cost(q.get("project"), q.get("task"), q.get("trace_prefix"), q.get("since"))
    out = {"event": "resolution", "decision_id": spec["decision_id"], "resolved_at": spec.get("resolved_at") or now(), "actual": actual,
           "outcome": spec["outcome"], "note": spec.get("note", "")}
    if q:
        out["llm_query"] = q
    return out


# ---------- rule ----------
def money(inputs, which, r):
    """USD-equivalent of an option's usd + wall + attention at one exchange rate, for one of point|low|high."""
    g = lambda k: inputs[k][which] if k in inputs else 0.0
    return g("usd") + g("minutes_wall") / 60 * r["usd_per_hour_wall"] + g("minutes_attention") / 60 * r["usd_per_hour_attention"]


def capture_rule(inputs, r):
    c = inputs["usd"]["point"]
    f, p = inputs["f"], inputs["p"]
    redo_lo, redo_hi = (money({k: v for k, v in inputs.items() if k != "usd"}, w, r) + (inputs["redo_extra_usd"][w] if "redo_extra_usd" in inputs else 0.0)
                        for w in ("low", "high"))
    # minutes_* are counted once by money(); redo_extra_usd is added separately above
    v_lo = capture_contract.verdict((f["low"], f["high"]), (p["low"], p["high"]), c, redo_lo)
    v_hi = capture_contract.verdict((f["low"], f["high"]), (p["low"], p["high"]), c, redo_hi)
    v = v_lo if v_lo == v_hi else "uncertain"
    R = c + (redo_lo + redo_hi) / 2
    return {"verdict": v, "C": c, "R_range": [c + redo_lo, c + redo_hi], "f_times_C": [f["low"] * c, f["high"] * c],
            "p_times_R_mid": [p["low"] * R, p["high"] * R], "break_even_extra_usd_mid": p["point"] * R, "point_extra_usd": f["point"] * c}


def option_cost(o, r):
    i = o.get("inputs", {})
    return {w: money(i, w, r) for w in ("point", "low", "high")}


def choose(options, r):
    """Dominance (worse on every axis, reversibility included) -> irreversible to Brian -> expected USD cost at one rate."""
    axes = ("usd", "minutes_wall", "minutes_attention")
    pt = lambda o, k: o.get("inputs", {}).get(k, {}).get("point", 0.0)
    rev = lambda o: o.get("reversible", True)
    dominated = set()
    for a in options:
        for b in options:
            if a is b:
                continue
            no_worse = all(pt(b, k) <= pt(a, k) for k in axes) and (rev(b) or not rev(a))
            better = any(pt(b, k) < pt(a, k) for k in axes) or (rev(b) and not rev(a))
            if no_worse and better:
                dominated.add(a["name"])
    live = [o for o in options if o["name"] not in dominated]
    out = {"dominated": sorted(dominated), "costs_usd": {o["name"]: option_cost(o, r) for o in options}}
    irrev = [o["name"] for o in live if not rev(o)]
    if irrev:
        out.update(verdict="to_brian", reason=f"irreversible option(s) among the non-dominated: {irrev}")
        return out
    best = min(live, key=lambda o: option_cost(o, r)["point"])
    rng = [o["name"] for o in live if o is not best and option_cost(o, r)["low"] <= option_cost(best, r)["high"]]
    out.update(verdict=best["name"], reason="lowest expected cost at one rate", ranges_overlap_with=rng)
    return out


def apply_rule(d, r):
    if d["decision_type"] == "capture_extra":
        out = capture_rule(d["inputs"], r)
        out["implied_choice"] = {"capture": "capture", "skip": "skip"}.get(out["verdict"], "uncertain")
        return out
    out = choose(d["options"], r)
    out["implied_choice"] = out["verdict"]
    return out


# ---------- summaries ----------
def join(decisions, resolutions, today):
    rows = []
    for d in sorted(decisions.values(), key=lambda d: d["ts"]):
        rs = resolutions.get(d["id"], [])
        res = rs[-1] if rs else None
        status = "resolved" if res else ("overdue" if d["resolve_by"] < today else "unresolved")
        rows.append({"decision": d, "resolution": res, "status": status})
    orphans = sorted(set(resolutions) - set(decisions))
    return rows, orphans


def posterior(decs):
    yes = sum(1 for d in decs if d["res"] and d["res"]["outcome"] == "yes")
    no = sum(1 for d in decs if d["res"] and d["res"]["outcome"] == "no")
    unk = sum(1 for d in decs if d["res"] and d["res"]["outcome"] == "unknown")
    a, b = PRIOR_BETA[0] + yes, PRIOR_BETA[1] + no
    return {"yes": yes, "no": no, "unknown_outcome": unk, "alpha": a, "beta": b, "p_mean": a / (a + b),
            "p_sd": math.sqrt(a * b / ((a + b) ** 2 * (a + b + 1))), "prior_mean": PRIOR_BETA[0] / sum(PRIOR_BETA)}


def log_ratios(decs, key):
    out = []
    for d in decs:
        if not d["res"]:
            continue
        e = d["dec"]["inputs"].get(key, {}).get("point")
        a = d["res"]["actual"].get(key)
        if e and a and e > 0 and a > 0:
            out.append(math.log(a / e))
    n = len(out)
    mean = sum(out) / n if n else 0.0
    shrunk = n * mean / (n + PRIOR_WEIGHT_N0)
    return {"n": n, "raw_mean": mean, "shrunk_mean": shrunk, "multiplier": math.exp(shrunk)}


def update_summary(decisions, resolutions, today):
    by = {t: [] for t in DECISION_TYPES}
    for d in decisions.values():
        rs = resolutions.get(d["id"], [])
        by.setdefault(d["decision_type"], []).append({"dec": d, "res": rs[-1] if rs else None, "overdue": not rs and d["resolve_by"] < today})
    out = {}
    for t, decs in by.items():
        resolved = [d for d in decs if d["res"]]
        s = {"decisions": len(decs), "resolved": len(resolved), "unresolved": len(decs) - len(resolved), "overdue": sum(d["overdue"] for d in decs),
             "beta": posterior(decs), "log_ratio_usd": log_ratios(decs, "usd"), "log_ratio_minutes_wall": log_ratios(decs, "minutes_wall")}
        needed = s["beta"]["yes"] + s["beta"]["no"]
        s["decisive_outcomes"] = needed
        s["enough_to_beat_prior"] = needed >= MIN_RESOLVED_FOR_UPDATE
        s["more_needed"] = max(0, MIN_RESOLVED_FOR_UPDATE - needed)
        out[t] = s
    return out


def fmt_est(e):
    return f"{e['point']:g} [{e['low']:g}..{e['high']:g}]"


# ---------- CLI ----------
def load_spec(arg):
    return json.loads(sys.stdin.read() if arg == "-" else Path(arg).read_text())


def cmd_add(a):
    spec = load_spec(a.spec)
    d = make_decision(spec, ts=a.ts)
    decisions, _, _ = load_events(a.dir)
    if d["id"] in decisions:
        raise ValueError(f"decision id {d['id']} already exists (ledger is append-only)")
    path = append(a.dir, d, d["ts"][:10])
    print(f"recorded decision {d['id']} -> {path}")


def cmd_resolve(a):
    decisions, _, _ = load_events(a.dir)
    spec = load_spec(a.spec) if a.spec else {}
    spec.setdefault("decision_id", a.id)
    for k, v in (("outcome", a.outcome), ("note", a.note), ("resolved_at", a.resolved_at)):
        if v is not None:
            spec[k] = v
    actual = spec.setdefault("actual", {})
    for k, v in (("usd", a.usd), ("minutes_wall", a.minutes_wall), ("minutes_attention", a.minutes_attention)):
        if v is not None:
            actual[k] = v
    if a.query_task or a.query_trace_prefix:
        spec["llm_query"] = {"project": a.query_project, "task": a.query_task, "trace_prefix": a.query_trace_prefix, "since": a.since}
    r = make_resolution(decisions, spec)
    path = append(a.dir, r, r["resolved_at"][:10])
    print(f"recorded resolution of {r['decision_id']} (outcome {r['outcome']}, actual {r['actual']}) -> {path}")


def cmd_show(a):
    decisions, resolutions, bad = load_events(a.dir)
    today = a.today or date.today().isoformat()
    rows, orphans = join(decisions, resolutions, today)
    for b in bad:
        print("PROBLEM:", b)
    for o in orphans:
        print(f"PROBLEM: resolution for unknown decision {o}")
    for row in rows:
        d, res = row["decision"], row["resolution"]
        inp = ", ".join(f"{k}={fmt_est(v)}" for k, v in d["inputs"].items())
        print(f"[{row['status'].upper()}] {d['id']} {d['ts'][:10]} {d['project']} {d['decision_type']} chose={d['chosen']} rule={d['rule']} reversible={d['reversible']} resolve_by={d['resolve_by']}")
        print(f"    est: {inp}")
        if res:
            print(f"    actual: {res['actual']} needed={res['outcome']} at {res['resolved_at'][:10]} {res['note']}")
    n = {s: sum(1 for r in rows if r["status"] == s) for s in ("resolved", "unresolved", "overdue")}
    unk = sum(1 for r in rows if r["resolution"] and r["resolution"]["outcome"] == "unknown")
    print(f"{len(rows)} decisions: {n['resolved']} resolved ({unk} with outcome unknown), {n['unresolved']} unresolved, {n['overdue']} overdue (as of {today})")
    return 1 if (bad or orphans) else 0


def cmd_update(a):
    decisions, resolutions, bad = load_events(a.dir)
    today = a.today or date.today().isoformat()
    for b in bad:
        print("PROBLEM:", b)
    out = update_summary(decisions, resolutions, today)
    print(f"Prior Beta{PRIOR_BETA} (mean {PRIOR_BETA[0] / sum(PRIOR_BETA):.2f}); log-ratio shrinkage prior weight n0={PRIOR_WEIGHT_N0}; ~{MIN_RESOLVED_FOR_UPDATE} decisive outcomes needed per type")
    for t, s in out.items():
        b = s["beta"]
        print(f"{t}: {s['decisions']} decisions, {s['resolved']} resolved, {s['unresolved']} unresolved ({s['overdue']} overdue); outcomes yes={b['yes']} no={b['no']} unknown={b['unknown_outcome']}")
        print(f"    p posterior Beta({b['alpha']},{b['beta']}) mean {b['p_mean']:.3f} +/- {b['p_sd']:.3f} (prior {b['prior_mean']:.2f}); "
              + ("enough outcomes to prefer over the prior" if s["enough_to_beat_prior"] else f"NOT enough: {s['more_needed']} more decisive outcomes needed, keep the prior"))
        for k in ("log_ratio_usd", "log_ratio_minutes_wall"):
            lr = s[k]
            print(f"    {k}: n={lr['n']} raw mean {lr['raw_mean']:+.3f} shrunk {lr['shrunk_mean']:+.3f} (actual/estimate x{lr['multiplier']:.2f})")
    if a.json:
        print(json.dumps(out, indent=1))
    return 1 if bad else 0


def cmd_rule(a):
    decisions, _, _ = load_events(a.dir)
    if a.id not in decisions:
        raise ValueError(f"unknown decision {a.id}")
    r = rates()
    if a.rate_wall is not None:
        r["usd_per_hour_wall"], r["is_placeholder"] = a.rate_wall, False
    if a.rate_attention is not None:
        r["usd_per_hour_attention"], r["is_placeholder"] = a.rate_attention, False
    d = decisions[a.id]
    out = apply_rule(d, r)
    print(f"rates: wall ${r['usd_per_hour_wall']:g}/h, attention ${r['usd_per_hour_attention']:g}/h" + (" (PLACEHOLDERS, not Brian's answer)" if r["is_placeholder"] else ""))
    print(json.dumps(out, indent=1))
    print(f"rule says {out['implied_choice']}; recorded choice was {d['chosen']}" + ("  -> FLIPS" if out["implied_choice"] not in (d["chosen"], "uncertain") else ""))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", type=Path, default=DEFAULT_DIR, help="ledger directory (default private/ledger)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("add-decision"); p.add_argument("spec", help="JSON file or - for stdin"); p.add_argument("--ts", help="ISO time (backfill only)")
    p = sub.add_parser("resolve"); p.add_argument("id"); p.add_argument("--spec"); p.add_argument("--outcome", choices=["yes", "no", "unknown"])
    p.add_argument("--usd", type=float); p.add_argument("--minutes-wall", type=float); p.add_argument("--minutes-attention", type=float)
    p.add_argument("--note"); p.add_argument("--resolved-at")
    p.add_argument("--query-project"); p.add_argument("--query-task"); p.add_argument("--query-trace-prefix"); p.add_argument("--since")
    p = sub.add_parser("show"); p.add_argument("--today")
    p = sub.add_parser("update"); p.add_argument("--today"); p.add_argument("--json", action="store_true")
    p = sub.add_parser("rule"); p.add_argument("id"); p.add_argument("--rate-wall", type=float); p.add_argument("--rate-attention", type=float)
    a = ap.parse_args(argv)
    try:
        return {"add-decision": cmd_add, "resolve": cmd_resolve, "show": cmd_show, "update": cmd_update, "rule": cmd_rule}[a.cmd](a) or 0
    except (ValueError, KeyError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
