"""Export Brian-attributed position/question events from per-chat graphs as one records.json (quote-bearing: keep under private/).

Usage: position_records.py OUT.json GRAPH_DIR [GRAPH_DIR ...]
Same evidence rule as ask_positions.py (speaker == actor, quote verbatim in that message); duplicates of one
(message, quote) are kept once. Also writes the per-chat disposition table: chats with graphs and how many events each gave.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from ask_positions import records  # noqa: E402


def main():
    out, dirs = Path(sys.argv[1]), [Path(d) for d in sys.argv[2:]]
    seen, recs = set(), []
    for r in records(dirs):
        k = (r["message_id"], r["quote"])
        if k not in seen:
            seen.add(k)
            recs.append(r)
    chats = {}
    for r in recs:
        chats[r["chat"]] = chats.get(r["chat"], 0) + 1
    out.write_text(json.dumps({"records": recs, "events_per_chat": chats}, indent=1), encoding="utf-8")
    print(json.dumps({"records": len(recs), "chats_with_events": len(chats)}))


if __name__ == "__main__":
    main()
