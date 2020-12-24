import sys
from collections import defaultdict

dirs = {'nw': (0, 1, -1), 'ne': (1, 0, -1), 'sw': (-1, 0, 1), 'se': (0, -1, 1),
        'w': (-1, 1, 0), 'e': (1, -1, 0)}
start = set()

for flip in sys.stdin.readlines():
    current = (0, 0, 0)

    while flip.strip():
        for direction in dirs:
            if (token := flip[:len(direction)]) == direction:
                current = tuple(sum(p) for p in zip(current, dirs[token]))
                flip = flip[len(direction):]
                break

    if current in start:
        start.remove(current)
    else:
        start.add(current)

black_tiles = set(start)

for i in range(100):
    neighbors = defaultdict(int)
    next_tiles = set()

    for tile in black_tiles:
        for delta in dirs.values():
            neighbor = tuple(sum(p) for p in zip(tile, delta))
            neighbors[neighbor] += 1

    for neighbor, flipped in neighbors.items():
        if (neighbor in black_tiles and flipped == 1) or flipped == 2:
            next_tiles.add(neighbor)

    black_tiles = next_tiles

print('Part 1:', len(start))
print('Part 2:', len(black_tiles))
