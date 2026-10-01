"""Normalize a ChatGPT Conversation Manager per-thread JSON into a Conversation.

Only visible user/assistant text is kept. Tool-role messages are not something either
participant said, so they are skipped and counted. Exporter message ids are kept in
`original_id`; the capture's completeness warning is carried into `coverage_note`.
"""
from .model import Conversation, Message, Participant


def parse_exporter_json(data: dict, user_label: str = "Brian") -> tuple[Conversation, dict]:
    for key in ("thread_id", "title", "messages"):
        if key not in data:
            raise ValueError(f"exporter JSON missing required field {key!r}")
    cid = f"chatgpt:{data['thread_id']}"
    user_id, assistant_id = f"participant:{user_label.lower()}", "participant:assistant"
    messages, skipped = [], {"tool": 0, "empty": 0, "other_role": 0}
    for m in data["messages"]:
        role, text = m.get("role"), (m.get("text") or "").strip()
        if role == "tool":
            skipped["tool"] += 1
            continue
        if role not in ("user", "assistant"):
            skipped["other_role"] += 1
            continue
        if not text:
            skipped["empty"] += 1
            continue
        ordinal = len(messages) + 1
        messages.append(Message(id=f"{cid}:msg{ordinal:04d}", ordinal=ordinal, text=m["text"],
                                original_id=m.get("message_id"), timestamp=m.get("created_at"),
                                actor_id=user_id if role == "user" else assistant_id))
    if not messages:
        raise ValueError(f"{cid}: no visible user or assistant text")
    note = (f"ChatGPT Conversation Manager capture ({data.get('capture_source', 'unknown')}); visible "
            f"user/assistant text only. Skipped {skipped['tool']} tool messages, {skipped['empty']} "
            f"empty, {skipped['other_role']} other-role. Message ids are local ordinals; exporter "
            "message ids are in original_id.")
    if data.get("completeness_warning"):
        note += f" COMPLETENESS WARNING: {data['completeness_warning']}"
    conv = Conversation(
        id=cid, title=data["title"], source_kind="normalized", coverage_note=note,
        participants=[Participant(id=user_id, label=user_label, role="user"),
                      Participant(id=assistant_id, label="Assistant", role="assistant")],
        messages=messages)
    return conv, skipped
