"""Reproduce the first-pass annotation from explicit curation, not a claimed live LLM run."""
import json
from pathlib import Path

from inquiry_graph.model import (Conversation, Candidates, Node, Relation, Binding,
    Move, StanceEvent, QuestionEvent, SIGNATURES, anchor)
from inquiry_graph.io import ingest, write_json

ROOT = Path(__file__).resolve().parent
source = Conversation.model_validate_json((ROOT / "seed/source-excerpts.json").read_text())
cur = json.loads((ROOT / "seed/curation.json").read_text())
messages = {m.id: m for m in source.messages}
keys = cur["source_keys"]
def mid(key):
    return messages[keys[key]]
def nid(slug):
    return f"{source.id}:n:{slug}"
def ground(key):
    msg = mid(key)
    return [anchor(msg, msg.text)]
def event(key):
    return {"actor_id": mid(key).actor_id, "at_message_id": mid(key).id, "anchors": ground(key)}

c = Candidates()
for slug, kind, text, key in cur["nodes"]:
    c.nodes.append(Node(id=nid(slug), kind=kind, text=text, anchors=ground(key)))
    if kind == "question":
        c.question_events.append(QuestionEvent(id=f"{source.id}:qe:{slug}", question_id=nid(slug),
                                              status="open", **event(key)))
for i, (kind, a, b, key) in enumerate(cur["relations"], 1):
    roles = list(SIGNATURES[kind])
    c.relations.append(Relation(id=f"{source.id}:r:{i:03}",kind=kind,
        bindings=[Binding(role=roles[0],ref=nid(a)),Binding(role=roles[1],ref=nid(b))],anchors=ground(key)))
last = None
for i, (kind, inputs, outputs, key) in enumerate(cur["moves"], 1):
    move_id = f"{source.id}:m:{i:03}"
    # 'after' is source chronology only, not a claim the previous move caused this one.
    c.moves.append(Move(id=move_id,kind=kind,input_ids=[nid(s) for s in inputs],
        output_ids=[nid(s) for s in outputs],after_move_ids=[last] if last else [],**event(key)))
    last = move_id
for i,(target, stance, key) in enumerate(cur["stances"],1):
    c.stance_events.append(StanceEvent(id=f"{source.id}:s:{i:03}", target_id=nid(target),
        stance=stance, origin="explicit", **event(key)))
for i,(target,status,key,answers) in enumerate(cur["question_updates"],1):
    c.question_events.append(QuestionEvent(id=f"{source.id}:qe:update:{i}",question_id=nid(target),
        status=status, answer_ids=[nid(s) for s in answers], **event(key)))
graph = ingest(source,c,method="assistant-curated-first-pass")
graph.notes = [cur["notice"], "After-move links encode recorded excerpt order only, not causal succession.",
               "Read docs/seed-review.md for analyst concerns about earlier philosophical overclaims."]
write_json(ROOT/"seed/candidates.json",c,replace=True)
write_json(ROOT/"seed/graph.json",graph,replace=True)
print(f"Built {len(c.nodes)} nodes, {len(c.relations)} relations, {len(c.moves)} moves")
