"""Executable V1 ontology. Structural types are separate from semantic validation."""
from enum import Enum
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Record(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class Participant(Record):
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    role: Literal["user", "assistant", "other"]


class Message(Record):
    id: str = Field(min_length=1)
    actor_id: str
    ordinal: int = Field(ge=1)
    text: str = Field(min_length=1)
    original_id: str | None = None
    timestamp: str | None = None


class Conversation(Record):
    id: str = Field(min_length=1)
    title: str
    source_kind: Literal["curated_excerpts", "chatgpt_export", "normalized"]
    coverage_note: str = Field(min_length=1)
    participants: list[Participant]
    messages: list[Message]


class Anchor(Record):
    message_id: str
    start: int = Field(ge=0)
    end: int = Field(ge=1)
    quote: str = Field(min_length=1)


class Grounded(Record):
    id: str = Field(min_length=1)
    anchors: list[Anchor] = Field(min_length=1)
    origin: Literal["explicit", "inferred"] = "inferred"
    review_status: Literal["proposed", "confirmed", "rejected"] = "proposed"


NodeKind = Literal["concept", "claim", "question", "hypothesis", "method", "example", "goal", "reference"]


class Node(Grounded):
    kind: NodeKind
    text: str = Field(min_length=1)


class Binding(Record):
    role: str
    ref: str


RelationKind = Literal[
    "supports", "challenges", "depends_on", "distinguishes", "reframes", "motivates",
    "answers", "exemplifies", "candidate_for", "part_of", "related_to", "supersedes"
]


class Relation(Grounded):
    kind: RelationKind
    bindings: list[Binding] = Field(min_length=2)


MoveKind = Literal[
    "ask", "clarify", "distinguish", "challenge", "retract", "hypothesize",
    "generalize", "deduce", "test", "reframe", "decompose", "connect", "scope",
    "summarize", "propose"
]


class Move(Grounded):
    kind: MoveKind
    actor_id: str
    input_ids: list[str]
    output_ids: list[str]
    at_message_id: str
    after_move_ids: list[str] = Field(default_factory=list)
    inference_family: Literal["induction", "abduction", "deduction", "unspecified"] = "unspecified"


class StanceEvent(Grounded):
    actor_id: str
    target_id: str
    stance: Literal["posits", "endorses", "questions", "rejects", "suspends", "retracts"]
    at_message_id: str


class QuestionEvent(Grounded):
    question_id: str
    status: Literal["open", "answered", "resolved", "deferred", "superseded", "reopened"]
    actor_id: str
    at_message_id: str
    answer_ids: list[str] = Field(default_factory=list)
    resolution_basis: str | None = None
    replacement_id: str | None = None


class Extraction(Record):
    method: str
    provider: str | None = None
    model: str | None = None
    prompt_version: str = "1.0.0"
    notes: list[str] = Field(default_factory=list)


class Candidates(Record):
    nodes: list[Node] = Field(default_factory=list)
    relations: list[Relation] = Field(default_factory=list)
    moves: list[Move] = Field(default_factory=list)
    stance_events: list[StanceEvent] = Field(default_factory=list)
    question_events: list[QuestionEvent] = Field(default_factory=list)


class Graph(Candidates):
    schema_version: Literal["1.0.0"] = "1.0.0"
    id: str
    conversations: list[Conversation]
    extractions: list[Extraction] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


# role -> (permitted target kinds; '*' permits any content, relation or move)
# First role points into relation; relation points to second role in graph views.
SIGNATURES = {
    "supports": {"premise": {"claim", "hypothesis", "example"}, "conclusion": {"claim", "hypothesis"}},
    "challenges": {"challenger": {"claim", "hypothesis", "example", "question"}, "target": {"*"}},
    "depends_on": {"dependent": {"*"}, "prerequisite": {"*"}},
    "distinguishes": {"left": {"*"}, "right": {"*"}},
    "reframes": {"original": {"question"}, "replacement": {"question"}},
    "motivates": {"reason": {"*"}, "result": {"*"}},
    "answers": {"answer": {"claim", "hypothesis", "method", "example"}, "question": {"question"}},
    "exemplifies": {"example": {"example"}, "general": {"*"}},
    "candidate_for": {"candidate": {"*"}, "problem": {"question", "goal"}},
    "part_of": {"part": {"*"}, "whole": {"*"}},
    "related_to": {"source": {"*"}, "target": {"*"}},
    "supersedes": {"new": {"*"}, "old": {"*"}},
}


COLLECTIONS = ("nodes", "relations", "moves", "stance_events", "question_events")


def anchor(message: Message, quote: str, occurrence: int | None = None) -> Anchor:
    """Ground a quote with Unicode character offsets; never silently pick a duplicate."""
    if not quote:
        raise ValueError("empty quote")
    starts, pos = [], 0
    while (pos := message.text.find(quote, pos)) >= 0:
        starts.append(pos)
        pos += 1
    if not starts:
        raise ValueError(f"quote not found in {message.id}")
    if occurrence is None and len(starts) != 1:
        raise ValueError(f"ambiguous quote in {message.id}; specify zero-based occurrence")
    index = 0 if occurrence is None else occurrence
    if index < 0 or index >= len(starts):
        raise ValueError("quote occurrence out of range")
    start = starts[index]
    return Anchor(message_id=message.id, start=start, end=start + len(quote), quote=quote)
