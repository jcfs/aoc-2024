W=101
H=103

def parse_input():
    robots = []
    for line in open('d14.in', "r").readlines():
        line = line.strip()
        if not line:
            continue
        p_str, v_str = line.split()
        px, py = map(int, p_str[2:].split(',')) 
        vx, vy = map(int, v_str[2:].split(','))  
        robots.append((px, py, vx, vy))
    return robots

def calculate_safety_factor(robots, time):
    mid_x = W // 2
    mid_y = H // 2

    grid = [[0 for _ in range(W)] for _ in range(H)]

    quadrants = [0, 0, 0, 0]

    for (px, py, vx, vy) in robots:
        nx = (px + vx * time) % W
        ny = (py + vy * time) % H

        grid[ny][nx] += 1

        if nx < mid_x and ny < mid_y:
            quadrants[0] += 1
        elif nx > mid_x and ny < mid_y:
            quadrants[1] += 1
        elif nx < mid_x and ny > mid_y:
            quadrants[2] += 1
        elif nx > mid_x and ny > mid_y:
            quadrants[3] += 1

    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]
    return safety_factor, grid

def part1():
    print(calculate_safety_factor(parse_input(), 100)[0])

def part2():
    bots = parse_input()
    for i in range(10000):
        grid = calculate_safety_factor(bots, i)[1]
        found = False
        for y in range(H - 4):
            for x in range(W - 4):
                if all(grid[y + dy][x + dx] > 0 for dy in range(5) for dx in range(5)):
                    print(i)
                    found = True
                    break
            if found:
                for y in range(H):
                    print(''.join('#' if grid[y][x] > 0 else '.' for x in range(W)))
                break

    pass

part1()
part2()