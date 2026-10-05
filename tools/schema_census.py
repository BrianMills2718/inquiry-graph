"""Census of what the produced graphs actually contain versus what the schema defines.

Usage: schema_census.py GRAPH_DIR [GRAPH_DIR ...] [--fail-on-empty]
Counts every collection, node kind, relation kind, move kind, stance and question status across graphs (deduplicated by conversation id) and
prints every schema-defined value that appears zero times. A zero is not always a bug (a field may be skipped on purpose), but it must be a
known, written-down choice: run this after each pipeline run and before starting a new use of the data, and compare the zeros with what that
use needs. Exit 1 with --fail-on-empty if any collection (moves, relations, ...) is empty.
"""
import argparse, collections, json, sys, typing
from pathlib import Path
from inquiry_graph import model

ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("dirs", nargs="+", type=Path); ap.add_argument("--fail-on-empty", action="store_true")
a = ap.parse_args()
seen, graphs = set(), 0
coll, nodes, rels, moves, stances, qstat = (collections.Counter() for _ in range(6))
for d in a.dirs:
    for f in sorted(d.glob("*.graph.json")):
        g = json.loads(f.read_text(encoding="utf-8")); cid = g["conversations"][0]["id"]
        if cid in seen: continue
        seen.add(cid); graphs += 1
        for k in model.COLLECTIONS: coll[k] += len(g.get(k, []))
        nodes.update(n["kind"] for n in g["nodes"]); rels.update(r["kind"] for r in g["relations"]); moves.update(m["kind"] for m in g.get("moves", []))
        stances.update(e["stance"] for e in g["stance_events"]); qstat.update(e.get("status") for e in g["question_events"])
def schema_values(field, cls):
    ann = cls.model_fields[field].annotation
    return list(typing.get_args(ann))
print(f"graphs: {graphs}"); print("collections:", dict(coll))
empty = []
for label, seen_c, want in (("node kind", nodes, list(typing.get_args(model.NodeKind))), ("relation kind", rels, sorted(model.SIGNATURES)),
                            ("move kind", moves, list(typing.get_args(model.MoveKind))), ("stance", stances, schema_values("stance", model.StanceEvent))):
    missing = [w for w in want if not seen_c.get(w)]
    print(f"{label}: seen {dict(seen_c)}"); print(f"  never seen: {missing or 'none'}")
    empty += [(label, w) for w in missing]
print("question statuses seen:", dict(qstat))
empty_coll = [k for k in model.COLLECTIONS if not coll[k]]
print("EMPTY COLLECTIONS:", empty_coll or "none")
if a.fail_on_empty and empty_coll: sys.exit(1)
