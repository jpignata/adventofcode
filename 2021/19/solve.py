import sys
from itertools import combinations


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def adjust(point, orientation):
    x, y, z = point

    return [(x, y, z), (y, z, x), (z, x, y), (z, y, -x), (y, x, -z),
            (x, z, -y), (x, -y, -z), (y, -z, -x), (z, -x, -y), (z, -y, x),
            (y, -x, z), (x, -z, y), (-x, y, -z), (-y, z, -x), (-z, x, -y),
            (-z, y, x), (-y, x, z), (-x, z, y), (-x, -y, z), (-y, -z, x),
            (-z, -x, y), (-z, -y, -x), (-y, -x, -z), (-x, -z, -y)][orientation]


def orientations(coords):
    return ((i, {adjust(coord, i) for coord in coords}) for i in range(24))


def dists(coords):
    return {a: {sum(abs(x - y) for x, y in zip(a, b)) for b in coords}
            for a in coords}


def overlap(offsets1, offsets2):
    for x, xdists in offsets1.items():
        for y, ydists in offsets2.items():
            if len(xdists & ydists) >= 12:
                return x, y


def find(scanner1, scanner2):
    if (result := overlap(dists(scanner1), dists(scanner2))):
        point1, point2 = result
        offsets1 = {sub(point1, x) for x in scanner1}
        offsets2 = {sub(point2, x) for x in scanner2}

        for orientation, coords in orientations(offsets2):
            if len(offsets1 & coords) >= 12:
                return sub(point1, adjust(point2, orientation)), orientation


scanners = []

for line in sys.stdin:
    if 'scanner' in line:
        scanners.append(set())
    elif ',' in line:
        scanners[-1].add(tuple(int(c) for c in line.split(',')))

beacons = scanners.pop(0)
locations = [(0, 0, 0)]

while scanners:
    for i, readings in enumerate(scanners):
        if (result := find(beacons, readings)):
            offset, orientation = result
            locations.append(offset)
            beacons |= {add(adjust(x, orientation), offset) for x in readings}
            del scanners[i]
            break

furthest = max(sum(abs(x-y) for x, y in zip(a, b))
               for a, b in combinations(locations, 2))

print('Part 1:', len(beacons))
print('Part 2:', furthest)
