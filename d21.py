from functools import cache

input_data = open('d21.in').read().strip().split('\n')

keyboard = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"],
]

control_pad = [
    [None, "^", "A"],
    ["<", "v", ">"]
]

def get_position(grid, symbol):
    for row_idx, row in enumerate(grid):
        if symbol in row:
            return (row_idx, row.index(symbol))

def calculate_movement_sequence(
    direction,
    repeat_count,
    current_layer,
    max_layers
):
    start_pos = get_position(control_pad, "A")
    direction_pos = get_position(control_pad, direction)
    
    steps_to_direction = min_steps(start_pos, direction_pos, current_layer - 1, max_layers)
    repeated_steps = repeat_count * min_steps(direction_pos, direction_pos, current_layer - 1, max_layers)
    steps_back_to_start = min_steps(direction_pos, start_pos, current_layer - 1, max_layers)
    
    return steps_to_direction + repeated_steps + steps_back_to_start

def calculate_diagonal_movement(
    primary_direction,
    secondary_direction,
    primary_steps,
    secondary_steps,
    current_layer,
    max_layers
):
    start_pos = get_position(control_pad, "A")
    primary_pos = get_position(control_pad, primary_direction)
    secondary_pos = get_position(control_pad, secondary_direction)
    
    steps_to_primary = min_steps(start_pos, primary_pos, current_layer - 1, max_layers)
    steps_to_secondary = min_steps(primary_pos, secondary_pos, current_layer - 1, max_layers)
    steps_to_finish = min_steps(secondary_pos, start_pos, current_layer - 1, max_layers)
    
    return steps_to_primary + primary_steps + steps_to_secondary + secondary_steps + steps_to_finish

@cache
def min_steps(start, end, layers, max_layers):
    if layers == 0:
        return 1

    # Determine movement directions
    vertical_move = (
        "^" if end[0] < start[0] else
        "v" if end[0] > start[0] else
        None
    )
    horizontal_move = (
        "<" if end[1] < start[1] else
        ">" if end[1] > start[1] else
        None
    )

    distance_x = abs(end[0] - start[0]) - 1
    distance_y = abs(end[1] - start[1]) - 1

    if not horizontal_move and not vertical_move:
        start_pos = get_position(control_pad, "A")
        return min_steps(start_pos, start_pos, layers - 1, max_layers)
    
    if not horizontal_move:
        return calculate_diagonal_movement(vertical_move, None, distance_x, 0, layers, max_layers)
    
    if not vertical_move:
        return calculate_movement_sequence(horizontal_move, distance_y, layers, max_layers)

    if layers == max_layers: # last layer
        if start[1] == 0 and end[0] == 3:
            return calculate_diagonal_movement(horizontal_move, vertical_move, distance_x, distance_y, layers, max_layers)
        if end[1] == 0 and start[0] == 3:
            return calculate_diagonal_movement(vertical_move, horizontal_move, distance_x, distance_y, layers, max_layers)
    else:
        if start[1] == 0:
            return calculate_diagonal_movement(horizontal_move, vertical_move, distance_x, distance_y, layers, max_layers)
        if end[1] == 0:
            return calculate_diagonal_movement(vertical_move, horizontal_move, distance_x, distance_y, layers, max_layers)
    
    return min(
        calculate_diagonal_movement(horizontal_move, vertical_move, distance_x, distance_y, layers, max_layers),
        calculate_diagonal_movement(vertical_move, horizontal_move, distance_x, distance_y, layers, max_layers)
    )

def calculate_score(num_layers):
    total_score = 0
    
    for line in input_data:
        code = line[:3]
        multiplier = int(code)
        sequence_total = 0
        
        start_sequence = "A" + code
        end_sequence = line[:4]

        for start, end in zip(start_sequence, end_sequence):
            start_pos = get_position(keyboard, start)
            end_pos = get_position(keyboard, end)
            sequence_total += min_steps(start_pos, end_pos, num_layers, num_layers)
            
        total_score += multiplier * sequence_total
    
    return total_score

def part1():
    print(calculate_score(3))

def part2():
    print(calculate_score(26))

part1()
part2()