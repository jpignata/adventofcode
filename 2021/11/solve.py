import sys
from itertools import product, count

grid = [[int(light) for light in line.strip()] for line in sys.stdin]
part1, part2 = 0, 0


def flash(x, y, flashing):
    if grid[y][x] > 9 and (x, y) not in flashing:
        flashing.add((x, y))

        neighbors = [(nx, ny) for dx, dy in product((-1, 0, 1), repeat=2)
                     if dx or dy
                     if 0 <= (nx := x+dx) < len(grid[0])
                     if 0 <= (ny := y+dy) < len(grid)]

        for (nx, ny) in neighbors:
            grid[ny][nx] += 1
            flash(nx, ny, flashing)


for step in count(1):
    flashing = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            grid[y][x] += 1

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            flash(x, y, flashing)

    if step <= 100:
        part1 += len(flashing)

    if len(flashing) == len(grid[0]) * len(grid):
        part2 = step
        break

    for (x, y) in flashing:
        grid[y][x] = 0

print('Part 1:', part1)
print('Part 2:', part2)
