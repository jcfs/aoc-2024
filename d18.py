from collections import deque

input = [ (line.split(',')[0], line.split(',')[1]) for line in  open("d18.in", "r").read().split("\n") ]
size = 71

directions = [(0,1), (0,-1), (1,0), (-1,0)]

def bfs(grid, start, end):
    visited = set()
    queue = deque()
    queue.append((start[0], start[1], 0))  
    visited.add((start[0], start[1]))
    
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < size and 0 <= ny < size:
                if (nx, ny) not in visited and not grid[ny][nx]:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist+1))
    
    return -1

def part1():
    grid = [[False for _ in range(size)] for _ in range(size)]

    for x, y in input[:1024]:
        if 0 <= int(x) < size and 0 <= int(y) < size:
            grid[int(y)][int(x)] = True
    print(bfs(grid, (0,0), (70,70)))

def part2():
    grid = [[False for _ in range(size)] for _ in range(size)]

    for x, y in input:
        grid[int(y)][int(x)] = True

        if bfs(grid, (0,0), (70,70)) == -1:
            print(f"{x},{y}")
            break

part1()
part2()