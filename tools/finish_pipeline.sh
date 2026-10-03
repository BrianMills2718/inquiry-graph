#!/bin/bash
# After the extraction services finish: retry failures once, reconcile, rebuild the combined map with generated names,
# publish it to the gated site, and run the cross-chat answer. Writes private/finish_report.txt. Hand-checking the answer
# and writing the completion report (C4, C5) still need a person or a fresh agent session.
# Usage (as a service, with the shell's PATH so the right codex is used):
#   systemd-run --user --unit=finish-pipeline --setenv=PATH="$PATH" tools/finish_pipeline.sh
set -u
cd "$(dirname "$0")/.."
R=private; W=$R/extract_full_20261003; LOG=$R/finish_report.txt
say() { echo "$(date -u +%FT%TZ) $*" | tee -a "$LOG"; }
say "waiting for extraction services"
while systemctl --user is-active --quiet 'extract-*'; do sleep 120; done
say "services finished; retrying failed chats once"
for d in "" kept new108; do
  dir="$W/${d}"; q=queue.json
  [ -f "$dir/$q" ] && .venv/bin/python tools/extract_queue.py "$dir/$q" "$(realpath "$dir")" --workers 2 >> "$LOG" 2>&1
done
.venv/bin/python tools/reconcile_snapshot.py $R/snapshot_reconciliation.json > $R/snapshot_summary.json 2>&1; say "reconcile exit $?"
G=""; for d in extract_test_20261003/out extract_full_20261003/out extract_full_20261003/kept/out extract_full_20261003/new108/out extract_full_20261003/single/out extract_full_20261003/lowconf/out; do [ -d "$R/$d" ] && G="$G $R/$d"; done
.venv/bin/python tools/position_records.py $R/records_full.json $G | tee -a "$LOG"
M=$R/position_map_full; mkdir -p $M
nice ~/.venvs/inquiry-maps/bin/python tools/position_topics.py $R/records_full.json $M --min-cluster 12 2>&1 | tail -1 | tee -a "$LOG"
.venv/bin/python tools/name_topics.py $R/records_full.json $M/topics.json $R/topic_names_full.json >> "$LOG" 2>&1
nice ~/.venvs/inquiry-maps/bin/python tools/position_topics.py $R/records_full.json $M --min-cluster 12 --names $R/topic_names_full.json 2>&1 | tail -1 | tee -a "$LOG"
ssh -o BatchMode=yes personal-vps 'mkdir -p /srv/apps/chat-atlas/site/positions' && scp -q $M/index.html personal-vps:/srv/apps/chat-atlas/site/positions/index.html && say "published to maps.brianmills.dev/positions/"
.venv/bin/python tools/ask_positions.py "Where have my views changed or pulled against each other across topics, and which questions do I keep leaving open?" $G --out $R/answer_full.json --top 80 2>&1 | tail -1 | tee -a "$LOG"
say "FINISH PIPELINE DONE: now hand-check private/answer_full.json and write the C5 report"
