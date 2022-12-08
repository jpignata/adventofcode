import sys
from math import inf, prod


def solve():
    grid = [[int(height) for height in line.strip()] for line in sys.stdin]

    print("Part 1:", visible(grid))
    print("Part 2:", ideal(grid))


def visible(grid):
    trees = set()
    length = len(grid)

    def find(x, y, dx, dy):
        max_height = -inf

        while 0 <= x < length and 0 <= y < length:
            if grid[y][x] > max_height:
                trees.add((x, y))
                max_height = grid[y][x]

            x += dx
            y += dy

    for i in range(length):
        find(i, 0, 0, 1)
        find(i, length - 1, 0, -1)
        find(0, i, 1, 0)
        find(length - 1, i, -1, 0)

    return len(trees)


def ideal(grid):
    length = len(grid)

    def score(x, y):
        distances = []

        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            nx, ny = x + dx, y + dy
            distance = 0

            while 0 <= nx < length and 0 <= ny < length:
                distance += 1

                if grid[ny][nx] >= grid[y][x]:
                    break

                nx += dx
                ny += dy

            distances.append(distance)

        return prod(distances)

    return max(score(x, y) for x in range(length) for y in range(length))


if __name__ == "__main__":
    solve()
