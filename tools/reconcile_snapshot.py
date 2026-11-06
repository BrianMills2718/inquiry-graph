"""C1 reconciliation: give every conversation from every source exactly one disposition, and check the totals add up.

Usage: reconcile_snapshot.py OUT.json   (paths below are the private inventory layout; override with flags)
Sources: ChatGPT exporter raw files, Kept vault files. Dispositions:
  failed_no_visible_text | excluded_agent_sent (thread id in the bridge agent-send log: the "user" turns are agents) |
  excluded_interest_filter:<category> | skipped_too_short (<200 chars of Brian text) | extracted_with_events |
  extracted_no_brian_events | extraction_failed | included_not_queued (passed the filter, never queued, no recorded reason) | pending | duplicate_of_exporter (Kept copy of a ChatGPT chat already counted).
Quote-free: only ids, titles' absence, counts. Exit status 1 if any conversation lacks a disposition or totals do not reconcile.
"""
import argparse
import collections
import glob
import json
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1] / "private"


def classify(cid, *, failed, agent, flt, short, graphs, failed_extract, events, queued=None):
    if cid in failed:
        return "failed_no_visible_text"
    if cid in agent:
        return "excluded_agent_sent"
    if cid in graphs:   # extracted later (e.g. the low-confidence rerun) even if the filter first excluded it
        return "extracted_with_events" if events.get(cid, 0) else "extracted_no_brian_events"
    if cid in flt and not flt[cid]["include"]:
        return "excluded_interest_filter:" + flt[cid]["category"]
    if cid in short:   # before "not filtered": short chats skip the filter (the 2026-11-05 export's 1,779)
        return "skipped_too_short"
    if cid not in flt:
        return "pending"   # not yet filtered (e.g. synced after the last filter run)
    if cid in failed_extract:
        return "extraction_failed"
    if queued is not None and cid not in queued:
        return "included_not_queued"   # no recorded reason: not proof it was too short
    return "pending"


def add_official_export(rows, disp, **cls):
    """Count each normalized official-export chat once; a chat already counted from another source is a duplicate."""
    for r in disp:
        cid = r["id"]
        if r["status"] != "normalized":
            rows["officialexport:" + cid] = "failed_no_visible_text"
        elif cid in rows:
            rows["officialexport:" + cid] = "duplicate_of_exporter"
        else:
            rows[cid] = classify(cid, failed=set(), agent=set(), **cls)


def jl(p):
    """Read a JSONL log. Blank lines and lines a crash left half-written (e.g. NUL bytes) are
    skipped and counted on stderr, so one damaged line cannot stop the whole coverage count."""
    if not Path(p).exists():
        return []
    rows, damaged = [], 0
    for x in open(p, errors="replace"):
        try:
            rows.append(json.loads(x))
        except json.JSONDecodeError:
            damaged += 1
    if damaged:
        print(f"{p}: {damaged} damaged line(s) skipped", file=sys.stderr)
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("out", type=Path)
    a = ap.parse_args()
    norm = json.loads((R / "archive-inventory/normalized_20261003/dispositions.json").read_text())
    kept = json.loads((R / "kept_normalized_20261003/dispositions.json").read_text())
    agent = set()
    for l in open(Path.home() / "code/chatgpt-conversation-manager-v0.2/data/observations/bridge-events.jsonl", errors="replace"):
        try:
            e = json.loads(l.replace("\x00", ""))
        except Exception:
            continue
        if e.get("thread_id"):
            agent.add("chatgpt:" + e["thread_id"])
    flt = {}
    for f in ["archive-inventory/public_filter/interest_v2_nolegal.json", "kept_normalized_20261003/interest.json", "extract_full_20261003/new108/interest.json", "claude_export_normalized_20261004/interest.json", "extract_full_20261003/chatgpt_export_20261105/interest.json"]:
        for x in json.loads((R / f).read_text()):
            flt[x["id"]] = x
    short = set()
    for f in ["extract_full_20261003/skipped_too_short.json", "extract_full_20261003/kept/skipped_too_short.json", "extract_full_20261003/new108/skipped_too_short.json", "extract_full_20261003/claude_export/skipped_too_short.json", "extract_full_20261003/chatgpt_export_20261105/skipped_too_short.json"]:
        short |= {x["id"] for x in json.loads((R / f).read_text())} if (R / f).exists() else set()
    # the ChatGPT queue builder skipped short chats without writing a file: recompute from the queue
    queued = set()
    for q in ["extract_full_20261003/queue.json", "extract_full_20261003/kept/queue.json", "extract_full_20261003/new108/queue.json", "extract_full_20261003/lowconf/queue.json", "extract_full_20261003/claude_export/queue.json", "extract_full_20261003/chatgpt_export_20261105/queue.json"]:
        queued |= {x["id"] for x in json.loads((R / q).read_text())}
    graphs, events, failed_extract = set(), collections.Counter(), set()
    gdirs = ["extract_full_20261003/out", "extract_full_20261003/kept/out", "extract_full_20261003/new108/out", "extract_full_20261003/single/out", "extract_full_20261003/claude_export/out", "extract_full_20261003/or_run/out", "extract_full_20261003/lowconf/out", "extract_test_20261003/out", "extract_full_20261003/chatgpt_export_20261105/run/out"]
    for d in gdirs:
        for f in glob.glob(str(R / d / "*.graph.json")):
            g = json.loads(Path(f).read_text())
            cid = g["conversations"][0]["id"]
            graphs.add(cid)
            events[cid] = sum(1 for k in ("stance_events", "question_events") for e in g[k] if e["actor_id"] == "participant:brian")
    for d in ["extract_full_20261003", "extract_full_20261003/kept", "extract_full_20261003/new108", "extract_full_20261003/single", "extract_full_20261003/lowconf", "extract_full_20261003/claude_export", "extract_full_20261003/chatgpt_export_20261105/run", "extract_full_20261003/or_run"]:
        failed_extract |= {r["id"] for r in jl(R / d / "dispositions.jsonl") if r["status"] == "failed"}
    rows = {}
    for k, v in norm.items():
        cid = "chatgpt:" + k.removeprefix("chatgpt:")
        if v["status"] == "failed":
            cid = "chatgpt:" + k
        rows[cid] = classify(cid, failed={"chatgpt:" + k for k, v in norm.items() if v["status"] == "failed"}, agent=agent, flt=flt,
                             short=short, queued=queued,
                             graphs=graphs, failed_extract=failed_extract, events=events)
    for k, v in kept.items():
        if v["status"] == "duplicate_of_exporter":
            rows["kept:" + k] = "duplicate_of_exporter"
        elif v["status"] == "failed":
            rows["kept:" + k] = "failed_no_visible_text"
        elif v["id"] in rows:   # Kept copy of a ChatGPT chat the exporter now also has
            rows["kept:" + k] = "duplicate_of_exporter"
        else:
            cid = v["id"]
            rows[cid] = classify(cid, failed=set(), agent=set(), flt=flt, short=short, queued=queued,
                                 graphs=graphs, failed_extract=failed_extract, events=events)
    cx = json.loads((R / "claude_export_normalized_20261004/dispositions.json").read_text())
    for uid, v in cx.items():
        key = "claude:" + uid
        if v["status"] == "failed":
            rows["claudeexport:" + uid] = "failed_no_visible_text"
        elif key in rows:   # the Kept copy of this chat is already counted; its graph (if any) serves both
            rows["claudeexport:" + uid] = "duplicate_of_kept"
        else:
            rows[key] = classify(key, failed=set(), agent=set(), flt=flt, short=short, queued=queued,
                                 graphs=graphs, failed_extract=failed_extract, events=events)
    # ChatGPT official export of 2026-11-05: only the chats the exporter never captured were normalized (inquiry-graph#239)
    ox = jl(R / "extract_full_20261003/chatgpt_export_20261105/dispositions.jsonl")
    add_official_export(rows, ox, flt=flt, short=short, queued=queued, graphs=graphs, failed_extract=failed_extract, events=events)
    by = collections.Counter(rows.values())
    sources = {"chatgpt_raw_files": len(norm), "kept_files": len(kept), "claude_export_conversations": len(cx), "chatgpt_official_export_20261105_only": len(ox)}
    ok = len(rows) == sum(sources.values())
    out = {"sources": sources, "conversations_with_disposition": len(rows), "reconciles": ok, "by_disposition": dict(by.most_common()), "dispositions": rows,
           "note": "Claude: official export ingested (819 normalized of 848). ChatGPT official export 2026-11-05: its 5,971 chats the exporter lacked are counted. Gemini official export: not yet ingested."}
    a.out.write_text(json.dumps(out, indent=1))
    print(json.dumps({k: out[k] for k in ("sources", "conversations_with_disposition", "reconciles", "by_disposition")}, indent=1))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
