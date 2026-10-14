"""Give each position-map topic a short plain-language name from its member quotes (Codex subscription route).

Usage: name_topics.py RECORDS.json TOPICS.json OUT_NAMES.json [--model M]
Sends up to 14 members per topic (idea + Brian's quote) and asks for a 2-5 word name that says what the topic is about;
for nested layers, broad topics are named first and each subtopic is told its parent's name. Resumes from OUT_NAMES.json.
Output {topic_id: name}; position_topics.py --names uses it. Names are generated, not hand-written.
--reuse PREV_TOPICS.json PREV_NAMES.json carries a name over to any new topic sharing at least half its members with an old
one (Jaccard), so a nightly rebuild only asks the model about topics that actually changed.
"""
import argparse
import asyncio
import json
from collections import Counter
from pathlib import Path

from pydantic import BaseModel, Field


class Name(BaseModel):
    name: str = Field(description="2 to 5 plain words naming the subject, no jargon fragments, no 'discussion of'.")


async def name_one(model, items, parent=None):
    from llm_client import acall_llm_structured
    body = "\n".join(f'- idea: {i["target"][:160]} | Brian: "{i["quote"][:200]}"' for i in items)
    if parent:
        body = f"These statements are one subtopic of the broader topic \"{parent}\". Name what sets this subtopic apart.\n\n" + body
    out, _ = await acall_llm_structured(
        model, [{"role": "system", "content": "Name the common subject of these quoted statements so the name tells a reader what they are about."},
                {"role": "user", "content": body}],
        response_model=Name, reasoning_effort="low", model_policy="enforce_allowlist", task="topic-name", trace_id="inquiry-graph/name-topics", max_budget=1.0,
        **({"codex_transport": "cli", "sandbox_mode": "read-only", "approval_policy": "never", "working_directory": str(Path("private/ask_cwd").resolve()),
            "model_justification": "Brian's Codex subscription for private topic names (2026-10-03)."} if model.startswith("codex/") else {}))
    return out.name


def parents(topics):
    """Nested layers (EVoC, finest first: L0, L1, ...): each topic's parent is the next-coarser topic holding most of its members."""
    layers = sorted({t["layer"] for t in topics}, key=lambda l: int(l[1:]) if l[1:].isdigit() else 0)
    up = {}
    for fine, coarse in zip(layers, layers[1:]):
        owner = {m: t["topic"] for t in topics if t["layer"] == coarse for m in t["members"]}
        for t in topics:
            if t["layer"] == fine:
                votes = Counter(owner[m] for m in t["members"] if m in owner)
                if votes:
                    up[t["topic"]] = votes.most_common(1)[0][0]
    return layers, up


def carry_names(topics, old_topics, old_names, threshold=0.5):
    """{new topic id: old name} for each new topic whose members overlap an old named topic by Jaccard >= threshold."""
    old = [(set(t["members"]), old_names[t["topic"]]) for t in old_topics if t["topic"] in old_names]
    out = {}
    for t in topics:
        m = set(t["members"])
        best = max(((len(m & o) / len(m | o), name) for o, name in old if m | o), default=(0, None))
        if best[0] >= threshold:
            out[t["topic"]] = best[1]
    return out


async def main_async(a):
    recs = {r["id"]: r for r in json.loads(a.records.read_text())["records"]}
    topics = json.loads(a.topics.read_text())["topics"]
    names = json.loads(a.out.read_text()) if a.out.exists() else {}   # resume: keep names already written
    if a.reuse:
        carried = carry_names(topics, json.loads(a.reuse[0].read_text())["topics"], json.loads(a.reuse[1].read_text()))
        names = {**carried, **names}
        print(f"carried {len(carried)} of {len(topics)} names from the previous build", flush=True)
    layers, up = parents(topics)
    sem = asyncio.Semaphore(a.concurrency)

    async def one(t):
        if str(t["topic"]) in names:
            return
        members = [recs[i] for i in t["members"] if i in recs][:14]
        async with sem:
            try:
                names[str(t["topic"])] = await name_one(a.model, members, names.get(up.get(t["topic"])))
            except Exception as e:   # one failed topic keeps its keyword name; say so instead of stopping the run
                print(f"FAILED {t['topic']}: {type(e).__name__}: {str(e)[:200]}", flush=True)
                return
        print(t["topic"], t["size"], names[str(t["topic"])], flush=True)
        a.out.write_text(json.dumps(names, indent=1))

    for layer in reversed(layers):   # broadest first, so each subtopic is named knowing its parent
        group = [t for t in topics if t["layer"] == layer]
        await asyncio.gather(*(one(t) for t in group))
    a.out.write_text(json.dumps(names, indent=1))
    print(f"named {len(names)} of {len(topics)} topics", flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("records", type=Path)
    ap.add_argument("topics", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--model", default="codex/gpt-5.6-luna", help="Codex subscription by default (no OpenRouter spend, per Brian 2026-10-11)")
    ap.add_argument("--concurrency", type=int, default=6)
    ap.add_argument("--reuse", nargs=2, type=Path, metavar=("PREV_TOPICS", "PREV_NAMES"), help="carry names over from a previous build")
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
