patterns, designs = open('d19.in').read().split('\n\n')
patterns = [ p.strip() for p in patterns.split(',') ]

designs = designs.split('\n')

def count_from_ways(design, patterns):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for p in patterns:
            plen = len(p)
            if i - plen >= 0 and dp[i - plen] and design[i - plen:i] == p:
                dp[i] += dp[i - plen]
    return dp[n]


def part1():
    r = 0
    for design in designs:
        if count_from_ways(design, patterns):
            r += 1
    print(r)

def part2():
    r = 0
    for design in designs:
        r += count_from_ways(design, patterns)
    print(r)

part1()
part2()
