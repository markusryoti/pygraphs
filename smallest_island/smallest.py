grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W'],
]

directions = [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
]

def smallest_island(grid):
    smallest = default_size(grid)
    visited = dict()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'L' and stringify(i, j) not in visited:
                size = bfs(grid, i, j, visited) 
                if size < smallest:
                    smallest = size

    return smallest

def default_size(grid):
    return len(grid) * len(grid[0])

def dfs(grid, i, j, visited):
    if stringify(i, j) in visited:
        return 0

    if off_map(grid, i, j):
        return 0

    if grid[i][j] == 'W':
        return 0

    visited[stringify(i, j)] = True
    size = 1

    for d in directions:
        new_i, new_j = i + d[0], j + d[1]
        size += dfs(grid, new_i, new_j, visited)

    return size

def bfs(grid, i, j, visited):
    q = [(i, j)]
    size = 0

    while len(q) > 0:
        curr = q.pop(0)
        visited[stringify(*curr)] = True
        size += 1

        for d in directions:
            new_i, new_j = curr[0] + d[0], curr[1] + d[1]

            if can_add(grid, new_i, new_j, visited):
                q.append((new_i, new_j))

    return size

def can_add(grid, i, j, visited):
    return not off_map(grid, i, j) and stringify(i, j) not in visited and not grid[i][j] == "W"

def stringify(i, j):
    return str(i) + ',' + str(j)

def off_map(grid, i, j):
    return i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1

def main():
    size = smallest_island(grid)
    print(f'smallest island: {size}')

if __name__ == "__main__":
    main()
