import sys
from itertools import product
from functools import lru_cache


def simulate(cubes, dims, cycles=6):
    cubes = {tuple(0 if i >= len(pos) else pos[i] for i in range(dims)): cube
            for pos, cube in cubes.items()}
    adjacent = [pos for pos in product(*((-1, 0, 1) for _ in range(dims)))
                if not all(p == 0 for p in pos)]

    @lru_cache(maxsize=None)
    def neighbors(pos):
        return [tuple(c + d for c, d in zip(pos, adj)) for adj in adjacent]

    for _ in range(cycles):
        next_cubes = cubes.copy()

        for pos in list(cubes):
            for neighbor in neighbors(pos):
                cubes[neighbor] = cubes.get(neighbor, 0)

        for pos in cubes:
            active = sum(cubes.get(neighbor, 0) for neighbor in neighbors(pos))

            if cubes[pos] == 1 and active != 2 and active != 3:
                next_cubes[pos] = 0
            elif cubes[pos] == 0 and active == 3:
                next_cubes[pos] = 1

        cubes = next_cubes

    return sum(cubes.values())


cubes = {}

for y, line in enumerate(sys.stdin.readlines()):
    for x, cell in enumerate(line.strip()):
        cubes[(x, y)] = 1 if cell == '#' else 0

print('Part 1:', simulate(cubes, 3))
print('Part 2:', simulate(cubes, 4))
