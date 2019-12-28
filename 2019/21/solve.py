from intcode import Computer


def execute(commands):
    computer = Computer.load()

    for command in commands.lstrip().split('\n'):
        computer.execute(command)

    computer.run()

    for output in computer.outputs:
        if output > 255:
            return output

    print('Failed ---')

    for character in computer.outputs:
        print(chr(character), end='')


walk = """
NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
"""

run = """
NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
NOT E T
NOT T T
OR H T
AND T J
RUN
"""

print('Part 1:', execute(walk))
print('Part 2:', execute(run))
