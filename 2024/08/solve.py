import sys
from collections import defaultdict
from itertools import permutations

antennas = defaultdict(list)
part1, part2 = set(), set()
maxx = maxy = 0

for y, line in enumerate(sys.stdin):
    maxy = max(y + 1, maxy)
    maxx = max(len(line.strip()), maxx)

    for x, char in enumerate(line.strip()):
        if char != ".":
            antennas[char].append((x, y))

for coords in antennas.values():
    for (x1, y1), (x2, y2) in permutations(coords, 2):
        dx, dy = x2 - x1, y2 - y1
        nx, ny = x1, y1

        while 0 <= nx < maxx and 0 <= ny < maxy:
            dists = sorted([abs(nx - x1) + abs(ny - y1), abs(nx - x2) + abs(ny - y2)])

            if dists[0] == dists[1] // 2:
                part1.add((nx, ny))

            part2.add((nx, ny))

            nx += dx
            ny += dy

print("Part 1:", len(part1))
print("Part 2:", len(part2))
