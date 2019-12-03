import sys
import operator
from collections import defaultdict


def closest_intersection(grid):
    distances = list()

    for cell, wires in grid.items():
        if len(wires) == 2:
            distances.append(sum(map(abs, cell)))

    return min(distances)


def fewest_steps_to_intersection(grid):
    steps = list()

    for _, wires in grid.items():
        if len(wires) == 2:
            steps.append(sum(wires.values()))

    return min(steps)


grid = defaultdict(lambda: defaultdict(int))
moves = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}

for wire, line in enumerate(sys.stdin):
    curr = (0, 0)
    total = 0

    for move in line.strip().split(','):
        direction = move[0]
        steps = int(move[1:])

        for _ in range(steps):
            curr = tuple(map(operator.add, curr, moves[direction]))
            total += 1
            grid[curr][wire] += total

print(f'Part 1: {closest_intersection(grid)}')
print(f'Part 2: {fewest_steps_to_intersection(grid)}')
