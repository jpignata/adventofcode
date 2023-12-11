import sys


def total(galaxies, empties, scale):
    def find(galaxy, other):
        distance = abs(galaxy[0] - other[0]) + abs(galaxy[1] - other[1])
        distance += sum(
            scale - 1
            for i in range(2)
            for coord in range(*sorted((galaxy[i], other[i])))
            for _coord in empties[i]
            if coord == _coord
        )
        return distance

    return sum(
        find(galaxy, other)
        for i, galaxy in enumerate(galaxies)
        for other in galaxies[i:]
    )


rows = [[char for char in line.strip()] for line in sys.stdin]
cols = list(zip(*rows[::-1]))
galaxies = [
    (x, y)
    for y in range(len(rows))
    for x in range(len(cols))
    if rows[y][x] == "#"
]
empties = [
    [i for i, col in enumerate(cols) if not any(char == "#" for char in col)],
    [i for i, row in enumerate(rows) if not any(char == "#" for char in row)],
]

print("Part 1:", total(galaxies, empties, 2))
print("Part 2:", total(galaxies, empties, 1000000))
