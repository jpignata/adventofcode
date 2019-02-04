import sys
import math


class Computer:
    def __init__(self, program, *, a=0, b=0, c=0, d=0):
        self.registers = {'a': a, 'b': b, 'c': c, 'd': d}
        self.program = program.copy()

    def run(self):
        self.ip = 0

        while self.ip < len(self.program):
            instruction = self.program[self.ip]
            self.ip += getattr(self, instruction[0])(*instruction[1:]) or 1
        return self

    def cpy(self, x, y):
        if x.lstrip('-').isdigit():
            self.registers[y] = int(x)
        else:
            self.registers[y] = self.registers[x]

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def jnz(self, x, y):
        if x.isdigit():
            x = int(x)
        else:
            x = self.registers[x]

        if x != 0:
            if y.lstrip('-').isdigit():
                return int(y)
            else:
                return self.registers[y]

    def tgl(self, x):
        if x.lstrip('-').isdigit():
            ip = self.ip + int(x)
        else:
            ip = self.ip + self.registers[x]

        if ip < len(program):
            instruction = self.program[ip]

            if len(instruction[1:]) == 1:
                if instruction[0] == 'inc':
                    self.program[ip] = ['dec', instruction[1]]
                else:
                    self.program[ip] = ['inc', instruction[1]]
            else:
                if instruction[0] == 'jnz':
                    self.program[ip] = ['cpy', *instruction[1:]]
                else:
                    self.program[ip] = ['jnz', *instruction[1:]]


def bypass(eggs, offset1, offset2):
    return math.factorial(eggs) + (offset1 * offset2)

program = [l.strip().split() for l in sys.stdin.readlines()]

print('Part 1:', Computer(program, a=7).run().registers['a'])
print('Part 2:', bypass(12, int(program[19][1]), int(program[20][1])))
