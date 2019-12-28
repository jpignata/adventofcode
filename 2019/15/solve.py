import sys
from collections import deque
from operator import add

from intcode import Computer


def build(grid):
    q = deque([[(0, 0), Computer.load().program]])
    station = (-1, -1)

    while q:
        position, program = q.popleft()
        output = -1

        for delta, command in directions:
            move = tuple(map(add, delta, position))

            computer = Computer(program.copy())
            computer.inputs.append(command)

            while not computer.outputs:
                computer.tick()

            output = computer.outputs.popleft()

            if output != 0:
                if move not in grid:
                    q.append([move, computer.program])

            if output == 2:
                station = move

            grid[move] = output

    return station


def find(grid):
    q = deque([[(0, 0), 0]])
    visited = set()

    while q:
        position, distance = q.popleft()
        visited.add(position)

        if grid[position] == 2:
            return distance

        for delta, _ in directions:
            move = tuple(map(add, position, delta))

            if move not in visited and move in grid and grid[move] != 0:
                q.append([move, distance + 1])


def fill(grid, start, minute=0):
    q = deque([[start, minute]])

    while q:
        position, minute = q.popleft()

        for delta, _ in directions:
            move = tuple(map(add, position, delta))

            if grid[move] == 1:
                grid[move] = 2

                q.append([move, minute + 1])

    return minute


grid = dict({(0, 0): 0})
directions = (((-1, 0), 1), ((0, 1), 4), ((1, 0), 2), ((0, -1), 3))
oxygen = build(grid)

print('Part 1:', find(grid))
print('Part 2:', fill(grid, oxygen))
