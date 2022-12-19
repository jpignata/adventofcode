import sys
from itertools import cycle


def solve():
    jets = list(sys.stdin.readline().strip())
    rocks = [
        ((0, 0), (1, 0), (2, 0), (3, 0)),
        ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
        ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
        ((0, 0), (0, 1), (0, 2), (0, 3)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),
    ]

    print("Part 1:", simulate(jets, rocks, 2022))
    print("Part 2:", simulate(jets, rocks, 1000000000000))


def simulate(jets, rocks, drops):
    def move(rock, dx, dy):
        next_rock = tuple((x + dx, y + dy) for x, y in rock)

        if any(x < 0 or y < 0 or x >= 7 for x, y in next_rock):
            return rock

        if any(grid.get((x, y), 0) for x, y in next_rock):
            return rock

        return next_rock

    jets = cycle(enumerate(jets))
    rocks = cycle(enumerate(rocks))
    grid = {}
    seen = {}
    height = -1

    for drop in range(drops):
        rock_index, rock = next(rocks)
        rock = move(rock, 2, height + 4)

        while True:
            jet_index, jet = next(jets)
            rock = move(rock, 1 if jet == ">" else -1, 0)
            next_rock = move(rock, 0, -1)

            if next_rock == rock:
                break

            rock = next_rock

        for x, y in rock:
            grid[x, y] = 1
            height = max(height, y)

        if (rock_index, jet_index) in seen:
            prev_drop, prev_height = seen[rock_index, jet_index]
            remaining = drops - drop - 1
            period = drop - prev_drop
            offset = height - prev_height

            if remaining % period == 0:
                return (remaining // period) * offset + height + 1

        seen[rock_index, jet_index] = drop, height

    return height + 1


if __name__ == "__main__":
    solve()
