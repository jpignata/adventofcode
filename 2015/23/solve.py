import sys
import re
from collections import namedtuple


class Computer:
    def __init__(self, *, a=0):
        self.registers = {'a': a, 'b': 0}

    def run(self, program):
        ip = 0

        while ip < len(program):
            instruction = program[ip]
            ip += getattr(self, instruction.name)(*instruction.args) or 1

        return self

    def hlf(self, r):
        self.registers[r] /= 2

    def tpl(self, r):
        self.registers[r] *= 3

    def inc(self, r):
        self.registers[r] += 1

    def jmp(self, offset):
        return offset

    def jie(self, r, offset):
        if self.registers[r] % 2 == 0:
            return offset

    def jio(self, r, offset):
        if self.registers[r] == 1:
            return offset


Instruction = namedtuple('Instruction', ['name', 'args'])
program = []

for line in sys.stdin.readlines():
    tokens = re.split(r',? ', line.strip())
    name = tokens[0]
    args = [int(t) if t[0] in ('+', '-') else t for t in tokens[1:]]
    program.append(Instruction(name, args))

part1 = Computer().run(program)
part2 = Computer(a=1).run(program)

print('Part 1:', part1.registers['b'])
print('Part 2:', part2.registers['b'])
