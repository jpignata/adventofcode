import sys
from itertools import cycle
from math import lcm
from re import findall

moves = sys.stdin.readline().strip()
edges = {}

for line in sys.stdin:
    if nodes := findall(r"[0-9A-Z]{3}", line):
        edges[nodes[0]] = {"L": nodes[1], "R": nodes[2]}


def find(current):
    steps = 0
    move = cycle(moves)

    while not current.endswith("Z"):
        current = edges[current][next(move)]
        steps += 1

    return steps


distances = [find(node) for node in edges if node.endswith("A")]

print("Part 1:", find("AAA"))
print("Part 2:", lcm(*distances))
