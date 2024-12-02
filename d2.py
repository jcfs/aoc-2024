reports = [[int(level) for level in line.strip().split()] for line in open('d2.in').readlines()]


def is_safe(report):
    diffs = [report[i+1] - report[i] for i in range(len(report) - 1)]
    if all(1 <= diff <= 3 for diff in diffs):
        return True
    if all(-3 <= diff <= -1 for diff in diffs):
        return True
    return False

sum = 0
for report in reports:
    if is_safe(report):
        sum += 1
#part 1 
print(sum)

sum = 0
for report in reports:
    if is_safe(report):
        sum += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                sum += 1
                break
#part 2
print(sum)

