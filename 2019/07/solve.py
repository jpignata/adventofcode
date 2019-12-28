import itertools

from intcode import Computer, Halt


def find(start, end):
    results = []

    for permutation in itertools.permutations(range(start, end + 1)):
        computers = [Computer.load([phase]) for phase in permutation]
        signal = 0

        for computer in itertools.cycle(computers):
            computer.inputs.append(signal)

            try:
                while not computer.outputs:
                    computer.tick()

                signal = computer.outputs.popleft()
            except Halt:
                results.append(signal)
                break

    return max(results)


print(f'Part 1: {find(0, 4)}')
print(f'Part 2: {find(5, 9)}')
