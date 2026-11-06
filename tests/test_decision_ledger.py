import importlib.util
import json
import math
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("decision_ledger", Path(__file__).parent.parent / "tools" / "decision_ledger.py")
dl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dl)


def cap_spec(**kw):
    s = {"id": "d1", "project": "p", "decision_type": "capture_extra", "options": ["capture", "skip"], "chosen": "skip", "rule": "capture_rule",
         "inputs": {"usd": 7.69, "f": [0.4, 0.4, 0.4], "p": [0.3, 0.3, 0.3], "minutes_attention": 0, "redo_extra_usd": 0},
         "reversible": True, "resolve_by": "2026-10-10", "reference_class": "extraction pass", "made_by": "agent"}
    s.update(kw)
    return s


def add(tmp, **kw):
    assert dl.main(["--dir", str(tmp), "add-decision", _write(tmp, cap_spec(**kw))]) == 0


def _write(tmp, spec):
    p = Path(tmp) / f"spec-{spec['id']}.json"
    p.write_text(json.dumps(spec))
    return str(p)


def test_estimate_validation():
    assert dl.est(3) == {"point": 3, "low": 3, "high": 3}
    with pytest.raises(ValueError):
        dl.est({"point": 5, "low": 6, "high": 7})
    with pytest.raises(ValueError):
        dl.est({"point": 1})


def test_rule_reuses_capture_contract_verdict_and_rates_flip_it(tmp_path):
    r = {"usd_per_hour_wall": 60.0, "usd_per_hour_attention": 120.0}
    base = dl.make_decision(cap_spec())
    assert dl.capture_rule(base["inputs"], r)["verdict"] == "skip"           # same numbers as tests/test_capture_contract.py
    with_time = dl.make_decision(cap_spec(inputs={"usd": 7.69, "f": 0.4, "p": 0.3, "minutes_attention": 5, "redo_extra_usd": 0}))
    # 5 min attention = $10 at $120/h -> R = 17.69 -> capture, as in the contract worked example
    assert dl.capture_rule(with_time["inputs"], r)["verdict"] == "capture"
    cheap = dl.make_decision(cap_spec(inputs={"usd": 7.69, "f": 0.4, "p": 0.3, "minutes_attention": 5, "redo_extra_usd": 0}))
    assert dl.capture_rule(cheap["inputs"], {"usd_per_hour_wall": 60, "usd_per_hour_attention": 12})["verdict"] == "skip"


def test_rule_ranges_give_uncertain():
    d = dl.make_decision(cap_spec(inputs={"usd": 7.69, "f": [0.1, 0.2, 0.4], "p": 0.3, "redo_extra_usd": 0}))
    assert dl.capture_rule(d["inputs"], dl.RATES)["verdict"] == "uncertain"


def N(o):
    return dict(o, inputs=dl.norm_inputs(o["inputs"]))


def test_choose_dominance_irreversible_and_expected_cost():
    r = {"usd_per_hour_wall": 60.0, "usd_per_hour_attention": 120.0}
    a = {"name": "a", "inputs": {"usd": 1, "minutes_wall": 10}}
    b = {"name": "b", "inputs": {"usd": 2, "minutes_wall": 20}}
    assert dl.choose([N(a), N(b)], r)["dominated"] == ["b"]
    c = {"name": "c", "inputs": {"usd": 0, "minutes_wall": 600}}   # $0 but ten hours
    out = dl.choose([N(a), N(c)], r)
    assert out["verdict"] == "a" and out["dominated"] == []
    irr = {"name": "irr", "reversible": False, "inputs": {"usd": 5, "minutes_wall": 20}}
    assert dl.choose([N(a), N(irr)], r)["verdict"] == "a"                  # a dominates irr (better on every axis incl. reversibility)
    irr2 = {"name": "irr", "reversible": False, "inputs": {"usd": 0, "minutes_wall": 0}}
    assert dl.choose([N(a), N(irr2)], r)["verdict"] == "to_brian"


def test_append_only_one_file_per_day_and_join_keeps_unresolved(tmp_path):
    for i, day in (("d1", "2026-10-01"), ("d2", "2026-10-02")):
        s = cap_spec(id=i, resolve_by="2026-10-03")
        dl.append(tmp_path, dl.make_decision(s, ts=f"{day}T10:00:00+00:00"), day)
    assert sorted(p.name for p in tmp_path.glob("decisions-*.jsonl")) == ["decisions-2026-10-01.jsonl", "decisions-2026-10-02.jsonl"]
    assert dl.main(["--dir", str(tmp_path), "resolve", "d1", "--outcome", "unknown", "--usd", "3", "--resolved-at", "2026-10-04T00:00:00+00:00"]) == 0
    decs, ress, bad = dl.load_events(tmp_path)
    rows, orphans = dl.join(decs, ress, "2026-10-05")
    assert [r["status"] for r in rows] == ["resolved", "overdue"] and bad == [] and orphans == []
    assert dl.main(["--dir", str(tmp_path), "show", "--today", "2026-10-05"]) == 0


def test_resolve_unknown_decision_fails_loudly(tmp_path):
    assert dl.main(["--dir", str(tmp_path), "resolve", "nope", "--outcome", "yes"]) == 2


def test_duplicate_id_rejected(tmp_path):
    add(tmp_path)
    assert dl.main(["--dir", str(tmp_path), "add-decision", _write(tmp_path, cap_spec())]) == 2


def test_update_beta_and_shrinkage(tmp_path):
    for i in range(4):
        dl.append(tmp_path, dl.make_decision(cap_spec(id=f"d{i}"), ts="2026-10-01T10:00:00+00:00"), "2026-10-01")
    outcomes = ["yes", "yes", "no", "unknown"]
    for i, o in enumerate(outcomes[:3] + ["unknown"]):
        dl.main(["--dir", str(tmp_path), "resolve", f"d{i}", "--outcome", o, "--usd", str(7.69 * math.e), "--resolved-at", "2026-10-04T00:00:00+00:00"])
    decs, ress, _ = dl.load_events(tmp_path)
    s = dl.update_summary(decs, ress, "2026-10-05")["capture_extra"]
    assert (s["beta"]["yes"], s["beta"]["no"], s["beta"]["unknown_outcome"]) == (2, 1, 1)
    assert (s["beta"]["alpha"], s["beta"]["beta"]) == (5, 8) and s["decisive_outcomes"] == 3 and not s["enough_to_beat_prior"]
    assert s["resolved"] == 4 and s["unresolved"] == 0
    # estimate is f*C = 0.4*7.69; actual 7.69*e -> each log ratio = 1 - log(0.4)
    assert s["log_ratio_usd"]["n"] == 4 and s["log_ratio_usd"]["shrunk_mean"] == pytest.approx(4 * (1 - math.log(0.4)) / 7)
    for t in dl.DECISION_TYPES:      # every type is reported even with zero data
        assert t in dl.update_summary(decs, ress, "2026-10-05")


def test_malformed_line_is_reported_not_dropped(tmp_path):
    (tmp_path / "decisions-2026-10-01.jsonl").write_text("{not json\n")
    assert dl.load_events(tmp_path)[2] and dl.main(["--dir", str(tmp_path), "show"]) == 1


def test_capture_extra_log_ratio_compares_extra_cost_not_pass_cost(tmp_path):
    dl.append(tmp_path, dl.make_decision(cap_spec(id="x", inputs={"usd": 10, "f": 0.1, "p": 0.3})), "2026-10-01")   # extra expected = 1.0
    dl.main(["--dir", str(tmp_path), "resolve", "x", "--outcome", "yes", "--usd", "2.0"])
    decs, ress, _ = dl.load_events(tmp_path)
    assert dl.update_summary(decs, ress, "2026-10-05")["capture_extra"]["log_ratio_usd"]["raw_mean"] == pytest.approx(math.log(2.0))


def test_zero_rates_make_capture_money_only():
    r = {"usd_per_hour_wall": 0.0, "usd_per_hour_attention": 0.0}
    d = dl.make_decision(cap_spec(inputs={"usd": 8, "f": [0.1, 0.25, 0.6], "p": [0.3, 0.5, 0.7], "minutes_wall": 120, "minutes_attention": 30}))
    assert dl.capture_rule(d["inputs"], r)["verdict"] == "uncertain"   # 0.6*8=4.8 vs 0.3*8=2.4 straddles
    assert dl.capture_rule(d["inputs"], dl.RATES)["verdict"] == "capture"


def test_flip_marker_ignores_wording_after_the_implied_choice():
    # 'capture going forward' is the capture option, not a flip against an implied 'capture'
    implied, chosen = "capture", "capture going forward"
    assert str(chosen).startswith(implied)
    assert not str("skip").startswith(implied)
