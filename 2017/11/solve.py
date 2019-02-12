import sys
import operator

dirs = {'nw': (-1, 0, 1), 'n': (-1, 1, 0), 'ne': (0, 1, -1), 'sw': (0, -1, 1),
        's': (1, -1, 0), 'se': (1, 0, -1)}
current = (0, 0, 0)
distance = furthest = 0

for move in sys.stdin.readline().strip().split(','):
    current = tuple(map(operator.add, current, dirs[move]))
    distance = max(map(abs, current))
    furthest = max(distance, furthest)

print('Part 1:', distance)
print('Part 2:', furthest)
