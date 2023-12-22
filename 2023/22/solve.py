import sys
from re import findall


def fall(bricks):
    grid = set()
    next_bricks = []
    total = 0

    def add(sx, sy, sz, ex, ey, ez):
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    grid.add((x, y, z))

    def remove(sx, sy, sz, ex, ey, ez):
        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                for z in range(sz, ez + 1):
                    grid.remove((x, y, z))

    def supported(sx, sy, sz, ex, ey, _):
        if not sz - 1:  # ground
            return True

        for x in range(sx, ex + 1):
            for y in range(sy, ey + 1):
                if (x, y, sz - 1) in grid:
                    return True

        return False

    bricks.sort(key=lambda b: b[2])

    for brick in bricks:
        add(*brick)

    for i, (sx, sy, sz, ex, ey, ez) in enumerate(bricks):
        while not supported(sx, sy, sz, ex, ey, ez):
            remove(sx, sy, sz, ex, ey, ez)
            add(sx, sy, sz - 1, ex, ey, ez - 1)
            sz -= 1
            ez -= 1

        next_bricks.append((sx, sy, sz, ex, ey, ez))
        total += bricks[i] != next_bricks[i]

    return next_bricks, total


bricks, _ = fall(
    [[int(num) for num in findall(r"\d+", line)] for line in sys.stdin]
)
disintegratable = total = 0

for i in range(len(bricks)):
    variant = bricks.copy()
    del variant[i]

    result, fell = fall(variant)
    disintegratable += result == variant
    total += fell

print("Part 1:", disintegratable)
print("Part 2:", total)
