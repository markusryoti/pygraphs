graph = {
    "f": ['g', 'i'],
    "g": ['h'],
    "h": [],
    "i": ['g', 'k'],
    "j": ['i'],
    "k": [],
}

def bfs_has_path(graph, src, dst):
    queue = [src]

    while len(queue) > 0:
        curr = queue.pop(0)

        if curr == dst:
            return True

        for n in graph[curr]:
            queue.append(n)

    return False

def main():
    has_path = bfs_has_path(graph, 'f', 'k')
    print(f"graph has path {has_path}")

if __name__ == "__main__":
    main()
