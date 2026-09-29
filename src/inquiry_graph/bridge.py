"""Normalize a chatgpt-bridge `read_chatgpt_chat` transcript into a Conversation.

The bridge renders a chat as Markdown with one `## user|assistant|tool (<ISO time>)`
header per message. Only visible user/assistant text is kept: tool output (web
pages, repository files the assistant read) is not something either participant
said. Messages with no visible text, such as the voice-mode opening of a chat,
are skipped and counted, never invented.
"""
import re

from .model import Conversation, Message, Participant

HEADER = re.compile(r"^## (user|assistant|tool) \(([^)]*)\)\s*$", re.M)
THREAD = re.compile(r"^conversation ([0-9a-f-]{36})", re.M)


def parse_bridge_markdown(text: str, conversation_id: str | None = None,
                          user_label: str = "Brian") -> tuple[Conversation, dict]:
    parts = HEADER.split(text)
    if len(parts) < 4:
        raise ValueError("no bridge message headers found")
    title = parts[0].lstrip().splitlines()[0].lstrip("# ").strip() if parts[0].strip() else "untitled"
    thread = THREAD.search(parts[0])
    cid = conversation_id or (f"chatgpt:{thread.group(1)}" if thread else None)
    if not cid:
        raise ValueError("conversation id not given and not present in the transcript header")
    user_id, assistant_id = f"participant:{user_label.lower()}", "participant:assistant"
    messages, skipped = [], {"tool": 0, "empty": 0}
    for i in range(1, len(parts) - 2, 3):
        role, at, body = parts[i], parts[i + 1], parts[i + 2].strip()
        if role == "tool":
            skipped["tool"] += 1
            continue
        if not body:
            skipped["empty"] += 1
            continue
        ordinal = len(messages) + 1
        messages.append(Message(id=f"{cid}:msg{ordinal:04d}", ordinal=ordinal, text=body, timestamp=at,
                                actor_id=user_id if role == "user" else assistant_id))
    if not messages:
        raise ValueError("transcript has no visible user or assistant text")
    conv = Conversation(
        id=cid, title=title, source_kind="normalized",
        coverage_note=(f"chatgpt-bridge transcript; visible user/assistant text only. Skipped "
                       f"{skipped['tool']} tool-output blocks and {skipped['empty']} messages with no "
                       "visible text (e.g. voice mode). Message ids are local ordinals; timestamps are "
                       "the bridge's."),
        participants=[Participant(id=user_id, label=user_label, role="user"),
                      Participant(id=assistant_id, label="Assistant", role="assistant")],
        messages=messages)
    return conv, skipped
