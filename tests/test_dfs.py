__author__ = "gjoshi"

from graph import Graph
from digraph import DiGraph
from algorithms.dfs import dfs


def test_dfs_on_graph_with_no_edges():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4, 5])

    assert dfs(g, 1) == [1]


def test_dfs_on_undirected_graph():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4, 5])
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    assert dfs(g, 1) == [1, 2, 4, 3]


def test_dfs_on_directed_graph():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4, 5])
    dg.add_edge(1, 2)
    dg.add_edge(1, 3)
    dg.add_edge(2, 4)
    dg.add_edge(3, 4)

    assert dfs(dg, 1) == [1, 2, 4, 3]