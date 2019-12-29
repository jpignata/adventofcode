import sys
from collections import deque, defaultdict


class Input(Exception):
    pass


class Halt(Exception):
    pass


class Computer:
    @classmethod
    def load(cls, inputs=[], *, filename=None):
        program = defaultdict(int)

        if filename:
            line = open(filename).readline()
        else:
            if not hasattr(cls, 'stdin'):
                cls.stdin = sys.stdin.readline()

            line = cls.stdin

        for i, digit in enumerate(line.split(',')):
            program[i] = int(digit)

        return Computer(program, inputs)

    def __init__(self, program, inputs=[]):
        self.program = program
        self.inputs = deque(inputs)
        self.outputs = deque([])
        self.halted = False
        self.pointer = 0
        self.base = 0
        self.operations = {1: self.add, 2: self.mul, 3: self.get, 4: self.put,
                           5: self.jump_if_true, 6: self.jump_if_false,
                           7: self.less_than, 8: self.equals, 9: self.set_base,
                           99: self.halt}

    def __setitem__(self, key, value):
        self.program[key] = value

    def __getitem__(self, key):
        if key < 0:
            raise RuntimeError(f'Invalid address: {key}')

        return self.program[key]

    def tick(self):
        opcode = str(self[self.pointer]).zfill(5)
        operation = self.operations[int(opcode[-2:])]
        params = self.params(opcode[2::-1])

        operation(*params)

    def run(self):
        while not self.halted:
            try:
                self.tick()
            except Halt:
                pass

    def execute(self, command):
        for c in [ord(c) for c in command.strip() + '\n']:
            self.inputs.append(c)

    def print_screen(self):
        while self.outputs:
            print(chr(self.outputs.popleft()), end='')

    def params(self, modes):
        params = list()

        for i, mode in enumerate(modes):
            position = i + 1
            param = None

            try:
                if mode == '0':
                    param = self.program[self.pointer + position]
                elif mode == '1':
                    param = self.pointer + position
                elif mode == '2':
                    param = self.program[self.pointer + position] + self.base
                else:
                    raise RuntimeError(f'Unknown parameter mode: {mode}')
            except IndexError:
                pass

            params.append(param)

        return params

    def add(self, param1, param2, param3):
        self[param3] = self[param1] + self[param2]
        self.pointer += 4

    def mul(self, param1, param2, param3):
        self[param3] = self[param1] * self[param2]
        self.pointer += 4

    def get(self, param1, *_):
        if len(self.inputs) == 0:
            raise Input

        self[param1] = self.inputs.popleft()
        self.pointer += 2

    def put(self, param1, *_):
        self.outputs.append(self[param1])
        self.pointer += 2

    def jump_if_true(self, param1, param2, *_):
        if self[param1] != 0:
            self.pointer = self[param2]
        else:
            self.pointer += 3

    def jump_if_false(self, param1, param2, *_):
        if self[param1] == 0:
            self.pointer = self[param2]
        else:
            self.pointer += 3

    def less_than(self, param1, param2, param3):
        self[param3] = int(self[param1] < self[param2])
        self.pointer += 4

    def equals(self, param1, param2, param3):
        self[param3] = int(self[param1] == self[param2])
        self.pointer += 4

    def set_base(self, param1, *_):
        self.base += self[param1]
        self.pointer += 2

    def halt(self, *_):
        self.halted = True
        raise Halt
