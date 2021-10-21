from typing import List, Optional

from .node import Node

class Graph:
    """Graph not oriented"""
    def __init__(self, nodes: List[Node]) -> None:
        self.nodes    = set(nodes)

    def addEdge(self, v: Node, u: Node, d: int) -> bool:
        return v.addAdjancent(u, d) and u.addAdjancent(v, d)

    def getNode(self, label: str) -> Optional[Node]:
        for node in self.nodes:
            if node.label == label:
                return node

    def __str__(self) -> str:
        s = ""
        for node in self.nodes:
            s = s + str(node) + " -> " + str(list(node.adj.keys())) + "\n"
        return s

    def __repr__(self) -> str:
        return self.__str__()
