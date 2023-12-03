import sys

part1 = part2 = 0
grid = [line.strip() for line in sys.stdin]
symbols = [
    (x, y)
    for y, row in enumerate(grid)
    for x, char in enumerate(row)
    if char not in ".0123456789"
]
visited = set()
maxx, maxy = len(grid[0]), len(grid)
directions = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]

for x, y in symbols:
    group = []

    for dx, dy in directions:
        if 0 <= (nx := x + dx) < maxx and 0 <= (ny := y + dy) < maxy:
            if grid[ny][nx].isdigit() and (nx, ny) not in visited:
                number = ""

                while nx and grid[ny][nx - 1].isdigit():
                    nx -= 1

                while nx < maxx and grid[ny][nx].isdigit():
                    number += grid[ny][nx]
                    visited.add((nx, ny))
                    nx += 1

                group.append(int(number))

    part1 += sum(group)

    if grid[y][x] == "*" and len(group) == 2:
        part2 += group[0] * group[1]

print("Part 1:", part1)
print("Part 2:", part2)
