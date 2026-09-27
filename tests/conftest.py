from pathlib import Path
import pytest
from inquiry_graph.io import load
from inquiry_graph.model import Graph

ROOT=Path(__file__).resolve().parents[1]
@pytest.fixture
def graph():
    return load(ROOT/'examples/seed/graph.json',Graph)
