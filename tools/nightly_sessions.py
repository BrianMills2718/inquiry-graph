"""Nightly: import coding sessions changed since yesterday, rebuild the private positions map, write the open-work reminder.

Usage: nightly_sessions.py [--since-hours 30] [--recent-days 3] [--skip-map]
Steps, each timed in the log (one file per day under private/logs/):
  1. import-session every Claude Code / Codex session file modified in the window into private/coding-sessions/rolling/
     (a malformed file is counted and skipped, not fatal);
  2. rebuild the positions map, carry topic names over from the previous build and name only new topics, rebuild with names;
  3. write private/coding-sessions/recent.md: for sessions active in the last few days, the goal, items still open,
     items whose status went unknown, and requests waiting on Brian. The start and where-are-we routines read it.
A failed step opens (or comments on) one keyed concern in BrianMills2718/inquiry-graph and exits non-zero.
The concern names only the step and exit status; private quotes never leave private/.
"""
import argparse
import datetime as dt
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[1]   # --data-root moves P, IG and PY (a worktree has no private/ or .venv)
P = ROOT / "private"
IG = ROOT / ".venv" / "bin" / "inquiry-graph"
PY = ROOT / ".venv" / "bin" / "python"                       # llm_client, for naming
MAPS_PY = Path.home() / ".venvs" / "inquiry-maps" / "bin" / "python"   # embeddings, EVoC, datamapplot
MAP = P / "xconv" / "positions_map"
NAMES = P / "xconv" / "positions_names.json"
CONCERN = Path.home() / "code" / "project-meta" / "scripts" / "concern_issue.py"


def log(msg):
    print(f"{dt.datetime.now().isoformat(timespec='seconds')} {msg}", flush=True)


def run(step, cmd):
    t = time.monotonic()
    r = subprocess.run([str(c) for c in cmd], cwd=P.parent, capture_output=True, text=True)
    log(f"{step}: exit {r.returncode} in {time.monotonic() - t:.0f}s")
    if r.returncode:
        log(f"{step} stderr tail:\n{r.stderr[-2000:]}")
        raise RuntimeError(f"{step} exited {r.returncode}")
    return r.stdout


def changed_sessions(hours):
    cut = time.time() - hours * 3600
    claude = [p for p in (Path.home() / ".claude" / "projects").glob("*/*.jsonl")]   # top level only; subagent files live in subfolders
    codex = list((Path.home() / ".codex" / "sessions").rglob("*.jsonl"))
    return sorted(p for p in claude + codex if p.stat().st_mtime >= cut)


def import_sessions(hours):
    out = P / "coding-sessions" / "rolling"
    ok = bad = 0
    for f in changed_sessions(hours):
        r = subprocess.run([str(IG), "import-session", str(f), str(out), "--force"], cwd=P.parent, capture_output=True, text=True)
        if r.returncode:
            bad += 1
            log(f"import skipped {f.name}: {(r.stderr.strip().splitlines() or ['?'])[-1][:200]}")
        else:
            ok += 1
    log(f"import: {ok} imported, {bad} skipped")
    if ok == 0 and bad:
        raise RuntimeError(f"import: every one of {bad} changed sessions failed")


def rebuild_map():
    prev_topics, prev_names = MAP / "topics.prev.json", NAMES.with_suffix(".prev.json")
    if (MAP / "topics.json").exists() and NAMES.exists():
        shutil.copy(MAP / "topics.json", prev_topics)
        shutil.copy(NAMES, prev_names)
    build = [MAPS_PY, TOOLS / "position_topics.py", P / "records_full.json", MAP, "--sessions", P / "coding-sessions"]
    run("map build", build)
    reuse = ["--reuse", prev_topics, prev_names] if prev_topics.exists() else []
    NAMES.unlink(missing_ok=True)   # names are keyed by this build's topic ids; carried ones come back through --reuse
    out = run("topic names", [PY, TOOLS / "name_topics.py", MAP / "records.json", MAP / "topics.json", NAMES, *reuse])
    failed = [l for l in out.splitlines() if l.startswith("FAILED")]
    log(f"topic names: {out.strip().splitlines()[-1] if out.strip() else '?'}; {len(failed)} failed (they keep keyword names)")
    run("map build with names", [*build, "--names", NAMES])


def recent_reminder(days):
    cut = time.time() - days * 86400
    graphs = sorted((p for p in (P / "coding-sessions").rglob("*.graph.json") if p.stat().st_mtime >= cut),
                    key=lambda p: p.stat().st_mtime, reverse=True)
    digests = json.loads(run("digest", [IG, "sessions", *graphs])) if graphs else []
    lines = [f"# Coding sessions active in the last {days} days", "",
             f"Built {dt.datetime.now():%Y-%m-%d %H:%M} by tools/nightly_sessions.py from {len(graphs)} imported sessions. "
             "Items come from each reply's closing fields; \"status unknown\" means an item dropped off the list with no closing word.", ""]
    seen = set()
    for d in digests:
        live = d["open"] + d["unknown_status"] + d["requests_open"]
        conv = d["conversations"][0]
        if not live or conv["id"] in seen:
            continue
        seen.add(conv["id"])
        lines += [f"## {conv['title'] or conv['id']}", f"{str(conv['from'])[:16]} to {str(conv['to'])[:16]}"]
        lines += [f"- Goal: {g}" for g in d["goals"][-1:]]
        lines += [f"- Open: {x}" for x in d["open"]]
        if d["unknown_status"]:   # often many near-repeats of older listings; the latest few are enough to jog memory
            lines.append(f"- Status unknown ({len(d['unknown_status'])}), latest: " + "; ".join(d["unknown_status"][-3:]))
        lines += [f"- Waiting on Brian: {x}" for x in d["requests_open"]]
        lines.append("")
    (P / "coding-sessions" / "recent.md").write_text("\n".join(lines), encoding="utf-8")
    log(f"reminder: {len(seen)} sessions with open items, from {len(graphs)} recent")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--since-hours", type=float, default=30)
    ap.add_argument("--recent-days", type=float, default=3)
    ap.add_argument("--skip-map", action="store_true", help="import and reminder only")
    ap.add_argument("--data-root", type=Path, help="checkout holding private/ and .venv (default: this script's checkout)")
    a = ap.parse_args()
    if a.data_root:
        global P, IG, PY, MAP, NAMES
        P, IG, PY = a.data_root / "private", a.data_root / ".venv/bin/inquiry-graph", a.data_root / ".venv/bin/python"
        MAP, NAMES = P / "xconv" / "positions_map", P / "xconv" / "positions_names.json"
    step = "import"
    try:
        import_sessions(a.since_hours)
        if not a.skip_map:
            step = "map"
            rebuild_map()
        step = "reminder"
        recent_reminder(a.recent_days)
        log("nightly: done")
    except Exception as e:
        log(f"nightly: FAILED at {step}: {e}")
        subprocess.run([sys.executable, str(CONCERN), "open", "--repo", "BrianMills2718/inquiry-graph", "--key", "inquiry-graph-nightly-sessions",
                        "--title", "Nightly coding-session import or map rebuild failed", "--source", "nightly-sessions",
                        "--body", f"Step `{step}` failed: {str(e)[:300]}. Full log: private/logs/nightly-{dt.date.today()}.log on Brian's laptop.",
                        "--occurrence", str(dt.date.today()), "--no-run-claim", "a scheduled import job failed; no model output graded"])
        sys.exit(1)


if __name__ == "__main__":
    main()
