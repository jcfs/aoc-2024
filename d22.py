from collections import defaultdict

lines = [ int(line) for line in open('d22.in').readlines() ]

def simulate_secrets(secret, iterations):
    secrets = []
    for _ in range(iterations):
        v1 = secret * 64
        secret = secret ^ v1
        secret = secret % 16777216

        v2 = secret // 32
        secret = secret ^ v2
        secret = secret % 16777216

        v3 = secret * 2048
        secret = secret ^ v3
        secret = secret % 16777216

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

        window = []
        seen = {}
        for i in range(len(changes)):
            window.append(changes[i])
            if len(window) == 4:
                sequence = tuple(window)
                if sequence not in seen:
                    banana = prices[i+1]  
                    bananas[sequence] += banana
                    seen[sequence] = True
                window.pop(0)

    max = 0
    for total_banana in bananas.values():
        if total_banana > max:
            max = total_banana

    print(max)

part1()
part2()
