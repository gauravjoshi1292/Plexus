__author__ = "gjoshi"


def is_cyclic_util(graph, node, parent, visited, curr_path):
    visited[node] = True
    curr_path[node] = True

    for n in graph.adj[node]:
        if n != parent and curr_path[n]:
            return True

        if not visited[n] and is_cyclic_util(graph, n, node, visited, curr_path):
            return True

    curr_path[node] = False
    return False


def is_cyclic(graph):
    visited = {}
    curr_path = {}
    parent = -1

    for node in graph.nodes_iter():
        visited[node] = False
        curr_path[node] = False

    for node in graph.nodes_iter():
        if not visited[node]:
            if is_cyclic_util(graph, node, parent, visited, curr_path):
                return True

    return False


def is_dag_util(graph, node, visited, curr_path):
    visited[node] = True
    curr_path[node] = True

    for n in graph.adj[node]:
        if curr_path[n]:
            return False

        if not visited[n] and not is_dag_util(graph, n, visited, curr_path):
            return False

    curr_path[node] = False

    return True


def is_dag(graph):
    visited = {}
    curr_path = {}

    for node in graph.nodes_iter():
        visited[node] = False
        curr_path[node] = False

    for node in graph.nodes_iter():
        if not visited[node]:
            if not is_dag_util(graph, node, visited, curr_path):
                return False

    return True