import sys
from operator import add, sub, eq, ne, ge, le, gt, lt
from collections import defaultdict, namedtuple

Instruction = namedtuple(
    "Instruction", ["register", "op", "value", "c_register", "c_op", "c_value"]
)
ops = {"inc": add, "dec": sub, "!=": ne, ">=": ge, "<=": le, ">": gt, "<": lt, "==": eq}


def parse(line):
    tokens = line.strip().split(" ")
    return Instruction(
        tokens[0],
        ops[tokens[1]],
        int(tokens[2]),
        tokens[4],
        ops[tokens[5]],
        int(tokens[6]),
    )


def run(instructions):
    registers = defaultdict(int)
    highest_value = 0

    for instr in instructions:
        if instr.c_op(registers[instr.c_register], instr.c_value):
            registers[instr.register] = instr.op(registers[instr.register], instr.value)
            highest_value = max(highest_value, registers[instr.register])

    return max(registers.values()), highest_value


instructions = [parse(line.strip()) for line in sys.stdin.readlines()]
current, highest = run(instructions)

print("Part 1:", current)
print("Part 2:", highest)
