from itertools import product

input = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""

input = open('d7.in').read()
equations = [rule.split(': ') for rule in input.strip().split("\n")]
equations = [(int(k), list(map(int, v.split()))) for k, v in equations]

def calculate_result(list_ints, target, ops):
    def apply_ops(ops_comb, nums):
        result = nums[0]
        for op, num in zip(ops_comb, nums[1:]):
            if op == "+":
                result += num
            elif op == "*":
                result *= num
            elif op == "||":
                result = int(f"{result}{num}")
                
            if result > target:
                return result
        return result

    combinations = product(ops, repeat=len(list_ints) - 1)
    return any(apply_ops(comb, list_ints) == target for comb in combinations)


def solve(ops):
    total = sum(k for k, v in equations if calculate_result(v, k, ops))
    print(total)

solve(["+", "*"])
solve(["+", "*", "||"])
