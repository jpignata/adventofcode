import math
import operator
import sys


def angle(a, b):
    return math.atan2(b[0] - a[0], a[1] - b[1]) % (2 * math.pi)


asteroids = [(x, y) for y, row in enumerate(sys.stdin.readlines())
             for x, cell in enumerate(row) if cell == '#']
visible = {a: len(set(angle(a, b) for b in asteroids)) for a in asteroids}
station = max(visible.items(), key=operator.itemgetter(1))[0]
asteroids.sort(key=lambda b: math.hypot(*map(operator.sub, b, station)))
destroyed = {b: sum(angle(station, b) == angle(station, c)
             for c in asteroids[:i]) for i, b in enumerate(asteroids)}
x, y = sorted(asteroids, key=lambda b: (destroyed[b], angle(station, b)))[199]

print(f'Part 1: {max(visible.values())}')
print(f'Part 2: {x * 100 + y}')
