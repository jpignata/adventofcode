import sys
from functools import cache
from itertools import combinations


def area(a, b):
    return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)


points = [tuple(map(int, line.split(","))) for line in sys.stdin]
edges = list(zip(points, points[1:] + points[:1]))
rectangles = sorted(combinations(points, 2), reverse=True, key=lambda pair: area(*pair))


def between(value, a, b):
    return min(a, b) <= value <= max(a, b)


@cache
def contains(x, y):
    inside = False

    for (x1, y1), (x2, y2) in edges:
        if x1 == x2 == x and between(y, y1, y2):
            return True

        if y1 == y2 == y and between(x, x1, x2):
            return True

        if x1 == x2 and (y1 > y) != (y2 > y) and x < x1:
            inside = not inside

    return inside


def boundary_crosses_interior(x1, y1, x2, y2):
    for (ex1, ey1), (ex2, ey2) in edges:
        if ex1 == ex2:
            if x1 < ex1 < x2 and max(y1, min(ey1, ey2)) < min(y2, max(ey1, ey2)):
                return True
        elif y1 < ey1 < y2 and max(x1, min(ex1, ex2)) < min(x2, max(ex1, ex2)):
            return True

    return False


def boundary_crosses_line(x1, y1, x2, y2):
    for (ex1, ey1), (ex2, ey2) in edges:
        if x1 == x2 and ey1 == ey2:
            if y1 < ey1 < y2 and min(ex1, ex2) < x1 < max(ex1, ex2):
                return True

        if y1 == y2 and ex1 == ex2:
            if x1 < ex1 < x2 and min(ey1, ey2) < y1 < max(ey1, ey2):
                return True

    return False


def contained(a, b):
    x1, x2 = sorted((a[0], b[0]))
    y1, y2 = sorted((a[1], b[1]))

    if not (
        contains(x1, y1)
        and contains(x1, y2)
        and contains(x2, y1)
        and contains(x2, y2)
    ):
        return False

    if x1 == x2 or y1 == y2:
        return contains((x1 + x2) / 2, (y1 + y2) / 2) and not boundary_crosses_line(
            x1, y1, x2, y2
        )

    return (
        contains((x1 + x2) / 2, (y1 + y2) / 2)
        and not boundary_crosses_interior(x1, y1, x2, y2)
    )


print("Part 1:", area(*rectangles[0]))
print("Part 2:", area(*next(pair for pair in rectangles if contained(*pair))))
