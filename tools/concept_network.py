"""Concept network and topic-by-month grid from chats, with no generative model.

Terms are spaCy named entities and short noun phrases. Two terms are linked when they appear in
the same chats. Communities (Louvain) are the topics. `--text user` uses only the human's turns;
`--text both` also uses the assistant's. Chats listed in the exporter's agent-send log are excluded:
they were opened by agents, so their user turns are not the human's. Absence from that log is not
proof of human authorship (the log starts 2026-09-16).
"""
import argparse
import collections
import json
import math
import re
from pathlib import Path

import networkx as nx
import spacy

ENT_TYPES = {"PERSON", "ORG", "GPE", "PRODUCT", "WORK_OF_ART", "EVENT", "LAW", "NORP", "FAC"}
CODE = re.compile(r"```.*?```", re.S)
URL = re.compile(r"https?://\S+")
BAD_TOKENS = {"i", "you", "it", "he", "she", "we", "they", "this", "that", "these", "those", "which", "what", "who", "one",
              "thing", "things", "way", "lot", "kind", "sort", "bit", "something", "anything", "everything", "ok", "okay",
              "example", "case", "part", "use", "step", "need", "question", "answer", "problem", "idea", "point", "time"}


def agent_threads(path: Path) -> set:
    ids, bad = set(), 0
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.strip():
            continue
        try:
            e = json.loads(line)
        except json.JSONDecodeError:
            bad += 1
            continue
        if e.get("thread_id"):
            ids.add(e["thread_id"])
    print(f"agent-send log: {len(ids)} threads, {bad} unparseable line(s) skipped")
    return ids


def load(conv_dir, exclude, since, until, text, max_chars):
    chats = []
    for f in sorted(conv_dir.glob("*.conv.json")):
        c = json.loads(f.read_text(encoding="utf-8"))
        if c["id"].split(":", 1)[1] in exclude:
            continue
        user = {p["id"] for p in c["participants"] if p["role"] == "user"}
        um = [m for m in c["messages"] if m["actor_id"] in user]
        stamps = sorted(m["timestamp"][:10] for m in um if m.get("timestamp"))
        if not stamps or not (since <= stamps[0] <= until):
            continue
        pick = um if text == "user" else c["messages"]
        body = URL.sub(" ", CODE.sub(" ", "\n".join(m["text"] for m in pick)))[:max_chars]
        if len(body.strip()) >= 40:
            chats.append({"chat": c["id"], "title": c["title"], "first": stamps[0], "month": stamps[0][:7], "doc": body})
    return chats


def terms(nlp, docs):
    out = []
    for d in nlp.pipe(docs, batch_size=8, n_process=6):
        seen = collections.Counter()
        for e in d.ents:
            if e.label_ in ENT_TYPES:
                t = e.text.strip().lower()
                if len(t) > 2 and t not in BAD_TOKENS:
                    seen[t] += 1
        for ch in d.noun_chunks:
            toks = [t for t in ch if not (t.is_stop or t.is_punct or t.pos_ in ("DET", "PRON", "NUM"))]
            if not toks or len(toks) > 3 or ch.root.pos_ not in ("NOUN", "PROPN"):
                continue
            if not all(t.is_alpha for t in toks):
                continue
            lem = " ".join(t.lemma_.lower() for t in toks)
            if len(lem) > 2 and lem not in BAD_TOKENS and not set(lem.split()) <= BAD_TOKENS:
                seen[lem] += 1
        out.append(seen)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conv_dir", type=Path)
    ap.add_argument("agent_log", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--text", choices=["user", "both"], required=True)
    ap.add_argument("--since", default="")
    ap.add_argument("--until", default="9999-12-31")
    ap.add_argument("--max-chars", type=int, default=20000)
    ap.add_argument("--min-df", type=int, default=4)
    a = ap.parse_args()
    chats = load(a.conv_dir, agent_threads(a.agent_log), a.since, a.until, a.text, a.max_chars)
    if not chats:
        raise SystemExit("no chats left after filters")
    nlp = spacy.load("en_core_web_sm", disable=["lemmatizer"] if False else [])
    per = terms(nlp, [c["doc"] for c in chats])
    n = len(chats)
    df = collections.Counter(t for p in per for t in p)
    keep = {t for t, k in df.items() if a.min_df <= k <= 0.12 * n}
    chat_terms = []
    for p in per:
        sc = {t: (1 + math.log(c)) * math.log(n / df[t]) for t, c in p.items() if t in keep}
        chat_terms.append([t for t, _ in sorted(sc.items(), key=lambda kv: -kv[1])[:25]])
    pair = collections.Counter()
    for ts in chat_terms:
        for i, x in enumerate(ts):
            for y in ts[i + 1:]:
                pair[tuple(sorted((x, y)))] += 1
    G = nx.Graph()
    for (x, y), k in pair.items():
        if k >= 3:
            G.add_edge(x, y, weight=k, npmi=math.log(k * n / (df[x] * df[y])) / -math.log(k / n))
    top = {}
    for node in G:
        nb = sorted(G[node].items(), key=lambda kv: -kv[1]["npmi"])[:8]
        top[node] = {m for m, _ in nb}
    H = nx.Graph()
    for x in G:
        for y in top[x]:
            H.add_edge(x, y, **G[x][y])
    comms = nx.community.louvain_communities(H, weight="weight", seed=7, resolution=1.0)
    comms = sorted((c for c in comms if len(c) >= 4), key=len, reverse=True)
    member, names = {}, {}
    for i, c in enumerate(comms):
        names[i] = " / ".join(t for t, _ in sorted(((t, H.degree(t, weight="weight")) for t in c), key=lambda kv: -kv[1])[:4])
        for t in c:
            member[t] = i
    by_chat = []
    grid = collections.defaultdict(collections.Counter)
    for c, ts in zip(chats, chat_terms):
        votes = collections.Counter(member[t] for t in ts if t in member)
        topic = votes.most_common(1)[0][0] if votes else None
        by_chat.append({"chat": c["chat"], "title": c["title"], "first": c["first"], "topic": topic})
        if topic is not None:
            grid[c["month"]][topic] += 1
    a.out_dir.mkdir(parents=True, exist_ok=True)
    (a.out_dir / "network.json").write_text(json.dumps({
        "nodes": [{"id": t, "df": df[t], "topic": member.get(t)} for t in H if t in member],
        "edges": [{"source": x, "target": y, "weight": d["weight"], "npmi": round(d["npmi"], 3)} for x, y, d in H.edges(data=True)
                  if x in member and y in member],
        "topics": {str(i): {"name": names[i], "terms": len(c)} for i, c in enumerate(comms)}}), encoding="utf-8")
    (a.out_dir / "chats.json").write_text(json.dumps(by_chat), encoding="utf-8")
    (a.out_dir / "grid.json").write_text(json.dumps({"months": sorted(grid), "topics": names,
                                                     "counts": {m: dict(grid[m]) for m in sorted(grid)}}), encoding="utf-8")
    print(json.dumps({"text": a.text, "chats": n, "terms_kept": len(keep), "nodes": H.number_of_nodes(), "edges": H.number_of_edges(),
                      "topics": len(comms), "chats_without_topic": sum(1 for b in by_chat if b["topic"] is None)}))


if __name__ == "__main__":
    main()
