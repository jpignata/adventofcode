from intcode import Computer


def run(value):
    computer = Computer.load([value])
    computer.run()

    return computer.outputs.pop()


print(f'Part 1: {run(1)}')
print(f'Part 2: {run(2)}')
