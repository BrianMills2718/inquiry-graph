"""Parse a speaker-labelled meeting transcript into a Conversation with one participant per speaker.

Input lines look like `**[MM:SS] Speaker Name:** text` (the format the Inside Success second brain's
get_meeting tool writes, kept verbatim in raw captures). A turn runs until the next such line.
Every speaker becomes a participant; `owner` (default Brian Mills) gets the `participant:brian`
id and role `user` so his positions line up with his chat archive; other people get role `other`.
Labels beginning `Audio shared by` are a shared-audio voice (for example an AI demo), not a
person: they get role `other` and the id `participant:shared-audio`, and callers must not
attribute positions to them. Text is kept exactly as written (no cleanup), so quotes stay verbatim.
"""

from __future__ import annotations

import datetime as dt
import re

from inquiry_graph.model import Conversation, Message, Participant

TURN = re.compile(r"^\*\*\[(?P<clock>\d{1,2}:\d{2}(?::\d{2})?)\] (?P<speaker>[^*]+?):\*\*\s?(?P<text>.*)$")
SHARED_AUDIO = "Audio shared by"


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def seconds(clock: str) -> int:
    parts = [int(p) for p in clock.split(":")]
    return parts[0] * 60 + parts[1] if len(parts) == 2 else parts[0] * 3600 + parts[1] * 60 + parts[2]


def parse_zoom_transcript(text: str, conversation_id: str, title: str, started_at: str | None = None,
                          owner: str = "Brian Mills") -> Conversation:
    turns: list[dict] = []
    for line in text.splitlines():
        m = TURN.match(line)
        if m:
            turns.append({"clock": m["clock"], "speaker": m["speaker"].strip(), "lines": [m["text"]]})
        elif turns:
            turns[-1]["lines"].append(line)
    if not turns:
        raise ValueError(f"{conversation_id}: no speaker-labelled turns found")
    start = dt.datetime.fromisoformat(started_at.replace("Z", "+00:00")) if started_at else None
    ids: dict[str, Participant] = {}
    for t in turns:
        s = t["speaker"]
        if s in ids:
            continue
        if s == owner:
            ids[s] = Participant(id="participant:brian", label=s, role="user")
        elif s.startswith(SHARED_AUDIO):
            ids[s] = Participant(id="participant:shared-audio", label=f"{s} (shared audio, not a person)", role="other")
        else:
            ids[s] = Participant(id=f"participant:{slug(s)}", label=s, role="other")
    messages = []
    for t in turns:
        body = "\n".join(t["lines"]).strip()
        if not body:
            continue
        n = len(messages) + 1
        stamp = (start + dt.timedelta(seconds=seconds(t["clock"]))).isoformat() if start else None
        messages.append(Message(id=f"{conversation_id}:turn{n:04d}", actor_id=ids[t["speaker"]].id, ordinal=n,
                                text=body, original_id=f"[{t['clock']}]", timestamp=stamp))
    return Conversation(id=conversation_id, title=title, source_kind="normalized",
                        coverage_note=f"Machine meeting transcript, {len(messages)} turns, speaker labels as recorded; text verbatim.",
                        participants=list(ids.values()), messages=messages)
