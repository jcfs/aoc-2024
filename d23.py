from collections import defaultdict

input = [ line.strip() for line in open('d23.in').readlines() ]

graph = defaultdict(set)

for line in input:
    a, b = line.split('-')
    graph[a].add(b)
    graph[b].add(a)

def part1():
    triangles = set()
    for n1 in graph.keys():
        for n2 in graph[n1]:
            for n3 in graph[n2]:
                if n3 in graph[n1]:
                    triangles.add(tuple(sorted([n1, n2, n3])))

    count = 0
    for trio in triangles:
        if any(node.startswith('t') for node in trio):
            count += 1
    print(count)

 
def part2():
    max = set()
    stack = []
    for node in graph.keys():
        c = set([node])
        stack.append((c, graph[node]))

    #print(stack)
    while stack:
        c, neighbors = stack.pop()

        if len(c) > len(max):
            max = c

        for node in neighbors:
            if c.issubset(graph[node]): 
                c.add(node)
                new_neighbors = graph[node] - c
                stack.append((c, new_neighbors))

    print(','.join(sorted(max)))


part1()
part2()