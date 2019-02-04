import sys
from itertools import count


class Computer:
    def __init__(self, *, a=0):
        self.registers = {'a': a, 'b': 0, 'c': 0, 'd': 0}

    def run(self, program):
        ip = 0

        while ip < len(program):
            instruction = program[ip]

            if instruction[0] == 'out':
                yield self.registers[instruction[1]]
                ip += 1
            else:
                ip += getattr(self, instruction[0])(*instruction[1:]) or 1

        return self

    def cpy(self, x, y):
        if x.isdigit():
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
            return int(y)


def find():
    for i in count(1):
        computer = Computer(a=i)
        sequence = []

        for out in computer.run(program):
            if ((out in (0, 1) and len(sequence) == 0) or
                    (out == 0 and sequence[-1] == 1) or
                    (out == 1 and sequence[-1] == 0)):
                sequence.append(out)

                if len(sequence) == 10:
                    return i
            else:
                break


program = [l.strip().split() for l in sys.stdin.readlines()]

print('Part 1:', find())
