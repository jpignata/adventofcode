import sys
from collections import deque


def activate(x, y, dir):
    q = deque([(x, y, dir)])
    visited = set()

    def enqueue(x, y, dir):
        nx, ny = x + dir[0], y + dir[1]

        if 0 <= nx < maxx and 0 <= ny < maxy:
            if (nx, ny, dir) not in visited:
                q.append((nx, ny, dir))

    while q:
        x, y, dir = q.popleft()
        cell = grid[y][x]

        if cell == "/":
            enqueue(x, y, (dir[1] * -1, dir[0] * -1))
        elif cell == "\\":
            enqueue(x, y, (dir[1], dir[0]))
        elif (cell == "|" and dir[0]) or (cell == "-" and dir[1]):
            enqueue(x, y, (dir[1], dir[0]))
            enqueue(x, y, (dir[1] * -1, dir[0] * -1))
        else:
            enqueue(x, y, dir)

        visited.add((x, y, dir))

    return len({(x, y) for x, y, _ in visited})


grid = [list(row) for row in sys.stdin.read().split("\n")]
maxx, maxy = len(grid[0]), len(grid)
start = [(0, y, (1, 0)) for y in range(maxy)]
start += [(maxx - 1, y, (-1, 0)) for y in range(maxy)]
start += [(x, 0, (0, 1)) for x in range(maxx)]
start += [(x, maxy - 1, (1, 0)) for x in range(maxx)]

print("Part 1:", activate(0, 0, (1, 0)))
print("Part 2:", max(activate(x, y, dir) for x, y, dir in start))
