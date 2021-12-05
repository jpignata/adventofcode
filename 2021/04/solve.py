import math
import sys

boards = []

for line in sys.stdin:
    if ',' in line:
        balls = {int(ball): i for i, ball in enumerate(line.split(','))}
    elif line == '\n':
        boards.append([])
    else:
        boards[-1].append([int(number) for number in line.split()])

first = (math.inf, None)
last = (-math.inf, None)

for i, board in enumerate(boards):
    ball = math.inf

    for row in board + list(zip(*board)):
        ball = min(ball, max(balls[num] for num in row if num in balls))

    first = min(first, (ball, i))
    last = max(last, (ball, i))


def score(ball, board):
    return sum(num for row in boards[board] for num in row
               if balls[num] > ball) * list(balls.keys())[ball]


print('Part 1:', score(*first))
print('Part 2:', score(*last))
