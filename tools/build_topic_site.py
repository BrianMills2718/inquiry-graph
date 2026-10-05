"""Build the gated topic site from run_topic_digests.py outputs: index (positions-by-topic.html), one page per topic (topics/<id>.html), and
open-questions.html (open_question claims + each topic's 'not established' text). Claims whose cites did not resolve are dropped.
Usage: build_topic_site.py <digests_dir> <out_dir>"""
import html, json, sys
from pathlib import Path
src, out = Path(sys.argv[1]), Path(sys.argv[2]); (out / "topics").mkdir(parents=True, exist_ok=True)
KIND = {"position": "Position", "change": "Changed over time", "conflict": "Pulls against itself", "open_question": "Open question"}
CSS = """<style>body{font:16px/1.5 system-ui;max-width:780px;margin:0 auto;padding:16px;color:#1b1b1b;background:#fff}h1{font-size:1.4rem}h2{font-size:1.1rem;margin-top:1.6rem}.sum{background:#eef4fb;padding:.6rem .8rem;border-radius:6px}.claim{margin:.9rem 0}blockquote{margin:.4rem 0 .4rem .5rem;padding-left:.7rem;border-left:3px solid #c9822b}blockquote small{display:block;color:#555}.gap,small,.meta{color:#444;font-size:.92rem}summary{color:#0b5cad;cursor:pointer;font-size:.9rem}a{color:#0b5cad}li{margin:.5rem 0}@media(prefers-color-scheme:dark){body{background:#121212;color:#e8e8e8}.sum{background:#1c2733}blockquote small,.gap,small,.meta{color:#aaa}summary,a{color:#7db4ee}}</style>"""
HEAD = '<!doctype html><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1"><title>%s</title>' + CSS
topics = json.load(open(src / "topics.json")); index, opens, dropped = [], [], 0
def quotes(c): return "".join(f"<blockquote>“{html.escape(e['quote'])}”<small>{e['date']} · {html.escape(e['title'])}</small></blockquote>" for e in sorted(c["evidence"], key=lambda e: e["date"]))
for t in topics:
    tid = t["topic"].split(":")[1]; f = src / f"{tid}.json"
    if not f.exists(): continue
    a = json.load(open(f)); claims = [c for c in a["claims"] if c.get("cites_resolved")]; dropped += len(a["claims"]) - len(claims)
    body = [f"<p><a href='../positions-by-topic.html'>All topics</a> · <a href='../open-questions.html'>What I keep leaving open</a></p><h1>{html.escape(t['name'])}</h1><p class=meta>{t['chats']} chats, {t['first'][:7]} to {t['last'][:7]}</p><p class=sum>{html.escape(a['summary'])}</p>"]
    for c in claims:
        body.append(f"<div class=claim><b>{KIND.get(c['kind'], c['kind'])}.</b> {html.escape(c['statement'])}<details><summary>{len(c['evidence'])} quotes from your chats</summary>{quotes(c)}</details></div>")
        if c["kind"] == "open_question": opens.append((t["name"], tid, c))
    if a.get("unsupported_or_unknown"): body.append(f"<p class=gap><b>Not established:</b> {html.escape(a['unsupported_or_unknown'])}</p>")
    (out / "topics" / f"{tid}.html").write_text(HEAD % html.escape(t["name"]) + "".join(body))
    index.append(f"<li><a href='topics/{tid}.html'>{html.escape(t['name'])}</a> <small>{t['chats']} chats · {len(claims)} claims</small><br><small>{html.escape(a['summary'][:230])}…</small></li>")
(out / "positions-by-topic.html").write_text(HEAD % "My positions by topic" + f"<h1>My positions by topic (private)</h1><p><a href='open-questions.html'>What I keep leaving open, across topics</a> · <a href='positions-by-topic-5.html'>Five hand-read topics</a></p><p class=meta>Each answer comes from your own words in ChatGPT, Claude and Gemini chats; pasted text is left out. Every quote is checked against its source message. Summaries are machine-written: a hand-check of 10 claims found 6 supported, 3 over-read and 1 weak, so treat the label (especially 'changed over time') as a lead to verify with the quotes.</p><ul>{''.join(index)}</ul>")
ob = [f"<li><b>{html.escape(n)}</b> · <a href='topics/{tid}.html'>topic</a><br>{html.escape(c['statement'])}<details><summary>{len(c['evidence'])} quotes</summary>{quotes(c)}</details></li>" for n, tid, c in opens]
(out / "open-questions.html").write_text(HEAD % "What I keep leaving open" + f"<p><a href='positions-by-topic.html'>All topics</a></p><h1>What I keep leaving open (private)</h1><p class=meta>{len(opens)} open questions across {len(topics)} topics, from your own questions and statements.</p><ul>{''.join(ob)}</ul>")
print(len(index), "topic pages;", len(opens), "open questions;", dropped, "unresolved claims dropped")
