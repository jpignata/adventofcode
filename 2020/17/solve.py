import sys
from itertools import product
from collections import defaultdict


def simulate3(cubes, cycles=6):
    adjacent = [xyz for xyz in product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1))
                if xyz != (0, 0, 0)]

    for _ in range(cycles):
        next_cubes = cubes.copy()

        for (x, y, z), cube in list(cubes.items()):
            neighbors = sum(cubes[(x+dx, y+dy, z+dz)]
                            for dx, dy, dz in adjacent)

        for (x, y, z), cube in list(cubes.items()):
            neighbors = sum(cubes[(x+dx, y+dy, z+dz)]
                            for dx, dy, dz in adjacent)

            if cube == 1 and neighbors not in (2, 3):
                next_cubes[(x, y, z)] = 0
            elif cube == 0 and neighbors == 3:
                next_cubes[(x, y, z)] = 1

        cubes = next_cubes

    return sum(cubes.values())


def simulate4(cubes, cycles=6):
    adjacent = [xyzw for xyzw in
                product((-1, 0, 1), (-1, 0, 1), (-1, 0, 1), (-1, 0, 1))
                if xyzw != (0, 0, 0, 0)]

    for _ in range(cycles):
        next_cubes = cubes.copy()

        for (x, y, z, w), cube in list(cubes.items()):
            neighbors = sum(cubes[(x+dx, y+dy, z+dz, w+dw)]
                            for dx, dy, dz, dw in adjacent)

        for (x, y, z, w), cube in list(cubes.items()):
            neighbors = sum(cubes[(x+dx, y+dy, z+dz, w+dw)]
                            for dx, dy, dz, dw in adjacent)

            if cube == 1 and neighbors not in (2, 3):
                next_cubes[(x, y, z, w)] = 0
            elif cube == 0 and neighbors == 3:
                next_cubes[(x, y, z, w)] = 1

        cubes = next_cubes

    return sum(cubes.values())


cubes3 = defaultdict(int)
cubes4 = defaultdict(int)

for y, line in enumerate(sys.stdin.readlines()):
    for x, cell in enumerate(line.strip()):
        cubes3[(x, y, 0)] = 1 if cell == '#' else 0
        cubes4[(x, y, 0, 0)] = 1 if cell == '#' else 0

print('Part 1:', simulate3(cubes3))
print('Part 2:', simulate4(cubes4))
