import sys
from itertools import product
from functools import cache


def simulate(cubes, dims, cycles=6):
    cubes = {tuple(pos[i] if i < len(pos) else 0 for i in range(dims)): active
             for pos, active in cubes.items()}
    deltas = [delta for delta in product(*((-1, 0, 1) for _ in range(dims)))
              if any(delta)]

    @cache
    def neighbors(pos):
        return [tuple(sum(p) for p in zip(pos, delta)) for delta in deltas]

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


cubes = {(x, y): int(cell == '#')
         for y, line in enumerate(sys.stdin.readlines())
         for x, cell in enumerate(line.strip())}

print('Part 1:', simulate(cubes, 3))
print('Part 2:', simulate(cubes, 4))
