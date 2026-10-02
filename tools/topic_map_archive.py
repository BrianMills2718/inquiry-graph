"""Chat-level topic map with BERTopic (no generative LLM) written as WizMap data.

One point per chat: its title plus the opening of the user's messages. Clusters come from
HDBSCAN over sentence embeddings; topic names are BERTopic's keyword labels (filler removed).
Every chat keeps its id, title and date range. topics.json lists each topic with size, keywords,
date range and example titles so the result can be read without opening the map.
"""
import argparse
import json
from pathlib import Path

import numpy as np
import umap
import wizmap
from bertopic import BERTopic
from hdbscan import HDBSCAN
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, CountVectorizer

from wizmap_archive import FILLER

DOC_CHARS = 2000
USER_MSGS = 8


def chats(conv_dir: Path):
    out = []
    for f in sorted(conv_dir.glob("*.conv.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        user = {p["id"] for p in c["participants"] if p["role"] == "user"}
        msgs = [m for m in c["messages"] if m["actor_id"] in user]
        stamps = sorted(m["timestamp"][:10] for m in msgs if m.get("timestamp"))
        body = " ".join(m["text"].strip() for m in msgs[:USER_MSGS])
        if len(body) < 20:
            continue
        out.append({"chat": c["id"], "title": c["title"], "first": stamps[0] if stamps else "", "last": stamps[-1] if stamps else "",
                    "user_msgs": len(msgs), "doc": f"{c['title']}. {body}"[:DOC_CHARS]})
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conv_dir", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--min-cluster", type=int, default=8)
    a = ap.parse_args()
    cs = chats(a.conv_dir)
    docs = [c["doc"] for c in cs]
    emb = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu").encode(
        docs, batch_size=64, show_progress_bar=True, normalize_embeddings=True)
    stop = sorted(ENGLISH_STOP_WORDS | FILLER)
    um5 = umap.UMAP(n_components=5, metric="cosine", random_state=7, n_neighbors=15, min_dist=0.0)
    hdb = HDBSCAN(min_cluster_size=a.min_cluster, min_samples=3, metric="euclidean", prediction_data=True)
    tm = BERTopic(embedding_model=None, umap_model=um5, hdbscan_model=hdb, calculate_probabilities=False,
                  vectorizer_model=CountVectorizer(stop_words=stop, ngram_range=(1, 2), min_df=2), top_n_words=6)
    topics, _ = tm.fit_transform(docs, embeddings=emb)
    xy = umap.UMAP(n_components=2, metric="cosine", random_state=7).fit_transform(emb)
    info = tm.get_topic_info().set_index("Topic")
    members = {}
    for c, t in zip(cs, topics):
        members.setdefault(t, []).append(c)
    listing = []
    for t, ms in sorted(members.items(), key=lambda kv: -len(kv[1])):
        words = [w for w, _ in (tm.get_topic(t) or [])][:6]
        dates = sorted(m["first"] for m in ms if m["first"])
        listing.append({"topic": int(t), "name": "unclustered" if t == -1 else " / ".join(words[:4]), "chats": len(ms),
                        "first": dates[0] if dates else "", "last": dates[-1] if dates else "",
                        "keywords": words, "examples": [m["title"] for m in ms[:5]]})
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "topics.json").write_text(json.dumps(listing, indent=1), encoding="utf-8")
    names = {r["topic"]: r["name"] for r in listing}
    labels = [int(t) for t in topics]
    group_names = [names.get(i, "unclustered") for i in range(-1, max(labels) + 1)]
    xs, ys = xy[:, 0].tolist(), xy[:, 1].tolist()
    shown = [f"[{names[t]}] {c['title'][:80]} · {c['first']} · {c['user_msgs']} msgs" for c, t in zip(cs, labels)]
    times = [c["first"] or "2026-01-01" for c in cs]
    data = wizmap.generate_data_list(xs, ys, shown, times=times, labels=[l + 1 for l in labels])
    grid = wizmap.generate_grid_dict(xs, ys, docs, "Chats by topic (BERTopic)", times=times, time_format="%Y-%m-%d",
                                     labels=[l + 1 for l in labels], group_names=group_names, stop_words=stop)
    wizmap.save_json_files(data, grid, str(a.out_dir))
    (a.out_dir / "chats.json").write_text(json.dumps([{k: c[k] for k in ("chat", "title", "first", "last", "user_msgs")} | {"topic": int(t)}
                                                       for c, t in zip(cs, labels)]), encoding="utf-8")
    print(json.dumps({"chats": len(cs), "topics": len([t for t in members if t != -1]), "unclustered": len(members.get(-1, []))}))


if __name__ == "__main__":
    main()
