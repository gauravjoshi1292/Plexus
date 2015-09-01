__author__ = "gjoshi"

import pytest
from algorithms.reachability import is_reachable, get_path
from graph import Graph
from digraph import DiGraph
from exception import PathNotFoundError


def test_reachability_on_undirected_graph():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4, 5])
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    assert is_reachable(g, 1, 2)
    assert is_reachable(g, 2, 1)
    assert is_reachable(g, 1, 3)
    assert is_reachable(g, 3, 1)
    assert is_reachable(g, 1, 4)
    assert is_reachable(g, 4, 1)
    assert is_reachable(g, 2, 3)
    assert is_reachable(g, 3, 2)
    assert is_reachable(g, 2, 4)
    assert is_reachable(g, 4, 2)
    assert is_reachable(g, 3, 4)
    assert is_reachable(g, 4, 3)


def test_source_is_reachable_from_source():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])

    assert is_reachable(dg, 1, 1)


def test_destination_is_reachable_if_path_exists():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(4, 2)

    assert is_reachable(dg, 1, 4)


def test_destination_is_not_reachable_if_path_does_not_exists():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)

    assert not is_reachable(dg, 1, 5)


def test_get_path_returns_path_when_source_and_destination_are_same():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])

    assert get_path(dg, 1, 1) == [1]


def test_get_path_returns_path_when_path_exists():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(4, 2)

    assert get_path(dg, 1, 4) == [1, 2, 3, 4]


def test_get_path_raises_path_not_found_error_if_no_path_exists():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(4, 2)

    with pytest.raises(PathNotFoundError):
        get_path(dg, 1, 5)