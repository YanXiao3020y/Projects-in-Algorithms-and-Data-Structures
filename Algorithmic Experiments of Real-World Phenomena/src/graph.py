# explanations for member functions are provided in requirements.py
# each file that uses a graph should import it from this file.
from collections import defaultdict
from collections.abc import Iterable


class Graph:
    # initialize the graph a given number of nodes and given edges.
    # edges are represented as tuples (u, v), where each edge is between node with index u and
    # node with index v.
    def __init__(self, num_nodes: int, edges: Iterable[tuple[int, int]]):
        self.num_nodes = num_nodes
        # self.num_edges = len(edges) # due to https://edstem.org/us/courses/38696/discussion/3150896
        self.num_edges = 0
        self.adjacency_list = defaultdict(set) # https://www.algotree.org/algorithms/adjacency_list/graph_as_adjacency_list_python/
        for u, v in edges:
            self.num_edges += 1
            self.adjacency_list[u].add(v)
            self.adjacency_list[v].add(u)

    # returns the number of nodes in the graph.
    def get_num_nodes(self) -> int:
        return self.num_nodes

    # returns the number of edges in the graph.
    def get_num_edges(self) -> int:
        return self.num_edges

    # given a node index, return an iterable type over the collection of its neighbors.
    # the iterable type can be a list, set, generator, etc.
    # each neighbor should appear exactly once.
    def get_neighbors(self, node: int) -> Iterable[int]:
        return self.adjacency_list[node]

    def is_adjacent(self, u: int, w: int) -> bool:
        if w in self.adjacency_list[u]:
            return True
        return False

# feel free to define new methods in addition to the above
# fill in the definitions of each required member function (above),
# and for any additional member functions you define
