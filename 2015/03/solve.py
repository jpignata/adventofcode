import sys
import operator
from collections import Counter
from itertools import cycle

directions = sys.stdin.readline().strip()
moves = {'>': (0, 1), '<': (0, -1), '^': (1, 0), 'v': (-1, 0)}


def deliver(number_of_santas=1):
    start = (0, 0)
    houses = Counter({start: number_of_santas})
    pos = {num: start for num in range(number_of_santas)}
    turn = cycle(pos)

    for move in directions:
        santa = next(turn)
        pos[santa] = tuple(map(operator.add, pos[santa], moves[move]))
        houses[pos[santa]] += 1

    return len(houses)


print('Part 1:', deliver())
print('Part 2:', deliver(2))
