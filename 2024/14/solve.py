import sys
from collections import Counter
from itertools import count
from math import prod
from re import findall

guards = []
maxx = maxy = 0

for line in sys.stdin:
    px, py, vx, vy = list(map(int, findall(r"-?\d+", line)))
    maxx, maxy = max(maxx, px + 1), max(maxy, py + 1)

    guards.append(((px, py), (vx, vy)))

for second in count():
    if second == 100:
        counts = Counter(
            (px < midx, py < midy)
            for (px, py), _ in guards
            if px != (midx := maxx // 2) and py != (midy := maxy // 2)
        )

        print("Part 1:", prod(counts.values()))

    if len(guards) == len({(x, y) for (x, y), _ in guards}):
        print("Part 2:", second)
        break

    guards = [
        ((((px + vx) % maxx, (py + vy) % maxy)), (vx, vy))
        for (px, py), (vx, vy) in guards
    ]
