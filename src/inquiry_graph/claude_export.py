"""Normalize Claude's official data export (conversations.json) into Conversations.

Each export conversation has uuid, name, created_at and chat_messages (sender human|assistant, text, created_at).
Only the visible `text` of human and assistant turns is kept; tool use and results live in `content` blocks and are not
anything either participant said. Ids are `claude:<uuid>`, the same form the Kept normalizer uses, so the two sources
reconcile by id.
"""
from .model import Conversation, Message, Participant


def parse_claude_conversation(c: dict, user_label: str = "Brian") -> Conversation:
    for key in ("uuid", "chat_messages"):
        if key not in c:
            raise ValueError(f"Claude export conversation missing {key!r}")
    cid = f"claude:{c['uuid']}"
    user_id, assistant_id = f"participant:{user_label.lower()}", "participant:assistant"
    messages = []
    for m in c["chat_messages"]:
        role = {"human": user_id, "assistant": assistant_id}.get(m.get("sender"))
        text = (m.get("text") or "").strip()
        if role is None or not text:
            continue
        ordinal = len(messages) + 1
        messages.append(Message(id=f"{cid}:msg{ordinal:04d}", ordinal=ordinal, text=m["text"], original_id=m.get("uuid"),
                                timestamp=m.get("created_at"), actor_id=role))
    if not messages:
        raise ValueError(f"{cid}: no visible human or assistant text")
    return Conversation(
        id=cid, title=(c.get("name") or "").strip() or "(untitled)", source_kind="normalized",
        coverage_note="Claude official data export; visible human/assistant text only (tool use and results omitted).",
        participants=[Participant(id=user_id, label=user_label, role="user"), Participant(id=assistant_id, label="Assistant", role="assistant")],
        messages=messages)
