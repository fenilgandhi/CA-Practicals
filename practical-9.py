'''
Implementation of Graph Searching (DFS and BFS).
'''


def Graph_DFS(graph, start):
    path = []
    queue = [start]

    while len(queue) > 0:
        next_node = queue.pop(-1)
        if next_node not in path:
            path += [next_node]
            queue += graph[next_node][::-1]

    print("Depth First Traversal of graph gives {0} ".format(path))


def Graph_BFS(graph, start):
    path = [start]

    index = 0
    while (index < len(path)):
        next_node = path[index]
        path += [i for i in graph[next_node] if i not in path]
        index += 1

    print("Breadth First Traversal of graph gives {0} ".format(path))


if __name__ == '__main__':
    '''
           1
         / | \
        2  3  4
       / \    |
      5   6   7
     /  \
    8    9
'''
    graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '3': [],
        '4': ['7'],
        '5': ['8', '9'],
        '6': [],
        '7': [],
        '8': [],
        '9': [],
    }

    Graph_DFS(graph, '1')
    Graph_BFS(graph, '1')
