#!/bin/bash
# Check brianmills2718's Gmail (through the robot browser on :9333) for today's "ChatGPT - Your data export is ready" email and download it.
# Run by the user timer chatgpt-export-watch (every 20 min). Marker: private/chatgpt_export/downloaded. Needs C:\Users\thela\robot\{cdp.js,cdp_nav.js,q_ready.js}.
M="$HOME/code/inquiry-graph/private/chatgpt_export"; mkdir -p "$M"; [ -f "$M/downloaded" ] && exit 0
R='C:\Users\thela\robot'; LOG="$M/watch.log"; say() { echo "$(date +%FT%T) $*" >> "$LOG"; }
powershell.exe -NoProfile -Command "try{(Invoke-RestMethod http://127.0.0.1:9333/json/version -TimeoutSec 3)|Out-Null}catch{exit 1}" >/dev/null 2>&1 || { say "robot browser down; starting it"; powershell.exe -NoProfile -ExecutionPolicy Bypass -File "$R\\start.ps1" -Name a -Urls 'https://mail.google.com/mail/u/0/' >/dev/null 2>&1; sleep 20; }
cmd.exe /c "cd /d $R && node cdp_nav.js 9333 mail.google.com https://mail.google.com/mail/u/0/#search/from%3Aopenai.com+subject%3A%22data+export%22+newer_than%3A1d" >/dev/null 2>&1
OUT=$(cmd.exe /c "cd /d $R && node cdp.js 9333 mail.google.com q_ready.js" 2>&1 | tr -d '\r')
HREF=$(echo "$OUT" | grep -o '"href": "[^"]*"' | head -1 | sed 's/"href": "//; s/"$//')
if [ -z "$HREF" ]; then say "not ready yet"; exit 0; fi
say "ready email found; downloading"
BEFORE=$(ls /mnt/c/Users/thela/Downloads | wc -l)
cmd.exe /c "cd /d $R && node cdp_nav.js 9333 mail.google.com $HREF" >/dev/null 2>&1
sleep 45
NEW=$(find /mnt/c/Users/thela/Downloads -maxdepth 1 -type f -mmin -3 ! -name "*.crdownload" | head -3)
if [ -n "$NEW" ]; then echo "$NEW" > "$M/downloaded"; say "downloaded: $NEW"; else say "link opened but no file appeared"; fi
