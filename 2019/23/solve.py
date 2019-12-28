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


def network(program):
    computers = list()
    last = dict()
    x, y = None, None

    for i in range(50):
        computer = Computer(program.copy())
        computer.inputs.append(i)
        computers.append(computer)

    while True:
        for i, computer in enumerate(computers):
            if computer.inputs:
                last[i] = computer.inputs[0]

            try:
                computer.tick()
            except Input:
                computer.inputs.append(-1)

            if len(computer.outputs) == 3:
                destination = computer.outputs.popleft()
                x = computer.outputs.popleft()
                y = computer.outputs.popleft()

                if destination == 255:
                    yield 255, x, y
                else:
                    computers[destination].inputs.append(x)
                    computers[destination].inputs.append(y)

        if all(v == -1 for v in last.values()):
            if x is not None and y is not None:
                yield 0, x, y
                computers[0].inputs.append(x)
                computers[0].inputs.append(y)


def first(program):
    for destination, x, y in network(program):
        if destination == 255:
            return y


def repeat(program):
    last = None

    for destination, x, y in network(program):
        if destination == 0:
            if last == y:
                return y

            last = y


program = defaultdict(int)

for i, digit in enumerate(sys.stdin.readline().split(',')):
    program[i] = int(digit)

print('Part 1:', first(program))
print('Part 2:', repeat(program))
