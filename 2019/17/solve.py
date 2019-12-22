import sys
from collections import deque, defaultdict
from operator import add
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


def build(program):
    computer = Computer(program)
    grid = []
    row = []

    while not computer.halted:
        computer.tick()

    while computer.outputs:
        char = computer.outputs.popleft()

        if char == 10:
            grid.append(row)
            row = []
        else:
            row.append(chr(char))

    return grid


def alignment_parameters(grid):
    moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
    intersections = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                for move in moves:
                    dx, dy = tuple(map(add, move, (x, y)))

                    if 0 <= dy < len(grid) and 0 <= dx < len(grid[dy]):
                        if grid[dy][dx] == '.':
                            break
                else:
                    intersections.append((x, y))

    return sum(x * y for x, y in intersections)


program = defaultdict(int)

for i, digit in enumerate(sys.stdin.readline().split(',')):
    program[i] = int(digit)

grid = build(program)

print('Part 1:', alignment_parameters(grid))
