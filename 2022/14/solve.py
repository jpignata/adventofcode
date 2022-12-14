import sys
from collections import defaultdict
from re import findall


def solve():
    paths = [
        [(int(x), int(y)) for x, y in findall(r"(\d+),(\d+)", line)]
        for line in sys.stdin
    ]
    grid = defaultdict(lambda: ".")

    for path in paths:
        for points in zip(path, path[1:]):
            (sx, sy), (ex, ey) = sorted(points)

            for y in range(sy, ey + 1):
                for x in range(sx, ex + 1):
                    grid[x, y] = "#"

    print("Part 1:", simulate(grid.copy()))
    print("Part 2:", simulate(grid.copy(), floor=True))


def simulate(grid, *, floor=False):
    settled = 0
    prev = None
    bottom = max(point[1] for point in grid) + 2

    if floor:
        for x in range(0, 1000):
            grid[x, bottom] = "#"

    while prev != (prev := settled):
        cx, cy = 500, 0

        while grid[cx, cy] != "o" and cy < bottom:
            if grid[cx, cy + 1] == ".":
                cy += 1
            elif grid[cx - 1, cy + 1] == ".":
                cx -= 1
                cy += 1
            elif grid[cx + 1, cy + 1] == ".":
                cx += 1
                cy += 1
            else:
                settled += 1
                grid[cx, cy] = "o"

    return settled


if __name__ == "__main__":
    solve()
