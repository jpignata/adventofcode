import sys
import operator
from itertools import count
from string import ascii_uppercase


def route(diagram):
    letters = list()
    dirs = {'u': (0, -1), 'd': (0, 1), 'l': (-1, 0), 'r': (1, 0)}
    direction = 'd'
    location = (diagram[0].index('|'), 0)

    for step in count(1):
        x, y = map(operator.add, location, dirs[direction])
        location = (x, y)
        char = diagram[y][x]

        if char == '+':
            if direction in ('d', 'u'):
                if x - 1 >= 0 and diagram[y][x - 1] == '-':
                    direction = 'l'
                elif x + 1 < len(diagram[0]) and diagram[y][x + 1] == '-':
                    direction = 'r'
            elif direction in ('l', 'r'):
                if y - 1 >= 0 and diagram[y - 1][x] == '|':
                    direction = 'u'
                elif y + 1 < len(diagram) and diagram[y + 1][x] == '|':
                    direction = 'd'
        elif char in ascii_uppercase:
            letters.append(char)
        elif char == ' ':
            return (''.join(letters), step)


letters, steps = route([list(line.rstrip('\n')) for line in sys.stdin])

print('Part 1:', letters)
print('Part 2:', steps)
