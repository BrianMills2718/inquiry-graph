#!/usr/bin/env python3
"""Look up Brian's own words on a topic from his chat history (ChatGPT, Claude, Gemini). One-shot, local, no model call, no network.
Returns the best-matching positions/questions he stated, each with the exact quote, date, chat title and chat id. Pasted/quoted text is excluded.
Usage: ~/.venvs/inquiry-maps/bin/python brian_positions.py "<topic or question>" [--top 15] [--json] [--rebuild] [--keyword-only] [--sessions [DIR ...]]
--sessions also searches what Brian typed in Claude Code and Codex sessions imported with `inquiry-graph import-session` (default private/coding-sessions);
prompts from headless launches (claude -p, codex exec, subagents) are labelled automated at import and never count as his words.
Retrieval is hybrid: BM25 keyword rank fused (reciprocal rank) with MiniLM embedding similarity, so synonyms and paraphrases match. Embeddings cached in private/positions_emb.npy.
Private data: reads ~/code/inquiry-graph/private (gitignored). Quote-bearing output stays in the session; do not publish it."""
import argparse, datetime as dt, json, re, sys
import numpy as np
from pathlib import Path
from rank_bm25 import BM25Okapi
ROOT = Path(__file__).resolve().parents[1]; R = ROOT / "private"; INDEX = R / "positions_index.json"; EMB = R / "positions_emb.npy"
sys.path.insert(0, str(ROOT / "tools")); from ask_positions import records, tok
DIRS = ["extract_test_20261003/out", "extract_full_20261003/out", "extract_full_20261003/kept/out", "extract_full_20261003/new108/out", "extract_full_20261003/single/out",
        "extract_full_20261003/claude_export/out", "extract_full_20261003/or_run/out", "extract_full_20261003/lowconf/out", "extract_full_20261003/gemini_takeout/out"]
def load(rebuild):
    if INDEX.exists() and not rebuild: return json.loads(INDEX.read_text())
    lab = json.loads((R / "authorship_full.json").read_text())
    skip = frozenset((r["message_id"], r["quote"]) for r in json.loads((R / "records_full.json").read_text())["records"] if lab.get(r["id"], {}).get("label") == "pasted_or_quoted")
    recs = records([R / d for d in DIRS if (R / d).is_dir()], skip); INDEX.write_text(json.dumps(recs)); return recs
SESS_EMB = R / "sessions_emb.npy"; SESS_IDS = R / "sessions_emb_ids.json"
HISTORY = [Path.home() / ".claude" / "history.jsonl", Path.home() / ".codex" / "history.jsonl"]   # every prompt Brian typed, kept after session files are gone


def _key(chat, text): return chat, " ".join(text.split())[:200]


def history_records(files, seen=()):
    """Brian's typed prompts from the Claude Code and Codex prompt histories, minus any already read from imported sessions.
    These files keep only interactive prompts (never headless launches), and outlive the session files they came from."""
    out, seen = [], set(seen)
    for f in map(Path, files):
        if not f.exists():
            continue
        codex = f.parent.name == ".codex"
        for line in f.open(encoding="utf-8"):
            try:
                d = json.loads(line)
            except ValueError:
                continue
            t = str(d.get("text" if codex else "display") or "").strip()
            sid = d.get("session_id" if codex else "sessionId")
            ts = d.get("ts" if codex else "timestamp")
            if not sid or not isinstance(ts, (int, float)) or len(t) < 25:
                continue
            chat = f"{'codex' if codex else 'claude-code'}:{sid}"
            if _key(chat, t) in seen:
                continue
            seen.add(_key(chat, t))
            when = dt.datetime.fromtimestamp(ts if codex else ts / 1000, dt.timezone.utc)
            where = "codex" if codex else Path(d.get("project") or "code").name
            out.append({"target": "", "quote": t[:600], "title": f"{where} session {sid[:8]}", "date": when.date().isoformat(),
                        "kind": "session prompt", "chat": chat, "message_id": f"{chat}:h{int(ts)}"})
    return out


def session_records(dirs, history=()):
    """Brian's own typed messages from imported session conversations, plus (with history files) every typed prompt
    the sessions no longer on disk held; one-word replies ("continue", "yes") carry no position."""
    out, seen = [], set()   # one session can be imported into several folders (a week and a month)
    for f in sorted(p for d in dirs for p in Path(d).rglob("*.conversation.json")):
        c = json.loads(f.read_text())
        for m in c["messages"]:
            t = m["text"].strip()
            if m["actor_id"] == "participant:brian" and len(t) >= 25 and _key(c["id"], t) not in seen:
                seen.add(_key(c["id"], t))
                out.append({"target": "", "quote": t[:600], "title": c["title"], "date": (m.get("timestamp") or "")[:10],
                            "kind": "session prompt", "chat": c["id"], "message_id": m["id"]})
    return out + history_records(history, seen)
def doc(r): return (r["target"] or r["quote"])[:300]
def embeddings(recs, rebuild, sessions=()):
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    if sessions:   # own cache, keyed by message ids, so adding sessions never re-encodes the chat records
        _, e = embeddings(recs, rebuild); ids = [r["message_id"] for r in sessions]
        if SESS_EMB.exists() and SESS_IDS.exists() and not rebuild and json.loads(SESS_IDS.read_text()) == ids: s = np.load(SESS_EMB)
        else:
            s = m.encode([doc(r) for r in sessions], batch_size=128, normalize_embeddings=True, show_progress_bar=False).astype("float16")
            np.save(SESS_EMB, s); SESS_IDS.write_text(json.dumps(ids))
        return m, np.concatenate([e, s])
    if EMB.exists() and not rebuild:
        e = np.load(EMB)
        if len(e) == len(recs): return m, e
    e = m.encode([doc(r) for r in recs], batch_size=128, normalize_embeddings=True, show_progress_bar=False).astype("float16"); np.save(EMB, e); return m, e
def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("query"); ap.add_argument("--top", type=int, default=15); ap.add_argument("--json", action="store_true"); ap.add_argument("--rebuild", action="store_true"); ap.add_argument("--keyword-only", action="store_true"); ap.add_argument("--sessions", nargs="*", metavar="DIR")
    a = ap.parse_args(); recs = load(a.rebuild); n_chat = len(recs)
    sess = session_records(a.sessions or [R / "coding-sessions"], HISTORY) if a.sessions is not None else []; recs = recs + sess
    sc = BM25Okapi([tok(r["target"] + " " + r["quote"] + " " + r["title"]) for r in recs]).get_scores(tok(a.query))
    order = [i for i in np.argsort(-sc)[:200] if sc[i] > 0]; fused = {i: 1 / (60 + k) for k, i in enumerate(order)}
    if not a.keyword_only:
        try: import sentence_transformers  # noqa: F401
        except ImportError: a.keyword_only = True; print("note: sentence_transformers missing in this venv, keyword-only; use ~/.venvs/inquiry-maps/bin/python for meaning match", file=sys.stderr)
    if not a.keyword_only:
        m, e = embeddings(recs[:n_chat], a.rebuild, sess); q = m.encode([a.query], normalize_embeddings=True)[0].astype("float16")
        for k, i in enumerate(np.argsort(-(e @ q))[:200]): fused[int(i)] = fused.get(int(i), 0) + 1 / (60 + k)
    seen, pick = set(), []
    for i in sorted(fused, key=lambda i: -fused[i]):
        k = (recs[i]["message_id"], recs[i]["quote"])
        if k in seen: continue
        seen.add(k); pick.append(recs[i])
        if len(pick) == a.top: break
    pick.sort(key=lambda r: r["date"])
    if a.json: print(json.dumps(pick, indent=1)); return
    print(f"{len(pick)} of {len(recs)} own-words records matched '{a.query}' (oldest first). Hybrid keyword + meaning match.")
    for r in pick: print(f"- {r['date']} | {r['title'][:60]} | {r['kind']} | \"{r['quote'][:300]}\"  [chat {r['chat']}]")
if __name__ == "__main__": main()
