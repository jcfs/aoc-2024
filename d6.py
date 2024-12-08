from copy import deepcopy

g = [list(line.strip()) for line in open('d6.in')]
R = len(g)
C = len(g[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

ix, iy = 0, 0
for i in range(R):
    for j in range(C):
        if g[i][j] == '^':
            ix, iy = i, j
            break

def part1():
    c = 0
    visited = set()
    current_dir = directions[3]
    sx, sy = ix, iy
    while True:
        nx, ny = sx + current_dir[0], sy + current_dir[1]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            break
        
        if g[nx][ny] == '#':
            current_dir = directions[(directions.index(current_dir) + 1) % 4]
            continue   

        if (nx, ny) not in visited:
            c+=1
            visited.add((nx, ny))
                    
        sx, sy = nx, ny

    print(c)    
    return visited

def part2(v1):
    c = 0
    for i, j in v1:
        if g[i][j] == '.':
            g[i][j] = '#'

        visited = set()

        current_dir = directions[3]
        sx, sy = ix, iy

        while True:
            nx, ny = sx + current_dir[0], sy + current_dir[1]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                break
            
            if g[nx][ny] == '#':
                current_dir = directions[(directions.index(current_dir) + 1) % 4]
                continue   

            if (nx, ny, current_dir) in visited:
                c+=1
                break
                        
            visited.add((nx, ny, current_dir))

            sx, sy = nx, ny
        g[i][j] = '.'

    print(c)

v = part1()
part2(v)