#!/bin/bash
# Phone reminder (ntfy, topic from ~/.secrets/api_keys.env) to click the ChatGPT/Gemini export download links.
# Runs from user timer export-reminder (10:00 and 17:00). Stops when private/chatgpt_export/reminders_done exists.
M="$HOME/code/inquiry-graph/private/chatgpt_export"; [ -f "$M/reminders_done" ] && exit 0
T=$(grep -E '^(export )?OPERATOR_NTFY_TOPIC=' "$HOME/.secrets/api_keys.env" | head -1 | cut -d= -f2- | tr -d "\"'")
[ -z "$T" ] && { echo "no ntfy topic" >&2; exit 1; }
MSG="Chat export check: open the therakorski and montaguecantsin Gmail, find 'Your data export is ready' from OpenAI, click Download, then tell Claude 'downloaded'. Also the Gemini export if its email arrived."
curl -fsS -m 20 -H "Title: Chat exports waiting" -d "$MSG" "https://ntfy.sh/$T" >/dev/null && echo "$(date +%FT%T) reminder sent" >> "$M/reminder.log"
