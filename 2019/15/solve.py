import curses
import random
import sys
import itertools
from collections import deque, defaultdict
from operator import itemgetter, add
from os import system


class Input(Exception):
    pass


class Computer:
    def __init__(self, program):
        self.halted = False
        self.program = program
        self.inputs = deque([])
        self.outputs = deque([])
        self.pointer = 0
        self.base = 0

    def param(self, opcode, position):
        modes = list(reversed(opcode[:3]))
        mode = modes[position - 1]

        try:
            if mode == '0':
                return self.program[self.pointer + position]
            elif mode == '1':
                return self.pointer + position
            elif mode == '2':
                return self.program[self.pointer + position] + self.base
            else:
                raise f'Unknown parameter mode: {mode}'
        except IndexError:
            return None

    def getval(self, address):
        if address < 0:
            raise f'Invalid address: {address}'

        return self.program[address]

    def add(self, param1, param2, param3):
        self.program[param3] = self.getval(param1) + self.getval(param2)
        self.pointer += 4

    def mul(self, param1, param2, param3):
        self.program[param3] = self.getval(param1) * self.getval(param2)
        self.pointer += 4

    def get(self, param1, *_):
        if len(self.inputs) == 0:
            raise Input
        self.program[param1] = self.inputs.popleft()
        self.pointer += 2

    def put(self, param1, *_):
        self.outputs.append(self.getval(param1))
        self.pointer += 2

    def jump_if_true(self, param1, param2, *_):
        if self.getval(param1) != 0:
            self.pointer = self.getval(param2)
        else:
            self.pointer += 3

    def jump_if_false(self, param1, param2, *_):
        if self.getval(param1) == 0:
            self.pointer = self.getval(param2)
        else:
            self.pointer += 3

    def less_than(self, param1, param2, param3):
        self.program[param3] = int(self.getval(param1) < self.getval(param2))
        self.pointer += 4

    def equals(self, param1, param2, param3):
        self.program[param3] = int(self.getval(param1) == self.getval(param2))
        self.pointer += 4

    def set_base(self, param1, *_):
        self.base += self.getval(param1)
        self.pointer += 2

    def halt(self, *_):
        self.halted = True

    def tick(self):
        operations = {1: self.add, 2: self.mul, 3: self.get, 4: self.put,
                      5: self.jump_if_true, 6: self.jump_if_false,
                      7: self.less_than, 8: self.equals, 9: self.set_base,
                      99: self.halt}

        opcode = str(self.getval(self.pointer)).zfill(5)
        param1 = self.param(opcode, 1)
        param2 = self.param(opcode, 2)
        param3 = self.param(opcode, 3)
        operation = operations[int(opcode[-2:])]

        operation(param1, param2, param3)


def build(program, grid):
    q = deque([[(0, 0), program.copy()]])
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


def draw(grid):
    for y in range(max(grid.keys(), key=itemgetter(1))[1]):
        for x in range(max(grid.keys(), key=itemgetter(0))[0]):
            if (x, y) not in grid:
                print('?', end='')
            elif grid[(x, y)] == 0:
                print('#', end='')
            elif grid[(x, y)] == 1:
                print('.', end='')
            elif grid[(x, y)] == 2:
                print('O', end='')
        print()


program = defaultdict(int)

for i, digit in enumerate(sys.stdin.readline().split(',')):
    program[i] = int(digit)

grid = dict({(0, 0): 0})
directions = (((-1, 0), 1), ((0, 1), 4), ((1, 0), 2), ((0, -1), 3))
oxygen = build(program, grid)

print(f'Part 1: {find(grid)}')
print(f'Part 2: {fill(grid, oxygen)}')
