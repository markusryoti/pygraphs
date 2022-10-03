graph = {
    "0": [8, 1, 5],
    "1": [0],
    "5": [0, 8],
    "8": [0, 5],
    "2": [3, 4],
    "3": [2, 4],
    "4": [3, 2]
}

def largest(graph):
    largest_size = 0
    visited = dict()

    for n in graph:
        count = dfs(graph, n, visited)
        #count = bfs(graph, n, visited)
        if count > largest_size:
            largest_size = count

    return largest_size

def bfs(graph, node, visited):
    count = 0
    q = [node]

    while len(q) > 0:
        curr = q.pop(0)

        if curr in visited:
            return count

        visited[curr] = True
        count += 1

        for n in graph[curr]:
            q.append(str(n))

    return count

def dfs(graph, node, visited):
    if node in visited:
        return 0

    count = 1
    visited[node] = True

    for n in graph[node]:
        count += dfs(graph, str(n), visited)

    return count

def main():
    ls = largest(graph)
    print(f'largest graph: {ls}')

if __name__ == "__main__":
    main()

