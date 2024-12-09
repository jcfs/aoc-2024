from collections import defaultdict
from itertools import zip_longest

input = """
2333133121414131402
"""

input = open("d9.in").read().strip()
#input = input.strip()

def parse_to_list_of_blocks(disk):
    digits = map(int, disk)
    blocks = []
    for idx, (file, empty) in enumerate(zip_longest(*[iter(digits)]*2, fillvalue=0)):
        blocks.extend([idx] * file)
        blocks.extend(['.'] * empty)
    
    return blocks

def get_contigous_free_space(blocks):
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

    return contiguous_free_space

def get_contigous_ids(blocks):
    contiguous_ids = defaultdict(list)
    for i, block in enumerate(blocks):
        if block != '.':
            contiguous_ids[block].append(i)
    return contiguous_ids

def checksum(blocks):
    return sum(i * int(blk) for i, blk in enumerate(blocks) if blk != '.')
    
def part1():
    blocks = parse_to_list_of_blocks(input)
    contiguous_ids = get_contigous_ids(blocks)

    first_free_space = 0
    for k, v in reversed(contiguous_ids.items()):  
        if all(b == '.' for b in blocks[blocks.index('.'):]):
            break

        for id in v:
            while blocks[first_free_space] != '.':
                first_free_space += 1

            blocks[first_free_space] = k
            blocks[id] = '.'

            first_free_space += 1

    print(checksum(blocks))


def part2():
    blocks = parse_to_list_of_blocks(input)

    contiguous_free_space = get_contigous_free_space(blocks)
    contiguous_ids = get_contigous_ids(blocks)

    for k, v in reversed(contiguous_ids.items()):
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

    print(checksum(blocks))


part1()
part2()
