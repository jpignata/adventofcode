import sys
from itertools import count

grid = {(x, y): char
        for y, line in enumerate(sys.stdin)
        for x, char in enumerate(line.strip())}
lenx, leny = [max(c) + 1 for c in zip(*grid.keys())]

for step in count(1):
    movements = 0
    next_grid = grid.copy()

    for (x, y), char in grid.items():
        if char == '>' and grid[((x + 1) % lenx, y)] == '.':
            next_grid[(x, y)] = '.'
            next_grid[((x + 1) % lenx, y)] = '>'
            movements += 1

    grid = next_grid.copy()

    for (x, y), char in grid.items():
        if char == 'v' and grid[(x, (y + 1) % leny)] == '.':
            next_grid[(x, y)] = '.'
            next_grid[(x, (y + 1) % leny)] = 'v'
            movements += 1

    grid = next_grid

    if movements == 0:
        print('Part 1:', step)
        break
