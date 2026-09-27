"""Closed-world structural checks, not a proof that recorded claims are true."""
from collections import Counter
import networkx as nx
from .model import Graph, COLLECTIONS, SIGNATURES


def validate(graph: Graph) -> dict:
    errors, warnings = [], []
    def error(code, item, detail):
        errors.append({"code": code, "item": item, "detail": detail})
    registry, messages, actors, context = {}, {}, {}, {}
    def register(key, value):
        if key in registry:
            error("duplicate_id", key, "IDs must be globally unique")
        registry[key] = value
    for conv in graph.conversations:
        register(conv.id, conv)
        local_actors = {p.id for p in conv.participants}
        if len(local_actors) != len(conv.participants):
            error("duplicate_actor", conv.id, "duplicate participant in conversation")
        for p in conv.participants:
            if p.id in actors and actors[p.id] != p:
                error("actor_conflict", p.id, "different definitions of participant")
            elif p.id not in actors:
                register(p.id, p)
            actors[p.id] = p
        ordinals = [m.ordinal for m in conv.messages]
        if len(set(ordinals)) != len(ordinals) or ordinals != sorted(ordinals):
            error("source_order", conv.id, "ordinals must be unique and increasing")
        for m in conv.messages:
            register(m.id, m)
            messages[m.id], context[m.id] = m, conv.id
            if m.actor_id not in local_actors:
                error("source_actor", m.id, "actor not a participant in this conversation")
    content = {n.id: n for n in graph.nodes}
    semantic = {x.id: x for field in ("nodes", "relations", "moves") for x in getattr(graph, field)}
    for field in COLLECTIONS:
        for obj in getattr(graph, field):
            register(obj.id, obj)
            for a in obj.anchors:
                m = messages.get(a.message_id)
                if m is None:
                    error("anchor_source", obj.id, a.message_id)
                elif a.end <= a.start or a.end > len(m.text) or m.text[a.start:a.end] != a.quote:
                    error("anchor_mismatch", obj.id, "quote/Unicode offsets do not match source")
            if hasattr(obj, "at_message_id"):
                at = messages.get(obj.at_message_id)
                if not at:
                    error("event_source", obj.id, obj.at_message_id)
                else:
                    if obj.actor_id != at.actor_id:
                        error("event_actor", obj.id, "event actor must be speaker at occurrence")
                    if not any(a.message_id == at.id for a in obj.anchors):
                        error("event_grounding", obj.id, "event needs anchor at its occurrence")
                if obj.actor_id not in actors:
                    error("unknown_actor", obj.id, obj.actor_id)
    def refs(obj, values, allowed=semantic):
        for ref in values:
            if ref not in allowed:
                error("dangling_reference", obj.id, ref)
    supersedes, order = nx.DiGraph(), nx.DiGraph()
    for r in graph.relations:
        sig = SIGNATURES[r.kind]
        counts = Counter(b.role for b in r.bindings)
        for role in counts.keys() - sig.keys():
            error("unknown_role", r.id, role)
        for role, kinds in sig.items():
            count = counts[role]
            if count < 1 or (count != 1 and not (r.kind == "supports" and role == "premise")):
                error("role_cardinality", r.id, role)
        if len({(b.role, b.ref) for b in r.bindings}) != len(r.bindings):
            error("duplicate_binding", r.id, "duplicate role player")
        refs(r, [b.ref for b in r.bindings])
        for b in r.bindings:
            if b.role in sig and b.ref in semantic:
                target = semantic[b.ref]
                kind = target.kind if b.ref in content else "relation_or_move"
                if "*" not in sig[b.role] and kind not in sig[b.role]:
                    error("role_type", r.id, f"{b.role} cannot target {kind}")
        if r.kind == "supersedes":
            roles = {b.role: b.ref for b in r.bindings}
            if "new" in roles and "old" in roles:
                supersedes.add_edge(roles["new"], roles["old"])
    moves = {m.id: m for m in graph.moves}
    for m in graph.moves:
        refs(m, m.input_ids + m.output_ids)
        refs(m, m.after_move_ids, moves)
        if not m.input_ids and not m.output_ids:
            error("empty_move", m.id, "move must involve content or a relation")
        for prior in m.after_move_ids:
            order.add_edge(prior, m.id)
            p = moves.get(prior)
            if p and p.at_message_id in messages and m.at_message_id in messages:
                if context[p.at_message_id] != context[m.at_message_id]:
                    error("cross_context_order", m.id, "after links require the same conversation; do not infer cross-chat chronology")
                elif messages[p.at_message_id].ordinal >= messages[m.at_message_id].ordinal:
                    error("temporal_order", m.id, "predecessor must occur earlier")
    for name, dag in (("supersession_cycle", supersedes), ("move_cycle", order)):
        if not nx.is_directed_acyclic_graph(dag):
            error(name, graph.id, "this subgraph must be acyclic")
    for s in graph.stance_events:
        refs(s, [s.target_id])
    status_keys = set()
    for e in graph.question_events:
        refs(e, [e.question_id], content)
        if e.question_id in content and content[e.question_id].kind != "question":
            error("question_type", e.id, "status target must be a question")
        refs(e, e.answer_ids, content)
        if e.status == "resolved" and not (e.answer_ids or e.resolution_basis):
            error("unsupported_resolution", e.id, "resolution needs answer or explicit basis")
        if e.status == "superseded" and not e.replacement_id:
            error("missing_replacement", e.id, "superseded question needs replacement")
        if e.replacement_id:
            refs(e, [e.replacement_id], content)
            if e.replacement_id == e.question_id or (e.replacement_id in content and content[e.replacement_id].kind != "question"):
                error("replacement_type", e.id, "replacement must be a different question")
        key = (e.actor_id, e.question_id, e.at_message_id)
        if key in status_keys:
            error("ambiguous_status", e.id, "multiple status events for actor/question at same occurrence")
        status_keys.add(key)
    # A dependency cycle may express circular reasoning or reciprocal questions. Flag, don't erase.
    deps = nx.DiGraph()
    for r in graph.relations:
        if r.kind == "depends_on" and r.review_status != "rejected":
            roles = {b.role: b.ref for b in r.bindings}
            if {"dependent", "prerequisite"} <= roles.keys():
                deps.add_edge(roles["dependent"], roles["prerequisite"])
    for component in nx.strongly_connected_components(deps):
        if len(component) > 1 or any(deps.has_edge(n, n) for n in component):
            warnings.append({"code": "dependency_cycle", "items": sorted(component)})
    return {"valid": not errors, "errors": errors, "warnings": warnings}


def require_valid(graph: Graph) -> Graph:
    report = validate(graph)
    if not report["valid"]:
        raise ValueError(report)
    return graph
