from typing import List, Optional

from .node import Node

class Graph:
    """
    Undirected graph implementation
    """

    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = set(nodes)

    def addEdge(self, src: Node, dst: Node, weight: int) -> bool:
        """Adds and edge to from `src` to `dst` with `weight`"""
        return src.addAdjancent(dst, weight) and dst.addAdjancent(src, weight)

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
