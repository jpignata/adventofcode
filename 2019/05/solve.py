from intcode import Computer


def run(user_id):
    computer = Computer.load([user_id])
    computer.run()

    return computer.outputs.pop()


print(f'Part 1: {run(1)}')
print(f'Part 2: {run(5)}')
