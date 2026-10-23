#!/usr/bin/env python3
"""Validate/query the mini megamodel without importing inquiry_graph."""

from __future__ import annotations
import argparse
import json
from collections import defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
MODEL = HERE / "mini-megamodel.json"
IMPLEMENTED = {"implemented-bounded", "implemented-demo"}

def load(path: Path = MODEL) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    reps = data.get("representations", [])
    maps = data.get("mappings", [])
    ids = [r["id"] for r in reps]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate representation id")
    known = set(ids)
    mids = [m["id"] for m in maps]
    if len(mids) != len(set(mids)):
        raise ValueError("duplicate mapping id")
    for m in maps:
        if m["source"] not in known or m["target"] not in known:
            raise ValueError(f"dangling mapping endpoint: {m['id']}")
        for key in ("status","mapping_kind","direction","evidence","preserves","losses","guarantee_transport","composition_policy"):
            if key not in m:
                raise ValueError(f"mapping {m['id']} missing {key}")
    return data

def edges(data: dict, implemented_only: bool) -> list[dict]:
    out=[]
    for m in data["mappings"]:
        if implemented_only and m["status"] not in IMPLEMENTED:
            continue
        out.append(m)
    return out

def paths(data: dict, source: str, target: str, implemented_only: bool = True) -> list[list[dict]]:
    graph=defaultdict(list)
    for m in edges(data, implemented_only):
        graph[m["source"]].append(m)
    q=deque([(source, [], {source})])
    found=[]
    while q:
        node,path,seen=q.popleft()
        if node==target:
            found.append(path)
            continue
        for m in graph[node]:
            if m["target"] in seen:
                continue
            q.append((m["target"], path+[m], seen|{m["target"]}))
    return found

def transportable(path: list[dict]) -> bool:
    """Conservative: no composed guarantee unless every edge explicitly permits it."""
    if not path:
        return True
    return all(
        m["guarantee_transport"] not in {"none", "none by default; preserved claims require explicit exporter/version-specific proof",
                                         "demo behavior only; no universal semantics-preservation theorem"}
        and m["composition_policy"] not in {"forbid", "forbid-unless-certified", "manual-only"}
        for m in path
    )

def summary(data: dict) -> dict:
    implemented = [m for m in data["mappings"] if m["status"] in IMPLEMENTED]
    nonimplemented = [m for m in data["mappings"] if m["status"] not in IMPLEMENTED]
    return {
        "representations": len(data["representations"]),
        "mappings": len(data["mappings"]),
        "implemented_mappings": [m["id"] for m in implemented],
        "nonimplemented_or_design_mappings": [m["id"] for m in nonimplemented],
        "mappings_with_declared_loss": [m["id"] for m in data["mappings"] if m["losses"]],
        "mappings_with_automatic_guarantee_transport": [
            m["id"] for m in data["mappings"]
            if m["guarantee_transport"] not in {"none", "none by default; preserved claims require explicit exporter/version-specific proof",
                                                "demo behavior only; no universal semantics-preservation theorem"}
            and m["composition_policy"] not in {"forbid", "forbid-unless-certified", "manual-only"}
        ],
    }

def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--source")
    p.add_argument("--target")
    p.add_argument("--all-declared", action="store_true", help="Include design/architectural mappings.")
    p.add_argument("--summary", action="store_true")
    args=p.parse_args()
    data=load()
    if args.summary or not (args.source and args.target):
        print(json.dumps(summary(data), indent=2))
    if args.source and args.target:
        ps=paths(data,args.source,args.target,implemented_only=not args.all_declared)
        print(json.dumps({
            "source":args.source,
            "target":args.target,
            "implemented_only":not args.all_declared,
            "paths":[
                {
                    "mapping_ids":[m["id"] for m in path],
                    "statuses":[m["status"] for m in path],
                    "declared_losses":[loss for m in path for loss in m["losses"]],
                    "automatic_guarantee_transport":transportable(path),
                }
                for path in ps
            ],
        },indent=2))

if __name__=="__main__":
    main()
