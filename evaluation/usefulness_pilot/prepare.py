"""Build the three reading conditions for the usefulness pilot (issue #38).

A: real transcript, visible user/assistant text only, cut at the last message
   that contains a seed excerpt. B: the 219 curated excerpts. C: the graph's
   human-readable report. Private derivatives go under private/usefulness/.
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRIV = ROOT / "private/usefulness"
norm = lambda s: re.sub(r"\s+", " ", s).strip()

raw = (PRIV / "founding-chat.md").read_text(encoding="utf-8")
blocks = re.split(r"^## (user|assistant|tool) \(([^)]*)\)\s*$", raw, flags=re.M)
msgs = [{"role": blocks[i], "at": blocks[i + 1], "text": blocks[i + 2].strip()}
        for i in range(1, len(blocks) - 2, 3)]
visible = [m for m in msgs if m["role"] in ("user", "assistant") and m["text"]]

excerpts = json.loads((ROOT / "examples/seed/source-excerpts.json").read_text(encoding="utf-8"))["messages"]
# Align each excerpt to the first message containing it. Short excerpts such as
# "Okay, do that." recur later in the chat and would push the cutoff forward.
last = -1
for e in excerpts:
    needle = norm(e["text"])
    if len(needle) < 30:
        continue
    first = next((i for i, m in enumerate(visible) if needle in norm(m["text"])), -1)
    last = max(last, first)
if last < 0:
    sys.exit("no excerpt matched the transcript; refusing to build an unaligned condition")

span = visible[: last + 1]
speaker = {"user": "BRIAN", "assistant": "ASSISTANT"}
a = "\n\n".join(f"[{i}] {speaker[m['role']]} ({m['at'][:16]}):\n{m['text']}" for i, m in enumerate(span))
b = "\n\n".join(f"[{e['id'].split(':')[-1]}] {'BRIAN' if e['actor_id'].endswith('brian') else 'ASSISTANT'}: {e['text']}" for e in excerpts)
c = (ROOT / "examples/seed/report.md").read_text(encoding="utf-8")

for name, text in (("A_transcript.txt", a), ("B_excerpts.txt", b), ("C_graph_report.md", c)):
    (PRIV / name).write_text(text, encoding="utf-8")
    print(f"{name}: {len(text):,} chars")
print(f"transcript span: {len(span)} visible messages, {span[0]['at'][:16]} .. {span[-1]['at'][:16]}")
