from collections import defaultdict

from intcode import Computer


def test(x, y):
    computer = Computer.load()
    computer.inputs.append(x)
    computer.inputs.append(y)
    computer.run()

    return computer.outputs.popleft()


def search(size):
    x = y = 0

    while not test(x + size - 1, y):
        y += 1

        while not test(x, y + size - 1):
            x += 1

    return x * 10000 + y


total = 0
grid = defaultdict(int)

for y in range(50):
    for x in range(50):
        output = test(x, y)
        total += output
        grid[(x, y)] = output

print("Part 1:", total)
print("Part 2:", search(100))
