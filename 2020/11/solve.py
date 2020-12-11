import sys
from itertools import product

adjacent = [xy for xy in product((-1, 0, 1), (-1, 0, 1)) if xy != (0, 0)]


def strategy_adjacent(x, y, rows):
    return sum(1 for (dx, dy) in adjacent
               if 0 <= y+dy < len(rows) and 0 <= x+dx < len(rows[0])
               if rows[y+dy][x+dx] == '#')


def strategy_visible(x, y, rows):
    occupied = 0

    for dx, dy in adjacent:
        nx, ny = x + dx, y + dy

        while 0 <= ny < len(rows) and 0 <= nx < len(rows[0]):
            if rows[ny][nx] == '.':
                nx += dx
                ny += dy
            else:
                occupied += rows[ny][nx] == '#'
                break

    return occupied


def simulate(rows, strategy, tolerance):
    next_rows = [row[:] for row in rows]

    for y, row in enumerate(rows):
        for x, seat in enumerate(row):
            if seat != '.':
                occupied = strategy(x, y, rows)

                if seat == 'L' and occupied == 0:
                    next_rows[y][x] = '#'
                elif seat == '#' and occupied >= tolerance:
                    next_rows[y][x] = 'L'

    if next_rows == rows:
        return sum(row.count('#') for row in rows)
    else:
        return simulate(next_rows, strategy, tolerance)


rows = [list(line.strip()) for line in sys.stdin.readlines()]

print('Part 1:', simulate(rows, strategy_adjacent, 4))
print('Part 2:', simulate(rows, strategy_visible, 5))
