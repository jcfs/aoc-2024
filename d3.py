import re

line = open('d3.in').read()

def part1():
    sum = 0
    for r in re.findall(r'mul\((\d+),(\d+)\)', line):
        x, y = map(int, r)
        sum += x * y
    print(sum)

def part2():
    sum = 0
    l = re.sub(r'don\'t\(\).*?do\(\)', '', line, flags=re.DOTALL)
    for r in re.findall(r'mul\((\d+),(\d+)\)', l):
        x, y = map(int, r)
        sum += x * y
    print(sum)

part1()
part2()