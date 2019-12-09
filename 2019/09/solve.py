import sys
import itertools
from collections import deque, defaultdict


class Computer:
    def __init__(self, program, value):
        self.halted = False
        self.program = program
        self.inputs = deque([value])
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

    def address(self, address):
        if address < 0:
            raise f'Invalid address: {address}'

        return self.program[address]

    def add(self, param1, param2, param3):
        self.program[param3] = self.address(param1) + self.address(param2)
        self.pointer += 4

    def mul(self, param1, param2, param3):
        self.program[param3] = self.address(param1) * self.address(param2)
        self.pointer += 4

    def get(self, param1, *_):
        self.program[param1] = self.inputs.popleft()
        self.pointer += 2

    def put(self, param1, *_):
        self.outputs.append(self.address(param1))
        self.pointer += 2

    def jump_if_true(self, param1, param2, *_):
        if self.address(param1) != 0:
            self.pointer = self.address(param2)
        else:
            self.pointer += 3

    def jump_if_false(self, param1, param2, *_):
        if self.address(param1) == 0:
            self.pointer = self.address(param2)
        else:
            self.pointer += 3

    def less_than(self, param1, param2, param3):
        self.program[param3] = int(self.address(param1) < self.address(param2))
        self.pointer += 4

    def equals(self, param1, param2, param3):
        self.program[param3] = int(self.address(param1) == self.address(param2))
        self.pointer += 4

    def set_base(self, param1, *_):
        self.base += self.address(param1)
        self.pointer += 2

    def halt(self, *_):
        self.halted = True

    def run(self):
        operations = {1: self.add, 2: self.mul, 3: self.get, 4: self.put,
                      5: self.jump_if_true, 6: self.jump_if_false,
                      7: self.less_than, 8: self.equals, 9: self.set_base,
                      99: self.halt}

        while not self.halted:
            opcode = str(self.address(self.pointer)).zfill(5)
            param1 = self.param(opcode, 1)
            param2 = self.param(opcode, 2)
            param3 = self.param(opcode, 3)
            operation = operations[int(opcode[-2:])]

            operation(param1, param2, param3)


def run(value):
    computer = Computer(program.copy(), value)
    computer.run()

    return computer.outputs.pop()


program = defaultdict(int)

for i, digit in enumerate(sys.stdin.readline().split(',')):
    program[i] = int(digit)

print(f'Part 1: {run(1)}')
print(f'Part 2: {run(2)}')
