'''
Implement prim’s algorithm
'''

class Graph():
    def __init__(self):
        self.vertices = []
        self.edges = {}
        self.max_len = -1

    def addEdge(self, a, b, length):
        if a not in self.vertices:
            self.vertices.append(a)
            self.edges[a] = {}

        if b not in self.vertices:
            self.vertices.append(b)
            self.edges[b] = {}

        self.edges[a][b] = length
        self.edges[b][a] = length

        if length > self.max_len:
            self.max_len = length + 1

    def getEdges(self, a):
        if a in self.vertices:
            return self.edges[a]

    def Prims(self, starting_node):
        mst_weight = 0
        mst_edges = []
        distance_to_nodes = dict([(v, (self.max_len, None)) for v in self.vertices])

        # Add the starting node
        distance_to_nodes[starting_node] = (-1, None)
        for vertex, length in self.getEdges(starting_node).items():
            if (distance_to_nodes[vertex][0] > length):
                distance_to_nodes[vertex] = (length, starting_node)

        while True:
            min_edge = self.max_len
            selected_vertex = None

            for vertex, length in distance_to_nodes.items():
                # Vertex already selected
                if length[0] < 0:
                    continue
                elif (length[0] < min_edge):
                    selected_vertex = vertex
                    min_edge = length[0]

            if (min_edge == self.max_len):
                break
            else:
                mst_edges.append((distance_to_nodes[selected_vertex][1], selected_vertex))
                mst_weight += distance_to_nodes[selected_vertex][0]
                distance_to_nodes[selected_vertex] = (-1, None)

                for vertex, length in self.getEdges(selected_vertex).items():
                    if (distance_to_nodes[vertex][0] > length):
                        distance_to_nodes[vertex] = (length, selected_vertex)

        print("Using Prim's Algorithm, we get MST having {0} weight of edges {1}".format(mst_weight, mst_edges))


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
    graph.Prims(0)
