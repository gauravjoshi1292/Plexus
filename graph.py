__author__ = "gjoshi"


class Graph(object):
    def __init__(self):
        self.no_of_nodes = 0
        self.no_of_edges = 0
        self.nodes = []
        self.edges = []
        self.adj = {}

    def add_node(self, node):
        self.nodes.append(node)
        self.adj[node] = []

    def add_nodes_from(self, list_of_nodes):
        for node in list_of_nodes:
            self.nodes.append(node)
            self.adj[node] = []

    def add_edge(self, source, destination):
        self.adj[source].append(destination)
        self.adj[destination].append(source)

    def nodes_iter(self):
        return iter(self.nodes)