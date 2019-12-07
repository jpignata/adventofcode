import sys
import itertools
from collections import deque


class Output(Exception):
    pass


class Halt(Exception):
    pass


class Computer:
    def __init__(self, program, phase):
        self.program = program
        self.inputs = deque([phase])
        self.outputs = deque([])
        self.pointer = 0

    def param(self, opcode, position):
        modes = list(reversed(opcode[1:3]))

        try:
            if modes[position - 1] == '1':
                return self.program[self.pointer + position]
            else:
                return self.program[self.program[self.pointer + position]]
        except IndexError:
            return None

    def add(self, param1, param2):
        address = self.program[self.pointer + 3]
        self.program[address] = param1 + param2
        self.pointer += 4

    def mul(self, param1, param2):
        address = self.program[self.pointer + 3]
        self.program[address] = param1 * param2
        self.pointer += 4

    def get(self, *_):
        address = self.program[self.pointer + 1]
        self.program[address] = self.inputs.popleft()
        self.pointer += 2

    def put(self, param1, *_):
        self.outputs.append(param1)
        self.pointer += 2

        raise Output

    def jump_if_true(self, param1, param2):
        if param1 != 0:
            self.pointer = param2
        else:
            self.pointer += 3

    def jump_if_false(self, param1, param2):
        if param1 == 0:
            self.pointer = param2
        else:
            self.pointer += 3

    def less_than(self, param1, param2):
        address = self.program[self.pointer + 3]

        if param1 < param2:
            self.program[address] = 1
        else:
            self.program[address] = 0

        self.pointer += 4

    def equals(self, param1, param2):
        address = self.program[self.pointer + 3]

        if param1 == param2:
            self.program[address] = 1
        else:
            self.program[address] = 0

        self.pointer += 4

    def halt(self, *_):
        raise Halt

    def operation(self, opcode):
        operations = {1: self.add, 2: self.mul, 3: self.get, 4: self.put,
                      5: self.jump_if_true, 6: self.jump_if_false,
                      7: self.less_than, 8: self.equals, 99: self.halt}

        return operations[opcode]

    def run(self):
        while True:
            opcode = str(program[self.pointer]).zfill(5)
            param1 = self.param(opcode, 1)
            param2 = self.param(opcode, 2)
            operation = self.operation(int(opcode[-2:]))

            operation(param1, param2)


def find(program, start, end):
    results = []

    for permutation in itertools.permutations(range(start, end + 1)):
        computers = [Computer(program.copy(), phase) for phase in permutation]
        signal = 0
        i = 0

        while True:
            computers[i].inputs.append(signal)

            try:
                computers[i].run()
            except Output:
                signal = computers[i].outputs.popleft()
            except Halt:
                results.append(signal)
                break

            i = (i + 1) % len(computers)

    return max(results)


program = [int(i) for i in sys.stdin.readline().split(',')]

print(f'Part 1: {find(program, 0, 4)}')
print(f'Part 2: {find(program, 5, 9)}')
