import sys
from itertools import count

grid = {(x, y): char
        for y, line in enumerate(sys.stdin)
        for x, char in enumerate(line.strip())}
lenx, leny = [max(c) + 1 for c in zip(*grid.keys())]

for step in count(1):
    moved = False

    for (x, y) in grid:
        adjacent = ((x + 1) % lenx, y)

        if grid[(x, y)] == '>' and grid[adjacent] == '.':
            grid[(x, y)] = '..'
            grid[adjacent] = '>>'
            moved = True

    for (x, y) in grid:
        adjacent = (x, (y + 1) % leny)

        if grid[(x, y)] == 'v' and grid[adjacent] in ('.', '..'):
            grid[(x, y)] = '...'
            grid[adjacent] = 'vv'
            moved = True

    if not moved:
        print('Part 1:', step)
        break

    for (x, y), char in grid.items():
        if len(char) > 1:
            grid[(x, y)] = char[0]
