from inquiry_graph.linker import Position, collect_positions, recall_pairs


def _p(pid, chat):
    return Position(id=pid, chat_id=chat, chat_title=chat, date=None, kind='claim', stance='posits', text=pid, quote=pid)


def test_recall_pairs_are_cross_chat_and_nearest_only():
    ps = [_p('a1', 'A'), _p('a2', 'A'), _p('b1', 'B'), _p('b2', 'B'), _p('c1', 'C')]
    vec = {'a1': [1, 0, 0], 'a2': [0.99, 0.1, 0], 'b1': [0.98, 0.05, 0.1], 'b2': [0, 1, 0], 'c1': [0, 0.1, 1]}
    pairs = recall_pairs(ps, vec, k=1, floor=0.3)
    assert all({a[0], b[0]} != {a[0]} for a, b, _ in pairs)  # never within one chat
    assert ('a1', 'b1') in {(a, b) for a, b, _ in pairs}
    assert not any('a2' in (a, b) and 'b2' in (a, b) for a, b, _ in pairs)  # below floor


def test_collect_positions_keeps_actor_stances_status_and_quotes(graph):
    brian = next(p.id for p in graph.conversations[0].participants if p.role == 'user')
    ps = collect_positions(graph, brian)
    assert ps and all(p.chat_id == graph.conversations[0].id for p in ps)
    ids = {p.id for p in ps}
    assert len(ids) == len(ps)  # one position per target
    nodes = {n.id: n for n in graph.nodes}
    for p in ps[:20]:
        assert p.text == nodes[p.id].text and p.quote
    questions = [p for p in ps if p.kind == 'question']
    assert any(p.question_status for p in questions)
