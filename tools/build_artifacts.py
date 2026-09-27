"""Generate reviewable artifacts; --check detects drift without overwriting files."""
import argparse
import json
from pathlib import Path
from inquiry_graph.model import Graph, Candidates, Conversation
from inquiry_graph.io import load
from inquiry_graph.render import mermaid, dot, report, html_view
from inquiry_graph.validate import require_valid

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--check',action='store_true')
a=p.parse_args()
graph=require_valid(load(ROOT/'examples/seed/graph.json',Graph))
outputs={
    **{f'schemas/{name}.schema.json':json.dumps(cls.model_json_schema(),ensure_ascii=False,indent=2)+'\n'
       for name,cls in [('graph',Graph),('candidates',Candidates),('conversation',Conversation)]},
    'examples/seed/inquiry-map.md':'# Recorded inquiry moves\n\nTemporal succession is not causation. All annotations are proposed; source attribution remains in graph.json.\n\n'+mermaid(graph,'inquiry'),
    'examples/seed/full-map.md':'# Full reified graph\n\nContent, relations and moves; use the smaller inquiry map first.\n\n'+mermaid(graph),
    'examples/seed/inquiry.dot':dot(graph,'inquiry'),
    'examples/seed/report.md':report(graph),
    'examples/seed/inspector.html':html_view(graph),
}
drift=[]
for name,text in outputs.items():
    path=ROOT/name
    if a.check:
        if not path.exists() or path.read_text(encoding='utf-8')!=text:
            drift.append(name)
    else:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text,encoding='utf-8')
if drift:
    raise SystemExit('Generated artifact drift: '+', '.join(drift))
print(f'{"Checked" if a.check else "Generated"} {len(outputs)} artifacts')
