import sys
from math import prod


def ride(grid, sx, sy):
    return sum(row[(sx * i) % len(row)] == "#" for i, row in enumerate(grid[::sy]))


grid = [line.strip() for line in sys.stdin.readlines()]

print("Part 1:", ride(grid, 3, 1))
print(
    "Part 2:",
    prod(ride(grid, x, y) for (x, y) in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))),
)
