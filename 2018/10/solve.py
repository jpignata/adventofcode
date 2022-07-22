import sys
import re
from operator import itemgetter, add
from itertools import count

stars = [tuple(map(int, re.findall(r"([-\d]+)", line))) for line in sys.stdin]

for second in count(1):
    for i, star in enumerate(stars):
        coords = tuple(map(add, (star[0], star[1]), (star[2], star[3])))
        stars[i] = coords + (star[2], star[3])

    minx, maxx = min(map(itemgetter(0), stars)), max(map(itemgetter(0), stars))
    miny, maxy = min(map(itemgetter(1), stars)), max(map(itemgetter(1), stars))

    if maxy - miny == 9:
        print("Part 1:")

        for y in range(maxy - miny + 1):
            for x in range(maxx - minx + 1):
                for star in stars:
                    if star[0] - minx == x and star[1] - miny == y:
                        sys.stdout.write("█")
                        break
                else:
                    sys.stdout.write(" ")

            print()

        print("Part 2:", second)
        break
