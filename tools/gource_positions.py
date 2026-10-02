"""Gource log of how Brian's positions grow and change, from Inquiry Graph extractions.

Directory = topic (named by the topic map), file = one position/question node. A node appears (A) when Brian
first takes a stance on it, and is touched (M) at each later stance. Colour is the stance: posits green,
endorses blue, questions yellow, rejects red, retracts/suspends grey. Captions mark each topic's first
appearance and the open questions he raises. Only stance events by the user participant are used.
"""
import argparse
import datetime as dt
import json
import re
from pathlib import Path

COLOR = {"posits": "3CB44B", "endorses": "4363D8", "questions": "FFE119", "rejects": "E6194B",
         "retracts": "A9A9A9", "suspends": "A9A9A9"}


def clean(s, n=36):
    return (re.sub(r"[|/\\\r\n]+", " ", s).strip()[:n] or "untitled")


def epoch(ts):
    return int(dt.datetime.fromisoformat(ts.replace("Z", "+00:00")).timestamp())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("graph_dir", type=Path)
    ap.add_argument("map_dir", type=Path, help="dir with communities.json and topic_names.json")
    ap.add_argument("out_log", type=Path)
    ap.add_argument("out_captions", type=Path)
    a = ap.parse_args()
    groups = json.loads((a.map_dir / "communities.json").read_text())["groups"]
    names = {n["topic"]: n["name"] for n in json.loads((a.map_dir / "topic_names.json").read_text())["names"]}
    topic_of = {nid: names.get(i + 1, f"topic-{i + 1}") for i, g in enumerate(groups) for nid in g}
    rows, first_seen, questions, missing = [], {}, [], 0
    for f in sorted(a.graph_dir.glob("*.graph.json")):
        g = json.loads(f.read_text(encoding="utf-8"))
        conv = g["conversations"][0]
        user = {p["id"] for p in conv["participants"] if p["role"] == "user"}
        when = {m["id"]: m.get("timestamp") for m in conv["messages"]}
        nodes = {n["id"]: n for n in g["nodes"]}
        seen = set()
        for e in sorted(g["stance_events"], key=lambda e: when.get(e["at_message_id"]) or ""):
            ts, n = when.get(e["at_message_id"]), nodes.get(e["target_id"])
            if e["actor_id"] not in user or not ts or n is None or e["target_id"] not in topic_of:
                missing += 1
                continue
            topic = topic_of[e["target_id"]]
            path = f"{clean(topic, 28)}/{n['kind']}/{clean(n['text'])}-{e['target_id'][-4:]}"
            t = epoch(ts)
            rows.append((t, "Brian", "M" if e["target_id"] in seen else "A", path, COLOR.get(e["stance"], "FFFFFF")))
            seen.add(e["target_id"])
            first_seen.setdefault(topic, t)
            if e["stance"] == "questions" and n["kind"] == "question":
                questions.append((t, "Open question: " + clean(n["text"], 70)))
    rows.sort()
    a.out_log.write_text("\n".join("|".join(map(str, r)) for r in rows) + "\n", encoding="utf-8")
    caps = [(t, f"New topic: {name}") for name, t in first_seen.items()] + questions[::6]
    a.out_captions.write_text("\n".join(f"{t}|{c}" for t, c in sorted(caps)) + "\n", encoding="utf-8")
    print(json.dumps({"events": len(rows), "topics": len(first_seen), "captions": len(caps), "skipped_stance_events": missing,
                      "first": dt.datetime.fromtimestamp(rows[0][0]).isoformat(), "last": dt.datetime.fromtimestamp(rows[-1][0]).isoformat()}))


if __name__ == "__main__":
    main()
