import sys
from math import sqrt


def variations(grid):
    def flipud(grid):
        return list(grid[::-1])

    def fliplr(grid):
        return [list(row[::-1]) for row in grid]

    def rotate(grid):
        return [list(row) for row in zip(*grid[::-1])]

    res = []

    for _ in range(2):
        res.extend([grid, flipud(grid), fliplr(grid), flipud(fliplr(grid))])
        grid = rotate(grid)

    return res


def connect(tiles):
    size = int(sqrt(len(tiles)))
    stack = [
        ([variant], [tile_id])
        for tile_id, variants in tiles.items()
        for variant in variants
    ]

    while stack:
        cand, ids = stack.pop()
        found = len(cand)
        y, x = divmod(found, size)

        if found == len(tiles):
            return cand, ids[0] * ids[size - 1] * ids[size * -1] * ids[-1]

        for other_id, others in tiles.items():
            if other_id not in ids:
                for other in others:
                    if x > 0 and (
                        [r[0] for r in other] != [r[-1] for r in cand[found - 1]]
                    ):
                        continue

                    if y > 0 and other[0] != cand[found - size][-1]:
                        continue

                    stack.append((cand + [other], ids + [other_id]))


def find(pieces, shape):
    size = int(sqrt(len(pieces)))
    tile_width = len(pieces[0]) - 2
    grid = [[None] * (tile_width * size) for _ in range(tile_width * size)]

    for y, row in enumerate(grid):
        for x in range(len(grid[0])):
            ctile = y // tile_width * size + x // tile_width
            cy = y % tile_width + 1
            cx = x % tile_width + 1
            grid[y][x] = pieces[ctile][cy][cx]

    total = sum(1 for row in grid for c in row if c == "#")
    found = 0

    for image in variations(grid):
        for y, row in enumerate(image):
            for x in range(len(row)):
                found += all(
                    0 <= y + dy < len(image)
                    and 0 <= x + dx < len(image[0])
                    and image[y + dy][x + dx] == "#"
                    for dx, dy in shape
                )

        if found:
            return total - len(shape) * found

    return None


def solve():
    monster = (
        (0, 0),
        (1, 1),
        (4, 1),
        (5, 0),
        (6, 0),
        (7, 1),
        (10, 1),
        (11, 0),
        (12, 0),
        (13, 1),
        (16, 1),
        (17, 0),
        (18, -1),
        (18, 0),
        (19, 0),
    )
    tiles = {}

    while line := sys.stdin.readline():
        if ":" in line:
            tile_id = int(line.strip()[-5:-1])
            tile = []

            while line := sys.stdin.readline().strip():
                tile.append(list(line))

            tiles[tile_id] = variations(tile)

    pieces, checksum = connect(tiles)
    roughness = find(pieces, monster)

    return checksum, roughness


if __name__ == "__main__":
    part1, part2 = solve()

    print("Part 1:", part1)
    print("Part 2:", part2)
