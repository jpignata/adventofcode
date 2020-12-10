import sys
from math import prod


def ride(grid, sx, sy):
    trees, x, y = 0, 0, 0

    while y < len(grid):
        trees += grid[y][x % len(grid[0])] == '#'
        x += sx
        y += sy

    return trees


grid = [line.strip() for line in sys.stdin.readlines()]
slopes = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)

print('Part 1:', ride(grid, 3, 1))
print('Part 2:', prod(ride(grid, x, y) for (x, y) in slopes))
