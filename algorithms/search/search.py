from typing import Set, List
from ds.graph import Graph
from ds.node import Node

def depth_first_search(
    graph: Graph, start: str, goal: str,
    key = lambda n: n.label,
    eql: Set = set(), path: List[Node] = []) -> List[Node]:

    root = graph.getNode(start)

    if root is None or root in eql:
        return []

    eql.add(root)

    if root.label == goal:
        path.insert(0, root)
        return path

    adj = list(root.adj.keys())
    adj.sort(key=key)

    for adj_node in adj:
        res = depth_first_search(graph, adj_node.label, goal, key, eql)
        if res != []: # arrivato al goal
            path.insert(0, root)
            return path

    return path

def breadth_first_search(
    graph: Graph, start: str, goal: str) -> List[Node]:

    root = graph.getNode(start)

    if root is None:
        return []

    eql      = set()
    frontier = [root]
    path     = []
    prevs    = {}

    while frontier != []:
        current = frontier.pop()
        adjacents = current.getAdjacents()
        for adj_node in adjacents:
            if prevs.get(adj_node) is None:
                prevs[adj_node] = current

            if adj_node.label == goal:
                while adj_node != root:
                    path.insert(0, adj_node)
                    adj_node = prevs[adj_node]
                path.insert(0, adj_node) #put root
                return path
            else:
                if adj_node not in eql:
                    eql.add(current)
                    frontier.insert(0, adj_node)

    return path
