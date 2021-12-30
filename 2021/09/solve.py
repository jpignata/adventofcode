import sys
from heapq import heappush, heappushpop
from math import prod


def dfs(x, y, visited):
    visited.add((x, y))

    return 1 + sum([dfs(nx, ny, visited) for dx, dy in deltas
                    if 0 <= (nx := x+dx) < length
                    if 0 <= (ny := y+dy) < length
                    if (nx, ny) not in visited
                    if grid[ny][nx] != 9])


deltas = ((1, 0), (0, 1), (-1, 0), (0, -1))
grid = [[int(point) for point in line.strip()] for line in sys.stdin]
length = len(grid)
risk = 0
largest = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        neighbors = [grid[ny][nx] for dx, dy in deltas
                     if 0 <= (nx := x+dx) < length
                     if 0 <= (ny := y+dy) < length]

        if cell < min(neighbors):
            risk += cell + 1
            size = dfs(x, y, set())

            if len(largest) < 3:
                heappush(largest, size)
            else:
                heappushpop(largest, size)

print('Part 1:', risk)
print('Part 2:', prod(largest))
