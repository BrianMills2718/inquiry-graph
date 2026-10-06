import json
from pathlib import Path

from inquiry_graph.frame_view import FrameProfile, project_frame, validate_frame_profile
from inquiry_graph.io import load
from inquiry_graph.model import Graph

ROOT = Path(__file__).parents[1]

CASES = [
    (
        "examples/seed/graph.json",
        "evaluation/frame_profiles/seed-candidate-generation-frame.json",
        {"model_hypothesis", "criterion"},
    ),
    (
        "examples/operational-games-2026-09-30/graph.json",
        "evaluation/frame_profiles/operational-games-frame.json",
        {"model_hypothesis", "boundary_access"},
    ),
    (
        "examples/conversations/2026-10-05-semantic-modeling/graph.json",
        "evaluation/frame_profiles/semantic-modeling-frame.json",
        {"model_hypothesis", "criterion"},
    ),
]


def load_profile(path: str) -> FrameProfile:
    return FrameProfile.model_validate(
        json.loads((ROOT / path).read_text(encoding="utf-8"))
    )


def test_real_frame_profiles_resolve_against_real_graphs():
    for graph_path, profile_path, expected_optional in CASES:
        graph = load(ROOT / graph_path, Graph)
        profile = load_profile(profile_path)
        assert validate_frame_profile(graph, profile) == []
        view = project_frame(graph, profile)
        assert set(view["roles"]) >= {"content", "applies_to", "active_query"}
        assert set(view["optional_coordinates_present"]) == expected_optional
        assert view["projection_only"] is True


def test_cross_case_invariant_is_thin():
    for graph_path, profile_path, _ in CASES:
        view = project_frame(load(ROOT / graph_path, Graph), load_profile(profile_path))
        assert "content" in view["roles"]
        assert "applies_to" in view["roles"]
        assert "active_query" in view["roles"]

    seed = project_frame(load(ROOT / CASES[0][0], Graph), load_profile(CASES[0][1]))
    ops = project_frame(load(ROOT / CASES[1][0], Graph), load_profile(CASES[1][1]))
    current = project_frame(load(ROOT / CASES[2][0], Graph), load_profile(CASES[2][1]))

    assert "boundary_access" not in seed["roles"]
    assert "criterion" not in ops["roles"]
    assert current["perspective_actor_id"] == "participant:brian"


def test_profile_rejects_unknown_refs_and_actor():
    graph = load(ROOT / CASES[2][0], Graph)
    profile = load_profile(CASES[2][1])
    profile.content.refs = ["missing"]
    profile.perspective_actor_id = "participant:missing"
    assert validate_frame_profile(graph, profile) == [
        "unknown frame ref for content: missing",
        "unknown frame perspective actor: participant:missing",
    ]
