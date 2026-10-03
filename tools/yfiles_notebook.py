"""Write a Jupyter notebook that shows an Inquiry Graph graph with yFiles Graphs for Jupyter (good automatic layouts).

yFiles for Jupyter is free only for per-user, interactive use inside JupyterLab/Notebook. Its licence forbids using it in an
automated process, outside Jupyter, or redistributing it, so the output here is a notebook to open locally, never a page to
publish. Its analytics may send anonymised usage data (label texts replaced by placeholders) to yWorks.
"""
import argparse
import json
from pathlib import Path

import nbformat as nbf

LOADER = r'''import json, collections
from yfiles_jupyter_graphs import GraphWidget

GRAPH = {path!r}
g = json.load(open(GRAPH))
nodes = {{n["id"]: n for n in g["nodes"]}}
KIND_COLOUR = {{"concept": "#4363d8", "claim": "#f58231", "hypothesis": "#911eb4", "question": "#ffe119",
               "goal": "#3cb44b", "method": "#46f0f0", "example": "#a9a9a9", "reference": "#808000", "group": "#e8e8e8"}}   # no red/green pairing

def short(t, n=60):
    t = " ".join(t.split()); return t if len(t) <= n else t[: n - 1] + "…"

w_nodes = [{{"id": n["id"], "properties": {{"label": short(n["text"]), "kind": n["kind"], "text": n["text"],
            "quote": (n["anchors"][0]["quote"] if n["anchors"] else "")}}}} for n in g["nodes"]]
w_edges = []
for r in g["relations"]:
    roles = {{b["role"]: b["ref"] for b in r["bindings"]}}
    ends = list(roles.values())
    if len(ends) >= 2:
        w_edges.append({{"id": r["id"], "start": ends[0], "end": ends[1],
                        "properties": {{"label": r["kind"], "quote": (r["anchors"][0]["quote"] if r["anchors"] else "")}}}})
# The extracted graph is sparse (many ideas have no relation), so group ideas by the conversation chunk they came from
# (the cNN in each id). Each group is a labelled box; relations still link ideas across boxes.
import re
chunk_of = lambda i: (re.search(r":(c\d+):", i) or [None, "c00"])[1]
groups = sorted({{chunk_of(n["id"]) for n in w_nodes}})
w_nodes += [{{"id": "group:" + c, "properties": {{"label": "Part " + str(int(c[1:]) + 1), "kind": "group", "text": "", "quote": ""}}}} for c in groups]
parent_of = {{n["id"]: "group:" + chunk_of(n["id"]) for n in w_nodes if not n["id"].startswith("group:")}}
print(f"{{len(w_nodes)}} nodes, {{len(w_edges)}} relations; kinds:", dict(collections.Counter(n['kind'] for n in g['nodes'])))
'''
SHOW = '''w = GraphWidget()
w.nodes, w.edges = w_nodes, w_edges
w.directed = True
w.node_label_mapping = lambda n: n["properties"]["label"]
w.edge_label_mapping = lambda e: e["properties"]["label"]
w.node_color_mapping = lambda n: KIND_COLOUR.get(n["properties"]["kind"], "#cccccc")
w.node_type_mapping = lambda n: n["properties"]["kind"]
w.node_parent_mapping = lambda n: parent_of.get(n["id"])
w.organic_layout()
w.show()'''
LAYOUTS = '''# Try another layout by running one of: w.organic_layout(), w.hierarchical_layout(), w.orthogonal_layout(), w.circular_layout(), w.tree_layout(), w.radial_layout()
# Click a node to see its text and the exact quote it came from in the side panel.'''


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("graph_json", type=Path)
    ap.add_argument("out_ipynb", type=Path)
    a = ap.parse_args()
    nb = nbf.v4.new_notebook()
    nb.cells = [nbf.v4.new_markdown_cell(f"# Inquiry Graph: {a.graph_json.name}\nPrivate: contains exact quotes. Open locally only."),
                nbf.v4.new_code_cell(LOADER.format(path=str(a.graph_json.resolve()))),
                nbf.v4.new_code_cell(SHOW), nbf.v4.new_code_cell(LAYOUTS)]
    a.out_ipynb.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, a.out_ipynb)
    print(f"wrote {a.out_ipynb}")


if __name__ == "__main__":
    main()
