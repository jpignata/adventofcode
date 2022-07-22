import sys
from collections import defaultdict
from copy import deepcopy


def part1(gen):
    def biodiversity(grid):
        return sum(
            2 ** ((y * len(r)) + x)
            for y, r in enumerate(grid)
            for x, c in enumerate(r)
            if c == "#"
        )

    seen = set()
    current = biodiversity(gen)

    while current not in seen:
        seen.add(current)
        next_gen = deepcopy(gen)

        for y, row in enumerate(gen):
            for x, cell in enumerate(row):
                adjacent = list()

                for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < len(gen[0]) and 0 <= ny < len(gen):
                        adjacent.append(gen[ny][nx])

                if cell == "#":
                    if adjacent.count("#") != 1:
                        next_gen[y][x] = "."
                elif cell == ".":
                    if 0 < adjacent.count("#") <= 2:
                        next_gen[y][x] = "#"

        gen = next_gen
        current = biodiversity(gen)

    return current


def part2(grid):
    def empty():
        return [["."] * 5 for _ in range(5)]

    maxx = len(grid[0])
    maxy = len(grid)

    grids = defaultdict(empty)
    grids[0] = grid

    for minute in range(200):
        next_grids = deepcopy(grids)

        for level in range(minute * -1 - 2, minute + 3):
            next_level = deepcopy(grids[level])

            for y in range(5):
                for x in range(5):
                    adjacent = list()

                    if (x, y) == (2, 2):
                        continue

                    for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < maxx and 0 <= ny < maxy:
                            if (nx, ny) != (2, 2):
                                adjacent.append(grids[level][ny][nx])

                    above = grids[level - 1]
                    below = grids[level + 1]

                    if y == 0:
                        adjacent.append(above[1][2])
                    elif y == 4:
                        adjacent.append(above[3][2])

                    if x == 0:
                        adjacent.append(above[2][1])
                    elif x == 4:
                        adjacent.append(above[2][3])

                    if (x, y) == (1, 2):
                        adjacent.extend(below[i][0] for i in range(5))
                    elif (x, y) == (3, 2):
                        adjacent.extend(below[i][-1] for i in range(5))
                    elif (x, y) == (2, 1):
                        adjacent.extend(below[0])
                    elif (x, y) == (2, 3):
                        adjacent.extend(below[-1])

                    cell = grids[level][y][x]

                    if cell == "#":
                        if adjacent.count("#") != 1:
                            next_level[y][x] = "."
                    elif cell == ".":
                        if 0 < adjacent.count("#") <= 2:
                            next_level[y][x] = "#"

            next_grids[level] = next_level

        grids = next_grids

    return sum(sum(row.count("#") for row in grid) for grid in grids.values())


grid = [[c for c in line.strip()] for line in sys.stdin]

print("Part 1:", part1(grid))
print("Part 2:", part2(grid))
