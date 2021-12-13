import sys
from collections import defaultdict


def fold(grid, axis, coord):
    next_grid = defaultdict(int)

    for point, value in grid.items():
        target = 0 if axis == 'x' else 1
        other = 1 if axis == 'x' else 0

        if point[target] > coord:
            next_point = [None, None]
            next_point[target] = 2 * coord - point[target]
            next_point[other] = point[other]
        else:
            next_point = point

        next_grid[tuple(next_point)] = value

    return next_grid


grid = defaultdict(int)
folds = []

for line in sys.stdin:
    if ',' in line:
        grid[tuple(int(number) for number in line.split(','))] = 1
    elif 'fold' in line:
        axis, coord = line.split()[-1].split('=')
        folds.append((axis, int(coord)))

for i, (axis, coord) in enumerate(folds):
    grid = fold(grid, axis, coord)

    if i == 0:
        print('Part 1:', sum(grid.values()))

maxx, maxy = [max(coord) for coord in zip(*grid.keys())]

print('Part 2:')

for y in range(maxy + 1):
    for x in range(maxx + 1):
        if grid[(x, y)]:
            print('█', end='')
        else:
            print(' ', end='')
    print()
