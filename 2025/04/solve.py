import sys
from itertools import count, product
from math import inf


def remove(rolls, times=inf):
    deltas = [(x, y) for x, y in product((-1, 0, 1), repeat=2) if x or y]
    removed = set()

    for i in count(1):
        prev = len(removed)

        for x, y in rolls:
            neighbors = sum(1 for dy, dx in deltas if (x + dx, y + dy) in rolls)

            if neighbors < 4:
                removed.add((x, y))

        rolls = rolls - removed

        if i == times or prev == len(removed):
            return len(removed)


def main():
    rolls = {
        (x, y)
        for y, row in enumerate(sys.stdin)
        for x, cell in enumerate(row.strip())
        if cell == "@"
    }

    print("Part 1:", remove(rolls, 1))
    print("Part 2:", remove(rolls))


if __name__ == "__main__":
    main()
