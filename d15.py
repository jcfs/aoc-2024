grid_lines, moves = open('d15.in').read().split('\n\n')
grid_lines = grid_lines.split('\n')
moves = moves.replace('\n', '')


def expand_grid(grid_lines):
    expanded_grid = []
    for row in grid_lines:
        expanded_row = ""
        for char in row:
            if char in {"#", "."}:
                expanded_row += char * 2
            elif char == "O":
                expanded_row += "[]"
            elif char == "@":
                expanded_row += "@."
        expanded_grid.append(expanded_row)
    return expanded_grid


def print_grid(grid, robot_pos=None):
    for y, row in enumerate(grid):
        row_str = ""
        for x, cell in enumerate(row):
            if robot_pos and (x, y) == robot_pos:
                row_str += "@"
            else:
                row_str += cell
        print(row_str)
    print()  


def find_robot(grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "@":
                return (x, y)


def execute_move_part1(grid, robot, move_char):
    move_directions = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }

    dx, dy = move_directions[move_char]
    to_move = []
    empty = 0
    x, y = robot

    current_x, current_y = x + dx, y + dy

    if not (0 <= current_y < len(grid) and 0 <= current_x < len(grid[0])):
        return robot, grid  

    while True:
        if grid[current_y][current_x] == ".":
            empty += 1
            break
        elif grid[current_y][current_x] in {"O", "[", "]"}:
            to_move.append(((current_x, current_y), grid[current_y][current_x]))
        else:
            break
        current_x += dx
        current_y += dy
        
        if not (0 <= current_y < len(grid) and 0 <= current_x < len(grid[0])):
            break  

    if empty > 0:
        new_robot = (x + dx, y + dy)

        for (mx, my), _ in to_move:
            if 0 <= my < len(grid) and 0 <= mx < len(grid[my]):
                grid[my] = grid[my][:mx] + '.' + grid[my][mx + 1:]

        for (mx, my), val in to_move:
            target_x, target_y = mx + dx, my + dy
            if 0 <= target_y < len(grid) and 0 <= target_x < len(grid[target_y]):
                grid[target_y] = grid[target_y][:target_x] + val + grid[target_y][target_x + 1:]
        robot = new_robot

    return robot, grid


def execute_move_part2(grid, robot, move_char):
    move_directions = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0)
    }

    dx, dy = move_directions[move_char]
    to_move = []
    empty = 0
    x, y = robot

    if move_char in {"^", "v"}:
        affected = [(x, y)]
        while True:
            all_empty = all(grid[ny + dy][nx + dx] == "." for (nx, ny) in affected)
            if all_empty:
                empty += 1
                break

            any_wall = any(grid[ny + dy][nx + dx] == "#" for (nx, ny) in affected)
            if any_wall:
                break

            hit = set()
            for nx, ny in affected:
                target_x, target_y = nx + dx, ny + dy
                if not (0 <= target_y < len(grid) and 0 <= target_x < len(grid[0])):
                    continue  
                if grid[target_y][target_x] == "[":
                    hit.add((target_x, target_y))
                    if target_x + 1 < len(grid[target_y]):
                        hit.add((target_x + 1, target_y))
                elif grid[target_y][target_x] == "]":
                    hit.add((target_x, target_y))
                    if target_x - 1 >= 0:
                        hit.add((target_x - 1, target_y))
            if not hit:
                break  
            affected = list(hit)
            for pos in hit:
                mx, my = pos
                if 0 <= my < len(grid) and 0 <= mx < len(grid[my]):
                    to_move.append((pos, grid[my][mx]))

    else:
        current_x, current_y = x + dx, y + dy

        if not (0 <= current_y < len(grid) and 0 <= current_x < len(grid[0])):
            return robot, grid  
        while True:
            if grid[current_y][current_x] == ".":
                empty += 1
                break
            elif grid[current_y][current_x] in {"O", "[", "]"}:
                to_move.append(((current_x, current_y), grid[current_y][current_x]))
            else:
                break
            current_x += dx
            current_y += dy
            
            if not (0 <= current_y < len(grid) and 0 <= current_x < len(grid[0])):
                break  

    if empty > 0:
        new_robot = (x + dx, y + dy)

        for (mx, my), _ in to_move:
            if 0 <= my < len(grid) and 0 <= mx < len(grid[my]):
                grid[my] = grid[my][:mx] + '.' + grid[my][mx + 1:]

        for (mx, my), val in to_move:
            target_x, target_y = mx + dx, my + dy
            if 0 <= target_y < len(grid) and 0 <= target_x < len(grid[target_y]):
                grid[target_y] = grid[target_y][:target_x] + val + grid[target_y][target_x + 1:]
        robot = new_robot

    return robot, grid


def process_part1(grid_lines, moves):
    grid = grid_lines.copy()

    robot_pos = find_robot(grid)
    x, y = robot_pos
    grid[y] = grid[y][:x] + '.' + grid[y][x + 1:]

    for move_char in moves:
        robot_pos, grid = execute_move_part1(grid, robot_pos, move_char)

    result = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in {"O", "["}:
                result += y * 100 + x

    return result


def process_part2(grid_lines, moves):
    grid = expand_grid(grid_lines).copy()

    robot_pos = find_robot(grid)
    x, y = robot_pos
    grid[y] = grid[y][:x] + '.' + grid[y][x + 1:]

    for move_char in moves:
        robot_pos, grid = execute_move_part2(grid, robot_pos, move_char)

    result = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell in {"O", "["}:
                result += y * 100 + x

    return result


def part1():
    print(process_part1(grid_lines, moves))


def part2():
    print(process_part2(grid_lines, moves))


part1()
part2()