"""Combined topic map of Brian's positions and questions: one point per attributed event.

Usage (needs the inquiry-maps env: sentence-transformers, umap, evoc or hdbscan, datamapplot, pandas):
  position_topics.py RECORDS.json OUT_DIR [--clusterer evoc|hdbscan] [--layers 150,60,25] [--sessions [DIR ...]]
--clusterer evoc (default) finds nested topic levels (coarse topics split into finer ones, shown in the page's topic tree);
hdbscan runs one independent clustering per --layers size, as before.
The page: click a point for a side panel (full quote, topic path, the rest of that conversation); filter by source, kind of
statement or date range; search the quotes; switch the colouring between topic levels, sources and kinds.
--sessions adds what Brian typed in imported coding sessions (default private/coding-sessions), one point per prompt, kind "session prompt".
Embeds 'idea + Brian's quote' locally (cached in OUT_DIR/embedding_cache.npz), clusters, writes OUT_DIR/index.html (interactive, hover shows chat title,
date, kind and the exact quote) and OUT_DIR/topics.json (every cluster with its members' ids, so membership reconciles to records.json).
Also writes OUT_DIR/records.json (chat records plus session prompts). Quote-bearing: keep OUT_DIR under private/.
Topic names default to keywords; name_topics.py OUT_DIR/records.json OUT_DIR/topics.json NAMES.json writes model names for --names.
Points the clusterer leaves out are shown under the topic of their nearest clustered neighbours; topics.json keeps them apart (nearest_members).
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import hashlib
import sys

import datamapplot
import numpy as np
import pandas as pd
import umap
from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer

ROOT = Path(__file__).resolve().parents[1]


def session_records(dirs):
    from brian_positions import session_records as load   # same loader as the positions search, so both read one definition of "Brian's prompt"
    return load(dirs)


APP_BY_PREFIX = {"claude-code": "Claude Code", "codex": "Codex", "chatgpt": "ChatGPT", "gemini": "Gemini", "claude": "Claude chat"}
APPS = list(APP_BY_PREFIX.values())
CODING = {"Claude Code", "Codex"}
# Okabe-Ito colours (colour-blind safe; no red against green): coding sessions warm, chats cool
SOURCE_COLOURS = {"Coding session": "#E69F00", "Chat": "#0072B2", "Claude Code": "#E69F00", "Codex": "#D55E00",
                  "ChatGPT": "#0072B2", "Gemini": "#56B4E9", "Claude chat": "#CC79A7", "Other": "#999999"}


def source(r):
    """The app a record came from, read from its conversation id prefix (e.g. 'codex:...', 'chatgpt:...')."""
    return APP_BY_PREFIX.get(r["chat"].split(":", 1)[0], "Other")


def with_ids(sessions):
    """Session prompts carry a message id but no record id; topics.json lists members by record id."""
    return [{**r, "id": f"session:{r['message_id']}"} for r in sessions]


KIND_GROUPS = {"posits": "Claim", "questions": "Question", "question:open": "Question", "question:reopened": "Question",
               "question:answered": "Question settled", "question:resolved": "Question settled", "question:superseded": "Question settled",
               "endorses": "Agrees", "rejects": "Rejects or retracts", "retracts": "Rejects or retracts",
               "suspends": "Puts off", "question:deferred": "Puts off", "session prompt": "Coding-session prompt"}
# Okabe-Ito (colour-blind safe, no red against green)
KIND_COLOURS = {"Claim": "#0072B2", "Question": "#56B4E9", "Question settled": "#009E73", "Agrees": "#CC79A7",
                "Rejects or retracts": "#D55E00", "Puts off": "#F0E442", "Coding-session prompt": "#E69F00", "Other": "#999999"}
PAGE = Path(__file__).with_name("position_topics_page.js")
MIN_PROMPT_WORDS = 4   # shorter coding-session prompts ("ok", "yes do it") carry no topic


def embed(docs, cache):
    """Embeddings and 2-D layout, cached by the exact documents so a re-run that only changes the page skips the slow part."""
    key = hashlib.sha256("\x1f".join(docs).encode()).hexdigest()
    if cache.exists():
        z = np.load(cache, allow_pickle=False)
        if str(z["key"]) == key:
            return z["emb"], z["xy"]
    emb = SentenceTransformer("all-MiniLM-L6-v2").encode(docs, batch_size=64, show_progress_bar=False, normalize_embeddings=True)
    xy = umap.UMAP(n_neighbors=30, min_dist=0.15, metric="cosine", random_state=7, low_memory=True).fit_transform(emb)
    np.savez(cache, key=key, emb=emb, xy=xy)
    return emb, xy


def cluster_layers(emb, clusterer, sizes):
    """Label arrays, finest first. EVoC's layers nest (each fine topic sits inside one coarser topic); HDBSCAN's do not."""
    if clusterer == "evoc":
        import evoc
        model = evoc.EVoC(base_min_cluster_size=10, random_state=7)
        model.fit_predict(emb)
        return [np.asarray(l) for l in model.cluster_layers_], [f"L{i}" for i in range(len(model.cluster_layers_))]
    import hdbscan
    red5 = umap.UMAP(n_components=5, n_neighbors=30, metric="cosine", random_state=7, low_memory=True).fit_transform(emb)
    sizes = sorted(sizes)
    return [hdbscan.HDBSCAN(min_cluster_size=ms, min_samples=5).fit_predict(red5) for ms in sizes], [str(ms) for ms in sizes]


def cached_layers(emb, clusterer, layers, cache):
    """cluster_layers, cached by the exact embeddings, so a rebuild that only adds topic names keeps the same topic ids."""
    key = hashlib.sha256(emb.tobytes() + f"{clusterer}|{layers}".encode()).hexdigest()
    if cache.exists():
        z = np.load(cache, allow_pickle=False)
        if str(z["key"]) == key:
            return [z[f"lab{i}"] for i in range(len(z["ids"]))], [str(x) for x in z["ids"]]
    labs, ids = cluster_layers(emb, clusterer, [int(x) for x in layers.split(",")])
    np.savez(cache, key=key, ids=np.array(ids), **{f"lab{i}": l for i, l in enumerate(labs)})
    return labs, ids


def nearest_topic(emb, lab, k=10):
    """Give each point the clusterer left out (-1) the most common topic among its k nearest clustered points (cosine)."""
    from sklearn.neighbors import NearestNeighbors
    lab = np.asarray(lab); inside = np.where(lab != -1)[0]; out = np.where(lab == -1)[0]
    if not len(inside) or not len(out):
        return lab.copy()
    nn = NearestNeighbors(n_neighbors=min(k, len(inside)), metric="cosine").fit(emb[inside])
    votes = lab[inside][nn.kneighbors(emb[out], return_distance=False)]
    shown = lab.copy()
    shown[out] = [Counter(v).most_common(1)[0][0] for v in votes]
    return shown


def page_js(recs, names, paths, kinds, apps, layer_sizes):
    """Data for the side panel, plus the panel, filter-hint and tooltip code from position_topics_page.js."""
    data = {"names": names, "layerSizes": layer_sizes, "recs": [[r["title"][:160], r["date"], apps[i], kinds[i], r["quote"], r["chat"], paths[i]] for i, r in enumerate(recs)]}
    return "const IG = " + json.dumps(data, ensure_ascii=False).replace("</", "<\\/") + ";\n" + PAGE.read_text(encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("records", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--clusterer", choices=["evoc", "hdbscan"], default="evoc")
    ap.add_argument("--layers", default="150,60,25", help="HDBSCAN min cluster sizes (only with --clusterer hdbscan)")
    ap.add_argument("--names", type=Path, help="JSON {topic_id: name} from name_topics.py; replaces keyword names")
    ap.add_argument("--sessions", nargs="*", metavar="DIR", help="also cluster Brian's coding-session prompts (default private/coding-sessions)")
    a = ap.parse_args()
    recs = json.loads(a.records.read_text(encoding="utf-8"))["records"]
    if a.sessions is not None:
        prompts = with_ids(session_records(a.sessions or [ROOT / "private" / "coding-sessions"]))
        kept = [r for r in prompts if len(r["quote"].split()) >= MIN_PROMPT_WORDS]
        print(f"session prompts: {len(prompts)}, dropped {len(prompts) - len(kept)} under {MIN_PROMPT_WORDS} words", flush=True)
        recs = recs + kept
    a.out.mkdir(parents=True, exist_ok=True)
    docs = [f'{r["target"]} {r["quote"]}' for r in recs]
    emb, xy = embed(docs, a.out / "embedding_cache.npz")
    lo, hi = np.percentile(xy, 0.5, axis=0), np.percentile(xy, 99.5, axis=0)   # a few far outliers must not stretch the view
    keep = np.all((xy >= lo - 0.1 * (hi - lo)) & (xy <= hi + 0.1 * (hi - lo)), axis=1)
    labs, layer_ids = cached_layers(emb, a.clusterer, a.layers, a.out / "cluster_cache.npz")
    near = [nearest_topic(emb, lab) for lab in labs]   # display only; topics.json members stay the clusterer's own
    stop = list(ENGLISH_STOP_WORDS | {"brian", "idea", "assistant", "think", "like", "just", "want", "need"})
    tf = TfidfVectorizer(stop_words=stop, ngram_range=(1, 2), max_features=4000).fit(docs)
    fn = tf.get_feature_names_out()
    given = json.loads(a.names.read_text()) if a.names else {}
    layers, topics, names = [], [], ["Unlabelled"]
    name_idx = np.zeros((len(recs), len(labs)), dtype=int)   # per point, per layer: index into names (0 = unlabelled)
    for li, (lab, lid) in enumerate(zip(labs, layer_ids)):
        arr = np.array(["Unlabelled"] * len(recs), dtype=object)
        for c in sorted(set(lab) - {-1}):
            idx = [i for i in range(len(recs)) if lab[i] == c]
            shown = [i for i in range(len(recs)) if near[li][i] == c]
            v = np.asarray(tf.transform([" ".join(docs[i] for i in idx)]).todense()).ravel()
            name = given.get(f"{lid}:{c}") or ", ".join(fn[j] for j in v.argsort()[::-1][:3])
            arr[shown] = name
            names.append(name); name_idx[shown, li] = len(names) - 1
            name_idx[[i for i in shown if lab[i] == -1], li] *= -1   # negative: placed by nearest neighbours, not by the clusterer
            dates = sorted(recs[i]["date"] for i in idx if recs[i]["date"])
            topics.append({"topic": f"{lid}:{c}", "layer": lid, "name": name, "size": len(idx), "first": dates[0] if dates else "", "last": dates[-1] if dates else "",
                           "chats": len({recs[i]["chat"] for i in idx}), "members": [recs[i]["id"] for i in idx],
                           "nearest_members": [recs[i]["id"] for i in shown if lab[i] == -1]})
        layers.append(arr)
        print(f"layer {lid}: {len(set(lab) - {-1})} topics, {int((lab == -1).sum())} unclustered", flush=True)
    (a.out / "records.json").write_text(json.dumps({"records": recs}, ensure_ascii=False), encoding="utf-8")   # chats + session prompts, for name_topics.py
    (a.out / "topics.json").write_text(json.dumps({"records": len(recs), "clusterer": a.clusterer, "layers": layer_ids, "topics": topics}, indent=1), encoding="utf-8")
    app = np.array([source(r) for r in recs], dtype=object)
    where = np.array(["Coding session" if x in CODING else "Chat" for x in app], dtype=object)
    kind = np.array([KIND_GROUPS.get(r["kind"], "Other") for r in recs], dtype=object)
    dates = pd.to_datetime(pd.Series([r["date"] or None for r in recs]), errors="coerce", utc=True, format="mixed").dt.tz_localize(None)
    print(f"undated records: {int(dates.isna().sum())} (shown at the earliest date in the date filter)", file=sys.stderr)
    dates = dates.fillna(dates.min())
    paths = [[int(name_idx[i, li]) for li in range(len(labs) - 1, -1, -1) if name_idx[i, li]] for i in range(len(recs))]   # coarse to fine; negative = nearest topic
    hover = [f'{r["title"][:120]} · {str(r["date"])[:10]} · {kind[i]} · {app[i]}\n“{r["quote"][:240]}”' for i, r in enumerate(recs)]   # datamapplot shows hover text as plain text
    sel = np.where(keep)[0]
    cat = lambda field, desc, values, colours: {"field": field, "description": desc, "kind": "categorical",
                                                "color_mapping": {k: colours[k] for k in colours if k in set(values)}, "show_legend": True}
    plot = datamapplot.create_interactive_plot(
        xy[sel], *[l[sel] for l in layers], hover_text=[hover[i] for i in sel], title="Positions (private)",
        sub_title=f"{len(recs)} statements from {len({r['chat'] for r in recs})} chats and coding sessions. {"Topic names are written by a model from each topic's quotes" if given else "Topic names are each topic's top keywords"}; points the clusterer left out take the topic of their nearest neighbours (marked in the side panel). Click a point to read it; hover any control for help.",
        enable_search=True, darkmode=False, font_family="Roboto", noise_label="Unlabelled",
        extra_point_data=pd.DataFrame({"idx": sel}), on_click="igShow(+`{idx}`)",
        enable_topic_tree=True, topic_tree_kwds={"title": "Topics (click to zoom)", "max_height": "38vh"}, cluster_layer_colormaps=True,
        histogram_data=dates.iloc[sel].reset_index(drop=True), histogram_n_bins=40, histogram_group_datetime_by="month",
        colormap_rawdata=[where[sel], app[sel], kind[sel]],
        colormap_metadata=[cat("where", "Coding session or chat", where[sel], SOURCE_COLOURS),
                           cat("app", "Which app", app[sel], {k: SOURCE_COLOURS[k] for k in APPS + ["Other"]}),
                           cat("kind", "Kind of statement", kind[sel], KIND_COLOURS)],
        custom_css=PAGE.with_suffix(".css").read_text(encoding="utf-8"),
        custom_html='<aside id="ig-panel" hidden><button id="ig-close" data-tip="Close this panel">×</button><div id="ig-body"></div></aside><div id="ig-tip" role="tooltip"></div>',
        custom_js=page_js(recs, names, paths, kind, app, [int(len(set(l.tolist()) - {-1})) for l in reversed(labs)]))
    plot.save(str(a.out / "index.html"))
    n_lab = [int((l != "Unlabelled").sum()) for l in layers]
    print(json.dumps({"records": len(recs), "plotted": int(keep.sum()), "layers": layer_ids, "events_labelled_per_layer": n_lab, "topics": len(topics)}))


if __name__ == "__main__":
    main()
