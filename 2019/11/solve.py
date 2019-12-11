import sys
import itertools
from collections import deque, defaultdict
from operator import itemgetter


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


def paint(program, panel=0):
    c = Computer(program)
    pos = (0, 0)
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
    direction = 0
    panels = defaultdict(int)
    panels[(0, 0)] = panel

    while not c.halted:
        c.inputs.append(panels[pos])

        while len(c.outputs) != 2 and not c.halted:
            c.tick()

        if c.outputs:
            panels[pos] = c.outputs.popleft()
            direction = (direction + (-1, 1)[c.outputs.popleft()]) % len(dirs)
            pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])

    return panels


def draw(program):
    panels = paint(program, 1)
    maxx = max(panels, key=itemgetter(0))[0]
    maxy = max(panels, key=itemgetter(1))[1]

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if panels[(x, y)] == 1:
                sys.stdout.write('█')
            else:
                sys.stdout.write(' ')

        print()


program = defaultdict(int)

for i, digit in enumerate(sys.stdin.readline().split(',')):
    program[i] = int(digit)

print(f'Part 1: {len(paint(program.copy()))}')
print('Part 2:')
draw(program)
