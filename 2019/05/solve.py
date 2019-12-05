import sys


def param(program, pointer, opcode, position):
    modes = list(reversed(opcode[1:3]))

    try:
        if modes[position - 1] == '1':
            return program[pointer + position]
        else:
            return program[program[pointer + position]]
    except IndexError:
        return None


def add(program, pointer, param1, param2):
    address = program[pointer + 3]
    program[address] = param1 + param2

    return pointer + 4


def mul(program, pointer, param1, param2):
    address = program[pointer + 3]
    program[address] = param1 * param2

    return pointer + 4


def get(program, pointer, *_):
    address = program[pointer + 1]
    program[address] = int(input('> '))

    return pointer + 2


def put(program, pointer, *_):
    address = program[pointer + 1]
    print(program[address])

    return pointer + 2


def jump_if_true(program, pointer, param1, param2):
    if param1 != 0:
        return param2

    return pointer + 3


def jump_if_false(program, pointer, param1, param2):
    if param1 == 0:
        return param2

    return pointer + 3


def less_than(program, pointer, param1, param2):
    address = program[pointer + 3]

    if param1 < param2:
        program[address] = 1
    else:
        program[address] = 0

    return pointer + 4


def equals(program, pointer, param1, param2):
    address = program[pointer + 3]

    if param1 == param2:
        program[address] = 1
    else:
        program[address] = 0

    return pointer + 4


def halt(*_):
    return None


def run(program):
    pointer = 0
    operations = {1: add, 2: mul, 3: get, 4: put, 5: jump_if_true,
                  6: jump_if_false, 7: less_than, 8: equals, 99: halt}

    while pointer is not None:
        opcode = str(program[pointer]).zfill(5)
        param1 = param(program, pointer, opcode, 1)
        param2 = param(program, pointer, opcode, 2)
        operation = operations[int(opcode[-2:])]
        pointer = operation(program, pointer, param1, param2)


with open(sys.argv[1]) as f:
    program = [int(i) for i in f.readline().strip().split(',')]
    run(program)
