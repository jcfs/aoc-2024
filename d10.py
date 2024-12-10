input = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

input = open('d10.in').read()
grid = [list(map(int, line)) for line in input.strip().split('\n')]

zeros = []
nines = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            zeros.append((i, j))
        if grid[i][j] == 9:
            nines.append((i, j))

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def in_bounds(i, j):
    return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

def bfs(grid, x, y, check_visited=False):
    queue = []
    visited = set()
    queue.append((x, y))
    visited.add((x, y))
    count = 0

    while queue:
        i, j = queue.pop(0)
        for di, dj in directions:
            idx = grid[i][j]
            ni, nj = i + di, j + dj
            if not in_bounds(ni, nj):
                continue
            
            if grid[ni][nj] != idx + 1:
                continue

            if check_visited and (ni, nj) in visited:
                continue

            if grid[ni][nj] == 9:
                count += 1
            
            queue.append((ni, nj))
            visited.add((ni, nj))

    return count

def part1():
    print(sum([bfs(grid, zero[0], zero[1], True) for zero in zeros]))

def part2():
    print(sum([bfs(grid, zero[0], zero[1]) for zero in zeros]))


part1()
part2()