import sys
from itertools import product, count


def flash(x, y):
    if grid[y][x] > 9 and (x, y) not in flashing:
        flashing.add((x, y))

        neighbors = [(nx, ny) for dx, dy in product((-1, 0, 1), repeat=2)
                     if dx or dy
                     if 0 <= (nx := x+dx) < size
                     if 0 <= (ny := y+dy) < size]

        for (nx, ny) in neighbors:
            grid[ny][nx] += 1
            flash(nx, ny)


grid = [[int(level) for level in line.strip()] for line in sys.stdin]
size = len(grid)
flashes = 0

for step in count(1):
    flashing = set()

    for y in range(size):
        for x in range(size):
            grid[y][x] += 1

    for y in range(size):
        for x in range(size):
            flash(x, y)

    if step <= 100:
        flashes += len(flashing)

    if len(flashing) == size ** 2:
        print('Part 1:', flashes)
        print('Part 2:', step)
        break

    for (x, y) in flashing:
        grid[y][x] = 0
