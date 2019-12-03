import sys
import operator


def run(program, noun, verb=0):
    opcodes = {1: operator.add, 2: operator.mul}
    program = program.copy()
    program[1], program[2] = noun, verb
    pointer = 0

    while program[pointer] != 99:
        opcode = program[pointer]
        operands = [program[program[pointer + i]] for i in range(1, 3)]
        address = program[pointer + 3]
        program[address] = opcodes[opcode](operands[0], operands[1])
        pointer += 4

    return program[0]


def find(program, target, start=0, end=100):
    while start <= end:
        mid = (start + end) // 2
        delta = target - run(program, mid)

        if 0 < delta < 100:
            return 100 * mid + delta
        elif delta > 100:
            start = mid + 1
        else:
            end = mid - 1


program = [int(i) for i in sys.stdin.readline().split(',')]

print(f'Part 1: {run(program, 12, 2)}')
print(f'Part 2: {find(program, 19690720)}')
