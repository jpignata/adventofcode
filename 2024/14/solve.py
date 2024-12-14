import sys
from collections import defaultdict
from itertools import count
from math import prod
from re import findall

guards = []
maxx = maxy = 0

for line in sys.stdin:
    px, py, vx, vy = list(map(int, findall(r"-?\d+", line)))
    maxx = max(maxx, px + 1)
    maxy = max(maxy, py + 1)

    guards.append(((px, py), (vx, vy)))

for second in count():
    counts = defaultdict(int)

    for (px, py), _ in guards:
        counts[(px < maxx // 2, py < maxy // 2)] += 1

    if second == 100:
        print("Part 1:", prod(counts.values()))

    if len(guards) == len({(x, y) for (x, y), _ in guards}):
        print("Part 2:", second)
        break

    guards = [
        ((((px + vx) % maxx, (py + vy) % maxy)), (vx, vy))
        for (px, py), (vx, vy) in guards
    ]
