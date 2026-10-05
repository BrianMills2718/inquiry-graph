"""Combined topic map of Brian's positions and questions: one point per attributed event.

Usage (needs the inquiry-maps env: sentence-transformers, umap, hdbscan, datamapplot):
  position_topics.py RECORDS.json OUT_DIR [--min-cluster 12]
Embeds 'idea + Brian's quote' locally, clusters with HDBSCAN, writes OUT_DIR/index.html (interactive, hover shows chat title,
date, kind and the exact quote) and OUT_DIR/topics.json (every cluster with its members' ids, so membership reconciles to records.json).
Quote-bearing: keep OUT_DIR under private/. Topic names default to keywords; name_topics.py can replace them.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import datamapplot
import hdbscan
import numpy as np
import umap
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("records", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--min-cluster", type=int, default=12)
    ap.add_argument("--names", type=Path, help="JSON {topic_id: name} from name_topics.py; replaces keyword names")
    a = ap.parse_args()
    recs = json.loads(a.records.read_text(encoding="utf-8"))["records"]
    a.out.mkdir(parents=True, exist_ok=True)
    docs = [f'{r["target"]} {r["quote"]}' for r in recs]
    emb = SentenceTransformer("all-MiniLM-L6-v2").encode(docs, batch_size=64, show_progress_bar=False, normalize_embeddings=True)
    xy = umap.UMAP(n_neighbors=15, min_dist=0.05, metric="cosine", random_state=7, low_memory=True).fit_transform(emb)
    lab = hdbscan.HDBSCAN(min_cluster_size=a.min_cluster, metric="euclidean").fit_predict(umap.UMAP(n_components=5, n_neighbors=15, metric="cosine", random_state=7, low_memory=True).fit_transform(emb))
    stop = list(ENGLISH_STOP_WORDS | {"brian", "idea", "assistant", "think", "like", "just", "want", "need"})
    names, topics = {-1: "Other"}, []
    for c in sorted(set(lab) - {-1}):
        idx = [i for i in range(len(recs)) if lab[i] == c]
        tf = TfidfVectorizer(stop_words=stop, ngram_range=(1, 2), max_features=2000).fit([docs[i] for i in range(len(recs))])
        v = np.asarray(tf.transform([" ".join(docs[i] for i in idx)]).todense()).ravel()
        kw = [tf.get_feature_names_out()[j] for j in v.argsort()[::-1][:3]]
        names[c] = ", ".join(kw)
        if a.names:
            names[c] = json.loads(a.names.read_text()).get(str(int(c)), names[c])
        dates = sorted(r["date"] for r in (recs[i] for i in idx) if r["date"])
        topics.append({"topic": int(c), "name": names[c], "size": len(idx), "first": dates[0] if dates else "", "last": dates[-1] if dates else "",
                       "chats": len({recs[i]["chat"] for i in idx}), "members": [recs[i]["id"] for i in idx]})
    other = [recs[i]["id"] for i in range(len(recs)) if lab[i] == -1]
    (a.out / "topics.json").write_text(json.dumps({"records": len(recs), "topics": topics, "unclustered": other,
                                                   "reconciles": sum(t["size"] for t in topics) + len(other) == len(recs)}, indent=1), encoding="utf-8")
    hover = [f'<b>{r["title"][:120]}</b> · {r["date"]} · {r["kind"]}<br><i>“{r["quote"][:240]}”</i>' for r in recs]
    plot = datamapplot.create_interactive_plot(xy, np.array([names[x] for x in lab]), hover_text=hover, title="Positions (private)",
                                               sub_title=f"Preview: {len(recs)} events, {len({r['chat'] for r in recs})} chats so far. Hover for quotes.",
                                               enable_search=True, darkmode=False, font_family="Roboto")
    plot.save(str(a.out / "index.html"))
    print(json.dumps({"records": len(recs), "topics": len(topics), "unclustered": len(other), "reconciles": sum(t["size"] for t in topics) + len(other) == len(recs)}))


if __name__ == "__main__":
    main()
