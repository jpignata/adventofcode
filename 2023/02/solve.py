import sys
from collections import defaultdict
from math import prod
from re import findall

part1 = part2 = 0
inventory = {"red": 12, "green": 13, "blue": 14}

for i, line in enumerate(sys.stdin):
    maxes = defaultdict(int)

    for amount, color in findall(r"(\d+) (\w+)", line):
        maxes[color] = max(maxes[color], int(amount))

    if all(amount <= inventory[color] for color, amount in maxes.items()):
        part1 += i + 1

    part2 += prod(maxes.values())

print("Part 1:", part1)
print("Part 2:", part2)
