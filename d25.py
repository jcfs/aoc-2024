schematics = [line for line in open('d25.in').read().split('\n\n')]

def parse(lines):
    top = lines[0]
    bottom = lines[6]

    if top == "#####" and bottom == ".....":
        t = "lock"
    elif top == "....." and bottom == "#####":
        t = "key"

    if t == "lock":
        heights = [sum(1 for row in range(7) if lines[row][col] == '#') - 1 for col in range(5)]
    else:
        heights = [0]*5
        for col in range(5):
            count = 0
            for row in range(6, -1, -1):  
                if lines[row][col] == '#':
                    count += 1
                else:
                    break
            heights[col] = count - 1

    return tuple(heights), t

def part1():
    locks = []
    keys = []

    for chunk in schematics:
        h, kind = parse(chunk.split('\n'))
        if kind == "lock":
            locks.append(h)
        else:
            keys.append(h)

    count = sum(
        all(lh + kh <= 5 for lh, kh in zip(lock_heights, key_heights))
            for lock_heights in locks
                for key_heights in keys
    )

    print(count)


part1()
