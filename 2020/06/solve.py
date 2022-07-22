import sys

part1, part2 = 0, 0
group = []

for line in [line.strip() for line in sys.stdin.readlines()] + [""]:
    if line:
        group.append(set(line))
    else:
        part1 += len(set.intersection(*group))
        part2 += len(set.union(*group))
        group = []

print("Part 1:", part1)
print("Part 2:", part2)
