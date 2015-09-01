__author__ = "gjoshi"

from graph import Graph


class DiGraph(Graph):
    def __int__(self):
        super(DiGraph, self).__init__()

    def add_edge(self, source, destination):
        self.adj[source].append(destination)