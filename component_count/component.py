graph = {
    "0": [8, 1, 5],
    "1": [0],
    "5": [0, 8],
    "8": [0, 5],
    "2": [3, 4],
    "3": [2, 4],
    "4": [3, 2]
}

def num_connected(graph):
    count = 0
    visited = dict()

    for node in graph:
        if node not in visited:
            bfs(graph, node, visited)
            count += 1

    return count

def bfs(graph, src, visited):
    q = [src]

    while len(q) > 0:
        curr = q.pop(0)

        if curr in visited:
            return

        visited[curr] = True

        for n in graph[curr]:
            q.append(str(n))

def main():
    count = num_connected(graph)
    print(f'count for graph: {count}')

if __name__ == "__main__":
    main()

