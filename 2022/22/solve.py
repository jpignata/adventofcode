import sys
from collections import defaultdict
from math import inf
from re import findall

grid = {}
rows = defaultdict(lambda: (inf, -inf))
cols = defaultdict(lambda: (inf, -inf))
orientations = ((1, 0), (0, 1), (-1, 0), (0, -1))
orientation = 0

for y, row in enumerate(sys.stdin):
    if "R" in row:
        path = tuple(
            int(token) if token.isdigit() else token
            for token in findall(r"(R|L|[0-9]+)", row)
        )
    else:
        for x, cell in enumerate(row):
            if cell in (".", "#"):
                if not grid:
                    current = x, y

                grid[x, y] = cell

                rows[y] = min(rows[y][0], x), max(rows[y][1], x)
                cols[x] = min(cols[x][0], y), max(cols[x][1], y)

for move in path:
    x, y = current

    if move == "R":
        orientation = (orientation + 1) % 4
    elif move == "L":
        orientation = (orientation - 1) % 4
    else:
        dx, dy = orientations[orientation]

        for _ in range(move):
            x += dx
            y += dy

            if (x, y) not in grid:
                if orientation == 0:
                    x, y = rows[y][0], y
                elif orientation == 1:
                    x, y = x, cols[x][0]
                elif orientation == 2:
                    x, y = rows[y][1], y
                elif orientation == 3:
                    x, y = x, cols[x][1]

            if grid[x, y] == "#":
                break

            current = x, y

print("Part 1:", (1000 * (current[1] + 1)) + (4 * (current[0] + 1)) + orientation)
