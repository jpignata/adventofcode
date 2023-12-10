import sys
from collections import deque

grid = {}
moves = {
    "|": ((0, -1), (0, 1)),
    "-": ((1, 0), (-1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, 1), (-1, 0)),
    "F": ((0, 1), (1, 0)),
}
start = (-1, -1)
dists = {}
q = deque([])

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        grid[(x, y)] = char

        if char == "S":
            start = (x, y)
            dists[(x, y)] = 0

for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    nx, ny = start[0] + dx, start[1] + dy

    if grid[(nx, ny)] != ".":
        for ddx, ddy in moves[grid[(nx, ny)]]:
            nnx, nny = nx + ddx, ny + ddy

            if nnx == start[0] and nny == start[1]:
                q.append((start[0] + dx, start[1] + dy, 1))

while q:
    x, y, steps = q.popleft()
    dists[(x, y)] = steps

    for dx, dy in moves[grid[(x, y)]]:
        nx, ny = x + dx, y + dy

        if grid[(nx, ny)] != "." and (nx, ny) not in dists:
            q.append((nx, ny, steps + 1))


empty = {(x, y) for (x, y), char in grid.items() if (x, y) not in dists}
outside = set()
maxx, maxy = max(grid)

for x, y in empty:
    visited = set()
    cells = [(x, y)]
    s = [(x, y)]

    if (x, y) in outside:
        continue

    while s:
        nx, ny = s.pop()

        if (nx, ny) in visited:
            continue

        visited.add((nx, ny))

        if (nx, ny) not in grid:
            for cell in cells:
                outside.add(cell)
        else:
            char = grid[(nx, ny)]

            if char == ".":
                cells.append((nx, ny))

                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    s.append((nx + dx, ny + dy))

            elif char in ("-", "|", "J", "F", "L", "7"):
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if (dx, dy) not in moves[char]:
                        if (nx, ny) not in dists:
                            cells.append((nx, ny))
                            s.append((nx + dx, ny + dy))

print("Part 1:", max(dists.values()))
print("Part 2:", len(empty - outside))
