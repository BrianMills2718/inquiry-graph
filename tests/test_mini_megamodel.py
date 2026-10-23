"""Structural expectations for the representation-interoperability mini-megamodel."""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1] / "examples" / "conversations" / "2026-09-30-level-one"
QUERY = HERE / "query_mini_megamodel.py"

spec = importlib.util.spec_from_file_location("mini_megamodel_query", QUERY)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def test_mini_megamodel_inventory_and_mapping_maturity():
    data = module.load()
    summary = module.summary(data)
    assert summary["representations"] == 8
    assert summary["mappings"] == 5
    assert set(summary["implemented_mappings"]) == {
        "sh-v2-to-ontocanon-governed-payload",
        "sh-v2-to-foundation-ir",
        "knowledgework-logical-to-postgresql",
    }
    assert set(summary["nonimplemented_or_design_mappings"]) == {
        "inquiry-v1-to-ontocanon-pack-profile",
        "dodaf-ir-to-fit-for-purpose-projections",
    }
    assert summary["mappings_with_automatic_guarantee_transport"] == []

def test_implemented_paths_do_not_promote_design_mappings():
    data = module.load()
    assert module.paths(data, "scientific-hypergraph-v2", "ontocanon-governed-carrier")
    assert module.paths(data, "scientific-hypergraph-v2", "ontocanon-foundation-ir")
    assert module.paths(data, "knowledgework-logical-model", "knowledgework-postgresql-schema")
    assert module.paths(data, "inquiry-graph-v1", "ontocanon-governed-carrier") == []
    assert module.paths(data, "dodaf-semantic-ir-v1", "representation-router-viewspec") == []

def test_declared_seams_are_visible_without_becoming_implemented():
    data = module.load()
    inquiry = module.paths(data, "inquiry-graph-v1", "ontocanon-governed-carrier", implemented_only=False)
    assert [[m["id"] for m in p] for p in inquiry] == [["inquiry-v1-to-ontocanon-pack-profile"]]
    assert inquiry[0][0]["status"] == "design-mapped-not-executable"
    dodaf = module.paths(data, "dodaf-semantic-ir-v1", "representation-router-viewspec", implemented_only=False)
    assert [[m["id"] for m in p] for p in dodaf] == [["dodaf-ir-to-fit-for-purpose-projections"]]
    assert dodaf[0][0]["status"] == "architecturally-compatible-not-direct-adapter"

def test_registry_does_not_invent_cross_domain_path():
    data = module.load()
    assert module.paths(data, "scientific-hypergraph-v2", "representation-router-viewspec", implemented_only=False) == []

def test_current_paths_do_not_automatically_transport_guarantees():
    data = module.load()
    for source, target in (
        ("scientific-hypergraph-v2", "ontocanon-governed-carrier"),
        ("scientific-hypergraph-v2", "ontocanon-foundation-ir"),
        ("knowledgework-logical-model", "knowledgework-postgresql-schema"),
    ):
        for path in module.paths(data, source, target):
            assert module.transportable(path) is False
