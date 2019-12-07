import sys
import itertools
from collections import deque

class Computer:
    def __init__(self, program, inputs):
        self.program = program
        self.inputs = deque(inputs)
        self.outputs = deque([])
        self.pointer = 0
        self.halted = False

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
        self.halted = True

    def operation(self, opcode):
        operations = {1: self.add, 2: self.mul, 3: self.get, 4: self.put,
                      5: self.jump_if_true, 6: self.jump_if_false,
                      7: self.less_than, 8: self.equals, 99: self.halt}

        return operations[opcode]

    def tick(self):
        if not self.halted:
            opcode = str(program[self.pointer]).zfill(5)
            param1 = self.param(opcode, 1)
            param2 = self.param(opcode, 2)
            operation = self.operation(int(opcode[-2:]))

            operation(param1, param2)


def find(program, permutations, part=1):
    results = []

    for permutation in permutations:
        computers = []

        for phase in permutation:
            computer = Computer(program.copy(), [phase])
            computers.append(computer)

        if part == 1:
            for i, computer in enumerate(computers):
                if computers[i - 1].outputs:
                    output = computers[i - 1].outputs.popleft()
                else:
                    output = 0

                computer.inputs.append(output)

                while not computer.halted:
                    computer.tick()

            results.append(computers[-1].outputs.popleft())

        if part == 2:
            while not computers[-1].halted:
                for i, computer in enumerate(computers):
                    if computers[i - 1].outputs:
                        output = computers[i - 1].outputs.popleft()
                    else:
                        output = 0

                    computer.inputs.append(output)

                    while len(computer.outputs) == 0 and not computer.halted:
                        computer.tick()

            results.append(computers[0].inputs.popleft())

    return max(results)


with open(sys.argv[1]) as f:
    program = [int(i) for i in f.readline().strip().split(',')]

    print(f'Part 1: {find(program, itertools.permutations(range(5)))}')
    print(f'Part 2: {find(program, itertools.permutations(range(5, 10)), 2)}')
