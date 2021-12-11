import sys
from heapq import heappush, heappop
from math import prod

grid = [[int(point) for point in line.strip()] for line in sys.stdin]
lowest = 0
largest = []
deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))


def dfs(x, y, visited):
    if ((x, y) in visited):
        return 0

    visited.add((x, y))

    if (grid[y][x] == 9):
        return 0

    return 1 + sum([dfs(nx, ny, visited) for dx, dy in deltas
                    if 0 <= (nx := x+dx) < len(grid[0])
                    if 0 <= (ny := y+dy) < len(grid)])


for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        neighbors = [grid[ny][nx] for dx, dy in deltas
                     if 0 <= (nx := x+dx) < len(grid[0])
                     if 0 <= (ny := y+dy) < len(grid)]

        if min(neighbors) > cell:
            size = dfs(x, y, set())
            lowest += cell + 1

            heappush(largest, size)

            while len(largest) > 3:
                heappop(largest)

print('Part 1:', lowest)
print('Part 2:', prod(largest))
