import sys
from collections import defaultdict


def isdigit(token):
    try:
        int(token)
        return True
    except ValueError:
        return False


class Coprocessor:
    def __init__(self, *, a=0):
        self.counts = defaultdict(int)
        self.registers = defaultdict(int)
        self.registers['a'] = a
        self.ip = 0

    def run(self, instructions):
        while self.ip >= 0 and self.ip < len(instructions):
            instruction = instructions[self.ip]
            self.ip += getattr(self, instruction[0])(*instruction[1:]) or 1
            self.counts[instruction[0]] += 1

        return self

    def set(self, x, y):
        if isdigit(y):
            self.registers[x] = int(y)
        else:
            self.registers[x] = self.registers[y]

    def sub(self, x, y):
        if isdigit(y):
            self.registers[x] -= int(y)
        else:
            self.registers[x] -= self.registers[y]

    def mul(self, x, y):
        if isdigit(y):
            self.registers[x] *= int(y)
        else:
            self.registers[x] *= self.registers[y]

    def jnz(self, x, y):
        if isdigit(x):
            val = int(x)
        else:
            val = self.registers[x]

        if val != 0:
            return int(y)


def emulate():
    b = (99 * 100) + 100000
    c = b + 17000
    g = b - c
    h = 0

    while g != 0:
        for d in range(2, b // 2):
            if b % d == 0:
                h += 1
                break

        g = b - c
        b += 17

    return h


instructions = [line.strip().split(' ') for line in sys.stdin]

print('Part 1:', Coprocessor().run(instructions).counts['mul'])
print('Part 2:', emulate())
