import sys

current = 50
part1 = part2 = 0

for line in sys.stdin:
    direction = -1 if line[0] == "L" else 1

    for _ in range(int(line[1:])):
        current = (current + direction) % 100

        if not current:
            part2 += 1

    if not current:
        part1 += 1

print("Part 1:", part1)
print("Part 2:", part2)
