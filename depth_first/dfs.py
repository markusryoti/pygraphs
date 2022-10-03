graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": [],
}

def dfs(graph, node):
    s = [node]

    while len(s) > 0:
        curr = s.pop()

        print(curr)
        
        for n in graph[curr]:
            s.append(n)

# def dfs_recursive(graph, node):
#     print(node)

#     for n in graph[node]:
#         dfs_recursive(graph, n)

def main():
    dfs(graph, 'a')

if __name__ == "__main__":
    main()

