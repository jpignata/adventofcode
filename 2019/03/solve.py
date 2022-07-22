import sys
import operator
from collections import defaultdict

grid = defaultdict(lambda: defaultdict(int))
moves = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
distances, steps = list(), list()

for wire, line in enumerate(sys.stdin):
    curr = (0, 0)
    total = 0

    for move in line.strip().split(","):
        for _ in range(int(move[1:])):
            curr = tuple(map(operator.add, curr, moves[move[0]]))
            total += 1
            grid[curr][wire] += total

for cell, wires in grid.items():
    if len(wires) == 2:
        distances.append(sum(map(abs, cell)))
        steps.append(sum(wires.values()))

print("Part 1:", min(distances))
print("Part 2:", min(steps))
