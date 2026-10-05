"""One person's positions and questions from an extracted meeting graph, each quote re-checked.

Usage: meeting_positions.py <meeting.graph.json> --speaker "<name>" [--json]
Prints only stance and question events whose actor is that speaker and whose quote is found verbatim in a
message that speaker wrote. Counts what was shown, and fails (exit 1) if any event attributed to the speaker
does not pass that check, so a mis-attributed quote can never be printed as theirs. Output is private.
"""
import argparse
import json
import sys
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("graph", type=Path)
    ap.add_argument("--speaker", required=True)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    g = json.loads(a.graph.read_text(encoding="utf-8"))
    conv = g["conversations"][0]
    people = {p["id"]: p["label"] for p in conv["participants"]}
    want = [pid for pid, label in people.items() if label.lower().startswith(a.speaker.lower())]
    if len(want) != 1:
        print(f"meeting_positions: speaker {a.speaker!r} matches {len(want)} participants: {sorted(people.values())}", file=sys.stderr)
        return 2
    pid = want[0]
    msgs = {m["id"]: m for m in conv["messages"]}
    nodes = {n["id"]: n for n in g["nodes"]}
    rows, bad = [], []
    for kind, field in (("stance", "stance_events"), ("question", "question_events")):
        for e in g.get(field, []):
            if e["actor_id"] != pid:
                continue
            for an in e["anchors"]:
                m = msgs[an["message_id"]]
                q = an["quote"]
                ok = m["actor_id"] == pid and m["text"][an["start"]:an["end"]] == q
                (rows if ok else bad).append({"kind": kind, "what": e.get("stance") or e.get("status"),
                                              "idea": nodes.get(e.get("target_id") or e.get("question_id"), {}).get("text", ""),
                                              "quote": q, "turn": m["original_id"], "message": m["id"]})
    if a.json:
        print(json.dumps({"speaker": people[pid], "shown": rows, "failed_check": bad}, indent=1))
    else:
        print(f"{people[pid]}: {len(rows)} positions and questions in {conv['title']} (each quote verbatim in a message {people[pid]} wrote)")
        for r in rows:
            print(f"- {r['turn']} {r['kind']} {r['what']}: “{r['quote']}” — {r['idea'][:120]}")
    print(json.dumps({"speaker": people[pid], "shown": len(rows), "failed_check": len(bad)}), file=sys.stderr)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
