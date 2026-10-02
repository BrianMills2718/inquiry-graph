"""Write a Gource custom log that animates the chat archive growing over time.

Each chat is a file placed under its topic directory. It is added when its first message is sent and
touched again at each later message. Gource users are the speakers (the human, the assistant). Chats in the
exporter's agent-send log are excluded. Topics come from a chats.json written by topic_map_archive.py.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

PALETTE = ["E6194B", "3CB44B", "FFE119", "4363D8", "F58231", "911EB4", "46F0F0", "F032E6", "BCF60C", "FABEBE",
           "008080", "E6BEFF", "9A6324", "FFFAC8", "800000", "AAFFC3", "808000", "FFD8B1", "000075", "A9A9A9"]


def clean(s: str) -> str:
    return re.sub(r"[|/\\]+", "-", s).strip()[:40] or "untitled"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("conv_dir", type=Path)
    ap.add_argument("topics_dir", type=Path, help="dir with chats.json and topics.json from topic_map_archive.py")
    ap.add_argument("agent_log", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--no-assistant", action="store_true")
    a = ap.parse_args()
    agent = set()
    for line in a.agent_log.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            t = json.loads(line).get("thread_id")
        except json.JSONDecodeError:
            continue
        if t:
            agent.add(t)
    chats = {c["chat"]: c for c in json.loads((a.topics_dir / "chats.json").read_text())}
    names = {t["topic"]: t["name"] for t in json.loads((a.topics_dir / "topics.json").read_text())}
    # Index by the conversation's own id, not its filename: the WEB-/WEB: filename mismatch must not hide a chat.
    paths = {json.loads(f.read_text(encoding="utf-8"))["id"]: f for f in a.conv_dir.glob("*.conv.json")}
    rows, kept = [], 0
    for cid, c in chats.items():
        if cid.split(":", 1)[1] in agent:
            continue
        conv = json.loads(paths[cid].read_text(encoding="utf-8"))
        user = {p["id"] for p in conv["participants"] if p["role"] == "user"}
        topic = clean(names.get(c["topic"], "unclustered")) if c["topic"] != -1 else "unclustered"
        color = PALETTE[(c["topic"] + 1) % len(PALETTE)]
        path = f"{topic}/{clean(c['title'])}-{cid[-4:]}"
        first = True
        for m in conv["messages"]:
            if not m.get("timestamp"):
                continue
            human = m["actor_id"] in user
            if not human and a.no_assistant:
                continue
            ts = int(dt.datetime.fromisoformat(m["timestamp"].replace("Z", "+00:00")).timestamp())
            rows.append((ts, "Brian" if human else "Assistant", "A" if first else "M", path, color))
            first = False
        kept += 1
    rows.sort()
    a.out.write_text("\n".join("|".join(map(str, r)) for r in rows) + "\n", encoding="utf-8")
    print(json.dumps({"chats": kept, "events": len(rows), "excluded_agent": sum(1 for c in chats if c.split(':', 1)[1] in agent)}))


if __name__ == "__main__":
    main()
