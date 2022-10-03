graph = {
    "a": ['c', 'b'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": [],
}

def bfs(graph, node):
    q = [node]

    while len(q) > 0:
        curr = q.pop(0)

        print(curr)

        for n in graph[curr]:
            q.append(n)

def main():
    bfs(graph, 'a')

if __name__ == "__main__":
    main()
