from types import FunctionType
from typing import Set, List
from python.ds.graph import Graph
from python.ds.node import Node

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
        if res != []:
            path.insert(0, root)
            return path

    return path

def breadth_first_search(
    graph: Graph, start: str, goal: str,
    expand: FunctionType, select: FunctionType) -> List[Node]:

    root = graph.getNode(start)

    if root is None:
        return []

    eql      = set()
    frontier = [root]
    path     = []
    prevs    = {}

    while frontier != []:
        current = select(frontier) # type: Node
        if current in eql:
            continue

        if current.label == goal:
            while current != root:
                path.insert(0, current)
                current = prevs[current]
            path.insert(0, current) #put root
            return path
        else:
            expanded = expand(current) # type: List[Node]

            for node in expanded:
                if prevs.get(node) is None:
                    prevs[node] = current

            eql.add(current)
            frontier.extend(expanded) # type: List[Node]

    return path

def uniform_cost_search(graph: Graph) -> None:

    pass
