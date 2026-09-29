"""Reference key for the cross-conversation goal (C2), built independently of the system.

It never uses inquiry-graph's extractor or onto-canon6. A model reads each whole
chat and lists Brian's positions and open questions, each with a verbatim quote
from one of Brian's own messages. Code checks every quote and drops any that is
not found. A second pass compares the verified per-chat lists and writes
cross-chat questions whose answers cite position ids.

Outputs go to private/xconv/key/ (they quote private chats).
"""
import json
import sys
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field
from llm_client import call_llm_structured, get_model

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
from inquiry_graph.live_extract import locate  # noqa: E402  (pure text matcher, no extraction)
from inquiry_graph.model import Conversation  # noqa: E402

PRIV = ROOT / "private/xconv"
OUT = PRIV / "key"
CHATS = ["6ab8563b", "6ab96260", "69c07755", "6a988a7a", "6a171ac3"]
MODEL = get_model("synthesis")
COMMON = dict(model_policy="enforce_allowlist", max_budget=4.00)


class Position(BaseModel):
    kind: Literal["position", "open_question"]
    statement: str = Field(description="self-contained statement of Brian's position or open question")
    stance: Literal["asserts", "leans_toward", "rejects", "asks", "uncertain"]
    message: int = Field(description="number [n] of Brian's message")
    quote: str = Field(description="exact verbatim span (5-30 words) from that Brian message")


class ChatPositions(BaseModel):
    positions: list[Position]


class CrossItem(BaseModel):
    category: Literal["agreement_across_chats", "conflict_or_tension", "recurring_open_question",
                      "change_over_time", "position_summary"]
    question: str = Field(description="a question an AI assistant to Brian might be asked, naming its topic concretely")
    answer_key: str
    key_points: list[str] = Field(description="2-4 atomic facts a correct answer must contain")
    position_ids: list[str] = Field(description="ids of the positions that support the key, from at least 2 chats where the category requires it")


class CrossKey(BaseModel):
    items: list[CrossItem]


def render(conv: Conversation) -> str:
    label = {p.id: ("BRIAN" if p.role == "user" else "ASSISTANT") for p in conv.participants}
    return "\n\n".join(f"[{m.ordinal}] {label[m.actor_id]}:\n{m.text}" for m in conv.messages)


def per_chat(cid: str) -> dict:
    path = OUT / f"{cid}.positions.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    conv = Conversation.model_validate_json((PRIV / f"{cid}.conv.json").read_text(encoding="utf-8"))
    prompt = f"""Read this entire conversation between BRIAN and an ASSISTANT ("{conv.title}").
List Brian's own substantive positions and open questions about ideas (not work instructions such as
"proceed", "write the doc", "review the repo"). Include positions he asserts, leans toward, rejects or is
uncertain about, and questions he raised that the conversation did not settle. An assistant proposal counts
only if Brian's own message takes a position on it. Each item needs the number of Brian's message and an
exact verbatim quote (5-30 words) from that message. Aim for the 10-25 most important items.

CONVERSATION:
{render(conv)}"""
    res, meta = call_llm_structured(MODEL, [{"role": "user", "content": prompt}], response_model=ChatPositions,
                                    reasoning_effort="high", task="synthesis",
                                    trace_id=f"inquiry-graph/xconv-key/positions/{cid}", **COMMON)
    brian = {m.ordinal: m for m in conv.messages if m.actor_id.endswith("brian")}
    kept, dropped = [], []
    for i, p in enumerate(res.positions):
        msg = brian.get(p.message)
        spans = locate(msg.text, p.quote) if msg else []
        rec = {**p.model_dump(), "id": f"{cid}:p{i:02d}", "chat": cid, "chat_title": conv.title}
        if spans:
            rec["verified_quote"] = spans[0]
            kept.append(rec)
        else:
            dropped.append(rec)
    data = {"chat": cid, "title": conv.title, "kept": kept, "dropped": dropped, "cost": meta.cost,
            "trace_id": f"inquiry-graph/xconv-key/positions/{cid}"}
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{cid}: {len(kept)} positions kept, {len(dropped)} dropped (quote not in a Brian message); ${meta.cost:.3f}")
    return data


def cross(all_positions: list[dict]) -> dict:
    path = OUT / "cross_key.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    listing = "\n".join(f"{p['id']} | chat \"{p['chat_title']}\" | {p['kind']}/{p['stance']} | {p['statement']}"
                        for chat in all_positions for p in chat["kept"])
    prompt = f"""Below are Brian's verified positions and open questions from 5 of his conversations.
Write 12 questions an AI assistant to Brian might be asked about his views ACROSS these conversations:
- 3 agreement_across_chats: the same view expressed in two or more chats;
- 3 conflict_or_tension: views in different chats that pull against each other (say how);
- 2 recurring_open_question: a question he raises in more than one chat and never settles;
- 2 change_over_time: a view that shifts between chats (chats span March to September 2026);
- 2 position_summary: his overall position on a named topic, drawing on several chats.
Each answer must be supported by the listed position ids (from at least 2 different chats, except
position_summary may use 1 chat if only one addresses it). Do not use outside knowledge.

POSITIONS (id | chat | kind/stance | statement):
{listing}"""
    res, meta = call_llm_structured(MODEL, [{"role": "user", "content": prompt}], response_model=CrossKey,
                                    reasoning_effort="high", task="synthesis",
                                    trace_id="inquiry-graph/xconv-key/cross", **COMMON)
    known = {p["id"]: p for chat in all_positions for p in chat["kept"]}
    kept, dropped = [], []
    for it in res.items:
        ids = [i for i in it.position_ids if i in known]
        chats = {known[i]["chat"] for i in ids}
        needs_two = it.category != "position_summary"
        ok = ids and len(ids) == len(it.position_ids) and (len(chats) >= 2 or not needs_two)
        (kept if ok else dropped).append({**it.model_dump(), "chats": sorted(chats)})
    data = {"kept": kept, "dropped": dropped, "cost": meta.cost, "trace_id": "inquiry-graph/xconv-key/cross"}
    path.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"cross key: {len(kept)} items kept, {len(dropped)} dropped (unknown ids or single-chat); ${meta.cost:.3f}")
    return data


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    per = [per_chat(c) for c in CHATS]
    cross(per)


if __name__ == "__main__":
    main()
