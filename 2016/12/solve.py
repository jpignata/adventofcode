import sys


class Computer:
    def __init__(self, *, a=0, b=0, c=0, d=0):
        self.registers = {"a": a, "b": b, "c": c, "d": d}

    def run(self, program):
        ip = 0

        while ip < len(program):
            instruction = program[ip]
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


program = [l.strip().split() for l in sys.stdin.readlines()]

print("Part 1:", Computer().run(program).registers["a"])
print("Part 2:", Computer(c=1).run(program).registers["a"])
