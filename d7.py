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

def calculate_result(list_ints, target, ops, result=0):
    if not list_ints:
        return result if result == target else None

    a = list_ints[0]
    for op in ops:
        new_result = result
        if op == "+":
            new_result += a
        elif op == "*":
            new_result = new_result * a if new_result != 0 else a
        elif op == "||":
            new_result = int(f"{new_result}{a}")

        res = calculate_result(list_ints[1:], target, ops, new_result)
        if res is not None:
            return res

    return None


def solve(ops):
    sum = 0
    for k, v in equations:
        if calculate_result(v, k, ops):
            sum += k
    print(sum)

solve(["+", "*"])
solve(["+", "*", "||"])