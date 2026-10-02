"""Atlas-style network map of chats (no generative LLM): one dot per chat, linked to its nearest chats
by text similarity, laid out with ForceAtlas2, coloured by community, with a legend of community shares.

Chats in the exporter's agent-send log are excluded (their user turns are agent prompts). Text is the
title plus the opening of the human and assistant turns, so the map reflects what the conversations were about.
"""
import os

# Keep the build light on a shared laptop: few threads, no tokenizer fork storms. Override by setting these first.
for _v in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS", "NUMBA_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ.setdefault(_v, "4")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")

import argparse
import hashlib
import collections
import json
import math
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from fa2_modified import ForceAtlas2
from matplotlib.collections import LineCollection
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer

from label_words import FILLER

# ChatGPT citation markers and similar tokens that carry no topic.
NOISE = {"brian", "steno", "filecite", "turn0file0", "turn0file1", "turn0file2", "turn1file0", "cite", "turn0search0", "l2-l2", "ac5", "rc2"}
# Words that read as personal when shown alone on a public label, even if the chats are about research.
# Keywords are skipped for the label only; the chats themselves were already filtered.
LABEL_AVOID = {"family", "income", "wife", "husband", "kids", "child", "children", "baby", "mom", "dad", "mother", "father",
               "health", "doctor", "medical", "pain", "mouth", "salary", "debt", "loan", "tax", "taxes", "rent", "mortgage",
               "divorce", "dating", "sex", "drug", "drugs", "therapy", "anxiety", "depression", "thomas"}
CODE = re.compile(r"```.*?```", re.S)
URL = re.compile(r"https?://\S+")
PALETTE = ["#e6194b", "#3cb44b", "#ffe119", "#4363d8", "#f58231", "#911eb4", "#46f0f0", "#f032e6", "#bcf60c", "#fabebe",
           "#008080", "#e6beff", "#9a6324", "#fffac8", "#800000", "#aaffc3", "#808000", "#ffd8b1", "#00bfff", "#ff69b4",
           "#7fffd4", "#ffa500", "#adff2f", "#dda0dd", "#87ceeb"]


class _Identity:
    """BERTopic's UMAP slot: embeddings passed in are already reduced, so pass them through."""
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X
    def fit_transform(self, X, y=None):
        return X


def cached(cache_dir, name, key, fn):
    """Load <cache_dir>/<name>-<key>.npy if present, else compute with fn() and save. Heavy steps run once per input set."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    f = cache_dir / f"{name}-{key}.npy"
    if f.exists():
        return np.load(f)
    val = np.asarray(fn())
    np.save(f, val)
    return val


def agent_threads(path):
    ids = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            t = json.loads(line).get("thread_id")
        except json.JSONDecodeError:
            continue
        if t:
            ids.add(t)
    return ids


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conv_dir", type=Path)
    ap.add_argument("agent_log", type=Path)
    ap.add_argument("out_png", type=Path)
    ap.add_argument("--since", default="")
    ap.add_argument("--until", default="9999-12-31")
    ap.add_argument("--k", type=int, default=7)
    ap.add_argument("--legend-rows", type=int, default=24)
    ap.add_argument("--html", type=Path, help="also write an interactive DataMapPlot page (hover, search, time filter)")
    ap.add_argument("--include", type=Path, help="JSON list of {id, include}; keep only chats with include=true")
    ap.add_argument("--public", action="store_true", help="write the interactive page with no titles, dates or search; hover shows only the community")
    ap.add_argument("--layers", default="", help="comma-separated HDBSCAN min cluster sizes, coarse to fine (e.g. 45,18,7): "
                    "BERTopic names each layer and DataMapPlot shows them as a zoomable topic tree")
    ap.add_argument("--names", type=Path, help="JSON {layer_size: {cluster_id: name}} from label_names.py; replaces keyword labels")
    ap.add_argument("--label-check", type=Path, help="JSON from label_check.py; labels with keep=false are shown as Unlabelled")
    ap.add_argument("--edges", action="store_true", help="bundle edges in the interactive page")
    a = ap.parse_args()
    agent = agent_threads(a.agent_log)
    allowed = None
    if a.include:
        rows = json.loads(a.include.read_text(encoding="utf-8"))
        allowed = {r["id"] for r in rows if r["include"]}
    chats = []
    for f in sorted(a.conv_dir.glob("*.conv.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        if c["id"].split(":", 1)[1] in agent or (allowed is not None and c["id"] not in allowed):
            continue
        user = {p["id"] for p in c["participants"] if p["role"] == "user"}
        stamps = sorted(m["timestamp"][:10] for m in c["messages"] if m["actor_id"] in user and m.get("timestamp"))
        if not stamps or not (a.since <= stamps[0] <= a.until):
            continue
        body = URL.sub(" ", CODE.sub(" ", " ".join(m["text"] for m in c["messages"][:12])))
        if len(body) > 60:
            chats.append({"id": c["id"], "title": c["title"], "first": stamps[0], "n": len(c["messages"]), "doc": f"{c['title']}. {body}"[:3000]})
    n = len(chats)
    cache_dir = a.out_png.parent / "cache"
    key = hashlib.sha256("\n".join(c["id"] + c["doc"][:200] for c in chats).encode()).hexdigest()[:16]
    emb = cached(cache_dir, "emb", key, lambda: SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu").encode(
        [c["doc"] for c in chats], batch_size=16, normalize_embeddings=True, show_progress_bar=False))
    sim = emb @ emb.T
    np.fill_diagonal(sim, -1)
    G = nx.Graph()
    G.add_nodes_from(range(n))
    for i in range(n):
        for j in np.argsort(-sim[i])[: a.k]:
            if sim[i, j] > 0.25:
                G.add_edge(i, int(j), weight=float(sim[i, j]))
    comms = sorted(nx.community.louvain_communities(G, weight="weight", seed=7, resolution=1.0), key=len, reverse=True)
    comm_of = {i: ci for ci, c in enumerate(comms) for i in c}
    def layout():
        pos = ForceAtlas2(outboundAttractionDistribution=True, scalingRatio=4.0, gravity=0.6, strongGravityMode=False,
                          barnesHutOptimize=True, verbose=False).forceatlas2_networkx_layout(G, pos=None, iterations=600)
        return np.array([pos[i] for i in range(n)])
    xy = cached(cache_dir, f"layout-k{a.k}", key, layout)
    vec = TfidfVectorizer(stop_words=sorted(ENGLISH_STOP_WORDS | FILLER | NOISE), ngram_range=(1, 2), min_df=2, max_df=0.3, token_pattern=r"[A-Za-z][A-Za-z0-9_\-]{2,}")
    X = vec.fit_transform([c["doc"] for c in chats])
    vocab = np.array(vec.get_feature_names_out())
    desc = {}
    for ci, c in enumerate(comms):
        if len(c) < 3:
            continue
        s = np.asarray(X[list(c)].mean(axis=0)).ravel() - np.asarray(X.mean(axis=0)).ravel()
        desc[ci] = ", ".join(vocab[np.argsort(-s)[:4]])
    fig = plt.figure(figsize=(20, 13.3), facecolor="black")
    ax = fig.add_axes([0.40, 0.02, 0.59, 0.96], facecolor="black")
    segs = [(xy[u], xy[v]) for u, v in G.edges if comm_of[u] == comm_of[v]]
    cols = [PALETTE[comm_of[u] % len(PALETTE)] for u, v in G.edges if comm_of[u] == comm_of[v]]
    ax.add_collection(LineCollection(segs, colors=cols, linewidths=0.25, alpha=0.25))
    cross = [(xy[u], xy[v]) for u, v in G.edges if comm_of[u] != comm_of[v]]
    ax.add_collection(LineCollection(cross, colors="#888888", linewidths=0.15, alpha=0.12))
    deg = np.array([G.degree(i) for i in range(n)])
    ax.scatter(xy[:, 0], xy[:, 1], s=14 + 6 * np.sqrt(deg), c=[PALETTE[comm_of[i] % len(PALETTE)] for i in range(n)], linewidths=0, alpha=0.95)
    for ci, c in enumerate(comms[:12]):
        if ci in desc:
            m = xy[list(c)].mean(axis=0)
            ax.text(m[0], m[1], desc[ci].split(", ")[0].upper(), color="white", fontsize=11, ha="center", va="center", weight="bold",
                    path_effects=[__import__("matplotlib.patheffects", fromlist=["x"]).withStroke(linewidth=3, foreground="black")])
    lo, hi = np.percentile(xy, 1, axis=0), np.percentile(xy, 99, axis=0)
    pad = 0.08 * (hi - lo)
    ax.set_xlim(lo[0] - pad[0], hi[0] + pad[0])
    ax.set_ylim(lo[1] - pad[1], hi[1] + pad[1])
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis("off")
    lx = fig.add_axes([0.02, 0.02, 0.36, 0.96], facecolor="black")
    lx.axis("off")
    lx.text(0.0, 0.97, f"Your ChatGPT chats: {n} chats, {len(comms)} communities", color="white", fontsize=16, weight="bold", va="top")
    lx.text(0.0, 0.935, "Each dot is a chat; lines join similar chats. Agent-opened chats excluded.", color="#bbbbbb", fontsize=11, va="top")
    lx.text(0.0, 0.88, "% of chats", color="white", fontsize=12, va="top")
    lx.text(0.14, 0.88, "What the community is about (top words)", color="white", fontsize=12, va="top")
    y = 0.85
    for ci, c in enumerate(comms[: a.legend_rows]):
        if ci not in desc:
            continue
        lx.add_patch(plt.Rectangle((0.0, y - 0.012), 0.025, 0.018, color=PALETTE[ci % len(PALETTE)]))
        lx.text(0.04, y, f"{100 * len(c) / n:4.1f}", color="white", fontsize=12, va="center")
        lx.text(0.14, y, desc[ci], color="white", fontsize=12, va="center")
        y -= 0.033
    if a.html:
        import datamapplot
        names = np.array([desc.get(comm_of[i], "Unlabelled") if comm_of[i] in desc else "Unlabelled" for i in range(n)], dtype=object)
        names = np.array([w.title().replace(", ", " / ") if w != "Unlabelled" else w for w in names], dtype=object)
        hover = list(names) if a.public else [f"{c['title'][:90]} ({c['first']}, {c['n']} messages)" for c in chats]
        dates = np.array([c["first"] for c in chats], dtype="datetime64[D]")
        layer_arrays = []
        if a.layers:
            import umap as umap_mod
            from bertopic import BERTopic
            from hdbscan import HDBSCAN
            from sklearn.feature_extraction.text import CountVectorizer
            um5 = cached(cache_dir, "umap5", key, lambda: umap_mod.UMAP(n_components=5, metric="cosine", random_state=7, n_neighbors=15, min_dist=0.0, low_memory=True).fit_transform(emb))
            stop = sorted(ENGLISH_STOP_WORDS | FILLER | NOISE)
            for k in [int(v) for v in a.layers.split(",")]:
                tm = BERTopic(embedding_model=None,
                              hdbscan_model=HDBSCAN(min_cluster_size=k, min_samples=2), calculate_probabilities=False,
                              vectorizer_model=CountVectorizer(stop_words=stop, ngram_range=(1, 2), min_df=2), top_n_words=4,
                              umap_model=_Identity())
                topics, _ = tm.fit_transform([c["doc"] for c in chats], embeddings=um5)
                label = {t: " / ".join([w for w, _ in tm.get_topic(t) if not (set(w.split()) & LABEL_AVOID)][:3]).title() for t in set(topics) if t != -1}
                clusters = a.out_png.with_name(f"layer_{k}_clusters.json")
                clusters.write_text(json.dumps({str(t): {"keywords": label[t], "titles": [chats[i]["title"] for i, tt in enumerate(topics) if tt == t]}
                                                for t in label}, indent=1), encoding="utf-8")
                if a.names:  # plain-language names replace keyword tags; a cluster with no name shows as Unlabelled
                    named = json.loads(a.names.read_text(encoding="utf-8")).get(str(k), {})
                    label = {t: named[str(t)] for t in label if str(t) in named}
                verdict = json.loads(a.label_check.read_text(encoding="utf-8")) if a.label_check else {}
                layer_arrays.append(np.array([label.get(t, "Unlabelled") if verdict.get(label.get(t), {"keep": True})["keep"] else "Unlabelled"
                                              for t in topics], dtype=object))
                layer_titles = a.out_png.with_name(f"layer_{k}_members.json")
                layer_titles.write_text(json.dumps({lab: [chats[i]["title"] for i, t in enumerate(topics) if label.get(t) == lab]
                                                    for lab in set(label.values())}, indent=1), encoding="utf-8")
                print(f"layer min_cluster_size={k}: {len(label)} groups, {sum(1 for t in topics if t == -1)} unlabelled")
        plot = datamapplot.create_interactive_plot(
            xy, *(layer_arrays or [names]), hover_text=hover, title="Brian's ChatGPT interests" if a.public else "Your ChatGPT chats",
            sub_title=(f"{n} chats about work and ideas. Personal chats are left out." if a.public else
                       f"{n} chats. Agent-opened chats excluded. Hover a dot for the chat; search the box; drag the time bars."),
            darkmode=True, cvd_safer=True, enable_topic_tree=bool(a.layers), enable_search=not a.public, histogram_data=None if a.public else dates, histogram_n_bins=24,
            point_radius_min_pixels=2, point_radius_max_pixels=14, edge_bundle=a.edges, inline_data=True,
            noise_label="Unlabelled", initial_zoom_fraction=0.9)
        a.html.parent.mkdir(parents=True, exist_ok=True)
        plot.save(str(a.html))
    a.out_png.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(a.out_png, dpi=110, facecolor="black")
    (a.out_png.with_suffix(".json")).write_text(json.dumps({"chats": n, "edges": G.number_of_edges(), "communities": len(comms),
        "sizes": [len(c) for c in comms[:30]], "desc": desc}, indent=1))
    print(json.dumps({"chats": n, "edges": G.number_of_edges(), "communities": len(comms), "top_sizes": [len(c) for c in comms[:10]]}))


if __name__ == "__main__":
    main()
