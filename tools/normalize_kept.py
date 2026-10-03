"""Normalize every Kept vault Markdown file into Conversation records, reconciled against the ChatGPT exporter set.

Writes <out>/<platform>-<id>.conv.json and <out>/dispositions.json. Every input file gets a disposition:
normalized, duplicate_of_exporter (same ChatGPT thread id already in --exporter-dir; the exporter copy is the fuller
record), or failed. Nothing is silently skipped.
"""
import argparse
import collections
import json
from pathlib import Path

from inquiry_graph.kept_markdown import parse_kept_markdown
from inquiry_graph.model import Graph
from inquiry_graph.validate import require_valid


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("vault_dir", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--exporter-dir", type=Path, help="directory of exporter *.conv.json; ChatGPT ids found there are not re-emitted")
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    have = {p.name.removesuffix(".conv.json") for p in a.exporter_dir.glob("*.conv.json")} if a.exporter_dir else set()
    disp = {}
    for f in sorted(a.vault_dir.rglob("*.md")):
        key = f"{f.parent.name}/{f.name}"
        try:
            conv, skipped = parse_kept_markdown(f.read_text(encoding="utf-8"))
            platform, _, raw_id = conv.id.partition(":")
            if platform == "chatgpt" and raw_id in have:
                disp[key] = {"status": "duplicate_of_exporter", "id": conv.id}
                continue
            require_valid(Graph(id="import-check", conversations=[conv]))
            (a.out_dir / f"{platform}-{raw_id}.conv.json").write_text(conv.model_dump_json(indent=1), encoding="utf-8")
            disp[key] = {"status": "normalized", "id": conv.id, "platform": platform, "warn": "COMPLETENESS WARNING" in (conv.coverage_note or "")}
        except Exception as e:
            disp[key] = {"status": "failed", "error": f"{type(e).__name__}: {str(e)[:200]}"}
    (a.out_dir / "dispositions.json").write_text(json.dumps(disp, indent=1), encoding="utf-8")
    by = collections.Counter((v.get("platform") or f.split("/")[0], v["status"]) for f, v in disp.items())
    print(json.dumps({"files": len(disp), **collections.Counter(v["status"] for v in disp.values()), "by_platform_status": {f"{k[0]}/{k[1]}": n for k, n in sorted(by.items())}}))


if __name__ == "__main__":
    main()
