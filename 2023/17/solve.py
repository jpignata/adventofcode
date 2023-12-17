import sys
from heapq import heappush, heappop
from collections import defaultdict


def find(grid, min_count, max_count):
    maxx, maxy = len(grid[0]), len(grid)
    h = [(0, 0, 0, 1, 0, 0)]
    dists = defaultdict(lambda: sys.maxsize)

    def enqueue(x, y, dx, dy, dir_count):
        nx, ny = x + dx, y + dy

        if 0 <= nx < maxx and 0 <= ny < maxy:
            alt = loss + grid[ny][nx]

            if dists[(nx, ny, dx, dy, dir_count + 1)] > alt:
                dists[(nx, ny, dx, dy, dir_count + 1)] = alt
                heappush(h, (alt, nx, ny, dx, dy, dir_count + 1))

    while h:
        loss, x, y, dirx, diry, dir_count = heappop(h)

        if (x, y) == (maxx - 1, maxy - 1) and dir_count >= min_count:
            return loss

        if dir_count < max_count:
            enqueue(x, y, dirx, diry, dir_count)

        if dir_count >= min_count:
            for dx, dy in ((-diry, dirx), (diry, -dirx)):
                enqueue(x, y, dx, dy, 0)


grid = [[int(cell) for cell in line.strip()] for line in sys.stdin]

print("Part 1:", find(grid, 1, 3))
print("Part 2:", find(grid, 4, 10))
