"""Mark each quoted position as Brian's own words, pasted/quoted text, or unclear.

Usage: check_authorship.py RECORDS.json OUT.json GRAPH_DIR [GRAPH_DIR ...] [--min-chars 600] [--workers 8]
The extractor only proves a quote sits in a message Brian SENT; a pasted plan or quoted AI reply is part of that message. For every event
whose message is longer than --min-chars, one structured call per message sees the opening of the message plus each quote in context and
labels it own_words | pasted_or_quoted | unclear. Shorter messages are labelled own_words by default (the label then reads 'short_default').
Output {record_id: {"label": ..., "why": ...}}; resumable (existing labels in OUT are kept). Quote-bearing: keep under private/.
"""
import argparse
import asyncio
import json
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


class Verdict(BaseModel):
    n: int = Field(description="quote number")
    label: Literal["own_words", "pasted_or_quoted", "unclear"]
    why: str = Field(description="under 15 words")


class Verdicts(BaseModel):
    verdicts: list[Verdict]


SYSTEM = ("A person (Brian) sent the message below to an AI. For each numbered quote taken from it, decide whether Brian wrote that sentence himself "
          "(own_words), or whether it is text he pasted or quoted from somewhere else, such as an AI reply, a plan, a document, code or a citation "
          "(pasted_or_quoted). Use unclear if you cannot tell. A sentence he wrote about pasted text is own_words; the pasted text itself is pasted_or_quoted.")


async def run(a):
    recs = json.loads(Path(a.records).read_text())["records"]
    out = json.loads(Path(a.out).read_text()) if Path(a.out).exists() else {}
    msgs = {}
    for d in a.graph_dirs:
        for f in Path(d).glob("*.graph.json"):
            c = json.loads(f.read_text())["conversations"][0]
            for m in c["messages"]:
                msgs.setdefault(m["id"], m["text"])
    groups = {}
    for r in recs:
        if r["id"] in out:
            continue
        t = msgs.get(r["message_id"], "")
        if len(t) <= a.min_chars:
            out[r["id"]] = {"label": "own_words", "why": "short_default"}
        else:
            groups.setdefault(r["message_id"], []).append(r)
    print(f"messages to check: {len(groups)} ({sum(len(v) for v in groups.values())} events); defaulted short: {len(out)}", flush=True)
    sem = asyncio.Semaphore(a.workers)
    from llm_client import acall_llm_structured

    async def one(mid, rs):
        t = msgs[mid]
        quotes = []
        for k, r in enumerate(rs, 1):
            i = t.find(r["quote"])
            ctx = t[max(0, i - 220): i + len(r["quote"]) + 220] if i >= 0 else r["quote"]
            quotes.append(f"[{k}] quote: {r['quote']}\n    in context: ...{ctx}...")
        body = f"MESSAGE (length {len(t)} chars). Opening:\n{t[:900]}\n\nQUOTES:\n" + "\n".join(quotes)
        async with sem:
            try:
                res, _ = await acall_llm_structured(
                    a.model, [{"role": "system", "content": SYSTEM}, {"role": "user", "content": body}], response_model=Verdicts,
                    reasoning_effort="low", model_policy="enforce_allowlist", task="authorship-check", trace_id=f"inquiry-graph/authorship/{mid}", max_budget=0.5,
                    model_justification="Brian approved (2026-10-05) an authorship check on quoted positions; same OpenRouter model as the extraction run.")
            except Exception as e:
                print("FAILED", mid[-24:], type(e).__name__, str(e)[:100], flush=True)
                return
        by = {v.n: v for v in res.verdicts}
        for k, r in enumerate(rs, 1):
            v = by.get(k)
            out[r["id"]] = {"label": v.label, "why": v.why} if v else {"label": "unclear", "why": "no verdict returned"}

    done = 0
    items = list(groups.items())
    for s in range(0, len(items), 200):
        await asyncio.gather(*(one(m, rs) for m, rs in items[s:s + 200]))
        Path(a.out).write_text(json.dumps(out), encoding="utf-8")
        done += min(200, len(items) - s)
        print(f"checked {done}/{len(items)} messages", flush=True)
    import collections
    print(json.dumps(collections.Counter(v["label"] for v in out.values())))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("records"); ap.add_argument("out"); ap.add_argument("graph_dirs", nargs="+")
    ap.add_argument("--min-chars", type=int, default=600)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--model", default="openrouter/openai/gpt-6-luna")
    asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    main()
