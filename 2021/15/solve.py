import math
import sys
from heapq import heappush, heappop


def search(grid):
    size = len(grid)
    target = (size - 1, size - 1)
    costs = [[math.inf] * size for _ in range(size)]
    q = [(0, (0, 0))]

    while q:
        cost, (x, y) = heappop(q)

        if (x, y) == target:
            return cost

        neighbors = [
            (next_cost, (nx, ny))
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1))
            if 0 <= (ny := y + dy) < size
            if 0 <= (nx := x + dx) < size
            if (next_cost := cost + grid[ny][nx]) < costs[ny][nx]
        ]

        for next_cost, (nx, ny) in neighbors:
            costs[ny][nx] = next_cost
            heappush(q, (next_cost, (nx, ny)))


grid = [[int(number) for number in line.strip()] for line in sys.stdin]
size, full_size = len(grid), len(grid) * 5
full_grid = [[None] * full_size for _ in range(full_size)]

for y in range(full_size):
    for x in range(full_size):
        if y < size and x < size:
            full_grid[y][x] = grid[y][x]
        elif x < size:
            full_grid[y][x] = full_grid[y - size][x] % 9 + 1
        else:
            full_grid[y][x] = full_grid[y][x - size] % 9 + 1

print("Part 1:", search(grid))
print("Part 2:", search(full_grid))
