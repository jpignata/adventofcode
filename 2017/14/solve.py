import sys
import operator
from collections import deque
from itertools import zip_longest
from functools import reduce


def knothash(input, *, rounds=64):
    def grouper(iterable, n):
        args = [iter(iterable)] * n
        return zip_longest(*args)

    numbers = deque(range(256))
    lengths = [ord(c) for c in input] + [17, 31, 73, 47, 23]
    skip = 0

    for _ in range(rounds):
        for length in lengths:
            q = deque()

            for _ in range(length):
                q.append(numbers.popleft())

            while q:
                numbers.appendleft(q.popleft())

            numbers.rotate((length + skip) * -1)
            skip += 1

    numbers.rotate((sum(lengths) * rounds) + sum(range(1, skip)))

    return "".join(
        f"{c:02x}" for c in [reduce(operator.xor, g) for g in grouper(numbers, 16)]
    )


def regions(grid):
    count = 0
    visited = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x, y) not in visited and grid[y][x] == "#":
                q = deque([(x, y)])
                count += 1

                while q:
                    nx, ny = q.popleft()

                    for delta in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                        dx, dy = map(operator.add, (nx, ny), delta)

                        if (
                            0 <= dx < len(grid[0])
                            and 0 <= dy < len(grid)
                            and (dx, dy) not in visited
                            and grid[dy][dx] == "#"
                        ):
                            q.append((dx, dy))

                    visited.add((nx, ny))

    return count


def build(key, length):
    grid = [[] for _ in range(length)]

    for i in range(len(grid)):
        for hex in knothash(f"{key}-{i}"):
            for bit in f"{int(hex, 16):04b}":
                grid[i].append("#" if bit == "1" else ".")

    return grid


grid = build("jxqlasbh", 128)

print("Part 1:", sum(row.count("#") for row in grid))
print("Part 2:", regions(grid))
