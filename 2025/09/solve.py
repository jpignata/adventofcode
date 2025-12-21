import sys
from itertools import combinations


def dist(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


points = [tuple(map(int, line.split(","))) for line in sys.stdin]
rectangles = sorted(combinations(points, 2), reverse=True, key=lambda pair: dist(*pair))

print("Part 1:", dist(*rectangles[0]))
