"""Derived reasoning-episode projection over an Inquiry Graph.

This module deliberately does not extend the core Graph schema. An episode
profile assigns existing graph objects to cross-case reasoning roles so the
same query shape can be tested across different inquiry regimes.
"""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .model import COLLECTIONS, Graph


class EpisodeRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


EpisodeRole = Literal[
    "salient_condition",
    "frame",
    "candidate",
    "evaluation",
    "commitment",
    "action_or_test",
    "update",
]


class EpisodeRoleBinding(EpisodeRecord):
    role: EpisodeRole
    refs: list[str] = Field(min_length=1)


class ReasoningEpisodeProfile(EpisodeRecord):
    schema_version: Literal["1.0.0"] = "1.0.0"
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)
    bindings: list[EpisodeRoleBinding] = Field(min_length=1)
    note: str | None = None


def _objects(graph: Graph):
    return {
        x.id: x
        for collection in COLLECTIONS
        for x in getattr(graph, collection)
        if x.review_status != "rejected"
    }


def validate_profile(graph: Graph, profile: ReasoningEpisodeProfile) -> list[str]:
    """Return validation errors without changing graph semantics."""
    obj = _objects(graph)
    errors: list[str] = []
    seen: set[str] = set()
    for binding in profile.bindings:
        if binding.role in seen:
            errors.append(f"duplicate episode role: {binding.role}")
        seen.add(binding.role)
        for ref in binding.refs:
            if ref not in obj:
                errors.append(f"unknown episode ref for {binding.role}: {ref}")
    return errors


def project_episode(graph: Graph, profile: ReasoningEpisodeProfile) -> dict:
    """Return a stable role-oriented view over existing graph objects."""
    errors = validate_profile(graph, profile)
    if errors:
        raise ValueError("; ".join(errors))
    obj = _objects(graph)
    roles = {}
    for binding in profile.bindings:
        roles[binding.role] = [
            {
                "id": ref,
                "kind": getattr(obj[ref], "kind", obj[ref].__class__.__name__.lower()),
                "label": getattr(obj[ref], "text", getattr(obj[ref], "kind", ref)),
                "review_status": obj[ref].review_status,
            }
            for ref in binding.refs
        ]
    return {
        "episode_id": profile.id,
        "label": profile.label,
        "roles": roles,
        "note": profile.note,
        "projection_only": True,
    }
