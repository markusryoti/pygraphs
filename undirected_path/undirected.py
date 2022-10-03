edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def build_graph(edges):
    graph = {}

    for edge in edges:
        a, b = edge

        if not a in graph:
            graph[a] = []
        if not b in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph

def has_path(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited:
        return False

    visited[src] = True

    for n in graph[src]:
        found = has_path(graph, n, dst, visited)

        if found:
            return True

    return False

def main():
    graph = build_graph(edges)
    p = has_path(graph, 'j', 'm', {})
    print(f'has path: {p}')

if __name__ == "__main__":
    main()

