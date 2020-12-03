import sys

grid = [[c for c in line.strip()] for line in sys.stdin.readlines()]


def ride(sx, sy):
    x, y = 0, 0
    trees = 0

    while y < len(grid):
        trees += grid[y][x % len(grid[0])] == '#'
        x += sx
        y += sy

    return trees


print('Part 1:', ride(3, 1))
print('Part 2:', ride(1, 1) * ride(3, 1) * ride(5, 1) * ride(7, 1) * ride(1, 2))
