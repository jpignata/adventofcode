import sys
from collections import defaultdict
from math import ceil
from operator import add


def run(grid, evolved=False):
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
    location = ceil(max(grid)[0] / 2), ceil(max(grid)[1] / 2)
    current = dirs[0]
    infected = 0

    for _ in range(10000000 if evolved else 10000):
        if evolved:
            if grid[location] == '#':
                current = dirs[(dirs.index(current) + 1) % len(dirs)]
                grid[location] = 'F'
            elif grid[location] == '.':
                current = dirs[(dirs.index(current) - 1) % len(dirs)]
                grid[location] = 'W'
            elif grid[location] == 'F':
                current = dirs[(dirs.index(current) + 2) % len(dirs)]
                grid[location] = '.'
            elif grid[location] == 'W':
                grid[location] = '#'
                infected += 1
        else:
            if grid[location] == '#':
                current = dirs[(dirs.index(current) + 1) % len(dirs)]
                grid[location] = '.'
            else:
                current = dirs[(dirs.index(current) - 1) % len(dirs)]
                grid[location] = '#'
                infected += 1

        location = tuple(map(add, location, current))

    return infected


grid = defaultdict(lambda: '.')

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        grid[(x, y)] = char

print('Part 1:', run(grid.copy()))
print('Part 2:', run(grid.copy(), evolved=True))
