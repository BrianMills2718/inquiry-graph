"""Derived frame projection over Inquiry Graph objects.

A frame profile is intentionally a thin sidecar. It does not add a core Frame
node kind and it does not require every method-specific framing coordinate to
exist. The invariant cross-case roles are frame content, inquiry scope, and an
active query; optional coordinates reuse distinctions already present in
method-specific formalisms such as participant-relative game framing.
"""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .model import COLLECTIONS, Graph


class FrameRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


Recovery = Literal["direct", "reconstructed", "analyst"]


class FrameBinding(FrameRecord):
    refs: list[str] = Field(min_length=1)
    recovery: Recovery = "direct"
    rationale: str | None = None


class FrameProfile(FrameRecord):
    schema_version: Literal["1.0.0"] = "1.0.0"
    id: str = Field(min_length=1)
    label: str = Field(min_length=1)

    # Cross-case invariant roles.
    content: FrameBinding
    applies_to: FrameBinding
    active_query: FrameBinding

    # Optional method-/case-specific coordinates.
    perspective_actor_id: str | None = None
    model_hypothesis: FrameBinding | None = None
    criterion: FrameBinding | None = None
    boundary_access: FrameBinding | None = None
    resources: FrameBinding | None = None

    note: str | None = None


def _objects(graph: Graph):
    return {
        x.id: x
        for collection in COLLECTIONS
        for x in getattr(graph, collection)
        if x.review_status != "rejected"
    }


def _participants(graph: Graph) -> set[str]:
    return {
        participant.id
        for conversation in graph.conversations
        for participant in conversation.participants
    }


def validate_frame_profile(graph: Graph, profile: FrameProfile) -> list[str]:
    obj = _objects(graph)
    errors: list[str] = []
    for role in (
        "content",
        "applies_to",
        "active_query",
        "model_hypothesis",
        "criterion",
        "boundary_access",
        "resources",
    ):
        binding = getattr(profile, role)
        if binding is None:
            continue
        for ref in binding.refs:
            if ref not in obj:
                errors.append(f"unknown frame ref for {role}: {ref}")
    if (
        profile.perspective_actor_id is not None
        and profile.perspective_actor_id not in _participants(graph)
    ):
        errors.append(
            f"unknown frame perspective actor: {profile.perspective_actor_id}"
        )
    return errors


def project_frame(graph: Graph, profile: FrameProfile) -> dict:
    errors = validate_frame_profile(graph, profile)
    if errors:
        raise ValueError("; ".join(errors))

    obj = _objects(graph)
    roles = {}
    recovery = {}
    for role in (
        "content",
        "applies_to",
        "active_query",
        "model_hypothesis",
        "criterion",
        "boundary_access",
        "resources",
    ):
        binding = getattr(profile, role)
        if binding is None:
            continue
        roles[role] = [
            {
                "id": ref,
                "kind": getattr(obj[ref], "kind", obj[ref].__class__.__name__.lower()),
                "label": getattr(obj[ref], "text", getattr(obj[ref], "kind", ref)),
                "review_status": obj[ref].review_status,
            }
            for ref in binding.refs
        ]
        recovery[role] = binding.recovery

    return {
        "frame_id": profile.id,
        "label": profile.label,
        "perspective_actor_id": profile.perspective_actor_id,
        "roles": roles,
        "recovery": recovery,
        "optional_coordinates_present": [
            role
            for role in ("model_hypothesis", "criterion", "boundary_access", "resources")
            if getattr(profile, role) is not None
        ],
        "note": profile.note,
        "projection_only": True,
    }
