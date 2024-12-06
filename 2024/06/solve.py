import sys
from collections import defaultdict
from itertools import cycle


def traverse(x, y, obstructions, edge):
    visited = defaultdict(set)
    dirs = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    dx, dy = next(dirs)

    while True:
        if (dx, dy) in visited[(x, y)]:
            return {}, True

        visited[(x, y)].add((dx, dy))

        while True:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx > edge or ny < 0 or ny > edge:
                return visited, False

            if (nx, ny) not in obstructions:
                break

            dx, dy = next(dirs)

        x, y = nx, ny


def main():
    obstructions = set()
    sx, sy = 0, 0

    for y, line in enumerate(sys.stdin):
        edge = y

        for x, char in enumerate(line.strip()):
            if char == "#":
                obstructions.add((x, y))
            elif char == "^":
                sx, sy = x, y

    path, _ = traverse(sx, sy, obstructions, edge)
    placements = sum(
        has_cycle
        for _, has_cycle in (
            traverse(sx, sy, obstructions | {(x, y)}, edge) for x, y in path
        )
    )

    print("Part 1:", len(path))
    print("Part 2:", placements)


if __name__ == "__main__":
    main()
