import sys
import operator
from itertools import combinations
from functools import reduce


def find_smallest(nums, target):
    for l in range(len(nums)):
        for c in combinations(nums, l):
            if sum(c) == target:
                return reduce(operator.mul, c)


weights = [int(weight.strip()) for weight in sys.stdin.readlines()]

print("Part 1:", find_smallest(weights, sum(weights) / 3))
print("Part 2:", find_smallest(weights, sum(weights) / 4))
