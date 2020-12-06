import sys
from functools import reduce

part1, part2, group = 0, 0, []

for line in [line.strip() for line in sys.stdin.readlines()] + ['']:
    if len(line):
        group.append(set(line))
    else:
        part1 += len(reduce(lambda x, y: x | y, group))
        part2 += len(reduce(lambda x, y: x & y, group))
        group = []

print('Part 1:', part1)
print('Part 2:', part2)
