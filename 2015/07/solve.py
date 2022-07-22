import sys
import re
import operator


class Instruction:
    def __init__(self, operands, operation, wires):
        self.operands = operands
        self.operation = operation
        self.wires = wires
        self.signal = None

    def __call__(self):
        if self.signal is None:
            values = []

            for operand in self.operands:
                if operand.isdigit():
                    values.append(int(operand))
                else:
                    values.append(wires[operand]())

            self.signal = self.operation(*values)

        return self.signal

    def reset(self):
        self.signal = None


pattern = re.compile(r"([a-z0-9]+)? ?([A-Z]+)? ?([a-z0-9]+)? ?-> ([a-z]+)")
operations = {
    "AND": operator.and_,
    "OR": operator.or_,
    "LSHIFT": operator.lshift,
    "RSHIFT": operator.rshift,
    "NOT": operator.inv,
    None: lambda x: x,
}
wires = dict()

for line in [line.strip() for line in sys.stdin.readlines()]:
    matches = pattern.match(line)
    operands = list(filter(None, matches.group(1, 3)))
    operation = operations[matches.group(2)]
    wire = matches.group(4)
    wires[wire] = Instruction(operands, operation, wires)

a = wires["a"]()

for _, wire in wires.items():
    wire.reset()

wires["b"].signal = a

print("Part 1:", a)
print("Part 2:", wires["a"]())
