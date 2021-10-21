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

# OLD
#def uniform_cost_search(graph: Graph, start: str, goal: str) -> List[Node]:
#    def expand(node: Node) -> List[Node]:
#        nodes = node.getAdjacents()
#        nodes.sort(key=lambda n: node.getDistance(n))
#        return nodes
#
#    def select(nodes: List[Node]) -> Node:
#        return nodes.pop()
#
#    return breadth_first_search(graph, start, goal, expand, select) # type: ignore

def uniform_cost_search(graph: Graph, start: str, goal: str) -> List[Node]:
    path = []
    root = graph.getNode(start)
    frontier = [root]
    exl = set()
    prev = {}
    
    while frontier != []:
        #select
        current = frontier.pop()

        if current is not None and current not in exl:
            #expansion
            expanded = current.getAdjacents()
            expanded.sort(key=lambda n: current.getDistance(n))

            for node in expanded:
                if prev.get(node) is None:
                    prev[node] = current

            exl.add(current)

            if current.label == goal:
                while current != root:
                    path.insert(0, current)
                    current = prev[current]
                path.insert(0, current)
                return path

            frontier.extend(expanded)
    return path
