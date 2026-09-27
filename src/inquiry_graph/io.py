"""Safe normalization, serialization, exact-identity union and candidate ingestion."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
from uuid import uuid4

from .model import Conversation, Graph, Candidates, Extraction, COLLECTIONS, anchor
from .validate import require_valid


def load(path, cls):
    return cls.model_validate_json(Path(path).read_text(encoding="utf-8"))


def write_json(path, value, replace=False):
    """Atomic replacement only with explicit permission; incomplete output is never canonical."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not replace:
        raise FileExistsError(f"{path} exists; choose another output or use --force")
    data = value.model_dump(mode="json") if hasattr(value, "model_dump") else value
    text = json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    fd, temporary = tempfile.mkstemp(prefix=".inquiry-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
            f.flush()
            os.fsync(f.fileno())
        if replace:
            os.replace(temporary, path)
        else:
            # Exclusive creation even when another process races this writer.
            os.link(temporary, path)
            os.unlink(temporary)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def import_export(data, conversation_id=None):
    """Follow only the active branch of a ChatGPT mapping tree. No hidden/tool messages."""
    if isinstance(data, dict) and "source_kind" in data:
        conv = Conversation.model_validate(data)
        if conversation_id and conv.id != conversation_id:
            raise ValueError("conversation ID not found")
        return [conv]
    raw = data if isinstance(data, list) else [data]
    result = []
    for obj in raw:
        if not isinstance(obj, dict):
            raise ValueError("export entries must be objects")
        cid = obj.get("id") or obj.get("conversation_id")
        if not isinstance(cid, str) or not cid:
            raise ValueError("export conversation requires a string id")
        if conversation_id and cid != conversation_id:
            continue
        mapping = obj.get("mapping")
        current = obj.get("current_node")
        if not isinstance(mapping, dict) or not isinstance(current, str) or current not in mapping:
            raise ValueError(f"{cid}: mapping/current_node missing or invalid; select active branch explicitly")
        chain, seen = [], set()
        while current is not None:
            if current in seen:
                raise ValueError(f"{cid}: cycle in export parent chain")
            if current not in mapping:
                raise ValueError(f"{cid}: dangling parent {current}")
            seen.add(current)
            record = mapping[current]
            if not isinstance(record, dict):
                raise ValueError(f"{cid}: mapping node must be an object")
            if record.get("parent") is not None and not isinstance(record["parent"], str):
                raise ValueError(f"{cid}: parent ID must be a string or null")
            chain.append((current, record.get("message")))
            current = record.get("parent")
        messages, participants, skipped = [], {}, 0
        for key, msg in reversed(chain):
            if not msg:
                continue
            if not isinstance(msg, dict) or not isinstance(msg.get("author"), dict) or not isinstance(msg.get("content"), dict):
                raise ValueError(f"{cid}: malformed message, author or content")
            if msg.get("metadata") is not None and not isinstance(msg["metadata"], dict):
                raise ValueError(f"{cid}: metadata must be an object")
            role = msg.get("author", {}).get("role")
            # Exclude analysis/commentary/system/tool and non-user-visible recipients.
            channel = (msg.get("metadata") or {}).get("channel") or msg.get("channel")
            recipient = msg.get("recipient")
            if (role not in ("user", "assistant") or channel not in (None, "final")
                    or recipient not in (None, "all")
                    or (msg.get("metadata") or {}).get("is_visually_hidden_from_conversation", False)):
                skipped += 1
                continue
            parts = (msg.get("content") or {}).get("parts", [])
            if not isinstance(parts, list):
                raise ValueError(f"{cid}: content parts must be an array")
            text_parts = [p for p in parts if isinstance(p, str)]
            skipped += len(parts) - len(text_parts)
            text = "\n".join(text_parts)
            if not text:
                skipped += 1
                continue
            aid = f"{cid}:actor:{role}"
            participants[aid] = {"id": aid, "label": role, "role": role}
            timestamp = msg.get("create_time")
            # Preserve timestamp as source string; never infer ordering across conversations.
            messages.append({"id": f"{cid}:message:{key}", "actor_id": aid,
                             "ordinal": len(messages) + 1, "text": text,
                             "original_id": msg.get("id") or key,
                             "timestamp": str(timestamp) if timestamp is not None else None})
        result.append(Conversation.model_validate({
            "id": cid, "title": obj.get("title") or cid, "source_kind": "chatgpt_export",
            "coverage_note": f"Active current_node ancestor branch only. Skipped {skipped} nontext/nonpublic records or parts. No access to hidden reasoning; check export visibility manually before sharing.",
            "participants": list(participants.values()), "messages": messages}))
    if not result:
        raise ValueError("conversation ID not found")
    return result


def ingest(source: Conversation, candidates: Candidates, *, method="response-file", model=None):
    """Source records are trusted inputs, never LLM-owned output. Review always starts proposed."""
    values = candidates.model_dump(mode="json")
    messages = {m.id: m for m in source.messages}
    for field in COLLECTIONS:
        for obj in values[field]:
            obj["review_status"] = "proposed"
            grounded = []
            for span in obj["anchors"]:
                message = messages.get(span["message_id"])
                if message is None:
                    raise ValueError(f"unknown source message {span['message_id']}")
                try:
                    exact = anchor(message, span["quote"])
                except ValueError as exc:
                    # A repeated quote requires an exact supplied position to select it.
                    if "ambiguous quote" not in str(exc) or message.text[span["start"]:span["end"]] != span["quote"]:
                        raise
                    grounded.append(span)
                else:
                    grounded.append(exact.model_dump(mode="json"))
            obj["anchors"] = grounded
    digest = hashlib.sha256(source.model_dump_json().encode()).hexdigest()
    graph = Graph(id=f"graph:{source.id}", conversations=[source], **values,
                  extractions=[Extraction(method=method, model=model,
                    notes=[f"source_sha256:{digest}", "Candidate annotations require review; structural validation is not semantic verification."])])
    return require_valid(graph)


def merge(graphs):
    """Idempotent set union with conflicts, not fuzzy identity resolution or belief overwrite."""
    if not graphs:
        raise ValueError("at least one graph required")
    for graph in graphs:
        require_valid(graph)
    values = {}
    for field in (*COLLECTIONS, "conversations"):
        collected = {}
        for graph in graphs:
            for item in getattr(graph, field):
                if item.id in collected and item != collected[item.id]:
                    raise ValueError(f"identity conflict in {field}: {item.id}")
                collected[item.id] = item
        values[field] = [collected[k] for k in sorted(collected)]
    notes = sorted({note for graph in graphs for note in graph.notes})
    extraction_map = {e.model_dump_json(): e for g in graphs for e in g.extractions}
    identifier = hashlib.sha256("\n".join(c.id for c in values["conversations"]).encode()).hexdigest()[:16]
    return require_valid(Graph(id=f"merged:{identifier}", **values, notes=notes,
                               extractions=[extraction_map[k] for k in sorted(extraction_map)]))


def quarantine(directory, raw, error):
    """Persist private failure data separately, never replace an existing canonical graph."""
    out = Path(directory) / f"failed-{uuid4().hex}.json"
    write_json(out, {"error": str(error), "raw_response": raw,
                     "warning": "Private source-derived data. This is not a validated graph."})
    return out
