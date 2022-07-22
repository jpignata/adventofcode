from intcode import Computer, Input


def network():
    computers = list()
    last = dict()
    x, y = None, None

    for i in range(50):
        computers.append(Computer.load([i]))

    while True:
        for i, computer in enumerate(computers):
            if computer.inputs:
                last[i] = computer.inputs[0]

            try:
                computer.tick()
            except Input:
                computer.inputs.append(-1)

            if len(computer.outputs) == 3:
                destination = computer.outputs.popleft()
                x = computer.outputs.popleft()
                y = computer.outputs.popleft()

                if destination == 255:
                    yield 255, x, y
                else:
                    computers[destination].inputs.append(x)
                    computers[destination].inputs.append(y)

        if all(v == -1 for v in last.values()):
            if x is not None and y is not None:
                yield 0, x, y
                computers[0].inputs.append(x)
                computers[0].inputs.append(y)


for destination, x, y in network():
    if destination == 255:
        print("Part 1:", y)
        break

last = None

for destination, x, y in network():
    if destination == 0:
        if last == y:
            print("Part 2:", y)
            break

        last = y
