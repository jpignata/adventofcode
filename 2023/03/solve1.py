import sys
from re import finditer

part1 = part2 = 0
symbols = []
outlines = []

for y, line in enumerate(sys.stdin):
    for match in finditer(r"(\d+|[^.])", line.strip()):
        if match[0].isnumeric():
            outline = {
                (x + dx, y + dy)
                for x in range(match.start(), match.end())
                for dx in (-1, 0, 1)
                for dy in (-1, 0, 1)
            }
            outlines.append((int(match[0]), outline))
        else:
            symbols.append((match.start(), y))

for symbol in symbols:
    if hits := [num for num, outline in outlines if symbol in outline]:
        part1 += sum(hits)

        if len(hits) == 2:
            part2 += hits[0] * hits[1]

print("Part 1:", part1)
print("Part 2:", part2)
