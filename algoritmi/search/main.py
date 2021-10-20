from .graph import Graph
from .node import Node
from .search import depth_first_search

if __name__ == "__main__":
    start = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    g = Node("G")

    nodes = [start, b, c, d, e, f, g]

    graph = Graph(nodes)
    graph.addEdge(start, b, 5)
    graph.addEdge(start, f, 5)
    graph.addEdge(b, d, 3)
    graph.addEdge(b, c, 7)
    graph.addEdge(f, d, 3)
    graph.addEdge(f, g, 5)
    graph.addEdge(d, g, 4)
    graph.addEdge(g, e, 3)

    print(depth_first_search(graph, start.label, e.label))
