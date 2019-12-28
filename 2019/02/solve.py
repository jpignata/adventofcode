from intcode import Computer, Halt


def run(noun, verb=0):
    computer = Computer.load()
    computer[1], computer[2] = noun, verb

    computer.run()

    return computer[0]


def find(target, start=0, end=100):
    while start <= end:
        mid = (start + end) // 2
        delta = target - run(mid)

        if 0 < delta < 100:
            return 100 * mid + delta
        elif delta > 100:
            start = mid + 1
        else:
            end = mid - 1


print('Part 1:', run(12, 2))
print('Part 2:', find(19690720))
