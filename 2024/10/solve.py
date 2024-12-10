import sys

grid = [list(map(int, line.strip())) for line in sys.stdin]
maxx, maxy = len(grid[0]), len(grid)
starts = [
    (x, y) for y, row in enumerate(grid) for x, height in enumerate(row) if not height
]


def dfs(x, y):
    if grid[y][x] == 9:
        yield (x, y)

    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        if 0 <= (nx := x + dx) < maxx and 0 <= (ny := y + dy) < maxy:
            if grid[ny][nx] == grid[y][x] + 1:
                yield from dfs(nx, ny)


print("Part 1:", sum(len(set(dfs(x, y))) for x, y in starts))
print("Part 2:", sum(len(list(dfs(x, y))) for x, y in starts))
