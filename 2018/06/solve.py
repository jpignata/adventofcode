import sys
import operator
from collections import defaultdict

coords = [tuple(map(int, line.split(', '))) for line in sys.stdin]
maxx = max(map(operator.itemgetter(0), coords)) + 1
maxy = max(map(operator.itemgetter(1), coords)) + 1
totals = defaultdict(int)
regions = defaultdict(int)
infinite = set()

for y in range(maxy):
    for x in range(maxx):
        min_distance = (float('inf'), float('inf'))

        for i, (cx, cy) in enumerate(coords):
            distance = abs(x - cx) + abs(y - cy)
            totals[(x, y)] += distance
            min_distance = min((distance, i), min_distance)

        regions[min_distance[1]] += 1

        if y in (0, maxy) or x in (0, maxx):
            infinite.add(min_distance[1])

print('Part 1:', max(d for r, d in regions.items() if r not in infinite))
print('Part 2:', sum(1 for distance in totals.values() if distance < 10000))
