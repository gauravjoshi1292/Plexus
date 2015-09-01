__author__ = "gjoshi"

import Queue


def bfs(graph, source):
    bfs_path = []
    visited = {}
    queue = Queue.Queue()

    for node in graph.nodes_iter():
        visited[node] = False

    visited[source] = True
    queue.put(source)

    while not queue.empty():
        source = queue.get()
        bfs_path.append(source)

        for n in graph.adj[source]:
            if not visited[n]:
                visited[n] = True
                queue.put(n)

    return bfs_path