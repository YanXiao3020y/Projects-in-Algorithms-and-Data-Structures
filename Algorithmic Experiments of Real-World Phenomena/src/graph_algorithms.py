# explanations for these functions are provided in requirements.py
from collections import deque
import random
from graph import Graph, defaultdict


def BFS(node: int, graph: Graph) -> (int, int):
    visited = set()
    queue = deque([(node, 0)])  # using deque instead of list is to increase the efficiency
    farthest_node = node
    farthest_distance = 0

    while queue:
        current_node, distance = queue.popleft()
        visited.add(current_node)

        if distance > farthest_distance:
            farthest_node = current_node
            farthest_distance = distance

        for neighbor in graph.get_neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return farthest_node, farthest_distance


def get_diameter(graph: Graph) -> int:
    random_vertex = random.randint(0, graph.get_num_nodes()-1)
    d_max = 0

    while True:
        random_vertex, farthest_distance = BFS(random_vertex, graph)
        if farthest_distance <= d_max:
            return d_max  # maybe need to add 1 later (from discussion)??? check grapescope test cases later to decide
        d_max = farthest_distance


def d_degeneracy_ordering(graph: Graph):
    l = set()
    l1 = []

    # Compute a number, dv, for each vertex v in G, which is the number of
    # neighbors of v that are not already in L. Initially, dv is just the degrees of v.
    degrees = {}
    vertices = list(range(0, graph.get_num_nodes()))  # since graph of vertex start from 0, and end at graph.get_num_nodes()-1
    # print(vertices)  # ??? need to verify later since the online explanation is different from experimental test case
    for v in vertices:
        degrees[v] = len(graph.get_neighbors(v))
    # print("degrees: ", degrees)

    # Initialize an array D such that D[i] contains a list of the vertices v that are not
    # already in L for which dv = i.
    d = [[] for _ in vertices]
    index = 0
    for value in degrees.values():
    # for index, value in enumerate(degrees):
        d[value].append(index)
        index += 1
    # print("d: ", d)

    n_v = [[] for _ in vertices]# Let Nv be a list of the neighbors of v that come before v in L
    k = 0
    i = 0  # index of d
    for _ in vertices:
        for sublist in d:   # Let i be the smallest index such that D[i] is nonempty.
        # for i, sublist in enumerate(d):
            if sublist:
                break
            i += 1
        k = max(k, i)
        v = sublist.pop()
        l.add(v)
        l1.append(v)
        # print(i, v)
        for neighbor in graph.get_neighbors(v):
            if neighbor not in l:
                d[degrees[neighbor]].remove(neighbor)
                degrees[neighbor] -= 1

                d[degrees[neighbor]].append(neighbor)
                # new_degree = degrees[neighbor]
                # if new_degree in d:
                #     d[new_degree].append(neighbor)
                # else:
                #     d[new_degree] = [neighbor]

                n_v[v].append(neighbor)

    return n_v, l1


def triangle_counting(graph: Graph) -> int:
    n_v, l = d_degeneracy_ordering(graph)
    num_triangles = 0
    for v in l:
    #     for u in n_v[v]:
    #         for w in n_v[v]:
    #             is_triangle = graph.is_adjacent(u, w)
    #             if is_triangle:
    #                 num_triangles += 1
    # return num_triangles / 2  # divided by 2 due to two ways of edge, u->w & w->u

        end = len(n_v[v])
        for u in range(0, end):
            for w in range(u, end):
                is_triangle = graph.is_adjacent(n_v[v][u], n_v[v][w])
                if is_triangle:
                    num_triangles += 1
    return num_triangles  # divided by 2 due to two ways of edge, u->w & w->u


    # num_triangles = 0
    # for u in graph.adjacency_list:
    #     if len(graph.adjacency_list) >= 2:
    #         for v in graph.adjacency_list[u]:
    #             if not v == u:
    #                 for w in graph.adjacency_list[u]:
    #                     if (not v == w) and (not w == u):
    #                         if w in graph.adjacency_list[v]:
    #                             num_triangles += 1
    # return num_triangles / 6


def num_of_2_edge_paths(graph: Graph) -> int:
    denominator = 0
    vertices = list(range(0, graph.get_num_nodes()))

    for v in vertices:
        degree = len(graph.get_neighbors(v))
        denominator += (degree * (degree - 1)) / 2

    return denominator


def get_clustering_coefficient(graph: Graph) -> float:
    num_triangles = triangle_counting(graph)
    denominator = num_of_2_edge_paths(graph)

    if denominator == 0:
        clustering_coefficient = 0
    else:
        clustering_coefficient = (3 * num_triangles) / denominator

    return clustering_coefficient


def get_degree_distribution(graph: Graph) -> dict[int, int]:
    degree = []
    vertices = list(range(0, graph.get_num_nodes()))
    for v in vertices:
        degree.append(len(graph.get_neighbors(v)))
    # print("degree: ", degree)

    h = [0] * graph.get_num_nodes()
    for v in vertices:
        h[degree[v]] += 1

    output = {}  # convert h to dict since the test cases require dict, and not contains 0 value
    for index, value in enumerate(h):
        if value != 0:
            output[index] = value

    return output

