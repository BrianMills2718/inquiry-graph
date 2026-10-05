"""Test whether candidate reasoning methods recur across Brian's whole chat archive.

Stages (each cached under private/motifs_recur/):
  corpus    Brian's own messages (15..1500 chars) from normalized archives, deduped by chat+text.
  embed     all-MiniLM-L6-v2 embeddings (run with the inquiry-maps venv).
  retrieve  top-K nearest corpus messages per seed message, excluding the seed chats.
  judge     one structured LLM call per method (run with the inquiry-or venv); verbatim quote check in code.
Usage: test_method_recurrence.py {corpus|embed|retrieve|judge} [--out private/motifs_recur]
"""
import argparse, glob, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = Path.home() / "code/chatgpt-conversation-manager-v0.2/data/raw/chats"
SEED_CHATS = {"6ab96260-eb14-83ea-ae11-f964811b3b4f", "6ab8563b-cbfc-83ea-81ed-a0acdea0ea9c"}
A, B = "6ab96260-eb14-83ea-ae11-f964811b3b4f", "6ab8563b-cbfc-83ea-81ed-a0acdea0ea9c"
# (chat, message number as in the handoff). Resolved against messages[] in the raw file; see resolve_seed.
METHODS = {
    "M1": ("define a thing by its role/intent, not its nature", [(A, 13), (A, 1453)]),
    "M2": ("treat a frame or boundary as a hypothesis and test it by acting", [(A, 1455), (A, 1678)]),
    "M3": ("separate describing a thing from playing or optimizing it well", [(A, 1682)]),
    "M4": ("ask for a concrete example to ground an abstraction", [(A, 1445), (A, 27)]),
    "M5": ("test an abstraction operationally: how would it be assessed or used", [(A, 1447), (A, 1518)]),
    "M6": ("step back to the goal and police scope (forest for the trees, don't drift into what is optimal)", [(B, 227), (B, 396), (A, 1682)]),
    "M7": ("order dependencies, then generalise the ordering (requirements before failure modes)", [(A, 876), (A, 828)]),
    "M8": ("factor into primitives, then check over/under-factoring (canonical factorization)", [(B, 146), (B, 96)]),
}
MIN, MAX = 15, 1500


def seed_text(chat, n):
    d = json.loads((RAW / f"{chat}.json").read_text())
    ms = d["messages"]
    m = ms[n]  # handoff numbers index messages[] directly (0-based)
    assert m["role"] == "user", (chat, n, m["role"])
    return m


def corpus(out):
    pats = ["private/kept_normalized_20261003/*.conv.json", "private/claude_export_normalized_20261004/*.conv.json",
            "private/official_exports/gemini_20261005/normalized/*.conv.json"]
    seen, rows, dropped_long, dropped_short, total = set(), [], 0, 0, 0
    for p in pats:
        for f in sorted(glob.glob(str(ROOT / p))):
            c = json.load(open(f))
            cid = c["id"].split(":", 1)[-1]
            for m in c["messages"]:
                if m.get("actor_id") != "participant:brian":
                    continue
                t = m["text"].strip()
                total += 1
                if len(t) < MIN: dropped_short += 1; continue
                if len(t) > MAX: dropped_long += 1; continue
                k = (c["id"], t)
                if k in seen: continue
                seen.add(k)
                rows.append({"i": len(rows), "chat": c["id"], "title": c["title"].strip().replace("\n", " ")[:100],
                             "date": (m.get("timestamp") or "")[:10], "mid": m["id"], "text": t})
    (out / "corpus.json").write_text(json.dumps(rows))
    stats = {"brian_messages_seen": total, "too_long": dropped_long, "too_short": dropped_short, "kept_deduped": len(rows),
             "chats": len({r["chat"] for r in rows})}
    (out / "corpus_stats.json").write_text(json.dumps(stats)); print(stats)


def embed(out):
    import numpy as np
    from sentence_transformers import SentenceTransformer
    st = SentenceTransformer("all-MiniLM-L6-v2")
    rows = json.loads((out / "corpus.json").read_text())
    np.save(out / "corpus_emb.npy", st.encode([r["text"] for r in rows], batch_size=64, normalize_embeddings=True, show_progress_bar=False))
    seeds = {k: [seed_text(c, n)["text"] for c, n in v[1]] for k, v in METHODS.items()}
    (out / "seeds.json").write_text(json.dumps(seeds, indent=1))
    flat = [(k, j, t) for k, ts in seeds.items() for j, t in enumerate(ts)]
    np.save(out / "seed_emb.npy", st.encode([t for _, _, t in flat], normalize_embeddings=True))
    (out / "seed_index.json").write_text(json.dumps([[k, j] for k, j, _ in flat]))


def retrieve(out, k=40):
    import numpy as np
    rows = json.loads((out / "corpus.json").read_text())
    E = np.load(out / "corpus_emb.npy"); S = np.load(out / "seed_emb.npy")
    idx = json.loads((out / "seed_index.json").read_text())
    ok = np.array([r["chat"].split(":", 1)[-1] not in SEED_CHATS for r in rows])
    cand = {}
    for (m, j), s in zip(idx, S):
        sims = E @ s; sims[~ok] = -9
        for i in np.argsort(-sims)[:k]:
            cand.setdefault(m, {}).setdefault(int(i), float(sims[i]))
    res = {m: [{**rows[i], "sim": round(v, 3)} for i, v in sorted(d.items(), key=lambda x: -x[1])] for m, d in cand.items()}
    (out / "candidates.json").write_text(json.dumps(res)); print({m: len(v) for m, v in res.items()})


def judge(out, model, batch=25):
    import asyncio
    from typing import Literal
    from pydantic import BaseModel, Field
    from llm_client import acall_llm_structured
    cands = json.loads((out / "candidates.json").read_text())

    class Call(BaseModel):
        id: int
        verdict: Literal["same_move", "different_move", "unclear"]
        quote: str = Field(description="Verbatim excerpt (under 120 chars) from the message showing the move; empty if not same_move.")
        reason: str = Field(description="One sentence.")
        different_move_name: str = Field(description="If different_move and it is a clear reasoning move, name it in 2-6 words; else empty.")

    class Calls(BaseModel):
        calls: list[Call]

    async def run():
        res = {}
        for m, (defn, _) in METHODS.items():
            seeds = json.loads((out / "seeds.json").read_text())[m]
            res[m] = []
            cs = cands[m]
            for b in range(0, len(cs), batch):
                chunk = cs[b:b + batch]
                body = "\n\n".join(f"[{c['i']}] {c['text']}" for c in chunk)
                sys_p = (f"Reasoning method: {defn}. Seed examples of Brian doing it:\n" + "\n".join("- " + s[:300] for s in seeds) +
                         "\n\nFor each candidate message by Brian, judge: same_move only if the message itself performs this reasoning move "
                         "(not merely the same topic or vocabulary); different_move if it performs another move or none; unclear if too little context. "
                         "Quote must be verbatim.")
                o, _ = await acall_llm_structured(model, [{"role": "system", "content": sys_p}, {"role": "user", "content": body}],
                    response_model=Calls, reasoning_effort="medium", model_policy="enforce_allowlist", task="method-recurrence",
                    trace_id="inquiry-graph/method-recurrence", max_budget=0.2)
                by = {c["i"]: c for c in chunk}
                for c in o.calls:
                    if c.id not in by: continue
                    r = by[c.id]; d = c.model_dump()
                    d["quote_verbatim"] = bool(c.quote) and c.quote in r["text"]
                    if c.verdict == "same_move" and not d["quote_verbatim"]:
                        d["verdict"] = "unclear"; d["reason"] += " [downgraded: quote not verbatim]"
                    res[m].append({**r, **d})
            print(m, sum(1 for x in res[m] if x["verdict"] == "same_move"), "same of", len(res[m]), flush=True)
        (out / "judged.json").write_text(json.dumps(res, indent=1))
    asyncio.run(run())


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("stage", choices=["corpus", "embed", "retrieve", "judge"])
    ap.add_argument("--out", type=Path, default=ROOT / "private/motifs_recur")
    ap.add_argument("--model", default="openrouter/openai/gpt-5.6-luna")
    a = ap.parse_args(); a.out.mkdir(parents=True, exist_ok=True)
    {"corpus": lambda: corpus(a.out), "embed": lambda: embed(a.out), "retrieve": lambda: retrieve(a.out),
     "judge": lambda: judge(a.out, a.model)}[a.stage]()
