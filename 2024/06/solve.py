import sys
from collections import defaultdict


def traverse(x, y, obstructions, edge):
    visited = defaultdict(set)
    dx, dy = 0, -1

    while True:
        if (dx, dy) in visited[(x, y)]:
            return {}, True

        visited[(x, y)].add((dx, dy))

        while True:
            if (nx := x + dx) < 0 or nx > edge or (ny := y + dy) < 0 or ny > edge:
                return visited, False

            if (nx, ny) in obstructions:
                dx, dy = dy * -1, dx
            else:
                x, y = nx, ny
                break


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
