# This class represent a graph
class Graph:

    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values()
                 for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

# This class represents a Node


class Node:

    # Initialize the class
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        # self.g = 0  # distance to start node
        # self.h = 0  # distance to goal node
        # self.f = 0  # total cost
        self.value = 0

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.value < other.value

    # Print node
    def __repr__(self):
        return ('{0}, {1}'.format(self.name, self.f))


# # A* Algorithm
# def astar_algorithm(graph, heuristics, start, end):
#     i = 0
#     # create lists for open nodes and closed nodes
#     open = []
#     closed = []

#     # create a start node and a goal node
#     start_node = Node(start, None)
#     end_node = Node(end, None)

#     # add the start node
#     open.append(start_node)

#     # loop until the open list is empty
#     while len(open) > 0:

#         # sort the open list to get the node with the lowest cost first
#         open.sort()

#         # get the node with the lowest cost and
#         # add it to the closed list
#         current_node = open.pop(0)
#         closed.append(current_node)

#         # if we have reached the goal, return the path
#         if current_node == end_node:
#             path = []
#             while current_node != start_node:
#                 path.append((current_node.name, current_node.g))
#                 current_node = current_node.parent
#             path.append((start_node.name, start_node.g))
#             # reverse the path and return
#             return path[::-1]

#         # get neighbors
#         neighbors = graph.get(current_node.name)

#         # loop neighbors
#         for key, value in neighbors.items():

#             # create neigbor node
#             neighbor = Node(key, current_node)

#             # check if neigbor has already been dealt with, i.e. is in the closed list
#             if (neighbor in closed):
#                 continue

#             # calculate full path cost
#             neighbor.g = current_node.g + \
#                 graph.get(current_node.name, neighbor.name)
#             neighbor.h = heuristics.get(neighbor.name)
#             neighbor.f = neighbor.g + neighbor.h

#             # check if neighbor is in open list and if it has a lower f value
#             if add_to_open(open, neighbor):
#                 open.append(neighbor)

#         i += 1
#         if i % 1000 == 0:
#             print(
#                 f"open: {len(open)} / closed: {len(closed)} / all nodes: {len(graph.nodes())}")

#     # if no path is found, return None
#     return None


# # helper function to check if a neighbor should be added to the open list
# def add_to_open(open, neighbor):
#     for node in open:
#         if (neighbor == node and neighbor.f > node.f):
#             return False
#     return True
