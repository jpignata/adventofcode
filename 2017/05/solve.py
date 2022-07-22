import sys
from itertools import count


def escape(instructions, *, strange_mode=False):
    ip = 0

    for i in count(0):
        if ip < 0 or ip >= len(instructions):
            return i

        next_ip = ip + instructions[ip]

        if strange_mode and instructions[ip] >= 3:
            instructions[ip] -= 1
        else:
            instructions[ip] += 1

        ip = next_ip


instructions = [int(line) for line in sys.stdin.readlines()]

print("Part 1", escape(instructions.copy()))
print("Part 2", escape(instructions.copy(), strange_mode=True))
