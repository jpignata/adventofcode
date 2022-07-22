import sys
from itertools import product

neighbors = tuple(xy for xy in product((-1, 0, 1), repeat=2) if any(xy))


def adjacent(x, y, rows):
    return sum(
        1
        for (dx, dy) in neighbors
        if 0 <= y + dy < len(rows) and 0 <= x + dx < len(rows[0])
        if rows[y + dy][x + dx] == "#"
    )


def visible(x, y, rows):
    occupied = 0

    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy

        while 0 <= ny < len(rows) and 0 <= nx < len(rows[0]):
            if rows[ny][nx] == ".":
                nx += dx
                ny += dy
            else:
                if rows[ny][nx] == "#":
                    occupied += 1

                break

    return occupied


def simulate(rows, strategy, tolerance):
    next_rows = [row[:] for row in rows]

    for y, row in enumerate(rows):
        for x, seat in enumerate(row):
            if seat != ".":
                occupied = strategy(x, y, rows)

                if seat == "L" and occupied == 0:
                    next_rows[y][x] = "#"
                elif seat == "#" and occupied >= tolerance:
                    next_rows[y][x] = "L"

    if next_rows == rows:
        return sum(row.count("#") for row in rows)

    return simulate(next_rows, strategy, tolerance)


def solve():
    rows = [list(line.strip()) for line in sys.stdin.readlines()]

    print("Part 1:", simulate(rows, adjacent, 4))
    print("Part 2:", simulate(rows, visible, 5))


if __name__ == "__main__":
    solve()
