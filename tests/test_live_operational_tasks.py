"""Task-state extraction regression: an instruction is not an attributed belief."""
from collections import Counter

from inquiry_graph.model import Conversation, Graph, Message, Participant
from inquiry_graph.live_extract import (
    INSTRUCTIONS, MEETING_INSTRUCTIONS, LChunk, convert, prompt_version,
)
from inquiry_graph.validate import validate
from inquiry_graph.views import open_questions


def test_live_instruction_requires_task_not_stance():
    assert "unfinished research" in INSTRUCTIONS
    assert "an open status event" in INSTRUCTIONS
    assert "Substantive" in MEETING_INSTRUCTIONS
    assert "tasks" in prompt_version()


def test_convert_accepts_open_task_and_preserves_speaker():
    user = Participant(id="participant:user", label="User", role="user")
    assistant = Participant(id="participant:assistant", label="ChatGPT", role="assistant")
    request = Message(id="request", actor_id=user.id, ordinal=1,
                      text="Please compare all five frameworks and do not invent a new factorization.")
    progress = Message(id="progress", actor_id=assistant.id, ordinal=2,
                       text="I am now finishing the scenario-by-scenario judgments; implementation tests remain open.")
    conv = Conversation(id="task-dialogue", title="Task terminal state", source_kind="normalized",
                        coverage_note="Synthetic regression exercising an explicit terminal task",
                        participants=[user, assistant], messages=[request, progress])
    out = LChunk.model_validate({
        "nodes": [{"key": "comparison", "kind": "task",
                   "text": "Complete the five-case comparison before implementation tests.",
                   "message": 2, "quote": progress.text}],
        "question_events": [{
            "speaker": "assistant", "question": "comparison", "status": "open",
            "message": 2, "quote": progress.text}],
        "stances": [{"speaker": "user", "target": "comparison", "stance": "endorses",
                     "message": 1, "quote": request.text}]
    })
    drops = Counter()
    candidates = convert(conv, 0, out, drops)
    graph = Graph(id="task-state-test", conversations=[conv],
                  nodes=candidates.nodes, question_events=candidates.question_events,
                  stance_events=[])
    # Only the assistant reported active work; no user belief or endorsement is inferred.
    assert not graph.stance_events
    assert len(graph.nodes) == 1
    assert graph.nodes[0].kind == "task"
    assert len(graph.question_events) == 1
    assert graph.question_events[0].actor_id == assistant.id
    assert validate(graph)["valid"], validate(graph)["errors"]
    agenda = open_questions(graph)
    assert len(agenda) == 1
    assert agenda[0]["status"] == "open"
    assert "five-case comparison" in agenda[0]["text"]
    assert drops["task_is_not_stance"] == 1\n    assert sum(drops.values()) == 1
