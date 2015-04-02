__author__ = "gjoshi"


import Queue
from exception import PathNotFoundError


def is_reachable(graph, source, destination):
    if source == destination:
        return True

    visited = {}

    for node in graph.nodes_iter():
        visited[node] = False

    queue = Queue.Queue()

    visited[source] = True
    queue.put(source)

    while not queue.empty():
        source = queue.get()

        for n in graph.adj[source]:
            if n == destination:
                return True

            if not visited[n]:
                visited[n] = True
                queue.put(n)

    return False


def construct_path(predecessors, source, destination):
    path = []
    start = destination

    while start != source:
        path.append(start)
        start = predecessors[start]

    path.append(start)
    path.reverse()
    return path


def get_path(graph, source, destination):
    visited = {}
    predecessors = {}
    start = source

    if source == destination:
        return construct_path(predecessors, source, destination)

    for node in graph.nodes_iter():
        visited[node] = False
        predecessors[node] = None

    queue = Queue.Queue()

    visited[source] = True
    queue.put(source)

    while not queue.empty():
        source = queue.get()

        for n in graph.adj[source]:
            if n == destination:
                predecessors[n] = source
                return construct_path(predecessors, start, destination)

            if not visited[n]:
                visited[n] = True
                predecessors[n] = source
                queue.put(n)

    raise PathNotFoundError(start, destination)