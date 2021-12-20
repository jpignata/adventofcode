import sys
from itertools import product


def enhance(grid, times):
    def pixel(x, y):
        bits = [str(grid.get((x+dx, y+dy), default)) for dy, dx in deltas]
        return algorithm[int(''.join(bits), 2)]

    for i in range(times):
        default = '0' if algorithm[0] == 0 or i % 2 == 0 else '1'
        pixels = {(x+dx, y+dy) for x, y in grid for dy, dx in deltas}
        grid = {(x, y): pixel(x, y) for x, y in pixels}

    return sum(grid.values())


deltas = list(product((-1, 0, 1), repeat=2))
algorithm = [int(c == '#') for c in sys.stdin.readline().strip()]
grid = {(x, y): int(char == '#')
        for y, line in enumerate(sys.stdin.readlines()[1:])
        for x, char in enumerate(line.strip())}

print('Part 1:', enhance(grid, 2))
print('Part 2:', enhance(grid, 50))
