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
            if grid[i][j] == 'L' and stringify(i, j) not in visited:
                bfs(grid, i, j, visited) 
                num += 1

    return num

def dfs(grid, i, j, visited):
    if off_map(grid, i, j):
        return

    if stringify(i, j) in visited:
        return

    if grid[i][j] == 'W':
        return

    visited[stringify(i, j)] = True

    for d in directions:
        new_i, new_j = i + d[0], j + d[1]
        dfs(grid, new_i, new_j, visited)

def bfs(grid, i, j, visited):
    q = [(i, j)]

    while len(q) > 0:
        curr = q.pop(0)
        visited[stringify(*curr)] = True

        if grid[curr[0]][curr[1]] == 'W':
            continue

        for d in directions:
            new_i, new_j = curr[0] + d[0], curr[1] + d[1]
            if stringify(new_i, new_j) not in visited and not off_map(grid, new_i, new_j):
                q.append((new_i, new_j))

def stringify(i, j):
    return str(i) + ',' + str(j)

def off_map(grid, i, j):
    return i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1

def main():
    islands = num_islands(grid)
    print(f'num islands: {islands}')

if __name__ == "__main__":
    main()
