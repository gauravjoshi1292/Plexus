__author__ = "gjoshi"

from graph import Graph
from digraph import DiGraph
from algorithms.cycle_check import is_dag, is_cyclic


def test_is_cyclic_with_empty_graph_returns_false():
    g = Graph()
    assert not is_cyclic(g)


def test_is_cyclic_with_graph_containing_single_node_returns_false():
    g = Graph()
    g.add_node(1)

    assert not is_cyclic(g)


def test_is_cyclic_with_graph_containing_self_loop_returns_true():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 1)

    assert is_cyclic(g)


def test_is_cyclic_with_graph_containing_parallel_edges_returns_false():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edge(1, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    assert not is_cyclic(g)


def test_is_cyclic_with_graph_containing_complex_cycle_returns_true():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)

    assert is_cyclic(g)


def test_is_cyclic_with_acyclic_graph_returns_false():
    g = Graph()
    g.add_nodes_from([1, 2, 3, 4])
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    assert not is_cyclic(g)


def test_is_dag_with_empty_graph_returns_true():
    dg = DiGraph()
    assert is_dag(dg)


def test_is_dag_with_graph_containing_single_node_returns_true():
    dg = DiGraph()
    dg.add_node(1)

    assert is_dag(dg)


def test_is_dag_with_dag_returns_true():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)

    assert is_dag(dg)


def test_is_dag_with_graph_containing_self_loop_returns_false():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(1, 1)

    assert not is_dag(dg)


def test_is_dag_with_graph_containing_simple_cycle_returns_false():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4])
    dg.add_edge(1, 2)
    dg.add_edge(2, 1)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)

    assert not is_dag(dg)


def test_is_dag_with_graph_containing_complex_cycle_returns_false():
    dg = DiGraph()
    dg.add_nodes_from([1, 2, 3, 4])
    dg.add_edge(1, 2)
    dg.add_edge(2, 3)
    dg.add_edge(3, 4)
    dg.add_edge(4, 1)

    assert not is_dag(dg)