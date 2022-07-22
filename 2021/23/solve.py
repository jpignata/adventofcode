import sys
from collections import defaultdict
from copy import deepcopy
from heapq import heappush, heappop
from math import inf


def freeze(grid):
    return "".join("".join(row) for row in grid)


def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def moves(grid, x, y):
    valid = (1, 2, 4, 6, 8, 10, 11)
    cost = energy[ord(grid[y][x]) - 65]
    destx = rooms[ord(grid[y][x]) - 65]
    spaces = [row[destx] for row in grid if row[destx] in amphipods]

    if x == destx and all(space == grid[y][x] for space in spaces):
        return

    if y == 1:
        for dx in (1, -1):
            nx = x

            while grid[y][nx + dx] == ".":
                if nx + dx == destx:
                    room = [
                        grid[ny][nx + dx]
                        for ny in range(y, len(grid))
                        if grid[ny][nx + dx] in amphipods
                    ]

                    if all(space == grid[y][x] for space in room) or not room:
                        ny = len(grid) - len(room) - 2
                        next_grid = deepcopy(grid)
                        next_grid[ny][nx + dx] = grid[y][x]
                        next_grid[y][x] = "."

                        yield distance((x, y), (nx + dx, ny)) * cost, next_grid

                nx += dx
    else:
        ny = y

        while grid[ny - 1][x] == ".":
            ny -= 1

        if ny == 1:
            nx = x

            for dx in (1, -1):
                while grid[ny][nx + dx] == ".":
                    if nx + dx in valid:
                        next_grid = deepcopy(grid)
                        next_grid[ny][nx + dx] = grid[y][x]
                        next_grid[y][x] = "."

                        yield distance((x, y), (nx + dx, ny)) * cost, next_grid

                    nx += dx


def search(grid):
    visited = defaultdict(lambda: inf)
    visited[freeze(grid)] = 0
    q = [(0, grid)]

    while q:
        total, grid = heappop(q)

        for i, amphipod in enumerate(amphipods):
            if grid[2][rooms[i]] != amphipod or grid[3][rooms[i]] != amphipod:
                break
        else:
            return total

        for y, row in enumerate(grid):
            for x, space in enumerate(row):
                if space not in amphipods:
                    continue

                for cost, next_grid in moves(grid, x, y):
                    grid_key = freeze(next_grid)

                    if (next_cost := total + cost) < visited[grid_key]:
                        visited[grid_key] = next_cost
                        heappush(q, (next_cost, next_grid))


amphipods = ("A", "B", "C", "D")
energy = (1, 10, 100, 1000)
rooms = (3, 5, 7, 9)
grid = [[c for c in line.rstrip()] for line in sys.stdin]
grid2 = deepcopy(grid)
grid2.insert(3, list("  #D#B#A#C#"))
grid2.insert(3, list("  #D#C#B#A#"))

print("Part 1:", search(grid))
print("Part 2:", search(grid2))
