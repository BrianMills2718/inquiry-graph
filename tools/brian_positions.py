#!/usr/bin/env python3
"""Look up Brian's own words on a topic from his chat history (ChatGPT, Claude, Gemini). One-shot, local, no model call, no network.
Returns the best-matching positions/questions he stated, each with the exact quote, date, chat title and chat id. Pasted/quoted text is excluded.
Usage: brian_positions.py "<topic or question>" [--top 15] [--json] [--rebuild]
Private data: reads ~/code/inquiry-graph/private (gitignored). Quote-bearing output stays in the session; do not publish it."""
import argparse, json, re, sys
from pathlib import Path
from rank_bm25 import BM25Okapi
ROOT = Path(__file__).resolve().parents[1]; R = ROOT / "private"; INDEX = R / "positions_index.json"
sys.path.insert(0, str(ROOT / "tools")); from ask_positions import records, tok
DIRS = ["extract_test_20261003/out", "extract_full_20261003/out", "extract_full_20261003/kept/out", "extract_full_20261003/new108/out", "extract_full_20261003/single/out",
        "extract_full_20261003/claude_export/out", "extract_full_20261003/or_run/out", "extract_full_20261003/lowconf/out"]
def load(rebuild):
    if INDEX.exists() and not rebuild: return json.loads(INDEX.read_text())
    lab = json.loads((R / "authorship_full.json").read_text())
    skip = frozenset((r["message_id"], r["quote"]) for r in json.loads((R / "records_full.json").read_text())["records"] if lab.get(r["id"], {}).get("label") == "pasted_or_quoted")
    recs = records([R / d for d in DIRS if (R / d).is_dir()], skip); INDEX.write_text(json.dumps(recs)); return recs
def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("query"); ap.add_argument("--top", type=int, default=15); ap.add_argument("--json", action="store_true"); ap.add_argument("--rebuild", action="store_true")
    a = ap.parse_args(); recs = load(a.rebuild)
    sc = BM25Okapi([tok(r["target"] + " " + r["quote"] + " " + r["title"]) for r in recs]).get_scores(tok(a.query))
    seen, pick = set(), []
    for i in sorted(range(len(recs)), key=lambda i: -sc[i]):
        k = (recs[i]["message_id"], recs[i]["quote"])
        if sc[i] <= 0 or k in seen: continue
        seen.add(k); pick.append(recs[i])
        if len(pick) == a.top: break
    pick.sort(key=lambda r: r["date"])
    if a.json: print(json.dumps(pick, indent=1)); return
    print(f"{len(pick)} of {len(recs)} own-words records matched '{a.query}' (oldest first). Keyword match: wording must overlap, so try synonyms.")
    for r in pick: print(f"- {r['date']} | {r['title'][:60]} | {r['kind']} | \"{r['quote'][:300]}\"  [chat {r['chat']}]")
if __name__ == "__main__": main()
