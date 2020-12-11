import sys
from copy import deepcopy
from itertools import product

adjacent = [c for c in tuple(product((-1, 0, 1), (-1, 0, 1))) if c != (0, 0)]


def strategy_adjacent(x, y, rows):
    return sum(1 for (dx, dy) in adjacent if 0 <= y+dy < len(rows)
               and 0 <= x+dx < len(rows[0]) and rows[y+dy][x+dx] == '#')


def strategy_visible(x, y, rows):
    occupied = 0

    for ax, ay in adjacent:
        dx, dy = ax, ay

        while 0 <= x+dx < len(rows[0]) and 0 <= y+dy < len(rows):
            if rows[y+dy][x+dx] == '.':
                dx += ax
                dy += ay
            elif rows[y+dy][x+dx] == '#':
                occupied += 1
                break
            else:
                break

    return occupied


def simulate(rows, strategy, tolerance):
    next_rows = deepcopy(rows)

    for y, row in enumerate(rows):
        for x, seat in enumerate(row):
            if seat != '.':
                occupied = strategy(x, y, rows)

                if seat == 'L' and occupied == 0:
                    next_rows[y][x] = '#'
                elif seat == '#' and occupied >= tolerance:
                    next_rows[y][x] = 'L'

    if next_rows == rows:
        return sum(1 for row in rows for seat in row if seat == '#')
    else:
        return simulate(next_rows, strategy, tolerance)


rows = [list(line.strip()) for line in sys.stdin.readlines()]

print('Part 1:', simulate(rows, strategy_adjacent, 4))
print('Part 2:', simulate(rows, strategy_visible, 5))
