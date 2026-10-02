"""Build a WizMap (poloclub) embedding map of the user's messages across normalized chats.

No generative LLM: a small sentence-embedding model, UMAP, and WizMap's own keyword
topics. Every point is one user message and keeps its chat id, title, message id and date,
so a point can be traced to its source. Output goes under the given private directory.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np
import umap
import wizmap
from label_words import FILLER
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from sentence_transformers import SentenceTransformer

MIN_CHARS = 20
EMBED_CHARS = 1500
SHOW_CHARS = 300
# Conversational filler that otherwise dominates WizMap's keyword topic labels ("ok-proceed-plan-lets").


def collect(conv_dir: Path):
    pts, excluded = [], Counter()
    for f in sorted(conv_dir.glob("*.conv.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        user = {p["id"] for p in c["participants"] if p["role"] == "user"}
        for m in c["messages"]:
            if m["actor_id"] not in user:
                continue
            text = m["text"].strip()
            if len(text) < MIN_CHARS:
                excluded["shorter_than_%d_chars" % MIN_CHARS] += 1
                continue
            date = (m.get("timestamp") or "")[:10]
            pts.append({"chat": c["id"], "title": c["title"], "message": m["id"],
                        "original_id": m.get("original_id"), "date": date, "text": text})
    return pts, excluded


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conv_dir", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--model", default="sentence-transformers/all-MiniLM-L6-v2")
    a = ap.parse_args()
    pts, excluded = collect(a.conv_dir)
    if not pts:
        raise SystemExit("no user messages found")
    emb = SentenceTransformer(a.model, device="cpu").encode(
        [p["text"][:EMBED_CHARS] for p in pts], batch_size=64, show_progress_bar=True, normalize_embeddings=True)
    xy = umap.UMAP(n_components=2, metric="cosine", random_state=7).fit_transform(emb)
    xs, ys = xy[:, 0].tolist(), xy[:, 1].tolist()
    shown = [f"[{p['title'][:60]} · {p['date'] or 'no date'}] {p['text'][:SHOW_CHARS]}" for p in pts]
    times = [p["date"] or "2026-01-01" for p in pts]
    data = wizmap.generate_data_list(xs, ys, shown, times=times)
    grid = wizmap.generate_grid_dict(xs, ys, [p["text"][:EMBED_CHARS] for p in pts], "User messages across ChatGPT chats",
                                     times=times, time_format="%Y-%m-%d",
                                     stop_words=sorted(ENGLISH_STOP_WORDS | FILLER))
    a.out_dir.mkdir(parents=True, exist_ok=True)
    wizmap.save_json_files(data, grid, str(a.out_dir))
    (a.out_dir / "points.json").write_text(json.dumps(
        [{k: p[k] for k in ("chat", "title", "message", "original_id", "date")} for p in pts]), encoding="utf-8")
    (a.out_dir / "build.json").write_text(json.dumps({
        "points": len(pts), "chats": len({p["chat"] for p in pts}), "excluded": dict(excluded), "model": a.model,
        "account_note": "Chats carry no account label yet; see the account-provenance backfill."}, indent=1))
    print(json.dumps({"points": len(pts), "chats": len({p["chat"] for p in pts}), "excluded": dict(excluded)}))


if __name__ == "__main__":
    main()
