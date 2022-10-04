edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]

def shortest_path(edges, src, dst):
    graph = build_graph(edges)
    return bfs(graph, src, dst)

def build_graph(edges):
    graph = dict()

    for e in edges:
        a, b = e

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[b].append(a)
        graph[a].append(b)

    return graph

def bfs(graph, start, dst):
    visited = dict()
    q = [[start, 0]]

    while len(q) > 0:
        curr = q.pop(0)
        curr_node, d_start = curr
        visited[curr_node] = True

        if curr_node == dst:
            return d_start

        for n in graph[curr_node]:
            if n not in visited:
                q.append([n, d_start + 1])

    return -1

def main():
    shortest = shortest_path(edges, 'w', 'z')
    print(f'shortest path is len: {shortest}')

if __name__ == "__main__":
    main()
