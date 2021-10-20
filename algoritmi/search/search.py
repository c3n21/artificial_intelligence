from typing import Set, List
from .graph import Graph
from .node import Node

def depth_first_search(
    graph: Graph, start: str, goal: str,
    key = lambda n: n.label,
    visited: Set = set(), path: List[Node] = []) -> List[Node]:

    current = graph.getNode(start)

    if current is None or current in visited:
        return []

    visited.add(current)

    if current.label == goal:
        path.insert(0, current)
        return path

    adj = list(current.adj.keys())
    adj.sort(key=key)

    for adj_node in adj:
        res = depth_first_search(graph, adj_node.label, goal, key, visited)
        if res != []: # arrivato al goal
            path.insert(0, current)
            return path

    return path

def breadth_first_search(graph: Graph):
    
    pass
