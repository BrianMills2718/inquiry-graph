import pytest

from inquiry_graph.kept_markdown import parse_kept_markdown

DOC = '''---
id: "abc"
platform: "claude"
title: "A title"
synced: 2026-10-03T15:57:26.093Z
messages: 3
tags:
  - "kept/claude"
---

# A title

### You — 2026-01-01T10:00:00.000Z

I think X.

### Step 1 — not a message header

### Assistant — 2026-01-01T10:00:05.000Z

Reply with a heading below.

### Step 2 — still the assistant

### tool — 2026-01-01T10:00:06.000Z

{"tool": "output"}
'''


def test_parses_speakers_and_keeps_inner_headings():
    conv, skipped = parse_kept_markdown(DOC)
    assert conv.id == "claude:abc" and conv.title == "A title"
    assert [m.actor_id for m in conv.messages] == ["participant:brian", "participant:assistant"]
    assert "### Step 2" in conv.messages[1].text and "### Step 1" in conv.messages[0].text
    assert skipped["tool"] == 1 and conv.messages[0].timestamp == "2026-01-01T10:00:00.000Z"
    assert "COMPLETENESS WARNING" not in conv.coverage_note


def test_declared_count_mismatch_is_flagged_not_hidden():
    conv, _ = parse_kept_markdown(DOC.replace("messages: 3", "messages: 9"))
    assert "COMPLETENESS WARNING" in conv.coverage_note


def test_missing_frontmatter_fails_loudly():
    with pytest.raises(ValueError):
        parse_kept_markdown("### You — 2026-01-01T10:00:00.000Z\nhi\n")
