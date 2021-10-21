from ds.graph import Graph
from ds.node import Node
from algorithms.search.search import breadth_first_search, depth_first_search

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

    print(f"Graph = \n{graph}")
    print(f"Path DFS = {depth_first_search(graph, start.label, e.label)}")
    print(f"Path BFS = {breadth_first_search(graph, start.label, e.label)}")
