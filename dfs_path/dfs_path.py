graph = {
    "f": ['g', 'i'],
    "g": ['h'],
    "h": [],
    "i": ['g', 'k'],
    "j": ['i'],
    "k": [],
}

def dfs_has_path(graph, src, dst):
    if src == dst:
        return True

    for n in graph[src]:
        if dfs_has_path(graph, n, dst):
            return True

    return False

def main():
    has_path = dfs_has_path(graph, 'f', 'k')
    print(f"graph has path {has_path}")

if __name__ == "__main__":
    main()
