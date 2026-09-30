#!/usr/bin/env python3
"""Executable finite check of the CQL pullback-composition fixture.

This does not implement CQL. It checks the concrete finite instance encoded in
cql-compositional-chain.json and mirrors the theorem Δ_F(Δ_G(I)) = Δ_(G∘F)(I).
The theorem itself comes from functorial data migration / precomposition.
"""

from __future__ import annotations
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = HERE / "cql-compositional-chain.json"

def load() -> dict:
    return json.loads(MODEL.read_text(encoding="utf-8"))

def by_id(data: dict) -> dict[str, dict]:
    return {m["id"]: m for m in data["mappings"]}

def compose(F: dict, G: dict) -> dict:
    """Return object/attribute maps for G∘F, where F:S→T and G:T→U."""
    return {
        "object_map": {k: G["object_map"][v] for k, v in F["object_map"].items()},
        "attribute_map": {k: G["attribute_map"][v] for k, v in F["attribute_map"].items()},
    }

def delta(mapping: dict, target_rows: list[dict], source_entity: str) -> list[dict]:
    """Concrete pullback for the one-entity schemas in this fixture."""
    return [
        {"id": row["id"], **{src_attr: row[tgt_attr] for src_attr, tgt_attr in mapping["attribute_map"].items()}}
        for row in target_rows
    ]

def check() -> dict:
    data=load()
    maps=by_id(data)
    F,G,GF=maps["F"],maps["G"],maps["GF"]
    composed=compose(F,G)
    assert composed["object_map"] == GF["object_map"]
    assert composed["attribute_map"] == GF["attribute_map"]

    u_rows=data["instance_U"]["Worker"]
    t_rows=delta(G,u_rows,"Employee")
    sequential=delta(F,t_rows,"Person")
    direct=delta(GF,u_rows,"Person")
    expected=data["expected_pullback_S"]["Person"]
    assert sequential == direct == expected

    # Negative preservation check: department is not in the source schema and
    # therefore is not claimed to survive the pullback.
    assert all("department" not in row for row in direct)

    return {
        "composite_mapping_matches": True,
        "sequential_equals_direct": True,
        "target_only_department_not_preserved": True,
        "rows": direct,
        "guarantee": data["guarantee"]["id"],
    }

if __name__ == "__main__":
    print(json.dumps(check(), indent=2))
