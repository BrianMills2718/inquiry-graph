"""Normalize a Claude export zip into Conversation records, reconciled against the Kept vault.

Usage: normalize_claude_export.py <export.zip> <out_dir> [--kept-ids compare_ids.json]
Writes <out_dir>/claude-<uuid>.conv.json and dispositions.json (normalized | failed). Every conversation gets a disposition;
`in_kept` records whether the Kept vault also had it (ids only).
"""
import argparse
import collections
import json
import zipfile
from pathlib import Path

from inquiry_graph.claude_export import parse_claude_conversation
from inquiry_graph.model import Graph
from inquiry_graph.validate import require_valid


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("zip", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--kept-ids", type=Path)
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    kept = set(json.loads(a.kept_ids.read_text())["kept_ids"]) if a.kept_ids else set()
    z = zipfile.ZipFile(a.zip)
    convs = []
    for n in z.namelist():
        if n.endswith(".json"):
            d = json.loads(z.read(n))
            convs += d if isinstance(d, list) else [d]
    disp = {}
    for c in convs:
        uid = c.get("uuid", "?")
        try:
            conv = parse_claude_conversation(c)
            require_valid(Graph(id="import-check", conversations=[conv]))
            (a.out_dir / f"claude-{uid}.conv.json").write_text(conv.model_dump_json(indent=1), encoding="utf-8")
            disp[uid] = {"status": "normalized", "id": conv.id, "in_kept": uid in kept}
        except Exception as e:
            disp[uid] = {"status": "failed", "error": f"{type(e).__name__}: {str(e)[:200]}", "in_kept": uid in kept}
    (a.out_dir / "dispositions.json").write_text(json.dumps(disp, indent=1), encoding="utf-8")
    print(json.dumps({"conversations": len(convs), **collections.Counter(v["status"] for v in disp.values()),
                      "also_in_kept": sum(1 for v in disp.values() if v["in_kept"])}))


if __name__ == "__main__":
    main()
