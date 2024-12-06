import re
from collections import defaultdict, deque   
import time

lines = open('d5.in').read().split("\n\n")
rules = [rule.split('|') for rule in lines[0].split("\n")]
pages = [page.split(",") for page in lines[1].split("\n")]

def sort(nodes, edges):
    graph = defaultdict(list)

    in_degree = {node: 0 for node in nodes}
    for src, dest in edges:
        graph[src].append(dest)
        in_degree[dest] += 1

    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_order

def reorder_pages(page, rules):
    nodes = set(page)
    edges = [(x, y) for x, y in rules if x in nodes and y in nodes]
    return sort(nodes, edges)

def part1():
    sum = 0
    for page in pages:
        if reorder_pages(page, rules) == page:
            sum += int(page[len(page)//2])
    print(sum)

def part2():
    sum = 0    
    for page in pages:
        ordered_page = reorder_pages(page, rules)
        if ordered_page != page:
            sum += int(ordered_page[len(ordered_page) // 2])
    print(sum)


part1()
part2()