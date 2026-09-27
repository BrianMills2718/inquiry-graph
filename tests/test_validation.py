from copy import deepcopy
import pytest
from pydantic import ValidationError
from inquiry_graph.model import Anchor, Node, Relation, Binding, QuestionEvent, anchor
from inquiry_graph.validate import validate


def codes(g):
    return {e['code'] for e in validate(g)['errors']}


def test_seed_valid(graph):
    assert validate(graph)=={'valid':True,'errors':[],'warnings':[]}
    assert len(graph.nodes)>=40 and len(graph.moves)>=25
    assert sum(n.kind=='question' for n in graph.nodes)>=15
    assert all(x.review_status=='proposed' for x in graph.nodes)


def test_unicode_anchor(graph):
    m=graph.conversations[0].messages[0].model_copy(update={'text':'α😀 z 😀'})
    a=anchor(m,'😀',1)
    assert (a.start,a.end)==(5,6) and m.text[a.start:a.end]==a.quote
    with pytest.raises(ValueError,match='ambiguous'):anchor(m,'😀')
    with pytest.raises(ValueError,match='not found'):anchor(m,'no')
    with pytest.raises(ValueError):anchor(m,'')
    with pytest.raises(ValueError):anchor(m,'😀',4)


@pytest.mark.parametrize('mutation,code',[
    ('offset','anchor_mismatch'),('quote','anchor_mismatch'),('source','anchor_source'),
    ('duplicate','duplicate_id'),('actor','event_actor'),('role','unknown_role'),
    ('cardinality','role_cardinality'),('type','role_type'),('dangling','dangling_reference'),
    ('temporal','temporal_order'),('empty_move','empty_move'),('question_type','question_type'),
    ('resolution','unsupported_resolution'),('replacement','missing_replacement'),
    ('source_order','source_order'),('event_grounding','event_grounding'),
])
def test_negative_invariants(graph,mutation,code):
    if mutation=='offset':graph.nodes[0].anchors[0].end+=1
    elif mutation=='quote':graph.nodes[0].anchors[0].quote='invented'
    elif mutation=='source':graph.nodes[0].anchors[0].message_id='missing'
    elif mutation=='duplicate':graph.nodes.append(graph.nodes[0].model_copy())
    elif mutation=='actor':graph.moves[0].actor_id='participant:assistant'
    elif mutation=='role':graph.relations[0].bindings[0].role='untyped'
    elif mutation=='cardinality':graph.relations[0].bindings=graph.relations[0].bindings[:1]
    elif mutation=='type':
        r=next(r for r in graph.relations if r.kind=='answers')
        r.bindings[1].ref=next(n.id for n in graph.nodes if n.kind=='claim')
    elif mutation=='dangling':graph.moves[0].output_ids=['unknown']
    elif mutation=='temporal':graph.moves[0].after_move_ids=[graph.moves[-1].id]
    elif mutation=='empty_move':graph.moves[0].input_ids=[];graph.moves[0].output_ids=[]
    elif mutation=='question_type':graph.question_events[0].question_id=next(n.id for n in graph.nodes if n.kind=='claim')
    elif mutation=='resolution':graph.question_events[0].status='resolved'
    elif mutation=='replacement':graph.question_events[0].status='superseded'
    elif mutation=='source_order':graph.conversations[0].messages[1].ordinal=1
    elif mutation=='event_grounding':graph.moves[0].anchors=graph.moves[1].anchors
    assert code in codes(graph)


def test_supersession_cycle(graph):
    r=next(r for r in graph.relations if r.kind=='supersedes')
    new=r.model_copy(deep=True)
    new.id='cycle'
    new.bindings[0].ref,new.bindings[1].ref=new.bindings[1].ref,new.bindings[0].ref
    graph.relations.append(new)
    assert 'supersession_cycle' in codes(graph)


def test_dependency_cycle_is_warning(graph):
    n=graph.nodes[0]
    graph.relations.append(Relation(id='self-dependency',kind='depends_on',
        bindings=[Binding(role='dependent',ref=n.id),Binding(role='prerequisite',ref=n.id)],anchors=n.anchors))
    r=validate(graph)
    assert r['valid'] and r['warnings'][0]['code']=='dependency_cycle'


def test_relation_can_be_challenged(graph):
    graph.relations[0].bindings[1].ref=graph.relations[1].id
    assert validate(graph)['valid']


def test_about_relation_accepts_reflective_targets(graph):
    subject=next(n for n in graph.nodes if n.id.endswith(':episode-self-application'))
    target=next(n for n in graph.nodes if n.id.endswith(':current-meta-model'))
    graph.relations.append(Relation(id='reflective-about',kind='about',
        bindings=[Binding(role='subject',ref=subject.id),Binding(role='object',ref=target.id)],anchors=subject.anchors))
    assert validate(graph)['valid']


def test_schema_rejects_extra_fields_and_unknown_kind(graph):
    data=graph.nodes[0].model_dump()
    data['truth_probability']=.97
    with pytest.raises(ValidationError):Node.model_validate(data)
    del data['truth_probability'];data['kind']='belief-certified'
    with pytest.raises(ValidationError):Node.model_validate(data)


def test_duplicate_status_at_occurrence(graph):
    e=graph.question_events[0].model_copy(deep=True);e.id='duplicate-status'
    graph.question_events.append(e)
    assert 'ambiguous_status' in codes(graph)


def test_cross_conversation_after_is_not_guessed(graph):
    from inquiry_graph.model import Conversation,Message
    actor=graph.conversations[0].participants[0]
    msg=Message(id='other:m',actor_id=actor.id,ordinal=1,text='Another conversation')
    graph.conversations.append(Conversation(id='other',title='Other',source_kind='normalized',
        coverage_note='Synthetic temporal test',participants=[actor],messages=[msg]))
    move=graph.moves[0].model_copy(deep=True)
    move.id='other:move';move.at_message_id=msg.id;move.anchors=[anchor(msg,msg.text)]
    move.after_move_ids=[graph.moves[-1].id]
    graph.moves.append(move)
    assert 'cross_context_order' in codes(graph)
