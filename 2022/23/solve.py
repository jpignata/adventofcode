import sys
from collections import defaultdict, deque
from itertools import product


def solve():
    gen = {
        (x, y)
        for y, row in enumerate(sys.stdin)
        for x, cell in enumerate(row)
        if cell == "#"
    }

    print("Part 1:", empty(evolve(gen, 10)[1]))
    print("Part 2:", evolve(gen)[0])


def evolve(gen, times=int(1e12)):
    def north(x, y):
        if all((x + nx, y - 1) not in gen for nx in range(-1, 2)):
            return x, y - 1

    def south(x, y):
        if all((x + nx, y + 1) not in gen for nx in range(-1, 2)):
            return x, y + 1

    def west(x, y):
        if all((x - 1, y + ny) not in gen for ny in range(-1, 2)):
            return x - 1, y

    def east(x, y):
        if all((x + 1, y + ny) not in gen for ny in range(-1, 2)):
            return x + 1, y

    directions = deque([north, south, west, east])
    adjacent = list(xy for xy in product((-1, 0, 1), repeat=2) if any(xy))

    for i in range(times):
        next_gen = set()
        moves = {}
        proposals = defaultdict(int)

        for x, y in gen:
            if any((x + dx, y + dy) in gen for dx, dy in adjacent):
                for direction in directions:
                    if proposal := direction(x, y):
                        moves[x, y] = proposal
                        proposals[proposal] += 1
                        break

            if (x, y) not in moves:
                moves[x, y] = x, y

        for current, proposal in moves.items():
            if proposals[proposal] == 1:
                next_gen.add(proposal)
            else:
                next_gen.add(current)

        if next_gen == gen:
            break

        directions.rotate(-1)
        gen = next_gen

    return i + 1, gen


def empty(gen):
    minx, maxx = min(x for x, _ in gen), max(x for x, _ in gen)
    miny, maxy = min(y for _, y in gen), max(y for _, y in gen)

    return ((maxx - minx + 1) * (maxy - miny + 1)) - len(gen)


if __name__ == "__main__":
    solve()
