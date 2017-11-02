{
    "Author": "Fenil Gandhi",
    "Version": "Python 3.6.2",
    "Description": "Implement Kruskal’s algorithm",
    "Input Parameters": "Graph Object constructed using each edge",
    "Input": {
        (0, 1): 7,
        (0, 3): 8,
        (1, 2): 6,
        (1, 3): 3,
        (2, 3): 4,
        (2, 4): 2,
        (2, 5): 5,
        (3, 4): 3,
        (4, 5): 2,
    },
    "Output": "Using Krushkal's Algorithm, we get MST having 17 units weight of edges [(2, 4), (4, 5), (1, 3), (3, 4), (0, 1)]",

}


class Graph():
    def __init__(self):
        self.vertices = set()
        self.edges = {}

    def addEdge(self, a, b, length):
        self.edges[(a, b)] = length
        self.vertices.update((a, b))

    def Krushkals(self):
        mst_weight = 0
        mst_edges = []
        mst_sets = [[i] for i in self.vertices]

        edges = sorted(self.edges, key=lambda x: self.edges[x])

        for edge in edges:
            a, b = edge
            for temp_set in mst_sets:
                if a in temp_set:
                    set_a = temp_set
                if b in temp_set:
                    set_b = temp_set

            if (set_a == set_b):
                continue
            else:
                mst_edges += [edge]
                mst_weight += self.edges[edge]
                mst_sets.remove(set_a)
                mst_sets.remove(set_b)
                mst_sets.append(set_a + set_b)

        print("Using Krushkal's Algorithm, we get MST having {0} units weight of edges {1}".format(mst_weight, mst_edges))


if __name__ == '__main__':
    graph = Graph()
    graph.addEdge(0, 1, 7)
    graph.addEdge(0, 3, 8)
    graph.addEdge(1, 2, 6)
    graph.addEdge(1, 3, 3)
    graph.addEdge(2, 3, 4)
    graph.addEdge(2, 4, 2)
    graph.addEdge(2, 5, 5)
    graph.addEdge(3, 4, 3)
    graph.addEdge(4, 5, 2)
    graph.Krushkals()
