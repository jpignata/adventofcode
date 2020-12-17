import sys
from itertools import product


def simulate(cubes, dims, cycles=6):
    cubes = {cube + (0,) * (dims - len(cube)) for cube in cubes}
    deltas = [diff for diff in product((-1, 0, 1), repeat=dims) if any(diff)]

    for _ in range(cycles):
        neighbors = {}

        for cube in cubes:
            for delta in deltas:
                neighbor = tuple(sum(p) for p in zip(cube, delta))
                neighbors[neighbor] = neighbors.get(neighbor, 0) + 1

        cubes = {neighbor for neighbor, active in neighbors.items()
                 if (neighbor in cubes and active == 2) or active == 3}

    return len(cubes)


cubes = {(x, y) for y, line in enumerate(sys.stdin.readlines())
         for x, cell in enumerate(line.strip()) if cell == '#'}

print('Part 1:', simulate(cubes, 3))
print('Part 2:', simulate(cubes, 4))
