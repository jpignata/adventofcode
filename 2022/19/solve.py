import sys
from math import prod
from operator import add, sub
from re import findall


def solve():
    blueprints = []

    for line in sys.stdin:
        data = tuple(int(number) for number in findall(r"[0-9]+", line))
        blueprints.append(
            (
                ((0, 0, 0, 0), (0, 0, 0, 0)),
                ((0, 0, 0, data[1]), (0, 0, 0, 1)),
                ((0, 0, 0, data[2]), (0, 0, 1, 0)),
                ((0, 0, data[4], data[3]), (0, 1, 0, 0)),
                ((0, data[6], 0, data[5]), (1, 0, 0, 0)),
            )
        )

    part1 = sum(simulate(blueprint) * (i + 1) for i, blueprint in enumerate(blueprints))
    part2 = prod(simulate(blueprint, 32) for blueprint in blueprints[:3])

    print("Part 1:", part1)
    print("Part 2:", part2)


def simulate(blueprint, minutes=24):
    s = [((0, 0, 0, 0), (0, 0, 0, 1))]

    for _ in range(minutes):
        next_s = []

        for items, robots in s:
            for costs, yields in blueprint:
                if all(item >= cost for item, cost in zip(items, costs)):
                    next_items = tuple(map(sub, items, costs))
                    next_items = tuple(map(add, next_items, robots))
                    next_robots = tuple(map(add, robots, yields))

                    next_s.append((next_items, next_robots))

        s = sorted(next_s, key=lambda x: tuple(map(add, x[0], x[1])))[-1000:]

    return max(s)[0][0]


if __name__ == "__main__":
    solve()
