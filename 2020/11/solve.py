import sys
from copy import deepcopy
from itertools import product

rows = [list(line.strip()) for line in sys.stdin.readlines()]
maxx, maxy = len(rows[0]), len(rows)
adjacent = tuple(pos for pos in tuple(product((-1, 0, 1), (-1, 0, 1)))
                 if pos != (0, 0))
generations = [rows]

while True:
    current_gen = generations[-1].copy()
    next_gen = deepcopy(generations[-1])

    for y, row in enumerate(current_gen):
        for x, seat in enumerate(row):
            if seat != '.':
                neighbors = [current_gen[y+dy][x+dx] for (dx, dy) in adjacent
                             if 0 <= y+dy < maxy and 0 <= x+dx < maxx]
                occupied = neighbors.count('#')

                if seat == 'L' and occupied == 0:
                    next_gen[y][x] = '#'
                elif seat == '#' and occupied >= 4:
                    next_gen[y][x] = 'L'

    if next_gen != current_gen:
        generations.append(next_gen)
    else:
        break

print('Part 1:', sum(1 for row in generations[-1] for seat in row if seat == '#'))

generations = [rows]

while True:
    current_gen = generations[-1].copy()
    next_gen = deepcopy(generations[-1])

    for y, row in enumerate(current_gen):
        for x, seat in enumerate(row):
            if seat != '.':
                occupied = 0

                for ax, ay in adjacent:
                    dx, dy = ax, ay
                    while 0 <= x+dx < maxx and 0 <= y+dy < maxy:
                        if current_gen[y+dy][x+dx] == '.':
                            dx += ax
                            dy += ay
                        elif current_gen[y+dy][x+dx] == '#':
                            occupied += 1
                            break
                        else:
                            break

                if seat == 'L' and occupied == 0:
                    next_gen[y][x] = '#'
                elif seat == '#' and occupied >= 5:
                    next_gen[y][x] = 'L'

    if next_gen != current_gen:
        generations.append(next_gen)
    else:
        break

print('Part 2:', sum(1 for row in generations[-1] for seat in row if seat == '#'))
