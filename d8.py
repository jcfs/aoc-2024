from collections import defaultdict
from itertools import combinations
from tqdm import tqdm

input = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
#input = [list(x) for x in input.strip().split("\n")]
input = [list(x) for x in open("d8.in").read().strip().split("\n")]

R=len(input)
C=len(input[0])

def parse(input):
    locations = defaultdict(list)
    for y in range(R):
        for x in range(C):
            if input[y][x] != ".":
                locations[input[y][x]].append((x, y))
    return locations

def inside_grid(p):
    return 0 <= p[0] < C and 0 <= p[1] < R

def part1():
    locations = parse(input)
    anti_nodes = set()
    
    for positions in locations.values():
        for a1, a2 in combinations(positions, 2):
            dx, dy = a2[0] - a1[0], a2[1] - a1[1]
            
            antinodes = [
                (a1[0] - dx, a1[1] - dy),  
                (a2[0] + dx, a2[1] + dy)   
            ]
            
            anti_nodes.update(pos for pos in antinodes if inside_grid(pos))

    print(len(anti_nodes))

def part2():
    locations = parse(input)
    anti_nodes = set()
    
    for positions in locations.values():
        for a1, a2 in combinations(positions, 2):
            dx, dy = a2[0] - a1[0], a2[1] - a1[1]
            
            anti_nodes.update((a1, a2))
            
            points_before = [(a1[0] - dx*i, a1[1] - dy*i) for i in range(1, max(R,C))]
            points_after = [(a2[0] + dx*i, a2[1] + dy*i) for i in range(1, max(R,C))]
            
            anti_nodes.update(filter(inside_grid, points_before + points_after))

    print(len(anti_nodes))

part1()
part2()