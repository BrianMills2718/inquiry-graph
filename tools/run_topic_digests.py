"""Run one focused ask_positions question per large topic (layer 25), skipping chore topics. Resumable: skips topics whose answer file exists.
Usage: run_topic_digests.py --n 100 --jobs 6 --outdir private/topic_digests"""
import argparse, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
CHORES = {"Introductory Physics Problems", "Python Development and Execution", "Python Code Debugging", "OpenAI API integration troubleshooting",
  "API Integration Troubleshooting", "Pandas DataFrame Tweet Processing", "Brian's Windows development environment", "Concurrent API Call Processing",
  "Streamlit application development", "Government Website Search Scraping", "Mermaid Diagram Feedback", "GitHub Workflows and Repositories",
  "Brian's Questions and Preferences", "Brian’s clarification questions", "Brian's clarification questions", "Brian's software development questions",
  "Brian’s Technical Setup and Workflows", "Brian’s Documentation Project Guidance", "Project goals and next steps", "Software Project Planning Guidance",
  "Google Concordia Setup and Compatibility", "Wire Adapter Schema Mapping", "Codex Usage and Automation", "Collaborative Document Revision"}
ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=100); ap.add_argument("--jobs", type=int, default=6)
ap.add_argument("--outdir", type=Path, default=Path("private/topic_digests")); a = ap.parse_args()
R = Path("private"); graphs = [str(R / d) for d in ["extract_test_20261003/out", "extract_full_20261003/out", "extract_full_20261003/kept/out", "extract_full_20261003/new108/out",
  "extract_full_20261003/single/out", "extract_full_20261003/claude_export/out", "extract_full_20261003/or_run/out", "extract_full_20261003/lowconf/out"] if (R / d).is_dir()]
topics = [t for t in json.load(open(R / "position_map_full/topics.json"))["topics"] if t["layer"] == 25 and t["name"] not in CHORES]
topics = sorted(topics, key=lambda t: -t["size"])[:a.n]
a.outdir.mkdir(parents=True, exist_ok=True)
json.dump([{k: t[k] for k in ("topic", "name", "size", "chats", "first", "last")} for t in topics], open(a.outdir / "topics.json", "w"), indent=1)
env = dict(os.environ, LLM_CLIENT_PROJECT_MONTHLY_BUDGET="15")
def run(t):
    out = a.outdir / f"{t['topic'].split(':')[1]}.json"
    if out.exists(): return t["name"], "skipped_done"
    q = f"What are my positions on {t['name']}, where have my views changed or pulled against each other, and which questions do I keep leaving open?"
    p = subprocess.run([sys.executable, "tools/ask_positions.py", q, *graphs, "--out", str(out), "--top", "80", "--authorship", str(R / "authorship_full.json"),
        "--records", str(R / "records_full.json")], capture_output=True, text=True, env=env)
    return t["name"], "ok" if p.returncode == 0 else "FAILED " + (p.stdout + p.stderr)[-200:]
with ThreadPoolExecutor(a.jobs) as ex:
    res = list(ex.map(run, topics))
from collections import Counter
print(Counter(r[1].split()[0] for r in res)); [print(r) for r in res if r[1].startswith("FAILED")]
