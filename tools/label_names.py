"""Name each topic cluster in plain words from its member chat titles, via the shared LLM client.

Input: layer_<k>_clusters.json files from atlas_map.py --layers ({cluster_id: {keywords, titles}}).
Output: {layer_size: {cluster_id: name}}. A cluster the model cannot name specifically gets no entry and
shows as Unlabelled, so a vague tag never reaches the map. Only titles of chats already filtered as interests are sent.
"""
import argparse
import asyncio
import json
import re
from pathlib import Path

from pydantic import BaseModel, Field

from llm_client import acall_llm_structured, get_model

MODEL = get_model("synthesis")  # the shared client's configured model for this kind of task
SYSTEM = (
    "You label clusters of chat titles for a map of a person's intellectual interests. Give each cluster a plain-language "
    "name of 2 to 5 words that tells a stranger what the chats are ABOUT, for example 'Knowledge graphs and ontologies', "
    "'Cold War intelligence history', 'Designing AI agent systems'. Never output a bare keyword list, a tool name alone, "
    "or a vague word like 'Paper', 'Approx' or 'Review'. If the titles do not share a specific subject, set specific=false."
)


class Name(BaseModel):
    name: str = Field(description="2-5 word plain-language subject name")
    specific: bool = Field(description="true only if the titles share one clear subject")


async def name_one(layer, cid, entry, sem):
    titles = entry["titles"][:20]
    user = f"Keyword hint (may be misleading): {entry['keywords']}\nChat titles ({len(entry['titles'])} total, showing {len(titles)}):\n" + "\n".join(f"- {t}" for t in titles)
    async with sem:
        out, _ = await acall_llm_structured(MODEL, [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
                                            response_model=Name, reasoning_effort="low", model_policy="enforce_allowlist", task="map-label-naming", trace_id=f"label-names/{layer}/{cid}", max_budget=0.05)
    return layer, cid, out


async def main_async(a):
    sem = asyncio.Semaphore(1)  # sequential: parallel calls hit llm_client issue #232
    jobs, result = [], {}
    for f in sorted(a.clusters):
        layer = re.search(r"layer_(\d+)_clusters", f.name).group(1)
        for cid, entry in json.loads(f.read_text(encoding="utf-8")).items():
            jobs.append(name_one(layer, cid, entry, sem))
    for coro in jobs:
        layer, cid, out = await coro
        if out.specific and len(out.name.split()) <= 7:
            result.setdefault(layer, {})[cid] = out.name.strip()
    return result, len(jobs)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("clusters", nargs="+", type=Path)
    ap.add_argument("out", type=Path)
    a = ap.parse_args()
    res, n = asyncio.run(main_async(a))
    a.out.write_text(json.dumps(res, indent=1), encoding="utf-8")
    print(json.dumps({"clusters": n, "named": sum(len(v) for v in res.values())}))


if __name__ == "__main__":
    main()
