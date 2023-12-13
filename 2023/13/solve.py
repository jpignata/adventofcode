import sys


def find(grid, smudges=0):
    for i in range(1, len(grid)):
        delta = sum(
            char1 != char2
            for row1, row2 in zip(grid[i:], grid[i - 1 :: -1])
            for char1, char2 in zip(row1, row2)
        )

        if delta == smudges:
            return i

    return 0


grids = [[]]
part1 = part2 = 0

for line in sys.stdin:
    if line.strip():
        grids[-1].append(list(line.strip()))
    else:
        grids.append([])

for grid in grids:
    part1 += 100 * find(grid) + find(list(zip(*grid)))
    part2 += 100 * find(grid, 1) + find(list(zip(*grid)), 1)

print("Part 1:", part1)
print("Part 2:", part2)
