"""Normalize chats from ChatGPT's official data export (conversations-NNN.json, mapping-tree format) into Conversation records.

Usage: normalize_chatgpt_export.py <conversations_dir> <ids.json> <out_dir> [--min-chars 200]
Only the ids in <ids.json> (a JSON list of bare conversation ids) are processed. Writes <out_dir>/chatgpt-<id>.conv.json,
dispositions.jsonl (one line per id: normalized | failed | missing_from_export), skipped_too_short.json (Brian wrote fewer than
--min-chars; same rule as the Claude export), titles.json (id, title, first user message: input to tools/interest_filter.py) and
queue.json (normalized, not too short; input to tools/extract_queue.py). Active branch only (src/inquiry_graph/io.py:import_export).
Ids are `chatgpt:<id>`, the same form the exporter normalizer uses.
"""
import argparse
import collections
import json
from pathlib import Path

from inquiry_graph.io import import_export
from inquiry_graph.model import Conversation, Graph, Message, Participant
from inquiry_graph.validate import require_valid


def parse_chatgpt_conversation(raw: dict, user_label: str = "Brian") -> Conversation:
    """One export entry -> Conversation with participant:brian / participant:assistant, like the Claude and exporter normalizers."""
    src = import_export(raw)[0]
    cid = f"chatgpt:{src.id}"
    user_id, assistant_id = f"participant:{user_label.lower()}", "participant:assistant"
    messages = []
    for m in src.messages:
        role = user_id if m.actor_id.endswith(":actor:user") else assistant_id
        ordinal = len(messages) + 1
        messages.append(Message(id=f"{cid}:msg{ordinal:04d}", ordinal=ordinal, text=m.text, original_id=m.original_id,
                                timestamp=m.timestamp, actor_id=role))
    if not messages:
        raise ValueError(f"{cid}: no visible user or assistant text")
    return Conversation(
        id=cid, title=(src.title or "").strip() or "(untitled)", source_kind="normalized",
        coverage_note="ChatGPT official data export; " + src.coverage_note,
        participants=[Participant(id=user_id, label=user_label, role="user"), Participant(id=assistant_id, label="Assistant", role="assistant")],
        messages=messages)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conversations_dir", type=Path)
    ap.add_argument("ids", type=Path)
    ap.add_argument("out_dir", type=Path)
    ap.add_argument("--min-chars", type=int, default=200)
    a = ap.parse_args()
    a.out_dir.mkdir(parents=True, exist_ok=True)
    want = set(json.loads(a.ids.read_text()))
    disp, short, titles, queue, seen = [], [], [], [], set()
    for f in sorted(a.conversations_dir.glob("conversations-*.json")):
        for raw in json.loads(f.read_text(encoding="utf-8")):
            uid = raw.get("id") or raw.get("conversation_id")
            if uid not in want or uid in seen:
                continue
            seen.add(uid)
            try:
                conv = parse_chatgpt_conversation(raw)
                require_valid(Graph(id="import-check", conversations=[conv]))
                path = a.out_dir / f"chatgpt-{uid}.conv.json"
                path.write_text(conv.model_dump_json(indent=1), encoding="utf-8")
                mine = [m.text for m in conv.messages if m.actor_id == "participant:brian"]
                chars = sum(len(t) for t in mine)
                disp.append({"id": conv.id, "status": "normalized", "brian_chars": chars})
                titles.append({"id": conv.id, "title": conv.title, "first": (mine[0] if mine else "")[:350]})
                item = {"id": conv.id, "file": str(path.resolve()), "brian_chars": chars}
                (queue if chars >= a.min_chars else short).append(item)
            except Exception as e:
                disp.append({"id": f"chatgpt:{uid}", "status": "failed", "error": f"{type(e).__name__}: {str(e)[:200]}"})
    for uid in sorted(want - seen):
        disp.append({"id": f"chatgpt:{uid}", "status": "missing_from_export"})
    with open(a.out_dir / "dispositions.jsonl", "w", encoding="utf-8") as fh:
        for d in disp:
            fh.write(json.dumps(d) + "\n")
    for name, obj in [("skipped_too_short.json", short), ("titles.json", titles), ("queue.json", queue)]:
        (a.out_dir / name).write_text(json.dumps(obj, indent=1), encoding="utf-8")
    print(json.dumps({"requested": len(want), **collections.Counter(d["status"] for d in disp),
                      "skipped_too_short": len(short), "queue": len(queue)}))


if __name__ == "__main__":
    main()
