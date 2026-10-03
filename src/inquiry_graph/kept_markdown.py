"""Normalize a Kept vault Markdown file (ChatGPT, Claude, Gemini, ...) into a Conversation.

Kept writes YAML-like frontmatter (id, platform, title, synced, messages, model) and then one
`### <You|Assistant|tool> — <ISO timestamp>` header per message. Only those exact structural
headers split messages, so a heading such as `### Step 1 — ...` inside a reply stays in its text.
Tool messages are skipped and counted, as in the ChatGPT exporter path.
"""
import re

from .model import Conversation, Message, Participant

_HEADER = re.compile(r"^### (You|Assistant|tool) — (\d{4}-\d\d-\d\dT[\d:.]+Z)\s*$", re.M)
_FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def _frontmatter(text: str) -> dict:
    m = _FRONT.match(text)
    if not m:
        raise ValueError("Kept file has no frontmatter")
    out = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and not line.startswith((" ", "-")):
            out[k.strip()] = v.strip().strip('"')
    return out


def parse_kept_markdown(text: str, user_label: str = "Brian") -> tuple[Conversation, dict]:
    fm = _frontmatter(text)
    for key in ("id", "platform", "title"):
        if not fm.get(key):
            raise ValueError(f"Kept frontmatter missing {key!r}")
    cid = f"{fm['platform']}:{fm['id']}"
    user_id, assistant_id = f"participant:{user_label.lower()}", "participant:assistant"
    body = text[_FRONT.match(text).end():]
    marks = list(_HEADER.finditer(body))
    messages, skipped = [], {"tool": 0, "empty": 0}
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        content = body[m.end():end].strip()
        if m.group(1) == "tool":
            skipped["tool"] += 1
            continue
        if not content:
            skipped["empty"] += 1
            continue
        ordinal = len(messages) + 1
        messages.append(Message(id=f"{cid}:msg{ordinal:04d}", ordinal=ordinal, text=content, timestamp=m.group(2),
                                actor_id=user_id if m.group(1) == "You" else assistant_id))
    if not messages:
        raise ValueError(f"{cid}: no visible user or assistant text")
    declared = fm.get("messages")
    note = (f"Kept vault capture ({fm['platform']}, synced {fm.get('synced', 'unknown')}); visible user/assistant "
            f"text only. Skipped {skipped['tool']} tool and {skipped['empty']} empty messages. Frontmatter declares "
            f"{declared} messages, {len(marks)} headers found.")
    if declared and declared.isdigit() and int(declared) != len(marks):
        note += " COMPLETENESS WARNING: declared message count differs from headers found."
    conv = Conversation(
        id=cid, title=fm["title"], source_kind="normalized", coverage_note=note,
        participants=[Participant(id=user_id, label=user_label, role="user"),
                      Participant(id=assistant_id, label="Assistant", role="assistant")],
        messages=messages)
    return conv, skipped
