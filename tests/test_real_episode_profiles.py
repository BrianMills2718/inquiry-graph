import json
from pathlib import Path

from inquiry_graph.episode_view import ReasoningEpisodeProfile, project_episode, validate_profile
from inquiry_graph.io import load
from inquiry_graph.model import Graph

ROOT = Path(__file__).parents[1]

CASES = [
    (
        "examples/seed/graph.json",
        "evaluation/reasoning_episode_profiles/seed-candidate-generation.json",
        7,
    ),
    (
        "examples/operational-games-2026-09-30/graph.json",
        "evaluation/reasoning_episode_profiles/operational-games-compositional-world.json",
        7,
    ),
    (
        "examples/conversations/2026-10-05-semantic-modeling/graph.json",
        "evaluation/reasoning_episode_profiles/semantic-modeling-partial.json",
        5,
    ),
]


def load_profile(path: str) -> ReasoningEpisodeProfile:
    return ReasoningEpisodeProfile.model_validate(
        json.loads((ROOT / path).read_text(encoding="utf-8"))
    )


def test_real_episode_profiles_resolve_against_real_graphs():
    for graph_path, profile_path, expected_roles in CASES:
        graph = load(ROOT / graph_path, Graph)
        profile = load_profile(profile_path)
        assert validate_profile(graph, profile) == []
        view = project_episode(graph, profile)
        assert view["coverage"]["bound_roles"] == expected_roles
        assert view["coverage"]["analyst"] == 0


def test_real_episode_recovery_is_not_uniformly_direct():
    seed = project_episode(
        load(ROOT / CASES[0][0], Graph),
        load_profile(CASES[0][1]),
    )
    ops = project_episode(
        load(ROOT / CASES[1][0], Graph),
        load_profile(CASES[1][1]),
    )
    current = project_episode(
        load(ROOT / CASES[2][0], Graph),
        load_profile(CASES[2][1]),
    )

    assert seed["coverage"] == {
        "bound_roles": 7,
        "direct": 5,
        "reconstructed": 2,
        "analyst": 0,
    }
    assert ops["coverage"] == {
        "bound_roles": 7,
        "direct": 6,
        "reconstructed": 1,
        "analyst": 0,
    }
    assert current["coverage"] == {
        "bound_roles": 5,
        "direct": 3,
        "reconstructed": 2,
        "analyst": 0,
    }
    assert "evaluation" not in current["roles"]
    assert "update" not in current["roles"]
