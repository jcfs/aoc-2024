from collections import deque

grid = [ line.strip() for line in open('d20.in').readlines() ]
rows = len(grid)
cols = len(grid[0])

start = None
end = None
for x, row in enumerate(grid):
    for y, char in enumerate(row):
        if char == 'S':
            start = (x, y)
        elif char == 'E':
            end = (x, y)

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
def neighbors(r, c, rows, cols):
    for dr, dc in dirs:
        nr, nc = r+dr, c+dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def is_wall(grid, r, c):
    return grid[r][c] == '#'

def is_track(grid, r, c):
    return grid[r][c] in ('.','S','E')

def bfs(grid, start_pos):
    dist = [[-1]*cols for _ in range(rows)]
    dist[start_pos[0]][start_pos[1]] = 0
    q = deque([start_pos])
    while q:
        r, c = q.popleft()
        for nr, nc in neighbors(r, c, rows, cols):
            if dist[nr][nc] == -1 and is_track(grid, nr, nc):
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist

def best_savings(N):
    dist_start = bfs(grid, start)
    normal_time = dist_start[end[0]][end[1]]
    if normal_time == -1:
        return
    
    dist_end = bfs(grid, end)
    
    best_savings = {}
    
    start_reachable_cells = []
    for r in range(rows):
        for c in range(cols):
            if dist_start[r][c] != -1 and is_track(grid, r, c):
                start_reachable_cells.append((r,c))
    
    for (xr, xc) in start_reachable_cells:
        base_time = dist_start[xr][xc]  
        
        ignore_dist = [[-1]*cols for _ in range(rows)]
        ignore_dist[xr][xc] = 0
        q = deque([(xr, xc)])
        
        while q:
            r, c = q.popleft()
            steps = ignore_dist[r][c]
            if steps == N:
                continue  
            
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if ignore_dist[nr][nc] == -1:
                        ignore_dist[nr][nc] = steps + 1
                        q.append((nr, nc))

        for yr in range(rows):
            for yc in range(cols):
                steps = ignore_dist[yr][yc]
                if steps == -1 or steps == 0:
                    continue

                if (yr, yc) == end:
                    cheated_time = base_time + steps
                    saving = normal_time - cheated_time
                    if saving > 0:
                        cheat_key = ((xr,xc),(yr,yc))
                        if cheat_key not in best_savings or best_savings[cheat_key] < saving:
                            best_savings[cheat_key] = saving
                else:
                    if is_track(grid, yr, yc):
                        if dist_end[yr][yc] != -1:
                            cheated_time = base_time + steps + dist_end[yr][yc]
                            saving = normal_time - cheated_time
                            if saving > 0:
                                cheat_key = ((xr,xc),(yr,yc))
                                if cheat_key not in best_savings or best_savings[cheat_key] < saving:
                                    best_savings[cheat_key] = saving
    
    count = sum(1 for v in best_savings.values() if v >= 100)
    print(count)


def part1():
    best_savings(2)

def part2():
    best_savings(20)


part1()
part2()