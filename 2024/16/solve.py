import sys
from collections import defaultdict
from heapq import heappop, heappush

grid = [list(line.strip()) for line in sys.stdin]
size = len(grid)
target, start = [(x, y) for y in range(size) for x in range(size) if grid[y][x] in "SE"]
distances = defaultdict(lambda: sys.maxsize)
seen = set()
h = [(0, start, (1, 0), {start})]

while h:
    score, (x, y), (dirx, diry), path = heappop(h)

    if score <= distances[(x, y, dirx, diry)]:
        distances[(x, y, dirx, diry)] = score

        if (x, y) == target and score <= distances[target]:
            distances[target] = score
            seen = seen | path

        for dx, dy, cost in (dirx, diry, 1), (diry, -dirx, 1001), (-diry, dirx, 1001):
            if grid[(ny := y + dy)][(nx := x + dx)] != "#":
                heappush(h, (score + cost, (nx, ny), (dx, dy), path | {(nx, ny)}))

print("Part 1:", distances[target])
print("Part 2:", len(seen))
