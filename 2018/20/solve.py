import sys
import operator
from collections import defaultdict

current = (0, 0)
directions = {'N': (0, -1), 'S': (0, 1), 'E': (1, 0), 'W': (-1, 0)}
rooms = defaultdict(lambda: float('inf'))
rooms[current] = 0
context = []

for char in sys.stdin.readline().strip():
    if char == '(':
        context.append(current)
    elif char == '|':
        current = context[-1]
    elif char == ')':
        current = context.pop()
    elif char in directions:
        cost = rooms[current]
        current = tuple(map(operator.add, current, directions[char]))
        rooms[current] = min(rooms[current], cost + 1)

print('Part 1:', max(rooms.values()))
print('Part 2:', sum(1 for cost in rooms.values() if cost >= 1000))
