import sys
from heapq import heappush, heappop
from collections import defaultdict


def find(grid, min_count, max_count):
    maxx, maxy = len(grid[0]), len(grid)
    h = [(0, 0, 0, 1, 0, 0)]
    dists = defaultdict(lambda: sys.maxsize)

    def enqueue(x, y, dx, dy, dir_count=0):
        if 0 <= (nx := x + dx) < maxx and 0 <= (ny := y + dy) < maxy:
            alt = loss + grid[ny][nx]

            if dists[(nx, ny, dx, dy, dir_count + 1)] > alt:
                dists[(nx, ny, dx, dy, dir_count + 1)] = alt
                heappush(h, (alt, nx, ny, dx, dy, dir_count + 1))

    while h:
        loss, x, y, dirx, diry, dir_count = heappop(h)

        if dir_count >= min_count:
            if x == maxx - 1 and y == maxy - 1:
                return loss

            for next_dirx, next_diry in ((-diry, dirx), (diry, -dirx)):
                enqueue(x, y, next_dirx, next_diry)

        if dir_count < max_count:
            enqueue(x, y, dirx, diry, dir_count)


grid = [[int(cell) for cell in line.strip()] for line in sys.stdin]

print("Part 1:", find(grid, 1, 3))
print("Part 2:", find(grid, 4, 10))
