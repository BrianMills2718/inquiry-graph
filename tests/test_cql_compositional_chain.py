"""Concrete finite check of the CQL functorial pullback-composition example."""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1] / "examples" / "conversations" / "2026-09-30-level-one"
CHECK = HERE / "check_cql_compositional_chain.py"

spec = importlib.util.spec_from_file_location("cql_chain_check", CHECK)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_cql_pullback_composition_fixture():
    result = module.check()
    assert result["composite_mapping_matches"] is True
    assert result["sequential_equals_direct"] is True
    assert result["target_only_department_not_preserved"] is True
    assert result["rows"] == [{"id": "w1", "name": "Ada"}, {"id": "w2", "name": "Lin"}]

def test_fixture_does_not_overclaim_preservation():
    data = module.load()
    assert "invertibility" in data["guarantee"]["not_claimed"]
    assert "preservation of U-only attributes such as department" in data["guarantee"]["not_claimed"]
    assert "arbitrary guarantee transport unrelated to Δ pullback" in data["guarantee"]["not_claimed"]
