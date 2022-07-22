from intcode import Computer


def run(value):
    computer = Computer.load([value])
    computer.run()

    return computer.outputs.pop()


print("Part 1:", run(1))
print("Part 2:", run(2))
