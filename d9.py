from collections import defaultdict

input = """
2333133121414131402
"""

input = open("d9.in").read().strip()
#input = input.strip()

def parse_to_list_of_blocks(disk):
    segments = list(map(int, disk))
    blocks = []
    file_id = 0
    is_file = True
    for length in segments:
        if is_file:
            for _ in range(length):
                blocks.append(str(file_id))
            file_id += 1
        else:
            for _ in range(length):
                blocks.append('.')
        is_file = not is_file

    return blocks

    
def part1():
    blocks = parse_to_list_of_blocks(input)

    contiguous_free_space = []
    start = None
    for i, block in enumerate(blocks):
        if block == '.':
            if start is None:
                start = i
        else:
            if start is not None:
                contiguous_free_space.append((start, i - start))
                start = None

    contiguous_ids = defaultdict(list)
    for i, block in enumerate(blocks):
        if block != '.':
            contiguous_ids[block].append(i)

    first_free_space = 0
    for k, v in reversed(contiguous_ids.items()):  
        seen_dot = False
        over = True
        for x in blocks:
            if x == '.':
                seen_dot = True
            if seen_dot and x != '.':
                over = False
                break

        if over:
            break   

        for id in v:
            while blocks[first_free_space] != '.':
                first_free_space += 1

            blocks[first_free_space] = k
            blocks[id] = '.'


            first_free_space += 1


    checksum = 0
    for i, blk in enumerate(blocks):
        if blk != '.':
            checksum += i * int(blk)
    print(checksum)


def part2():
    blocks = parse_to_list_of_blocks(input)

    contiguous_free_space = []
    start = None
    for i, block in enumerate(blocks):
        if block == '.':
            if start is None:
                start = i
        else:
            if start is not None:
                contiguous_free_space.append((start, i - start))
                start = None
    if start is not None:
        contiguous_free_space.append((start, len(blocks) - start))

    contiguous_ids = defaultdict(list)
    for i, block in enumerate(blocks):
        if block != '.':
            contiguous_ids[block].append(i)

    sorted_files = sorted(contiguous_ids.items(), key=lambda x: int(x[0]), reverse=True)

    for k, v in sorted_files:
        needed_free_space = len(v)
        file_start = min(v)  

        for i, (run_start, length) in enumerate(contiguous_free_space):
            if length >= needed_free_space and (run_start + needed_free_space) <= file_start:
                for j in range(needed_free_space):
                    blocks[run_start + j] = k
                for idx in v:
                    blocks[idx] = '.'

                new_start = run_start + needed_free_space
                new_length = length - needed_free_space
                if new_length > 0:
                    contiguous_free_space[i] = (new_start, new_length)
                else:
                    contiguous_free_space.pop(i)

                break

    checksum = 0
    for i, blk in enumerate(blocks):
        if blk != '.':
            checksum += i * int(blk)
    print(checksum)

part1()
part2()
