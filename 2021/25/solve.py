import sys
from itertools import count

east, south = set(), set()
lenx, leny = 0, 0

for y, line in enumerate(sys.stdin):
    leny = max(leny, y + 1)

    for x, char in enumerate(line.strip()):
        lenx = max(lenx, x + 1)

        if char == ">":
            east.add((x, y))
        elif char == "v":
            south.add((x, y))

for step in count(1):
    next_east, next_south = set(), set()

    for (x, y) in east:
        adjacent = ((x + 1) % lenx, y)

        if adjacent not in east and adjacent not in south:
            next_east.add(adjacent)
        else:
            next_east.add((x, y))

    for (x, y) in south:
        adjacent = (x, (y + 1) % leny)

        if adjacent not in next_east and adjacent not in south:
            next_south.add(adjacent)
        else:
            next_south.add((x, y))

    if next_east == east and next_south == south:
        print("Part 1:", step)
        break

    east, south = next_east, next_south
