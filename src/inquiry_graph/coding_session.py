"""Coding-agent sessions: normalize a Claude Code or Codex session record (one .jsonl per session) into a
Conversation, and read the fixed end-of-reply fields into grounded candidates without an LLM.

Kept: Brian's own typed messages, each turn's assistant text (all text blocks between two of his messages,
joined), and one `tool` message per work product the record shows: a pull request link (Claude Code's
`pr-link` records, or a PR URL in Codex tool output) and a `git commit` result line. Dropped: system and
hook injections, tool calls and other tool output, thinking, sidechains (subagents) and compaction summaries.

The end-of-reply fields are a fixed labelled format ("- **Active subgoals** -- ..."), so reading them is
structure parsing, not prose interpretation. What they yield:
- `Session goal`            -> one goal node per distinct wording
- `Active subgoals`         -> one task node per item, with an assistant `open` status event at that turn
- `Done` "Closed: X (word)" -> a status event from the fixed closure vocabulary (CLOSURE_WORDS)
- `Need anything from human` (unless "No") -> a question node, `open` at that turn; Brian's next message
  records a proposed `answered` event (that he replied, not that the reply settled it)
- each tool message        -> a work node, `part_of` the goal current at that point
Everything is `proposed`; concepts and Brian's reasoning come from the ordinary `extract --llm` path run on the
same Conversation, and the two graphs combine with `merge`.
"""
import hashlib
import json
import re
from pathlib import Path

from .model import Binding, Candidates, Conversation, Message, Node, Participant, QuestionEvent, Relation, anchor

USER, ASSISTANT, TOOL = "participant:brian", "participant:assistant", "participant:tool"

# Closure words agents write in `Done` ("Closed: <item> (<word>)") and the question status each means.
CLOSURE_WORDS = {"done": "resolved", "answered": "answered", "put off": "deferred", "reopened": "reopened",
                 "dropped": "dropped", "replaced by": "superseded"}

_FIELD = re.compile(r"^[-*]\s+\*\*(Session goal|Active subgoals|Done|Need anything from human)\*\*\s*[—:\-]+\s*(.+)$",
                    re.MULTILINE)
_CLOSED = re.compile(r"Closed:\s*(?P<item>[^()]+?)\s*\((?P<word>done|answered|put off|reopened|dropped|replaced by\s+(?P<new>[^)]+))\)")
_LABEL = re.compile(r"\b(Current|Other):\s*")
_COMMIT = re.compile(r"^\[[\w./+-]+(?: \(root-commit\))? [0-9a-f]{7,40}\] .+$", re.MULTILINE)
_PR = re.compile(r"https://github\.com/[\w.-]+/[\w.-]+/pull/\d+")
_INJECTED = ("<", "This session is being continued", "Another Claude session", "# AGENTS.md instructions",
             "A session-scoped Stop hook", "[Request interrupted")


def _own_text(text: str) -> bool:
    return bool(text.strip()) and not text.lstrip().startswith(_INJECTED)


def _claude_events(lines):
    for rec in lines:
        if rec.get("isSidechain") or rec.get("isCompactSummary") or rec.get("isMeta"):
            continue
        kind, ts = rec.get("type"), rec.get("timestamp")
        if kind == "pr-link" and rec.get("prUrl"):
            yield "tool", rec["prUrl"], ts
        elif kind == "user":
            content = rec.get("message", {}).get("content")
            if isinstance(content, str):
                if _own_text(content):
                    yield "user", content, ts
                continue
            for block in content or []:
                if block.get("type") == "text" and _own_text(block.get("text", "")):
                    yield "user", block["text"], ts
                elif block.get("type") == "tool_result":
                    body = block.get("content")
                    if isinstance(body, list):
                        body = "\n".join(b.get("text", "") for b in body if isinstance(b, dict))
                    for line in _COMMIT.findall(body or ""):
                        yield "tool", line, ts
        elif kind == "assistant":
            for block in rec.get("message", {}).get("content") or []:
                if block.get("type") == "text" and block.get("text", "").strip():
                    yield "assistant", block["text"], ts


def _codex_events(lines):
    for rec in lines:
        p, ts = rec.get("payload") or {}, rec.get("timestamp")
        if rec.get("type") != "response_item":
            continue
        if p.get("type") == "message" and p.get("role") in ("user", "assistant"):
            for block in p.get("content") or []:
                text = block.get("text", "")
                if p["role"] == "user" and _own_text(text):
                    yield "user", text, ts
                elif p["role"] == "assistant" and text.strip():
                    yield "assistant", text, ts
        elif p.get("type") == "function_call_output":
            out = p.get("output")
            out = out if isinstance(out, str) else json.dumps(out)
            for url in _PR.findall(out):
                yield "tool", url, ts
            for line in _COMMIT.findall(out):
                yield "tool", line, ts


def parse_session(path) -> Conversation:
    """One session record -> Conversation. The client is detected from the record, not the file name."""
    path = Path(path)
    lines, broken = [], 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.strip():
            try:
                lines.append(json.loads(raw))
            except json.JSONDecodeError:   # a live session's last line can be half-written
                broken += 1
    codex = any(rec.get("type") == "session_meta" for rec in lines[:5])
    meta = next((rec.get("payload", {}) for rec in lines if rec.get("type") == "session_meta"), {})
    first = next((rec for rec in lines if rec.get("cwd")), {})
    sid = meta.get("id") or first.get("sessionId") or path.stem
    cwd = meta.get("cwd") or first.get("cwd") or "?"
    cid = f"{'codex' if codex else 'claude-code'}:{sid}"
    messages, turn, seen_tools = [], [], set()
    pending_tools = []

    def add(actor, text, ts):
        n = len(messages) + 1
        messages.append(Message(id=f"{cid}:msg{n:04d}", ordinal=n, actor_id=actor, text=text, timestamp=ts))

    def flush():
        if turn:
            add(ASSISTANT, "\n\n".join(t for t, _ in turn), turn[-1][1])
            turn.clear()
        for text, ts in pending_tools:
            add(TOOL, text, ts)
        pending_tools.clear()

    for actor, text, ts in (_codex_events(lines) if codex else _claude_events(lines)):
        if actor == "assistant":
            turn.append((text, ts))
        elif actor == "tool":
            if text not in seen_tools:
                seen_tools.add(text)
                pending_tools.append((text, ts))
        else:
            flush()
            add(USER, text, ts)
    flush()
    if not messages:
        raise ValueError(f"{cid}: no visible messages")
    return Conversation(
        id=cid, title=f"{Path(cwd).name} session {sid[:8]}", source_kind="normalized",
        coverage_note=(f"{'Codex' if codex else 'Claude Code'} session record {path.name}, cwd {cwd}. Brian's typed "
                       "messages, assistant text per turn, and pull-request/commit lines from tool records; hooks, "
                       "tool calls, other tool output, thinking and subagents omitted."
                       + (f" {broken} unreadable record line(s) skipped." if broken else "")),
        participants=[Participant(id=USER, label="Brian", role="user"),
                      Participant(id=ASSISTANT, label="Assistant", role="assistant"),
                      Participant(id=TOOL, label="Tool record", role="other")],
        messages=messages)


def _key(text: str) -> str:
    return hashlib.sha256(" ".join(text.lower().split()).encode()).hexdigest()[:12]


def _items(value: str) -> list[str]:
    """`Current: a. Other: b; c` -> [a, b, c]. Items are separated by the labels and by semicolons."""
    parts = []
    for chunk in _LABEL.split(value):
        if chunk in ("Current", "Other"):
            continue
        parts += [p.strip(" .") for p in chunk.split(";")]
    return [p for p in parts if p and p.lower() not in ("none", "n/a")]


def reply_field_candidates(conv: Conversation) -> Candidates:
    """Grounded goal/task/question/work candidates from the end-of-reply fields and tool messages."""
    nodes, events, relations = {}, {}, []
    by_text = {}
    goal_now, request_open = None, None
    cid = conv.id

    def node(kind, text, message, quote=None):
        nid = f"{cid}:{kind}:{_key(text)}"
        if nid not in nodes:
            spans = message.text.count(quote or text)
            nodes[nid] = Node(id=nid, kind=kind, text=text, origin="explicit",
                              anchors=[anchor(message, quote or text, 0 if spans > 1 else None)])
            by_text[_key(text)] = nid
        return nid

    def event(qid, status, message, quote, replacement=None):
        # One status per item per turn; a closure word in Done overrides the same turn's listing as open.
        if (qid, message.ordinal) in events and status == "open":
            return
        spans = message.text.count(quote)
        events[(qid, message.ordinal)] = (QuestionEvent(id=f"{qid}:status:{message.ordinal}", question_id=qid, status=status, actor_id=message.actor_id,
                                    at_message_id=message.id, replacement_id=replacement, origin="explicit",
                                    resolution_basis=f"agent wrote: {quote}" if status == "resolved" else None,
                                    anchors=[anchor(message, quote, 0 if spans > 1 else None)]))

    for m in conv.messages:
        if m.actor_id == USER:
            if request_open:
                event(request_open, "answered", m, m.text)
                request_open = None
            continue
        if m.actor_id == TOOL:
            wid = node("work", m.text, m)
            if goal_now:
                relations.append(Relation(id=f"{wid}:part_of:{_key(goal_now)}", kind="part_of", origin="explicit",
                                          anchors=[anchor(m, m.text)],
                                          bindings=[Binding(role="part", ref=wid), Binding(role="whole", ref=goal_now)]))
            continue
        for field, value in _FIELD.findall(m.text):
            value = value.strip()
            if field == "Session goal":
                goal_now = node("goal", value, m)
            elif field == "Active subgoals":
                for item in _items(value):
                    event(node("task", item, m), "open", m, item)
            elif field == "Done":
                for c in _CLOSED.finditer(value):
                    item, word = c["item"].strip(), c["word"]
                    tid = by_text.get(_key(item)) or node("task", item, m)
                    if c["new"]:
                        new = c["new"].strip()
                        event(tid, "superseded", m, c.group(0), replacement=by_text.get(_key(new)) or node("task", new, m))
                    else:
                        event(tid, CLOSURE_WORDS[word], m, c.group(0))
            elif field == "Need anything from human" and not value.lower().startswith("no"):
                request_open = node("question", value, m)
                event(request_open, "open", m, value)
    return Candidates(nodes=list(nodes.values()), relations=relations, question_events=list(events.values()))


def session_digest(graph) -> dict:
    """What an agent needs to resume: goals, items still listed as open at the last listing, items that
    dropped out of the list with no closure word (status unknown), closed items, work and open requests."""
    msgs = {m.id: (c.id, m.ordinal) for c in graph.conversations for m in c.messages}
    nodes = {n.id: n for n in graph.nodes}
    latest = {}
    for e in graph.question_events:
        if e.question_id not in latest or msgs[latest[e.question_id].at_message_id][1] <= msgs[e.at_message_id][1]:
            latest[e.question_id] = e
    last_listing = max((msgs[e.at_message_id][1] for e in graph.question_events
                        if e.status == "open" and nodes[e.question_id].kind == "task"), default=None)
    out = {"conversations": [{"id": c.id, "title": c.title, "messages": len(c.messages),
                              "from": c.messages[0].timestamp, "to": c.messages[-1].timestamp} for c in graph.conversations],
           "goals": [n.text for n in nodes.values() if n.kind == "goal"],
           "open": [], "unknown_status": [], "closed": [], "requests_open": [],
           "work": [n.text for n in nodes.values() if n.kind == "work"]}
    for qid, e in latest.items():
        n = nodes[qid]
        if n.kind == "question":
            if e.status == "open":
                out["requests_open"].append(n.text)
        elif e.status == "open":
            (out["open"] if msgs[e.at_message_id][1] == last_listing else out["unknown_status"]).append(n.text)
        else:
            out["closed"].append({"item": n.text, "status": e.status})
    return out
