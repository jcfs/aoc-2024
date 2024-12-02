lines = open('d1.in').readlines()

l1 = [int(x.split()[0]) for x in lines]
l2 = [int(x.split()[1]) for x in lines]

# zip both lists and find the difference
print(sum([abs(x-y) for x,y in zip(sorted(l1), sorted(l2))]))

print(sum([x * l2.count(x) for x in l1]))
