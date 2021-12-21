import sys
import re
from itertools import cycle, count, product
from functools import cache


def deterministic(position1, position2):
    positions = [position1, position2]
    scores = [0, 0]
    die = cycle(range(1, 101))

    for turn in count():
        roll = sum(next(die) for _ in range(3))
        player = turn % 2
        positions[player] = ((positions[player] + roll - 1) % 10) + 1
        scores[player] += positions[player]

        if scores[player] >= 1000:
            return min(scores) * (turn + 1) * 3


@cache
def quantum(position1, position2, score1=0, score2=0, new_round=True):
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1

    position = position1 if new_round else position2
    next_positions = [((position + roll - 1) % 10) + 1 for roll in rolls]

    if new_round:
        turns = [quantum(position, position2, score1 + position, score2, False)
                 for position in next_positions]
    else:
        turns = [quantum(position1, position, score1, score2 + position)
                 for position in next_positions]

    return tuple(sum(wins) for wins in list(zip(*turns)))


start1, start2 = [int(position) for line in sys.stdin.readlines()
                  for position in re.findall(r'\d$', line)]
rolls = [sum(roll) for roll in product(range(1, 4), repeat=3)]

print('Part 1:', deterministic(start1, start2))
print('Part 2:', max(quantum(start1, start2)))
