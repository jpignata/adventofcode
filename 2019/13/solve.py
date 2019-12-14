import curses
import sys
import itertools
from collections import deque, defaultdict
from operator import itemgetter
from os import system


class Input(Exception):
    pass


def draw(screen, score):
    maxx = max(screen, key=itemgetter(0))[0]
    maxy = max(screen, key=itemgetter(1))[1]

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if screen[(x, y)] == 0:
                stdscr.addstr(y, x, ' ')
            elif screen[(x, y)] == 1:
                if y == 0:
                    stdscr.addstr(y, x, '+' if x == 0 or x == maxx else '-')
                else:
                    stdscr.addstr(y, x, '|')
            elif screen[(x, y)] == 2:
                stdscr.addstr(y, x, '█')
            elif screen[(x, y)] == 3:
                stdscr.addstr(y, x, '▄')
            elif screen[(x, y)] == 4:
                stdscr.addstr(y, x, '◉')

    stdscr.addstr(0, 2, f'SCORE {score}')
    stdscr.refresh()


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


program = defaultdict(int)

for i, digit in enumerate(sys.stdin.readline().split(',')):
    program[i] = int(digit)

computer = Computer(program.copy())

while not computer.halted:
    computer.tick()

blocks = sum(1 for i, c in enumerate(computer.outputs)
             if c == 2 and (i + 1) % 3 == 0)
computer = Computer(program.copy())
computer.program[0] = 2
screen = dict()
score = 0
paddle = (0, 0)
ball = (0, 0)
stdscr = curses.initscr()

curses.curs_set(False)

while not computer.halted:
    try:
        computer.tick()
    except Input:
        if ball[0] > paddle[0]:
            computer.inputs.append(1)
        elif ball[0] < paddle[0]:
            computer.inputs.append(-1)
        elif ball[0] == paddle[0]:
            computer.inputs.append(0)

        draw(screen, score)

    if len(computer.outputs) == 3:
        x, y, tile_or_score = [computer.outputs.popleft() for _ in range(3)]

        if x == -1:
            score = tile_or_score
        else:
            screen[(x, y)] = tile_or_score

            if tile_or_score == 3:
                paddle = (x, y)
            elif tile_or_score == 4:
                ball = (x, y)

curses.endwin()

print(f'Part 1: {blocks}')
print(f'Part 2: {score}')
