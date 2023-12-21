import sys
from itertools import count


def run(grid, active, generations=64):
    maxx, maxy = list(active)[0]

    for _ in range(generations):
        next_active = set()

        for y in range(maxy + 2):
            for x in range(maxx + 2):
                if (x, y) in grid:
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy

                        if (nx, ny) in grid and (nx, ny) in active:
                            next_active.add((x, y))
                            maxx = max(x, maxx)
                            maxy = max(y, maxy)
                            break

        active = next_active

    return len(active)


def run2(grid, active):
    current = list(active)[0]
    minx, miny = current
    maxx, maxy = current

    smaxx, smaxy = max(grid)[0] + 1, max(grid, key=lambda a: a[1])[1] + 1

    for i in count():
        next_active = set()

        for y in range(miny - 5, maxy + 5):
            for x in range(minx - 5, maxx + 5):
                if (x % smaxx, y % smaxy) in grid:
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy

                        if (nx % smaxx, ny % smaxy) in grid and (nx, ny) in active:
                            next_active.add((x, y))
                            minx, maxx = min(x, minx), max(x, maxx)
                            miny, maxy = min(y, miny), max(y, maxy)

                            break

        active = next_active

        for y in range(miny - 5, maxy + 5):
            for x in range(minx - 5, maxx + 5):
                if (x % smaxx, y % smaxy) in grid:
                    if (x, y) in active:
                        print("O", end="")
                    else:
                        print(".", end="")
                else:
                    print("#", end="")
            print()

        # if i + 1 in (6, 10, 50, 100, 500, 1000, 5000):
        #    print("score", i, len(active))

    return len(active)


start = set()
active = set()

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == "S":
            active.add((x, y))

        if char != "#":
            start.add((x, y))

print("Part 1:", run(start, active))
# print("Part 2:", run2(start, active))
