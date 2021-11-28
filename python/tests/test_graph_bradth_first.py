from challenges.graph_breadth_first.graph_breadth_first import Graph

def test_breadth_first():

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
 
    assert g.BFS(2) == [2, 0, 3, 1]