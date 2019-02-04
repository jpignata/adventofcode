import sys
import numpy as np

grid = np.zeros((6, 50))

for tokens in [line.split(' ') for line in sys.stdin.readlines()]:
    if tokens[0] == 'rect':
        x, y = tuple(map(int, tokens[1].split('x')))
        grid[:y, :x] = 1
    elif tokens[0] == 'rotate':
        axis, start, positions = tokens[1], int(tokens[2][2:]), int(tokens[4])

        if axis == 'row':
            grid[start] = np.roll(grid[start], positions)
        elif axis == 'column':
            grid[:, start] = np.roll(grid[:, start], positions)

print('Part 1:', int(sum(sum(grid))))
print('Part 2:')

for row in grid:
    for char in row:
        if char:
            sys.stdout.write('█')
        else:
            sys.stdout.write(' ')

    print()
