import sys
from collections import defaultdict, deque
from string import ascii_letters

grid = [[c for c in line.strip("\n")] for line in sys.stdin]
portals = defaultdict(list)
conns = dict()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == ".":
            for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                nx, ny = x + dx, y + dy
                is_in_bounds = 0 <= nx < len(grid[0]) and 0 <= ny < len(grid)
                is_portal = grid[ny][nx] in ascii_letters

                if is_in_bounds and is_portal:
                    if -1 in (dx, dy):
                        portal = grid[ny + dy][nx + dx] + grid[ny][nx]
                    else:
                        portal = grid[ny][nx] + grid[ny + dy][nx + dx]

                    if nx + dx == 0 or nx + dx == len(grid[0]) - 1:
                        change = -1
                    elif ny + dy == 0 or ny + dy == len(grid) - 1:
                        change = -1
                    else:
                        change = 1

                    portals[portal].append(((x, y), change))

for cells in portals.values():
    if len(cells) == 2:
        conns[cells[0][0]] = (cells[1][0], cells[0][1])
        conns[cells[1][0]] = (cells[0][0], cells[1][1])

start = portals["AA"][0][0]
end = portals["ZZ"][0][0]


def find(start, end, grid, conns, *, recurse=False):
    q = deque([(start, 0, 0)])
    visited = set()

    while q:
        (x, y), steps, level = q.popleft()

        if (x, y) == end and level == 0:
            return steps

        if (x, y) in conns:
            (nx, ny), change = conns[(x, y)]
            next_level = level + change if recurse else level

            if next_level >= 0 and (nx, ny, next_level) not in visited:
                q.append(((nx, ny), steps + 1, next_level))

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy
            is_in_bounds = 0 <= nx < len(grid[0]) and 0 <= ny < len(grid)
            is_passage = grid[ny][nx] == "."

            if is_in_bounds and is_passage and (nx, ny, level) not in visited:
                q.append(((nx, ny), steps + 1, level))

        visited.add((x, y, level))


print("Part 1:", find(start, end, grid, conns))
print("Part 2:", find(start, end, grid, conns, recurse=True))
