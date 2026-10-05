"""Second pass: ask a model to connect ideas that have no relation, across the whole chat (not just one chunk).

Usage: link_isolated.py <in_dir/out> <out_dir/out> [--limit N] [--workers 8] [--model M] [--min-isolated 3]
For each graph with at least --min-isolated unlinked ideas, send the idea list (id number, kind, text) and get back typed
links by number. Code validates every link (known numbers, no self-link, no duplicate, kind rules else related_to) and writes it
with origin=inferred, review_status=proposed, anchored on the SOURCE idea's own verbatim quote. Existing content is untouched.
"""
import argparse
import asyncio
import json
import os
from collections import Counter
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from inquiry_graph.model import SIGNATURES

KINDS = list(SIGNATURES)
WINDOW, OVERLAP = 160, 30


class Link(BaseModel):
    kind: Literal[tuple(KINDS)]  # type: ignore[valid-type]
    first: int = Field(description="number of the idea filling the FIRST role of the kind's signature")
    second: int = Field(description="number of the idea filling the SECOND role")


class Links(BaseModel):
    links: list[Link] = Field(default_factory=list)


SYSTEM = ("You connect ideas extracted from one conversation. Ideas marked * currently have NO link. Propose links only where the two ideas are "
          "clearly related in the conversation. Strongly prefer attaching each * idea to its single most related idea; add other links sparingly. "
          "Use related_to when unsure which specific kind fits. Relation kinds and their (first, second) roles: " +
          "; ".join(f"{k}({', '.join(v)})" for k, v in SIGNATURES.items()) + ". Never link an idea to itself. Return no link rather than a guess.")


def windows(n):
    if n <= WINDOW:
        return [(0, n)]
    out, s = [], 0
    while s < n:
        out.append((s, min(n, s + WINDOW)))
        if s + WINDOW >= n:
            break
        s += WINDOW - OVERLAP
    return out


async def link_graph(sem, g, model):
    from llm_client import acall_llm_structured
    nodes = g["nodes"]
    linked = {b["ref"] for r in g["relations"] for b in r["bindings"]}
    added, rejected = [], Counter()
    have = {(r["kind"], tuple(b["ref"] for b in r["bindings"])) for r in g["relations"]}
    for a, b in windows(len(nodes)):
        body = "\n".join(f"{i}{'*' if nodes[i]['id'] not in linked else ' '} [{nodes[i]['kind']}] {nodes[i]['text'][:170]}" for i in range(a, b))
        async with sem:
            out, _ = await acall_llm_structured(
                model, [{"role": "system", "content": SYSTEM}, {"role": "user", "content": f"Conversation: {g['conversations'][0]['title']}\n\nIdeas:\n{body}"}],
                response_model=Links, reasoning_effort="medium", model_policy="enforce_allowlist", task="link-isolated-ideas",
                trace_id=f"inquiry-graph/link-isolated/{g['conversations'][0]['id']}/{a}", max_budget=0.5,
                model_justification="Brian approved (2026-10-05) an OpenRouter linking pass over finished graphs; same model as the extraction run.")
        for l in out.links:
            if not (a <= l.first < b and a <= l.second < b) or l.first == l.second:
                rejected["bad_number_or_self"] += 1
                continue
            kind = l.kind
            f, s = nodes[l.first], nodes[l.second]
            r1, r2 = list(SIGNATURES[kind])
            if any("*" not in SIGNATURES[kind][role] and n["kind"] not in SIGNATURES[kind][role] for role, n in ((r1, f), (r2, s))):
                kind = "related_to"
                r1, r2 = list(SIGNATURES[kind])
                rejected["downgraded_to_related_to"] += 1
            key = (kind, (f["id"], s["id"]))
            if key in have or (kind == "related_to" and ("related_to", (s["id"], f["id"])) in have):
                rejected["duplicate"] += 1
                continue
            have.add(key)
            added.append({"id": f"{g['conversations'][0]['id']}:L:r{len(added):03d}", "anchors": f["anchors"][:1], "origin": "inferred",
                          "review_status": "proposed", "kind": kind,
                          "bindings": [{"role": r1, "ref": f["id"]}, {"role": r2, "ref": s["id"]}]})
    g["relations"] += added
    g["extractions"].append({"method": "llm-isolated-linker", "provider": "openrouter", "model": model, "prompt_version": "link-1.0",
                             "notes": [f"{len(added)} links added over {len(windows(len(nodes)))} window(s)"]})
    return len(added), rejected


async def main_async(a):
    src, dst = Path(a.src), Path(a.dst)
    dst.mkdir(parents=True, exist_ok=True)
    jobs = []
    for f in sorted(src.glob("*.graph.json")):
        if (dst / f.name).exists():
            continue
        g = json.loads(f.read_text())
        linked = {b["ref"] for r in g["relations"] for b in r["bindings"]}
        iso = sum(1 for n in g["nodes"] if n["id"] not in linked)
        if len(g["nodes"]) >= 8 and iso >= a.min_isolated:
            jobs.append((f, g))
    if a.limit:
        jobs = jobs[: a.limit]
    sem = asyncio.Semaphore(a.workers)
    tot, rej, done, fail = 0, Counter(), 0, 0

    async def one(f, g):
        nonlocal tot, done, fail
        try:
            n, r = await link_graph(sem, g, a.model)
        except Exception as e:  # leave the graph un-linked and say so; never half-write
            fail += 1
            print("FAILED", f.name, type(e).__name__, str(e)[:120], flush=True)
            return
        (dst / f.name).write_text(json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8")
        tot += n; rej.update(r); done += 1
    await asyncio.gather(*(one(f, g) for f, g in jobs))
    print(json.dumps({"graphs_linked": done, "failed": fail, "links_added": tot, "rejected": dict(rej), "candidates": len(jobs)}))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("src"); ap.add_argument("dst")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--model", default="openrouter/openai/gpt-6-luna")
    ap.add_argument("--min-isolated", type=int, default=3)
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
