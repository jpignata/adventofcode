import sys
from math import sqrt


def top(tile):
    return tile[0]


def bottom(tile):
    return tile[-1]


def left(tile):
    return [row[0] for row in tile]


def right(tile):
    return [row[-1] for row in tile]


def fliplr(tile):
    return [list(row[::-1]) for row in tile]


def flipud(tile):
    return list(tile[::-1])


def rot90(tile):
    return [list(row) for row in zip(*tile[::-1])]


def connect(tiles):
    size = int(sqrt(len(tiles)))
    s = []

    for tile_id, variants in tiles.items():
        for variant in variants:
            s.append(([variant], [tile_id]))

    while s:
        placed, tile_ids = s.pop()
        found = len(placed)

        if found == len(tiles):
            checksum = tile_ids[0] * tile_ids[size - 1] * \
                       tile_ids[size * -1] * tile_ids[-1]
            return placed, checksum
        else:
            y, x = divmod(len(placed), size)

            for other_id, variants in tiles.items():
                if other_id not in tile_ids:
                    for v in variants:
                        if x > 0 and right(placed[found - 1]) != left(v):
                            continue

                        if y > 0 and bottom(placed[found - size]) != top(v):
                            continue

                        s.append((placed + [v], tile_ids + [other_id]))


def hunt(tiles):
    monster = ((0, 0), (1, 1), (4, 1), (7, 1), (10, 1), (13, 1), (16, 1),
               (5, 0), (6, 0), (11, 0), (12, 0), (17, 0), (18, 0), (19, 0),
               (18, -1))
    multiplier = int(sqrt(len(tiles)))
    size = (len(tiles[0]) - 2)
    maxx, maxy = len(tiles[0][0][0]), len(tiles[0][0])
    image = [[None] * (size * multiplier) for _ in range(size * multiplier)]

    for y, row in enumerate(image):
        for x in range(len(image[0])):
            ct = ((y // size) * multiplier) + (x // size)
            cy = y % size + 1
            cx = x % size + 1
            image[y][x] = tiles[ct][cy][cx]

    for _ in range(2):
        images = [image, flipud(image), fliplr(image), flipud(fliplr(image))]

        for variant in images:
            found = 0

            for y, row in enumerate(variant):
                for x, cell in enumerate(row):
                    if cell == '#':
                        found += all(0 <= y+dy < len(variant) and
                                     0 <= x+dx < len(variant[0]) and
                                     variant[y+dy][x+dx] == '#'
                                     for dx, dy in monster)

            if found > 0:
                total = sum(1 for row in variant for c in row if c == '#')
                return total - (len(monster) * found)

        image = rot90(image)


tiles = {}

while (line := sys.stdin.readline()):
    if ':' in line:
        tile_id = int(line.strip()[-5:-1])
        tile = []

        while ((line := sys.stdin.readline().strip())):
            tile.append(list(line))

        tiles[tile_id] = []

        for _ in range(2):
            tiles[tile_id].append(tile)
            tiles[tile_id].append(fliplr(tile))
            tiles[tile_id].append(flipud(tile))
            tiles[tile_id].append(fliplr(flipud(tile)))
            tile = rot90(tile)

connected, checksum = connect(tiles)

print('Part 1:', checksum)
print('Part 2:', hunt(connected))
