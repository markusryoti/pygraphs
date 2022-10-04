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

def num_islands(grid):
    num = 0
    visited = dict()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            is_new = bfs(grid, i, j, visited) 
            if is_new:
                num += 1

    return num

def dfs(grid, i, j, visited):
    if off_map(grid, i, j):
        return False

    if stringify(i, j) in visited:
        return False

    if grid[i][j] == 'W':
        return False

    visited[stringify(i, j)] = True

    for d in directions:
        new_i, new_j = i + d[0], j + d[1]
        dfs(grid, new_i, new_j, visited)

    return True

def bfs(grid, i, j, visited):
    if stringify(i, j) in visited:
        return False

    if grid[i][j] == 'W':
        return False

    q = [(i, j)]

    while len(q) > 0:
        curr = q.pop(0)

        if grid[curr[0]][curr[1]] == 'W':
            continue

        visited[stringify(*curr)] = True

        for d in directions:
            new_i, new_j = curr[0] + d[0], curr[1] + d[1]
            if not off_map(grid, new_i, new_j) and stringify(new_i, new_j) not in visited:
                q.append((new_i, new_j))

    return True

def stringify(i, j):
    return str(i) + ',' + str(j)

def off_map(grid, i, j):
    return i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1

def main():
    islands = num_islands(grid)
    print(f'num islands: {islands}')

if __name__ == "__main__":
    main()
