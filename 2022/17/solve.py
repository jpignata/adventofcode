import sys
from itertools import cycle


def solve():
    jets = list(sys.stdin.readline().strip())

    print("Part 1:", simulate(jets, 7, 2022))
    print("Part 2:", simulate(jets, 7, 1000000000000, detect=True))


def simulate(jets, width, drops, *, detect=False):
    def move(rock, dx, dy):
        new_rock = tuple((x + dx, y + dy) for x, y in rock)

        if any(x < 0 or y < 0 or x >= width for x, y in new_rock):
            return rock

        if any(grid.get((x, y), 0) for x, y in new_rock):
            return rock

        return new_rock

    grid = {}
    seen = {}
    jets = cycle(enumerate(jets))
    rocks = cycle(
        enumerate(
            [
                ((0, 0), (1, 0), (2, 0), (3, 0)),
                ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
                ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
                ((0, 0), (0, 1), (0, 2), (0, 3)),
                ((0, 0), (1, 0), (0, 1), (1, 1)),
            ]
        )
    )

    for drop in range(drops + 1):
        rock_index, rock = next(rocks)
        height = max((y for _, y in grid), default=-1)
        rock = tuple((x + 2, y + height + 4) for x, y in rock)

        while True:
            jet_index, jet = next(jets)
            dx = 1 if jet == ">" else -1

            rock = move(rock, dx, 0)
            new_rock = move(rock, 0, -1)

            if new_rock == rock:
                break

            rock = new_rock

            if detect:
                height = max((y for _, y in grid), default=0)

                if (rock_index, jet_index) in seen:
                    seendrop, seenheight = seen[rock_index, jet_index]

                    if (drops - drop) % (drop - seendrop) == 0:
                        remaining = (drops - drop) // (drop - seendrop)
                        offset = height - seenheight

                        return remaining * offset + height + 1

                seen[rock_index, jet_index] = drop, height

        for x, y in rock:
            grid[x, y] = 1

    return height + 1


if __name__ == "__main__":
    solve()
