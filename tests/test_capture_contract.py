import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("capture_contract", Path(__file__).parent.parent / "tools" / "capture_contract.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


def _contract(moves, cost=7.69, redo_extra=0.0):
    fields = {n: {"captured": True} for n in cc.COLLECTIONS}
    fields["moves"] = moves
    return {"run": {"expected_cost_usd": cost, "redo_extra_cost_usd": redo_extra}, "fields": fields}


def test_verdicts_follow_the_ratio_rule():
    assert cc.verdict([0.1, 0.1], [0.3, 0.3], 7.69, 0) == "capture"      # 0.77 < 2.31
    assert cc.verdict([0.4, 0.4], [0.3, 0.3], 7.69, 0) == "skip"         # 3.08 >= 2.31
    assert cc.verdict([0.1, 0.4], [0.3, 0.3], 7.69, 0) == "uncertain"    # range straddles break-even
    assert cc.verdict([0.4, 0.4], [0.3, 0.3], 7.69, 10.0) == "capture"   # redo also costs attention: 3.08 < 0.3*17.69 = 5.31


def test_uncaptured_without_estimates_fails():
    problems, verdicts = cc.check(_contract({"captured": False, "reason": "skipped", "blocks_later_uses": ["motifs"]}))
    assert verdicts["moves"] == "unestimated" and any("estimates missing" in p for p in problems)


def test_skip_needs_clear_verdict_or_approval():
    moves = {"captured": False, "reason": "costly", "blocks_later_uses": [], "marginal_cost_fraction": [0.1, 0.4], "p_later_need": [0.3, 0.3]}
    problems, _ = cc.check(_contract(moves))
    assert any("approved_by" in p for p in problems)
    problems, _ = cc.check(_contract(dict(moves, approved_by="brian", approved_at="2026-10-05")))
    assert problems == []


def test_clear_skip_passes_and_missing_collection_fails():
    moves = {"captured": False, "reason": "costly", "blocks_later_uses": [], "marginal_cost_fraction": [0.5, 0.6], "p_later_need": [0.05, 0.1]}
    assert cc.check(_contract(moves))[0] == []
    c = _contract(moves)
    del c["fields"]["relations"]
    assert any("relations" in p for p in cc.check(c)[0])


def test_init_writes_a_contract_that_lists_every_collection(tmp_path):
    out = tmp_path / "c.json"
    cc.init(out, 5.0, 0.0)
    import json
    assert set(json.loads(out.read_text())["fields"]) == set(cc.COLLECTIONS)


def test_captured_field_with_requires_env_fails_unless_run_is_set_up(monkeypatch):
    c = _contract({"captured": True, "requires_env": {"INQUIRY_EXTRACT_MOVES": "1"}})
    monkeypatch.delenv("INQUIRY_EXTRACT_MOVES", raising=False)
    assert any("INQUIRY_EXTRACT_MOVES" in p for p in cc.check(c)[0])
    monkeypatch.setenv("INQUIRY_EXTRACT_MOVES", "1")
    assert cc.check(c)[0] == []
