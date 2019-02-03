import sys
import re
from itertools import permutations
from collections import deque


def viable(nodes):
    viable = []
    pairs = permutations(nodes.values(), 2)

    for pair in pairs:
        a, b = pair
        if a[0] > 0 and a[0] <= b[1]:
            viable.append(pair)

    return viable


def find(nodes, width):
    for (x, y), (used, _) in nodes.items():
        if used == 0:
            empty = (x, y)
            break

    q = deque([empty])
    costs = {empty: 0}

    while q:
        x, y = q.popleft()

        if y == 0:
            return costs[(x, y)] + (width - x - 1) + (5 * (width - 2))

        for dx, dy in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            nx, ny = x + dx, y + dy

            if (nx, ny) in nodes:
                size = sum(nodes[(x, y)])

                if (nx, ny) not in costs and nodes[(nx, ny)][0] < size:
                    costs[(nx, ny)] = costs[(x, y)] + 1
                    q.append((nx, ny))


pattern = r'x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T'
nodes = dict()
width = 0

for line in sys.stdin.readlines():
    matches = re.search(pattern, line)

    if matches:
        x, y, _, used, avail = map(int, matches.groups())
        nodes[(x, y)] = (used, avail)
        width = max(width, x + 1)

print('Part 1:', len(viable(nodes)))
print('Part 2:', find(nodes, width))
