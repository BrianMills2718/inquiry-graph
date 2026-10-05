"""Turn Google Takeout 'My Activity/Gemini Apps/MyActivity.html' prompts that no local source holds into Conversation records.
Takeout has no chat ids, so prompts within --gap-min minutes of each other become one conversation (id gemini:takeout-<first-timestamp>).
Usage: normalize_gemini_takeout.py MyActivity.html absent_prompts.json out_dir [--gap-min 45]
absent_prompts.json = [[date, prompt_text], ...] from the coverage comparison; only those prompts are written."""
import argparse, hashlib, html, json, re
from datetime import datetime, timedelta, timezone
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("html", type=Path); ap.add_argument("absent", type=Path); ap.add_argument("out", type=Path); ap.add_argument("--gap-min", type=int, default=45)
a = ap.parse_args(); a.out.mkdir(parents=True, exist_ok=True)
norm = lambda s: re.sub(r"[^a-z0-9]+", " ", html.unescape(s).lower()).strip()
want = {norm(b)[:200] for _, b in json.loads(a.absent.read_text())}
TZ = {"EDT": -4, "EST": -5}
rows = []
for c in re.findall(r'<div class="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1">(.*?)</div>', a.html.read_text(encoding="utf-8"), flags=re.S):
    s = re.sub(r"\s+", " ", html.unescape(re.sub(r"<br\s*/?>", "\n", re.sub(r"<[^>]+>", "\x00", c)).replace("\x00", " "))).strip() if False else None
    t = html.unescape(re.sub(r"<br\s*/?>", "\n", c)); t = re.sub(r"<[^>]+>", "", t)
    if not t.strip().startswith("Prompted"): continue
    m = re.search(r"([A-Z][a-z]{2} \d{1,2}, \d{4}), (\d{1,2}):(\d{2}):(\d{2})\s?([AP]M) (E[SD]T|[A-Z]{3})", t)
    if not m: continue
    prompt = t[len("Prompted"):m.start()].strip(); resp = re.sub(r"[ \t]+", " ", t[m.end():]).strip()
    if norm(prompt)[:200] not in want: continue
    d = datetime.strptime(f"{m.group(1)} {m.group(2)}:{m.group(3)}:{m.group(4)} {m.group(5)}", "%b %d, %Y %I:%M:%S %p") - timedelta(hours=TZ.get(m.group(6), 0))
    rows.append((d.replace(tzinfo=timezone.utc), prompt, resp))
rows.sort(); convs, cur = [], []
for r in rows:
    if cur and r[0] - cur[-1][0] > timedelta(minutes=a.gap_min): convs.append(cur); cur = []
    cur.append(r)
if cur: convs.append(cur)
for chat in convs:
    cid = "gemini:takeout-" + chat[0][0].strftime("%Y%m%dT%H%M%S")
    msgs = []
    for ts, p, resp in chat:
        for actor, text in (("participant:brian", p), ("participant:assistant", resp)):
            if text.strip(): msgs.append({"id": f"{cid}:msg{len(msgs)+1:04d}", "actor_id": actor, "ordinal": len(msgs) + 1, "text": text, "original_id": hashlib.sha1((cid + str(len(msgs)) + text[:50]).encode()).hexdigest()[:12], "timestamp": ts.strftime("%Y-%m-%dT%H:%M:%S.000Z")})
    conv = {"id": cid, "title": re.sub(r"\s+", " ", chat[0][1])[:80], "source_kind": "normalized", "coverage_note": "Google Takeout My Activity (Gemini Apps), requested 2026-10-05; prompts absent from Kept; grouped into chats by a 45-minute gap, so chat boundaries are inferred; visible text only.",
            "participants": [{"id": "participant:brian", "label": "Brian", "role": "user"}, {"id": "participant:assistant", "label": "Assistant", "role": "assistant"}], "messages": msgs}
    (a.out / (cid.replace(":", "-") + ".conv.json")).write_text(json.dumps(conv, ensure_ascii=False, indent=1))
print(f"{len(rows)} prompts matched of {len(want)} wanted -> {len(convs)} conversations in {a.out}")
