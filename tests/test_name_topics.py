import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from name_topics import carry_names, parents  # noqa: E402


def test_each_subtopic_gets_the_broader_topic_holding_most_of_its_members():
    topics = [
        {"topic": "L1:0", "layer": "L1", "members": ["a", "b", "c"]},
        {"topic": "L1:1", "layer": "L1", "members": ["d", "e", "f", "g"]},
        # spans both broad topics; most members are in L1:1, so that is its parent
        {"topic": "L0:0", "layer": "L0", "members": ["c", "d", "e"]},
        {"topic": "L0:1", "layer": "L0", "members": ["a", "b"]},
        # members the broader layer left out give no parent
        {"topic": "L0:2", "layer": "L0", "members": ["z"]},
    ]
    layers, up = parents(topics)
    assert layers == ["L0", "L1"]
    assert up == {"L0:0": "L1:1", "L0:1": "L1:0"}


def test_a_rebuilt_topic_keeps_its_name_only_when_most_members_are_the_same():
    old = [{"topic": "L0:0", "members": ["a", "b", "c", "d"]}, {"topic": "L0:1", "members": ["x", "y"]}]
    names = {"L0:0": "Budget caps", "L0:1": "Map colours"}
    new = [
        {"topic": "L0:5", "members": ["a", "b", "c", "e"]},       # 3 of 5 shared: renumbered, same topic
        {"topic": "L0:6", "members": ["x", "p", "q", "r"]},       # 1 of 5 shared: a different topic, needs a new name
        {"topic": "L0:7", "members": ["n"]},                      # brand new
    ]
    assert carry_names(new, old, names) == {"L0:5": "Budget caps"}
