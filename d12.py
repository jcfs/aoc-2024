input = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""

input = open('d12.in').read().strip()
grid = [list(line) for line in input.strip().split("\n")]

rows = len(grid)
cols = len(grid[0])

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs(grid, x, y, visited):
    plant_type = grid[x][y]
    queue = [(x, y)]
    region_cells = []
    visited[x][y] = True

    while queue:
        r, c = queue.pop(0)
        region_cells.append((r,c))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and not visited[nr][nc] and grid[nr][nc] == plant_type:
                visited[nr][nc] = True
                queue.append((nr,nc))

    return region_cells

def find_perimeter(grid, x, y, visited):
    t = grid[x][y]
    region_cells = bfs(grid, x, y, visited)

    perimeter = 0
    for (r,c) in region_cells:
        for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != t:
                perimeter += 1

    area = len(region_cells)
    return area, perimeter

def find_borders(grid, x, y, visited):
    region_cells = bfs(grid, x, y, visited)
    region_set = set(region_cells)

    count = 0

    for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        boundary_cells = set()
        for cell in region_cells:
            n = (cell[0] + d[0], cell[1] + d[1])
            if n not in region_set:
                boundary_cells.add(n)
        print(boundary_cells)
        
        cells_to_remove = set()
        for cell in boundary_cells:
            current_cell = (cell[0] + d[1], cell[1] + d[0])
            while current_cell in boundary_cells:
                cells_to_remove.add(current_cell)
                current_cell = (current_cell[0] + d[1], current_cell[1] + d[0])
        print(cells_to_remove)
        
        count += len(boundary_cells) - len(cells_to_remove)

    area = len(region_cells)
    return area, count


def part1():
    visited = [[False]*cols for _ in range(rows)]
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, perimeter = find_perimeter(grid, r, c, visited)
                price = area * perimeter
                total_price += price

    print(total_price)

def part2():
    visited = [[False]*cols for _ in range(rows)]
    total_price = 0

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                area, boarders = find_borders(grid, r, c, visited)
                price = area * boarders
                total_price += price

    print(total_price)  

part1()
part2()