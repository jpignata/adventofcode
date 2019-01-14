import sys


def step(start_grid):
    adjacent = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1),
                (1, 1))
    size = len(start_grid)
    next_grid = [[]] * size

    for y, row in enumerate(start_grid):
        next_grid[y] = ['.'] * size

        for x, light in enumerate(row):
            neighbors_on = 0

            for change in adjacent:
                nx, ny = [(a+b) for a, b in zip((x, y), change)]

                if nx >= 0 and ny >= 0 and nx < size and ny < size:
                    neighbors_on += start_grid[ny][nx] == '#'

            if neighbors_on == 3 or (light == '#' and neighbors_on == 2):
                next_grid[y][x] = '#'

    return next_grid


def activate_corners(grid):
    last = len(grid) - 1
    grid[0][0] = grid[0][last] = grid[last][0] = grid[last][last] = '#'

    return grid


grid = [list(line.strip()) for line in sys.stdin.readlines()]
part1 = grid.copy()
part2 = activate_corners(grid.copy())

for i in range(100):
    part1 = step(part1)
    part2 = step(part2)
    activate_corners(part2)

print('Part 1:', sum([row.count('#') for row in part1]))
print('Part 2:', sum([row.count('#') for row in part2]))
