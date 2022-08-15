import sys
from dataclasses import dataclass, field
from re import findall
from typing import List, Set


@dataclass
class Sample:
    before: List[int]
    instruction: List[int]
    after: List[int]
    candidates: Set[str] = field(default_factory=set)


def extract(line):
    return [int(digit) for digit in findall(r"\d+", line)]


class Device:
    def __init__(self):
        self.registers = [0, 0, 0, 0]

    def op_addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]

    def op_addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b

    def op_mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]

    def op_muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b

    def op_banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]

    def op_bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b

    def op_borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]

    def op_bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b

    def op_setr(self, a, b, c):
        self.registers[c] = self.registers[a]

    def op_seti(self, a, b, c):
        self.registers[c] = a

    def op_gtir(self, a, b, c):
        self.registers[c] = int(a > self.registers[b])

    def op_gtri(self, a, b, c):
        self.registers[c] = int(self.registers[a] > b)

    def op_gtrr(self, a, b, c):
        self.registers[c] = int(self.registers[a] > self.registers[b])

    def op_eqri(self, a, b, c):
        self.registers[c] = int(self.registers[a] == b)

    def op_eqir(self, a, b, c):
        self.registers[c] = int(a == self.registers[b])

    def op_eqrr(self, a, b, c):
        self.registers[c] = int(self.registers[a] == self.registers[b])

    def execute(self, op, instruction):
        getattr(self, op)(*instruction)

    def reset(self, values=[0, 0, 0, 0]):
        self.registers = values[:]

    def ops(self):
        return [method for method in dir(self) if method.startswith("op_")]


samples = []
instructions = []
mapped = {}
found = set()
device = Device()
ops = device.ops()
matches_three_or_more = 0
lines = iter(sys.stdin.readlines())

while line := next(lines, None):
    digits = extract(line)

    if line.startswith("Before"):
        sample = Sample(digits, extract(next(lines)), extract(next(lines)))
        samples.append(sample)
    elif digits:
        instructions.append(digits)

for sample in samples:
    for op in ops:
        device.reset(sample.before)
        device.execute(op, sample.instruction[1:])

        if device.registers == sample.after:
            sample.candidates.add(op)

    if len(sample.candidates) >= 3:
        matches_three_or_more += 1

while len(mapped) != len(ops):
    for sample in samples:
        code = sample.instruction[0]

        if code not in mapped:
            if len(sample.candidates) == 1:
                mapped[code] = sample.candidates.pop()
                found.add(mapped[code])
            else:
                sample.candidates -= found

device.reset()

for instruction in instructions:
    device.execute(mapped[instruction[0]], instruction[1:])

print("Part 1:", matches_three_or_more)
print("Part 2:", device.registers[0])
