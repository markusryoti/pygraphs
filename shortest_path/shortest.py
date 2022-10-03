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
            graph[a] = [b]
        else:
            graph[a].append(b)

        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)

    return graph

def bfs(graph, start, dst):
    shortest = 100
    visited = dict()

    q = [[start, 0]]

    while len(q) > 0:
        curr = q.pop(0)
        curr_node, d_from_start = curr[0], curr[1]
        visited[curr_node] = True

        if curr_node == dst:
            if d_from_start < shortest:
                shortest = d_from_start

        d_from_start += 1

        for n in graph[curr_node]:
            if n not in visited:
                q.append([n, d_from_start])

    return shortest

def main():
    shortest = shortest_path(edges, 'w', 'z')
    print(f'shortest path is len: {shortest}')

if __name__ == "__main__":
    main()
