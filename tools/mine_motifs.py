"""Mine candidate reasoning motifs from Brian's own typed relations across chat graphs.

Stages (run in order; each writes under --out, which should be gitignored private/):
  load   -> relations.json : Brian-anchored relations (every anchor in a participant:brian message, quote verbatim), deduped by chat id
  embed  -> clusters.json  : MiniLM embeddings + HDBSCAN within each relation kind, then a cross-kind pass; keeps clusters spanning
                             >=5 chats and >=3 topic areas (layer-25 topics via position_map_full/topics.json, else chat title)
  name   -> motifs.json    : one structured LLM call per cluster (Pydantic); cited relation ids are checked and every cited quote is
                             re-verified verbatim against its message; ranked by chats, year span and recency
Usage: mine_motifs.py {load|embed|name|report} --out private/motifs [--budget 0.80]
Needs sentence_transformers/hdbscan (~/.venvs/inquiry-maps) for embed; llm_client (~/.venvs/inquiry-or) for name.
"""
import argparse
import asyncio
import json
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = ["out", "kept/out", "new108/out", "single/out", "claude_export/out", "or_run/out", "gemini_takeout/out"]
BASE = ROOT / "private/extract_full_20261003"
BRIAN = "participant:brian"


def load(out):
    seen, rels, kinds_all, chats = set(), [], Counter(), 0
    for d in DIRS:
        for f in sorted((BASE / d).glob("*.graph.json")):
            g = json.loads(f.read_text(encoding="utf-8"))
            conv = g["conversations"][0]
            if conv["id"] in seen:
                continue
            seen.add(conv["id"])
            chats += 1
            msgs = {m["id"]: m for m in conv["messages"]}
            nodes = {n["id"]: n for n in g["nodes"]}
            for r in g["relations"]:
                if r["kind"] == "answers" or not r["anchors"]:
                    continue
                ok = all((m := msgs.get(a["message_id"])) and m["actor_id"] == BRIAN and a["quote"] in m["text"] for a in r["anchors"])
                if not ok:
                    continue
                ends = [nodes[b["ref"]] for b in r["bindings"] if b["ref"] in nodes]
                if len(ends) < 2:
                    continue
                kinds_all[r["kind"]] += 1
                dates = [msgs[a["message_id"]].get("timestamp") or "" for a in r["anchors"]]
                rels.append({"id": r["id"], "chat": conv["id"], "title": conv["title"].strip().replace("\n", " ")[:100], "kind": r["kind"],
                             "date": min(dates)[:10], "roles": [(b["role"], nodes[b["ref"]]["text"]) for b in r["bindings"] if b["ref"] in nodes],
                             "anchors": [{"message_id": a["message_id"], "quote": a["quote"]} for a in r["anchors"]]})
    (Path(out) / "relations.json").write_text(json.dumps({"chats_scanned": chats, "per_kind": kinds_all, "relations": rels}, indent=1), encoding="utf-8")
    print(json.dumps({"chats_scanned": chats, "brian_relations": len(rels), "per_kind": kinds_all}))


def topic_of(rels):
    """Message-id -> layer-25 topic, from the position-record topics; relations fall back to the chat's majority topic."""
    tp = json.loads((ROOT / "private/position_map_full/topics.json").read_text())
    recs = {r["id"]: r for r in json.loads((ROOT / "private/records_full.json").read_text())["records"]}
    layer = min(t["layer"] for t in tp["topics"])
    msg_t, chat_t = {}, defaultdict(Counter)
    for t in tp["topics"]:
        if t["layer"] != layer:
            continue
        for m in t["members"]:
            r = recs.get(m)
            if r:
                msg_t[r["message_id"]] = t["topic"]
                chat_t[r["chat"]][t["topic"]] += 1
    names = {t["topic"]: t["name"] for t in tp["topics"] if t["layer"] == layer}
    out = {}
    for r in rels:
        t = next((msg_t[a["message_id"]] for a in r["anchors"] if a["message_id"] in msg_t), None)
        if t is None and chat_t.get(r["chat"]):
            t = chat_t[r["chat"]].most_common(1)[0][0]
        out[r["id"]] = (t, names.get(t))
    return out, layer


def rel_text(r, with_quote=True):
    s = r["kind"] + ": " + " | ".join(f"{role}: {t}" for role, t in r["roles"])
    return s + (" || " + r["anchors"][0]["quote"][:300] if with_quote else "")


def embed(out):
    import hdbscan
    import numpy as np
    from sentence_transformers import SentenceTransformer
    rels = json.loads((Path(out) / "relations.json").read_text())["relations"]
    tmap, layer = topic_of(rels)
    for r in rels:
        r["topic"], r["topic_name"] = tmap[r["id"]]
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Embed the endpoint texts and the raw quote separately so a cluster can be tested against extractor phrasing.
    E_nodes = model.encode([rel_text(r, False) for r in rels], normalize_embeddings=True, batch_size=128)
    E_full = model.encode([rel_text(r) for r in rels], normalize_embeddings=True, batch_size=128)
    np.save(Path(out) / "emb_full.npy", E_full)
    groups = []  # (scope, indices)
    by_kind = defaultdict(list)
    for i, r in enumerate(rels):
        by_kind[r["kind"]].append(i)
    for k, idx in by_kind.items():
        groups.append((k, idx))
    groups.append(("ACROSS_KINDS", list(range(len(rels)))))
    clusters = []
    for scope, idx in groups:
        if len(idx) < 30:
            continue
        X = E_full[idx]
        lab = hdbscan.HDBSCAN(min_cluster_size=8, min_samples=3, metric="euclidean", cluster_selection_method="leaf").fit_predict(X)
        for c in sorted(set(lab) - {-1}):
            mem = [idx[j] for j in np.where(lab == c)[0]]
            chats = {rels[i]["chat"] for i in mem}
            tops = {rels[i]["topic"] or rels[i]["title"] for i in mem}
            if len(chats) < 5 or len(tops) < 3:
                continue
            cen = X[lab == c].mean(0)
            order = sorted(mem, key=lambda i: -float(E_full[i] @ cen))
            clusters.append({"cluster": f"{scope}:{c}", "scope": scope, "n": len(mem), "chats": len(chats), "topics": len(tops),
                             "members": [rels[i]["id"] for i in order]})
    (Path(out) / "relations_topics.json").write_text(json.dumps(rels), encoding="utf-8")
    (Path(out) / "clusters.json").write_text(json.dumps({"topic_layer": layer, "clusters": clusters}, indent=1), encoding="utf-8")
    print(json.dumps({"relations": len(rels), "clusters_kept": len(clusters), "by_scope": Counter(c["scope"] for c in clusters)}))
    np.save(Path(out) / "emb_nodes.npy", E_nodes)


def _norm(s):
    return " ".join(s.split())


class Cite(__import__("pydantic").BaseModel):
    relation_id: str
    quote: str


def _models():
    from typing import Literal
    from pydantic import BaseModel, Field

    class Motif(BaseModel):
        verdict: Literal["motif", "topic", "extractor_phrasing"] = Field(description="motif = a recurring way of reasoning that would apply across subjects; topic = the members share a subject; extractor_phrasing = they share wording that comes from the labelling, not from Brian's words")
        name: str = Field(description="Short plain-words name for the move (not the subject).")
        move: str = Field(description="One sentence: what Brian does when he reasons this way.")
        example: str = Field(description="One concrete example drawn from the cited relations.")
        why: str = Field(description="One sentence on why this verdict, including what varies across the cluster.")
        cites: list[Cite] = Field(description="3-6 relations you relied on, each with its id exactly as shown and a verbatim substring of Brian's quote shown for it.")
    return Motif


async def name_one(cl, byid, model, budget, rels_per=14):
    from llm_client import acall_llm_structured
    Motif = _models()
    mem = [byid[i] for i in cl["members"]]
    pick, seen = [], Counter()
    for r in mem:  # nearest-to-centroid first, at most 2 per chat so one chat cannot dominate the sample
        if seen[r["chat"]] < 2:
            seen[r["chat"]] += 1
            pick.append(r)
        if len(pick) == rels_per:
            break
    ev = "\n".join(f'{r["id"]} | {r["date"]} | {r["kind"]} | ' + " ; ".join(f"{a}: {t[:140]}" for a, t in r["roles"]) + f' | Brian said: "{r["anchors"][0]["quote"][:260]}"' for r in pick)
    system = ("You judge whether a cluster of Brian's own reasoning relations is a MOTIF: a recurring way of reasoning (a kind of distinction, "
              "decomposition, prerequisite check, reframing of a question, standard of evidence) that shows up regardless of subject. It is a TOPIC if the members "
              "mostly share a subject, product or project, and EXTRACTOR_PHRASING if what they share is wording from the endpoint labels rather than from what Brian said. "
              "Judge from Brian's own words (the quotes) first; endpoint texts are an outside labeller's paraphrase. Use only the records given. Cite ids exactly and quote verbatim.")
    out, meta = await acall_llm_structured(model, [{"role": "system", "content": system}, {"role": "user", "content": f"Cluster of {cl['n']} relations over {cl['chats']} chats; sample:\n{ev}"}],
        response_model=Motif, reasoning_effort="medium", model_policy="enforce_allowlist", task="motif-naming", trace_id="inquiry-graph/mine-motifs", max_budget=budget)
    return out, pick


def name(out, model="openrouter/openai/gpt-5.6-luna", budget=0.80, limit=40):
    out = Path(out)
    rels = json.loads((out / "relations_topics.json").read_text())
    byid = {r["id"]: r for r in rels}
    cl = json.loads((out / "clusters.json").read_text())["clusters"]
    cl.sort(key=lambda c: -(c["chats"] * c["topics"]))
    cl = cl[:limit]
    per = budget  # llm_client scopes max_budget to the whole trace_id, so each call gets the total cap
    res, spent_est = [], 0.0

    async def go():
        sem = asyncio.Semaphore(4)

        async def one(c):
            async with sem:
                try:
                    return c, await name_one(c, byid, model, per)
                except Exception as e:  # fail loudly in the output, not silently
                    return c, e
        return await asyncio.gather(*[one(c) for c in cl])
    for c, r in asyncio.run(go()):
        if isinstance(r, Exception):
            res.append({**{k: c[k] for k in ("cluster", "n", "chats", "topics")}, "error": repr(r)[:300]})
            continue
        o, pick = r
        shown = {x["id"]: x for x in pick}
        checks = []
        for ct in o.cites:
            rel = shown.get(ct.relation_id)
            okq = bool(rel) and any(_norm(ct.quote) in _norm(a["quote"]) for a in rel["anchors"]) and len(_norm(ct.quote)) > 0
            checks.append({"relation_id": ct.relation_id, "quote": ct.quote, "verbatim_ok": okq})
        mem = [byid[i] for i in c["members"]]
        years = sorted({m["date"][:4] for m in mem if m["date"]})
        res.append({**{k: c[k] for k in ("cluster", "scope", "n", "chats", "topics")}, "years": years, "last": max(m["date"] for m in mem),
                    "verdict": o.verdict, "name": o.name, "move": o.move, "example": o.example, "why": o.why, "cites": checks,
                    "cites_all_verbatim": bool(checks) and all(x["verbatim_ok"] for x in checks), "members": c["members"]})
    (out / "motifs_raw.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps({"clusters_named": len(res), "verdicts": Counter(r.get("verdict", "error") for r in res), "cites_all_verbatim": sum(r.get("cites_all_verbatim", False) for r in res)}))


def _grams(t, n=3):
    w = [x for x in "".join(c.lower() if c.isalnum() else " " for c in t).split()]
    return {" ".join(w[i:i + n]) for i in range(len(w) - n + 1)}


def report(out):
    """Rank, artifact tests, top-quote selection. Writes motifs.json (ranked, with quotes) for hand-checking and motifs.md."""
    out = Path(out)
    rels = {r["id"]: r for r in json.loads((out / "relations_topics.json").read_text())}
    msgtext = {}
    for d in DIRS:
        for f in sorted((BASE / d).glob("*.graph.json")):
            g = json.loads(f.read_text(encoding="utf-8"))
            for m in g["conversations"][0]["messages"]:
                msgtext[m["id"]] = len(m["text"])
    raw = json.loads((out / "motifs_raw.json").read_text())
    res = []
    for c in raw:
        mem = [rels[i] for i in c["members"]]
        # Extractor-phrasing test: the most common 3-gram across endpoint texts; how often does it occur in endpoints vs in Brian's raw quotes?
        cnt = Counter(g for r in mem for g in set().union(*[_grams(t) for _, t in r["roles"]]))
        gram, ng = cnt.most_common(1)[0]
        nq = sum(gram in _grams(" ".join(a["quote"] for a in r["anchors"])) for r in mem)
        longmsg = sum(max(msgtext.get(a["message_id"], 0) for a in r["anchors"]) > 2000 for r in mem)
        qdup = Counter(" ".join(r["anchors"][0]["quote"].lower().split())[:60] for r in mem)
        dupchats = sum(1 for r in mem if qdup[" ".join(r["anchors"][0]["quote"].lower().split())[:60]] > 1)
        yrs = sorted({r["date"][:4] for r in mem if r["date"]})
        # three dated quotes from different chats and, where possible, different years (nearest-to-centroid first; short, non-pasted messages)
        quotes, seen_c, seen_y = [], set(), set()
        for pass_ in (0, 1):
            for r in mem:
                q = r["anchors"][0]["quote"]
                if r["chat"] in seen_c or len(quotes) == 3 or not (25 <= len(q) <= 400) or max(msgtext.get(a["message_id"], 0) for a in r["anchors"]) > 2000:
                    continue
                if pass_ == 0 and r["date"][:4] in seen_y:
                    continue
                quotes.append({"relation_id": r["id"], "date": r["date"], "chat_title": r["title"], "quote": q})
                seen_c.add(r["chat"]); seen_y.add(r["date"][:4])
        res.append({**{k: v for k, v in c.items() if k != "members"}, "members_n": len(mem), "years": yrs,
                    "artifact_test": {"top_endpoint_3gram": gram, "members_with_it_in_endpoints": ng, "members_with_it_in_raw_quotes": nq,
                                      "members_anchored_in_msgs_over_2000_chars": longmsg, "members_sharing_quote_opening_with_another": dupchats},
                    "quotes": quotes, "relation_ids": c["members"]})
    ok = [r for r in res if "error" not in r]
    ok.sort(key=lambda r: (r["verdict"] != "motif", -r["chats"], -len(r["years"]), r["last"]), reverse=False)
    # rank: motifs first, then by chats desc, years desc, recency desc
    ok.sort(key=lambda r: (r["verdict"] != "motif", -r["chats"], -len(r["years"]), -int(r["last"].replace("-", "") or 0)))
    (out / "motifs.json").write_text(json.dumps({"ranked": ok}, indent=1), encoding="utf-8")
    lines = ["# Candidate reasoning motifs (private; contains Brian's verbatim words)\n",
             "Ranked: model-judged motifs first, then by chats spanned, years spanned, recency. `paste-risk` = share of the cluster's relations anchored in messages over 2000 characters, where Brian most likely pasted a spec or document rather than reasoning; high paste-risk means treat the motif as unproven.\n"]
    for i, r in enumerate([x for x in ok if x["verdict"] == "motif"], 1):
        at = r["artifact_test"]
        risk = at["members_anchored_in_msgs_over_2000_chars"] / r["members_n"]
        conf = "low" if risk > 0.5 else ("medium" if r["chats"] < 10 else "medium-high")
        qs = list(r["quotes"])
        if len(qs) < 3:  # fall back to any other distinct-chat quotes, flagged
            used = {q["relation_id"] for q in qs}
            for rid in r["relation_ids"]:
                rl = rels[rid]
                if rid not in used and rl["chat"] not in {rels[u]["chat"] for u in used} and len(qs) < 3:
                    qs.append({"relation_id": rid, "date": rl["date"], "chat_title": rl["title"], "quote": rl["anchors"][0]["quote"][:300], "flag": "from a long message"})
                    used.add(rid)
        lines += [f"## {i}. {r['name']}", f"- Move: {r['move']}", f"- Example: {r['example']}",
                  f"- Spread: {r['chats']} chats, {r['topics']} topics, years {', '.join(r['years'])}; found in relation kind {r['scope']}",
                  f"- Confidence: {conf} (paste-risk {risk:.0%}; model's reason: {r['why']})"]
        lines += [f"  - {q['date']} | {q['chat_title'][:50]} | \"{q['quote'][:300]}\"" + (" [from a long message]" if q.get("flag") else "") + f" ({q['relation_id'][-30:]})" for q in qs]
        lines.append("")
    (out / "motifs.md").write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"ranked": len(ok), "motifs": sum(r["verdict"] == "motif" for r in ok)}))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stage", choices=["load", "embed", "name", "report"])
    ap.add_argument("--out", type=Path, default=ROOT / "private/motifs")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    {"load": load, "embed": embed, "name": name, "report": report}.get(a.stage, lambda o: None)(a.out)


if __name__ == "__main__":
    main()
