import re
import sys
from collections import Counter
from itertools import product


def coords(p1, p2):
    if p1 > p2:
        return range(p1, p2 - 1, -1)

    return range(p1, p2 + 1)


part1, part2 = Counter(), Counter()

for line in sys.stdin:
    x1, y1, x2, y2 = [int(number) for number in re.findall(r'\d+', line)]
    rangex = coords(x1, x2)
    rangey = coords(y1, y2)

    if x1 == x2 or y1 == y2:
        points = list(product(rangex, rangey))
        part1.update(points)
        part2.update(points)
    else:
        part2.update(zip(rangex, rangey))

print('Part 1:', sum(count > 1 for count in part1.values()))
print('Part 2:', sum(count > 1 for count in part2.values()))
