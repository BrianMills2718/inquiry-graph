"""Build a browsable site of per-chat Inquiry Graph views: a searchable list, one shared viewer, one small JSON file per chat.

Usage: build_site.py <out_dir> --graph-dirs DIR [DIR ...] [--authorship authorship.json --records records.json] [--limit N]
Graph dirs are given in priority order; a chat takes the graph with the most relations (so a second-pass linked graph beats the original).
Output (private: quote-bearing; serve it only behind the gate): index.html (search by title), viewer.html (?id=<chat>), data/<chat>.json.
Each idea carries the stances taken on it, with an authorship tag from check_authorship.py (own words / pasted / unclear) when provided.
"""
import argparse
import json
import re
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
KIND = {"concept": "#4363d8", "claim": "#f58231", "hypothesis": "#911eb4", "question": "#ffe119", "goal": "#3cb44b",
        "method": "#46f0f0", "example": "#a9a9a9", "reference": "#808000"}


KEY_SHAPES = re.compile(r"\b(sk-[A-Za-z0-9_\-]{20,}|AIza[0-9A-Za-z_\-]{30,}|(?:ghp_|gho_|github_pat_)[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|xox[abprs]-[A-Za-z0-9\-]{10,})")


def redact_keys(text):
    """Pages are served from a shared host: never publish anything shaped like an API key, even one pasted into a chat."""
    return KEY_SHAPES.sub("[redacted key]", text)


def short(t, n=70):
    t = " ".join(t.split())
    return t if len(t) <= n else t[: n - 1] + "…"


def chunk_of(i):
    m = re.search(r":(c\d+):", i)
    return m.group(1) if m else "c00"


def elements(g, auth):
    conv = g["conversations"][0]
    who = {p["id"]: p["label"] for p in conv["participants"]}
    stances = {}
    for e in g["stance_events"]:
        a = e["anchors"][0] if e["anchors"] else {}
        tag = auth.get((a.get("message_id"), a.get("quote"))) if e["actor_id"] == "participant:brian" else None
        stances.setdefault(e["target_id"], []).append({"who": who.get(e["actor_id"], e["actor_id"]), "stance": e["stance"], "quote": a.get("quote", "")[:300], "auth": tag})
    els = [{"data": {"id": "g:" + c, "label": "Part %d" % (int(c[1:]) + 1), "group": True}} for c in sorted({chunk_of(n["id"]) for n in g["nodes"]})]
    for n in g["nodes"]:
        els.append({"data": {"id": n["id"], "parent": "g:" + chunk_of(n["id"]), "label": short(n["text"]), "kind": n["kind"], "text": n["text"],
                             "quote": (n["anchors"][0]["quote"][:400] if n["anchors"] else ""), "color": KIND.get(n["kind"], "#999"), "stances": stances.get(n["id"], [])}})
    for r in g["relations"]:
        ends = [b["ref"] for b in r["bindings"]]
        if len(ends) >= 2:
            els.append({"data": {"id": r["id"], "source": ends[0], "target": ends[1], "label": r["kind"], "quote": (r["anchors"][0]["quote"][:300] if r["anchors"] else ""),
                                 "inferred": ":L:" in r["id"]}})
    return conv, els


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("out", type=Path)
    ap.add_argument("--graph-dirs", nargs="+", required=True)
    ap.add_argument("--authorship", type=Path)
    ap.add_argument("--records", type=Path)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args()
    auth = {}
    if a.authorship and a.records:
        lab = json.loads(a.authorship.read_text())
        for r in json.loads(a.records.read_text())["records"]:
            if r["id"] in lab:
                auth[(r["message_id"], r["quote"])] = lab[r["id"]]["label"]
    best = {}
    for d in a.graph_dirs:
        for f in Path(d).glob("*.graph.json"):
            n = len(json.loads(f.read_text())["relations"])
            if f.name not in best or n > best[f.name][0]:
                best[f.name] = (n, f)
    (a.out / "data").mkdir(parents=True, exist_ok=True)
    rows = []
    for name, (nrel, f) in sorted(best.items()):
        g = json.loads(f.read_text())
        if len(g["nodes"]) < 3:
            continue
        conv, els = elements(g, auth)
        cid = name.removesuffix(".graph.json")
        stamps = sorted(m["timestamp"][:10] for m in conv["messages"] if m.get("timestamp"))
        (a.out / "data" / f"{cid}.json").write_text(redact_keys(json.dumps({"title": conv["title"][:200], "elements": els, "kinds": KIND}, ensure_ascii=False, separators=(",", ":"))), encoding="utf-8")
        rows.append({"id": cid, "title": " ".join(conv["title"].split())[:110], "date": stamps[0] if stamps else "", "ideas": len(g["nodes"]), "links": nrel,
                     "source": conv["id"].split(":", 1)[0]})
        if a.limit and len(rows) >= a.limit:
            break
    subprocess.run(["npx", "esbuild", "app.js", "--bundle", "--minify", "--format=iife", "--outfile=bundle.js"], cwd=HERE, check=True)
    viewer = (HERE / "index.src.html").read_text(encoding="utf-8").replace('<script src="bundle.js"></script>', "<script>" + (HERE / "bundle.js").read_text(encoding="utf-8").replace("</script>", "<\\/script>") + "</script>")
    (a.out / "viewer.html").write_text(viewer, encoding="utf-8")
    rows.sort(key=lambda r: r["date"], reverse=True)
    index = ('<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>Chats</title>'
             '<style>body{font:16px/1.4 system-ui;max-width:52rem;margin:1rem auto;padding:0 16px}input{width:100%;box-sizing:border-box;font:inherit;padding:.6rem;margin:.5rem 0 1rem}'
             'li{margin:.35rem 0}small{color:#555}</style><h1>Chats as idea graphs</h1><p><small>Private. Type to search titles; click a chat to open its graph. '
             'Dashed lines are links proposed by a second pass.</small></p><input id=q placeholder="Search chat titles" autofocus><ul id=l></ul><script>const R=' +
             json.dumps(rows, ensure_ascii=False).replace("</", "<\\/") + ';const l=document.getElementById("l"),q=document.getElementById("q");'
             'function draw(){const t=q.value.toLowerCase();l.innerHTML=R.filter(r=>r.title.toLowerCase().includes(t)).slice(0,300).map(r=>`<li><a href="viewer.html?id=${r.id}">${r.title.replace(/</g,"&lt;")||"(untitled)"}</a> '
             '<small>${r.date} · ${r.source} · ${r.ideas} ideas, ${r.links} links</small></li>`).join("")}q.oninput=draw;draw()</script>')
    (a.out / "index.html").write_text(index, encoding="utf-8")
    print(json.dumps({"chats": len(rows), "out": str(a.out)}))


if __name__ == "__main__":
    main()
