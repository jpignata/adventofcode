import sys
from collections import defaultdict
from itertools import cycle


def find(x, y, obstacles, boundary):
    visited = defaultdict(int)
    path = set()
    dirs = cycle([(0, -1), (1, 0), (0, 1), (-1, 0)])
    dir_ = next(dirs)

    while True:
        if visited[(x, y, dir_)]:
            return path, True

        visited[(x, y, dir_)] += 1
        path.add((x, y))

        while True:
            nx, ny = x + dir_[0], y + dir_[1]

            if nx < 0 or nx > boundary or ny < 0 or ny > boundary:
                return path, False

            if (nx, ny) not in obstacles:
                break

            dir_ = next(dirs)

        x, y = nx, ny


def main():
    obstacles = set()
    sx, sy = 0, 0
    boundary = 0

    for y, line in enumerate(sys.stdin):
        boundary = max(boundary, y)

        for x, char in enumerate(line.strip()):
            if char == "#":
                obstacles.add((x, y))
            elif char == "^":
                sx, sy = x, y

    path, _ = find(sx, sy, obstacles, boundary)

    print("Part 1:", len(path))
    print(
        "Part 2:",
        sum(
            has_cycle
            for _, has_cycle in (
                find(sx, sy, obstacles | {(x, y)}, boundary)
                for x, y in path - {(sx, sy)}
            )
        ),
    )


if __name__ == "__main__":
    main()
