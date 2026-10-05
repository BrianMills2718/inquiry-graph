"""Give each position-map topic a short plain-language name from its member quotes (Codex subscription route).

Usage: name_topics.py RECORDS.json TOPICS.json OUT_NAMES.json [--model M]
Sends up to 14 members per topic (idea + Brian's quote) and asks for a 2-5 word name that says what the topic is about.
Output {topic_id: name}; position_topics.py --names uses it. Names are generated, not hand-written.
"""
import argparse
import asyncio
import json
from pathlib import Path

from pydantic import BaseModel, Field


class Name(BaseModel):
    name: str = Field(description="2 to 5 plain words naming the subject, no jargon fragments, no 'discussion of'.")


async def name_one(model, items):
    from llm_client import acall_llm_structured
    body = "\n".join(f'- idea: {i["target"][:160]} | Brian: "{i["quote"][:200]}"' for i in items)
    out, _ = await acall_llm_structured(
        model, [{"role": "system", "content": "Name the common subject of these quoted statements so the name tells a reader what they are about."},
                {"role": "user", "content": body}],
        response_model=Name, reasoning_effort="low", model_policy="enforce_allowlist", task="topic-name", trace_id="inquiry-graph/name-topics", max_budget=1.0,
        **({"codex_transport": "cli", "sandbox_mode": "read-only", "approval_policy": "never", "working_directory": str(Path("private/ask_cwd").resolve()),
            "model_justification": "Brian's Codex subscription for private topic names (2026-10-03)."} if model.startswith("codex/") else {}))
    return out.name


async def main_async(a):
    recs = {r["id"]: r for r in json.loads(a.records.read_text())["records"]}
    topics = json.loads(a.topics.read_text())["topics"]
    names = {}
    for t in topics:
        names[str(t["topic"])] = await name_one(a.model, [recs[i] for i in t["members"][:14]])
        print(t["topic"], t["size"], names[str(t["topic"])], flush=True)
    a.out.write_text(json.dumps(names, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("records", type=Path)
    ap.add_argument("topics", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--model", default="openrouter/openai/gpt-5.6-luna")
    asyncio.run(main_async(ap.parse_args()))


if __name__ == "__main__":
    main()
