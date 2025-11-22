import pytest
from main import bfs_distances


# Normal tests (4)


def test_simple_line_distances():
    graph = {
        "Gate": ["A"],
        "A": ["Gate", "B"],
        "B": ["A", "C"],
        "C": ["B"],
    }
    dist = bfs_distances(graph, "Gate")
    assert dist == {"Gate": 0, "A": 1, "B": 2, "C": 3}


def test_star_graph_distances():
    graph = {
        "Gate": ["A", "B", "C"],
        "A": ["Gate"],
        "B": ["Gate"],
        "C": ["Gate"],
    }
    dist = bfs_distances(graph, "Gate")
    assert dist["Gate"] == 0
    assert dist["A"] == 1
    assert dist["B"] == 1
    assert dist["C"] == 1
    assert len(dist) == 4


def test_branching_graph_distances():
    graph = {
        "Gate": ["X", "Y"],
        "X": ["Gate", "Z"],
        "Y": ["Gate"],
        "Z": ["X"],
    }
    dist = bfs_distances(graph, "Gate")
    assert dist["X"] == 1
    assert dist["Y"] == 1
    assert dist["Z"] == 2


def test_graph_with_cycle_distances():
    graph = {
        "Gate": ["A"],
        "A": ["Gate", "B"],
        "B": ["A", "C"],
        "C": ["B", "Gate"],
    }
    dist = bfs_distances(graph, "Gate")
    # Either Gate->A->B or Gate->C->B, but shortest is length 2
    assert dist["B"] == 2


# Edge-case tests (3)


def test_start_not_in_graph_returns_empty():
    graph = {"A": ["B"], "B": ["A"]}
    dist = bfs_distances(graph, "Gate")
    assert dist == {}


def test_isolated_start_node():
    graph = {
        "Gate": [],
        "A": ["B"],
        "B": ["A"],
    }
    dist = bfs_distances(graph, "Gate")
    assert dist == {"Gate": 0}


def test_disconnected_components_only_reachable_recorded():
    graph = {
        "Gate": ["A"],
        "A": ["Gate"],
        "X": ["Y"],
        "Y": ["X"],
    }
    dist = bfs_distances(graph, "Gate")
    assert "Gate" in dist and "A" in dist
    assert "X" not in dist and "Y" not in dist


# Complex tests (3)


def test_larger_graph_mixed_structure():
    graph = {
        "Gate": ["S1", "S2"],
        "S1": ["Gate", "S3", "S4"],
        "S2": ["Gate", "S5"],
        "S3": ["S1"],
        "S4": ["S1", "S6"],
        "S5": ["S2"],
        "S6": ["S4"],
    }
    dist = bfs_distances(graph, "Gate")
    assert dist["Gate"] == 0
    assert dist["S1"] == 1
    assert dist["S2"] == 1
    assert dist["S3"] == 2
    assert dist["S4"] == 2
    assert dist["S5"] == 2
    assert dist["S6"] == 3


@pytest.mark.parametrize(
    "start,expected",
    [
        ("S1", {"S1": 0, "Gate": 1, "S3": 1, "S4": 1, "S2": 2, "S5": 3, "S6": 2}),
        ("S5", {"S5": 0, "S2": 1, "Gate": 2, "S1": 3, "S3": 4, "S4": 4, "S6": 5}),
    ],
)
def test_parametrized_starts(start, expected):
    graph = {
        "Gate": ["S1", "S2"],
        "S1": ["Gate", "S3", "S4"],
        "S2": ["Gate", "S5"],
        "S3": ["S1"],
        "S4": ["S1", "S6"],
        "S5": ["S2"],
        "S6": ["S4"],
    }
    dist = bfs_distances(graph, start)
    assert dist == expected


def test_large_tree_structure():
    # A simple tree of 8 nodes
    graph = {
        "Gate": ["A", "B"],
        "A": ["Gate", "C", "D"],
        "B": ["Gate", "E"],
        "C": ["A"],
        "D": ["A"],
        "E": ["B", "F", "G"],
        "F": ["E"],
        "G": ["E"],
    }
    dist = bfs_distances(graph, "Gate")
    assert dist["F"] == 3
    assert dist["G"] == 3
    assert len(dist) == 8
