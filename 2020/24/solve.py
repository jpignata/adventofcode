import re
import sys

dirs = {
    "nw": (0, -1),
    "ne": (1, -1),
    "sw": (-1, 1),
    "se": (0, 1),
    "w": (-1, 0),
    "e": (1, 0),
}
tokens = re.compile("|".join(dirs))
start = set()

for flip in sys.stdin.readlines():
    pos = 0, 0

    for direction in tokens.findall(flip):
        pos = tuple(c + r for c, r in zip(pos, dirs[direction]))

    if pos in start:
        start.remove(pos)
    else:
        start.add(pos)

tiles = set(start)

for i in range(100):
    neighbors = {}
    next_tiles = set()

    for tile in tiles:
        for delta in dirs.values():
            neighbor = tuple(c + r for c, r in zip(tile, delta))
            neighbors[neighbor] = neighbors.get(neighbor, 0) + 1

    for neighbor, flipped in neighbors.items():
        if (neighbor in tiles and flipped == 1) or flipped == 2:
            next_tiles.add(neighbor)

    tiles = next_tiles

print("Part 1:", len(start))
print("Part 2:", len(tiles))
