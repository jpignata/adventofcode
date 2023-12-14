import sys


def tilt(grid, direction):
    def _key(a):
        i = 0 if direction[0] else 1
        return a[i] * direction[i] * -1

    maxy, maxx = len(grid), len(grid[0])
    grid = [row[:] for row in grid]
    rounded = [
        (x, y) for y in range(maxy) for x in range(maxx) if grid[y][x] == "O"
    ]

    for x, y in sorted(rounded, key=_key):
        while 0 <= x < maxx and 0 <= y < maxy:
            nx, ny = x + direction[0], y + direction[1]

            if 0 <= nx < maxx and 0 <= ny < maxy and grid[ny][nx] == ".":
                grid[y][x] = "."
                grid[ny][nx] = "O"
                y = ny
                x = nx
            else:
                break

    return grid


def measure(grid):
    return sum(row.count("O") * (len(grid) - y) for y, row in enumerate(grid))


def detect(grid, target=1000000000):
    seen = {}
    loads = {}

    for i in range(target):
        config = "".join("".join(row) for row in grid)
        loads[i] = measure(grid)

        if config in seen:
            length = i - seen[config]
            start = target - seen[config]
            period = start % length + seen[config]

            return loads[period]

        seen[config] = i

        for direction in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            grid = tilt(grid, direction)


grid = [list(line.strip()) for line in sys.stdin]

print("Part 1:", measure(tilt(grid, (0, -1))))
print("Part 2:", detect(grid))
