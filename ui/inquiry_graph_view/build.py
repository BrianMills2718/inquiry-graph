"""Build a standalone, offline HTML view of one Inquiry Graph graph.

Usage: python build.py <graph.json> <out.html>
Ideas are grouped by the conversation chunk in their id (the cNN part). ELK packs the group boxes into a grid and lays out
each box's ideas and relations. The page embeds exact quotes: keep the output private. Requires `npm install` here once.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
KIND = {"concept": "#4363d8", "claim": "#f58231", "hypothesis": "#911eb4", "question": "#ffe119", "goal": "#3cb44b",
        "method": "#46f0f0", "example": "#a9a9a9", "reference": "#808000"}   # no red/green pair


def short(t, n=70):
    t = " ".join(t.split())
    return t if len(t) <= n else t[: n - 1] + "…"


def main(graph_path, out_path):
    g = json.loads(Path(graph_path).read_text(encoding="utf-8"))
    chunk = lambda i: (re.search(r":(c\d+):", i) or [None, "c00"])[1]
    els = [{"data": {"id": "g:" + c, "label": "Part %d" % (int(c[1:]) + 1), "group": True}} for c in sorted({chunk(n["id"]) for n in g["nodes"]})]
    for n in g["nodes"]:
        els.append({"data": {"id": n["id"], "parent": "g:" + chunk(n["id"]), "label": short(n["text"]), "kind": n["kind"], "text": n["text"],
                             "quote": (n["anchors"][0]["quote"] if n["anchors"] else ""), "color": KIND.get(n["kind"], "#999")}})
    for r in g["relations"]:
        ends = [b["ref"] for b in r["bindings"]]
        if len(ends) >= 2:
            els.append({"data": {"id": r["id"], "source": ends[0], "target": ends[1], "label": r["kind"],
                                 "quote": (r["anchors"][0]["quote"] if r["anchors"] else "")}})
    (HERE / "data.json").write_text(json.dumps({"title": g["conversations"][0]["title"], "elements": els, "kinds": KIND}), encoding="utf-8")
    subprocess.run(["npx", "esbuild", "app.js", "--bundle", "--minify", "--format=iife", "--outfile=bundle.js", "--loader:.json=json"], cwd=HERE, check=True)
    page = (HERE / "index.src.html").read_text(encoding="utf-8").replace(
        '<script src="bundle.js"></script>', "<script>" + (HERE / "bundle.js").read_text(encoding="utf-8").replace("</script>", "<\\/script>") + "</script>")
    Path(out_path).write_text(page, encoding="utf-8")
    print(f"wrote {out_path} ({len(page) // 1024} KB, {len(g['nodes'])} ideas, {len(g['relations'])} relations)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
