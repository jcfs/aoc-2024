import heapq

directions = {
        0: (1, 0),   
        1: (0, 1),   
        2: (-1, 0),  
        3: (0, -1),  
    }

maze = [ line.strip() for line in open('d16.in').readlines() ]
height = len(maze)
width = len(maze[0])

start = None
end = None
for y, row in enumerate(maze):
    for x, char in enumerate(row):
        if char == 'S':
            start = (x, y)
        elif char == 'E':
            end = (x, y)

def dijkstra(sx, sy):
    min_cost = [ [ [float('inf')] * 4 for _ in range(width) ] for _ in range(height) ]
    predecessors = [ [ [[] for _ in range(4)] for _ in range(width) ] for _ in range(height) ]

    heap = []
    initial_direction = 0  
    heapq.heappush(heap, (0, sx, sy, initial_direction))
    min_cost[sy][sx][initial_direction] = 0

    while heap:
        cost, x, y, dir = heapq.heappop(heap)

        if cost > min_cost[y][x][dir]:
            continue

        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] != '#':
            new_cost = cost + 1
            if new_cost < min_cost[ny][nx][dir]:
                min_cost[ny][nx][dir] = new_cost
                predecessors[ny][nx][dir].append((x, y, dir))
                heapq.heappush(heap, (new_cost, nx, ny, dir))
            elif new_cost == min_cost[ny][nx][dir]:
                predecessors[ny][nx][dir].append((x, y, dir))   

        for new_dir in [(dir - 1) % 4, (dir + 1) % 4]:
            new_cost = cost + 1000
            if new_cost < min_cost[y][x][new_dir]:
                min_cost[y][x][new_dir] = new_cost
                predecessors[y][x][new_dir].append((x, y, dir))
                heapq.heappush(heap, (new_cost, x, y, new_dir))
            elif new_cost == min_cost[y][x][new_dir]:
                predecessors[y][x][new_dir].append((x, y, dir))


    return min_cost, predecessors

def backtrack(predecessors, min_cost, end_pos):
    ex, ey = end_pos
    best = min(min_cost[ey][ex])

    end_states = []
    for dir in range(4):
        if min_cost[ey][ex][dir] == best:
            end_states.append((ex, ey, dir))

    best_path_tiles = set()

    queue = []

    for state in end_states:
        queue.append(state)
        best_path_tiles.add((state[0], state[1]))

    visited = set(end_states)

    while queue:
        x, y, dir = queue.pop()
        for pred in predecessors[y][x][dir]:
            px, py, _ = pred
            best_path_tiles.add((px, py))
            if pred not in visited:
                visited.add(pred)
                queue.append(pred)

    return best_path_tiles

def part1():
    min_cost, _ = dijkstra(*start)
    print(min(min_cost[end[1]][end[0]]))

def part2():
    min_cost, predecessors = dijkstra(*start)
    result = backtrack(predecessors, min_cost, end)

    def print_maze():
        for y, row in enumerate(maze):
            for x, char in enumerate(row):
                if (x, y) in result:
                    print('\033[92mO\033[0m', end='')
                else:
                    print(char, end='')
            print()

    print_maze()

    print(len(result))

part1()
part2()
