__author__ = "gjoshi"


def dfs_util(graph, v, visited, dfs_path):
    visited[v] = True
    dfs_path.append(v)

    for node in graph.adj[v]:
        if not visited[node]:
            dfs_util(graph, node, visited, dfs_path)


def dfs(graph, source):
    visited = {}
    dfs_path = []

    for node in graph.nodes_iter():
        visited[node] = False

    dfs_util(graph, source, visited, dfs_path)

    return dfs_path