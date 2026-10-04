#!/bin/bash
# Ask the running ChatGPT exporter for the full list of chat ids (read-only) of each account, one at a time.
# Run this yourself in a WSL terminal: it reads the exporter's token from the exporter's own settings file and never prints it.
# Usage: tools/inventory_accounts.sh [account ...]   (default: the three known accounts)
set -u
EXPORTER="$HOME/code/chatgpt-conversation-manager-v0.2"
OUT="$(cd "$(dirname "$0")/.." && pwd)/private/openai_inventory_$(date +%Y%m%d)"
mkdir -p "$OUT"
TOK=$(grep '^RENAMER_TOKEN=' "$EXPORTER"/.env | cut -d= -f2- | tr -d '"'"'"'\r')
[ -n "$TOK" ] || { echo "no token found"; exit 1; }
ACCTS=("$@"); [ ${#ACCTS[@]} -gt 0 ] || ACCTS=(brianmills2718@gmail.com therakorski@gmail.com montaguecantsin@gmail.com)
for a in "${ACCTS[@]}"; do
  for try in 1 2; do
    code=$(curl -s -m 900 -H "Authorization: Bearer $TOK" "http://127.0.0.1:8787/api/inventory-chats?account=$a" -o "$OUT/$a.json" -w '%{http_code}')
    echo "$a try $try: http $code ($(wc -c < "$OUT/$a.json") bytes)"
    [ "$code" = 200 ] && break
    [ $try = 1 ] && { echo "waiting 5 minutes before one retry (rate limit?)"; sleep 300; }
  done
done
echo "done; now ask Claude to compare, or run: python3 tools/compare_inventory.py $OUT"
