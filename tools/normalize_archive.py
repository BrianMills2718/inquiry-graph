"""Normalize every Conversation Manager per-thread JSON in a directory into Conversation records.

Writes <out>/<raw filename stem>.conv.json and <out>/dispositions.json (normalized, or failed with the error).
Nothing is silently skipped: every input file gets a disposition.
"""
import argparse
import collections
import json
from pathlib import Path

from inquiry_graph.exporter_json import parse_exporter_json
from inquiry_graph.model import Graph
from inquiry_graph.validate import require_valid


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("raw_dir", type=Path)
    ap.add_argument("out_dir", type=Path)
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    disp = {}
    for f in sorted(a.raw_dir.glob("*.json")):
        if f.name.endswith(".history.jsonl"):
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
            conv, _ = parse_exporter_json(d)
            require_valid(Graph(id="import-check", conversations=[conv]))
            (a.out_dir / f"{f.stem}.conv.json").write_text(conv.model_dump_json(indent=1), encoding="utf-8")
            disp[f.stem] = {"status": "normalized", "id": conv.id, "account": d.get("capture_account"), "warn": bool(d.get("completeness_warning"))}
        except Exception as e:
            disp[f.stem] = {"status": "failed", "error": f"{type(e).__name__}: {str(e)[:200]}"}
    (a.out_dir / "dispositions.json").write_text(json.dumps(disp, indent=1), encoding="utf-8")
    print(json.dumps({"files": len(disp), **collections.Counter(v["status"] for v in disp.values())}))


if __name__ == "__main__":
    main()
