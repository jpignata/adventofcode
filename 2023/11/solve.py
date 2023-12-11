import sys


def find(empty, a, b, scale):
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])

    for x, y in empty:
        if x:
            for _x in range(*sorted([a[0], b[0]])):
                if _x == x:
                    distance += scale - 1

        if y:
            for _y in range(*sorted([a[1], b[1]])):
                if _y == y:
                    distance += scale - 1

    return distance


grid = [[char for char in line.strip()] for line in sys.stdin]
empty = []

for i, row in enumerate(grid):
    if all(char == "." for char in row):
        empty.append((0, i))

for i, col in enumerate(zip(*grid[::-1])):
    if all(char == "." for char in col):
        empty.append((i, 0))

galaxies = [
    (x, y)
    for y, row in enumerate(grid)
    for x in range(len(row))
    if row[x] == "#"
]
part1 = sum(
    find(empty, galaxy, other, 2)
    for i, galaxy in enumerate(galaxies)
    for other in galaxies[i:]
    if galaxy != other
)
part2 = sum(
    find(empty, galaxy, other, 1000000)
    for i, galaxy in enumerate(galaxies)
    for other in galaxies[i:]
    if galaxy != other
)

print("Part 1:", part1)
print("Part 2:", part2)
