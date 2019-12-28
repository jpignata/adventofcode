from intcode import Computer


def run(user_id):
    computer = Computer.load([user_id])
    computer.run()

    return computer.outputs.pop()


print('Part 1:', run(1))
print('Part 2:', run(5))
