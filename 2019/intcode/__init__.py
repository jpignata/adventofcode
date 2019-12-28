import sys
from collections import deque, defaultdict


class Input(Exception):
    pass


class Halt(Exception):
    pass


class Computer:
    @classmethod
    def load_file(cls, filename):
        return cls.load_program(open(filename).readline())

    @classmethod
    def load(cls, inputs=[]):
        if not hasattr(cls, 'stdin'):
            cls.stdin = sys.stdin.readline()

        return cls.load_program(cls.stdin, inputs)

    @classmethod
    def load_program(cls, line, inputs=[]):
        program = defaultdict(int)

        for i, digit in enumerate(line.split(',')):
            program[i] = int(digit)

        return Computer(program, inputs)

    def __init__(self, program, inputs=[]):
        self.halted = False
        self.program = program
        self.inputs = deque(inputs)
        self.outputs = deque([])
        self.pointer = 0
        self.base = 0

    def __setitem__(self, key, value):
        self.program[key] = value

    def __getitem__(self, key):
        return self.program[key]

    def execute(self, command):
        ords = [ord(c) for c in command] + [ord('\n')]

        for c in ords:
            self.inputs.append(c)

    def print_screen(self):
        while self.outputs:
            print(chr(self.outputs.popleft()), end='')

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
                raise RuntimeError(f'Unknown parameter mode: {mode}')
        except IndexError:
            return None

    def getval(self, address):
        if address < 0:
            raise RuntimeError(f'Invalid address: {address}')

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
        raise Halt

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

    def run(self):
        while not self.halted:
            try:
                self.tick()
            except Halt:
                pass
