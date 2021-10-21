from typing import List

class Node:
    def __init__(self, label: str) -> None:
        self.adj = {} # type: dict['Node', int]
        self.label = label # type: str

    def addAdjancent(self, new: 'Node', d : int) -> bool:
        self.adj[new] = d
        return True

    def getAdjacents(self) -> List['Node']:
        return list(self.adj.keys())

    def __str__(self) -> str:
        return f"Node '{self.label}'"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Node) and o.label == self.label

    def __hash__(self) -> int:
        return self.label.__hash__()
