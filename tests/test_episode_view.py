from inquiry_graph.episode_view import (
    EpisodeRoleBinding,
    ReasoningEpisodeProfile,
    project_episode,
    validate_profile,
)
from inquiry_graph.model import Anchor, Conversation, Graph, Message, Node, Participant


ROLES = [
    "salient_condition",
    "frame",
    "candidate",
    "evaluation",
    "commitment",
    "action_or_test",
    "update",
]


def make_graph(prefix: str, texts: list[str]) -> Graph:
    message = Message(
        id=f"{prefix}:m1",
        actor_id="participant:user",
        ordinal=1,
        text=" | ".join(texts),
    )
    nodes = []
    offset = 0
    for i, text in enumerate(texts):
        start = message.text.index(text, offset)
        offset = start + len(text)
        nodes.append(
            Node(
                id=f"{prefix}:n{i}",
                anchors=[Anchor(message_id=message.id, start=start, end=offset, quote=text)],
                origin="explicit",
                review_status="proposed",
                kind="hypothesis" if i in (1, 2) else "claim",
                text=text,
            )
        )
    conversation = Conversation(
        id=f"{prefix}:conversation",
        title=prefix,
        source_kind="curated_excerpts",
        coverage_note="Minimal test fixture for derived reasoning-episode projection.",
        participants=[Participant(id="participant:user", label="User", role="user")],
        messages=[message],
    )
    return Graph(id=prefix, conversations=[conversation], nodes=nodes)


def make_profile(prefix: str, label: str) -> ReasoningEpisodeProfile:
    return ReasoningEpisodeProfile(
        id=f"{prefix}:episode",
        label=label,
        bindings=[
            EpisodeRoleBinding(role=role, refs=[f"{prefix}:n{i}"])
            for i, role in enumerate(ROLES)
        ],
        note="Projection-only test profile.",
    )


def test_same_episode_profile_shape_covers_three_regimes():
    cases = {
        "org": [
            "project feels stalled",
            "feedback/control frame",
            "simplify and clarify roles",
            "compare interventions against clarity and feedback",
            "commit to a reframing experiment",
            "test a smaller problem frame",
            "revise the active frame",
        ],
        "tech": [
            "real validator fails",
            "expected-vs-observed diagnostic frame",
            "RPC-vs-streams diagnosis",
            "compare candidate causes against validator evidence",
            "commit to architecture-level repair",
            "rerun the real validator",
            "revise the diagnosis/model",
        ],
        "ent": [
            "aspiration plus available capabilities",
            "paid-engagement opportunity frame",
            "candidate bounded engagement",
            "evaluate fit, downside, and learning value",
            "commit to a small engagement",
            "deliver and measure",
            "update future capability/feasible space",
        ],
    }

    for prefix, texts in cases.items():
        graph = make_graph(prefix, texts)
        profile = make_profile(prefix, prefix)
        assert validate_profile(graph, profile) == []
        view = project_episode(graph, profile)
        assert list(view["roles"]) == ROLES
        assert view["projection_only"] is True


def test_profile_rejects_unknown_refs():
    graph = make_graph("bad", ["a", "b", "c", "d", "e", "f", "g"])
    profile = make_profile("bad", "bad")
    profile.bindings[0].refs = ["missing"]
    assert validate_profile(graph, profile) == [
        "unknown episode ref for salient_condition: missing"
    ]
