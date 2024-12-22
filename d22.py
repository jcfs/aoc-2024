from collections import defaultdict

lines = [ int(line) for line in open('d22.in').readlines() ]

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def simulate_secrets(secret, iterations):
    secrets = []
    for _ in range(iterations):
        secret = prune(mix(secret, secret * 64))
        secret = prune(mix(secret, secret // 32))
        secret = prune(mix(secret, secret * 2048))
        secrets.append(secret)
    return secrets

def part1():
    total = sum(simulate_secrets(secret, 2000)[-1] for secret in lines)
    print(total)

def part2():
    bananas = defaultdict(int)

    for secret in lines:
        prices = [s % 10 for s in simulate_secrets(secret, 2000)]
        changes = [b - a for a, b in zip(prices[:-1], prices[1:])]

        seen = set()
        max_value = 0
        for i in range(len(changes) - 3):
            sequence = tuple(changes[i:i+4])
            if sequence not in seen:
                bananas[sequence] += prices[i+4]
                if bananas[sequence] > max_value:
                    max_value = bananas[sequence]
                seen.add(sequence)

    print(max_value)

part1()
part2()
