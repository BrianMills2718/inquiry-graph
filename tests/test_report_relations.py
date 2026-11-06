"""The readable report must carry reasons and replacements as text, not bare IDs (usefulness pilot, issue #38)."""
from inquiry_graph.render import report, _clip


def _roles(rel):
    return {b.role: b.ref for b in rel.bindings}


def test_motivates_reason_and_result_text_appear_together(graph):
    text = {n.id: n.text for n in graph.nodes}
    out = report(graph)
    rel = next(r for r in graph.relations if r.kind == "motivates" and r.review_status != "rejected")
    roles = _roles(rel)
    line = next(l for l in out.splitlines() if l.startswith("- ") and "*because:*" in l
                and _clip(text[roles["reason"]]).split("…")[0][:60] in l)
    assert _clip(text[roles["result"]]).split("…")[0][:60] in line.split(" — ")[0]
    assert "## Decisions and reasons" in out


def test_supersedes_reads_old_replaced_by_new(graph):
    text = {n.id: n.text for n in graph.nodes}
    out = report(graph)
    rel = next(r for r in graph.relations if r.kind == "supersedes")
    roles = _roles(rel)
    old, new = (_clip(text[roles[k]])[:60] for k in ("old", "new"))
    assert any(old in l and "*was replaced by:*" in l and new in l.split("*was replaced by:*")[1] for l in out.splitlines())


def test_move_inputs_and_outputs_show_node_text_not_ids(graph):
    out = report(graph)
    move = next(m for m in graph.moves if m.output_ids and m.review_status != "rejected")
    assert f"Outputs: {move.output_ids[0]}" not in out
    text = {n.id: n.text for n in graph.nodes}
    assert _clip(text[move.output_ids[0]], 80)[:50] in out
