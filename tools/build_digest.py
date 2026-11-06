"""Render topic answers (ask_positions.py outputs) as one readable page: claim, kind, then the exact dated quotes under it.
Usage: build_digest.py out.html answer1.json [answer2.json ...]"""
import html, json, sys
out, files = sys.argv[1], sys.argv[2:]
KIND = {"position": "Position", "change": "Changed over time", "conflict": "Pulls against itself", "open_question": "Open question"}
parts = []
for f in files:
    a = json.load(open(f)); parts.append(f"<section><h2>{html.escape(a['question'])}</h2><p class=sum>{html.escape(a['summary'])}</p>")
    for c in a["claims"]:
        parts.append(f"<div class=claim><b>{KIND.get(c['kind'], c['kind'])}.</b> {html.escape(c['statement'])}<details><summary>{len(c['evidence'])} quotes from your chats</summary>")
        for e in sorted(c["evidence"], key=lambda e: e["date"]):
            parts.append(f"<blockquote>“{html.escape(e['quote'])}”<small>{e['date']} · {html.escape(e['title'])}</small></blockquote>")
        parts.append("</details></div>")
    if a.get("unsupported_or_unknown"): parts.append(f"<p class=gap><b>Not established:</b> {html.escape(a['unsupported_or_unknown'])}</p>")
    parts.append("</section>")
open(out, "w").write("""<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>My positions by topic</title>
<style>body{font:16px/1.5 system-ui;max-width:780px;margin:0 auto;padding:16px;color:#1b1b1b;background:#fff}h1{font-size:1.4rem}h2{font-size:1.1rem;margin-top:2.2rem;border-top:2px solid #0b5cad;padding-top:.8rem}.sum{background:#eef4fb;padding:.6rem .8rem;border-radius:6px}.claim{margin:.9rem 0}blockquote{margin:.4rem 0 .4rem .5rem;padding-left:.7rem;border-left:3px solid #c9822b}blockquote small{display:block;color:#555}.gap{color:#444;font-size:.92rem}summary{color:#0b5cad;cursor:pointer;font-size:.9rem}@media(prefers-color-scheme:dark){body{background:#121212;color:#e8e8e8}.sum{background:#1c2733}blockquote small,.gap{color:#aaa}summary{color:#7db4ee}}</style>
<h1>My positions by topic (private)</h1><p>Each answer comes from your own words in ChatGPT, Claude and Gemini chats. Every quote is checked against the source message. Pasted text is left out.</p>"""+"".join(parts))
