import sys
from itertools import pairwise


def check(report):
    differences_valid = all(1 <= abs(l1 - l2) <= 3 for l1, l2 in pairwise(report))
    increasing = report == sorted(report)
    decreasing = report == sorted(report, reverse=True)

    return differences_valid and (increasing or decreasing)


def find(report):
    return any(check(report[:i] + report[i + 1 :]) for i in range(len(report)))


reports = [list(map(int, line.split())) for line in sys.stdin]

print("Part 1:", sum(check(report) for report in reports))
print("Part 2:", sum(find(report) for report in reports))
