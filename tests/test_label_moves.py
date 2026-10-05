import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location("label_moves", Path(__file__).resolve().parents[1] / "tools/label_moves.py")
lm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lm)


def test_vocabulary_is_the_agreed_set():
    ontology = Path(__file__).resolve().parents[1] / "docs/ontology.md"
    text = ontology.read_text()
    inhouse = [m for m in lm.MOVES if m not in {"define_by_role", "frame_as_hypothesis", "request_example", "factor_and_check", "step_back", "none_of_these"}]
    assert len(inhouse) == 15 and all(f"`{m}`" in text for m in inhouse)
    assert len(lm.MOVES) == 21 and set(lm.POLICY) == {"prior_art_first", "over_engineering_critique"}
    assert not set(lm.POLICY) & set(lm.MOVES)


def test_seed_list_has_22_unique_entries():
    assert len(set(lm.SEEDS)) == len(lm.SEEDS) == 22
