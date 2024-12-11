from collections import defaultdict

input = """
125 17
"""

input = open('d11.in').read().strip()

def transform_stone(s):
    if s == "0":
        result = ["1"]
    else:
        length = len(s)
        if length % 2 == 0:
            half = length // 2
            result = [(part.lstrip('0') or '0') for part in (s[:half], s[half:])]
        else:
            result = [str(int(s)*2024)]
    
    return result

def transform_dict(stone_dict):
    trans = defaultdict(int)
    for stone, count in stone_dict.items():
        ns = transform_stone(stone)
        for t in ns:
            trans[t] += count
    return trans

def transform(times):
    initial_stones = input.split()
    
    stone_dict = defaultdict(int)
    for st in initial_stones:
        stone_dict[st] += 1
    
    for _ in range(times):
        stone_dict = transform_dict(stone_dict)
    
    total_stones = sum(stone_dict.values())
    return total_stones

def part1():
    print(transform(25))

def part2():
    print(transform(75))


part1()
part2()