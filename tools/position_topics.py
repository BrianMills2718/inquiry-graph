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
    ap.add_argument("--layers", default="150,60,25", help="HDBSCAN min cluster sizes, coarse to fine")
    ap.add_argument("--names", type=Path, help="JSON {topic_id: name} from name_topics.py; replaces keyword names")
    a = ap.parse_args()
    recs = json.loads(a.records.read_text(encoding="utf-8"))["records"]
    a.out.mkdir(parents=True, exist_ok=True)
    docs = [f'{r["target"]} {r["quote"]}' for r in recs]
    emb = SentenceTransformer("all-MiniLM-L6-v2").encode(docs, batch_size=64, show_progress_bar=False, normalize_embeddings=True)
    xy = umap.UMAP(n_neighbors=30, min_dist=0.15, metric="cosine", random_state=7, low_memory=True).fit_transform(emb)
    lo, hi = np.percentile(xy, 0.5, axis=0), np.percentile(xy, 99.5, axis=0)   # a few far outliers must not stretch the view
    keep = np.all((xy >= lo - 0.1 * (hi - lo)) & (xy <= hi + 0.1 * (hi - lo)), axis=1)
    red5 = umap.UMAP(n_components=5, n_neighbors=30, metric="cosine", random_state=7, low_memory=True).fit_transform(emb)
    sizes = [int(x) for x in a.layers.split(",")]
    stop = list(ENGLISH_STOP_WORDS | {"brian", "idea", "assistant", "think", "like", "just", "want", "need"})
    tf = TfidfVectorizer(stop_words=stop, ngram_range=(1, 2), max_features=4000).fit(docs)
    fn = tf.get_feature_names_out()
    given = json.loads(a.names.read_text()) if a.names else {}
    layers, topics = [], []
    for ms in sizes:
        lab = hdbscan.HDBSCAN(min_cluster_size=ms, min_samples=5).fit_predict(red5)
        arr = np.array(["Unlabelled"] * len(recs), dtype=object)
        for c in sorted(set(lab) - {-1}):
            idx = [i for i in range(len(recs)) if lab[i] == c]
            v = np.asarray(tf.transform([" ".join(docs[i] for i in idx)]).todense()).ravel()
            name = given.get(f"{ms}:{c}") or ", ".join(fn[j] for j in v.argsort()[::-1][:3])
            arr[idx] = name
            dates = sorted(recs[i]["date"] for i in idx if recs[i]["date"])
            topics.append({"topic": f"{ms}:{c}", "layer": ms, "name": name, "size": len(idx), "first": dates[0] if dates else "", "last": dates[-1] if dates else "",
                           "chats": len({recs[i]["chat"] for i in idx}), "members": [recs[i]["id"] for i in idx]})
        layers.append(arr)
        print(f"layer {ms}: {len(set(lab) - {-1})} topics, {int((lab == -1).sum())} unclustered", flush=True)
    (a.out / "topics.json").write_text(json.dumps({"records": len(recs), "layers": sizes, "topics": topics}, indent=1), encoding="utf-8")
    hover = [f'<b>{r["title"][:120]}</b> · {r["date"]} · {r["kind"]}<br><i>“{r["quote"][:240]}”</i>' for r in recs]
    sel = np.where(keep)[0]
    plot = datamapplot.create_interactive_plot(xy[sel], *[l[sel] for l in layers], hover_text=[hover[i] for i in sel], title="Positions (private)",
                                               sub_title=f"{len(recs)} quoted events from {len({r['chat'] for r in recs})} chats. Zoom for detail; hover for the quote.",
                                               enable_search=True, darkmode=False, font_family="Roboto", noise_label="Unlabelled")
    plot.save(str(a.out / "index.html"))
    n_lab = [int((l != "Unlabelled").sum()) for l in layers]
    print(json.dumps({"records": len(recs), "plotted": int(keep.sum()), "layers": sizes, "events_labelled_per_layer": n_lab, "topics": len(topics)}))


if __name__ == "__main__":
    main()
