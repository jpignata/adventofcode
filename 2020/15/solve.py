import sys


def play(numbers, rounds):
    seen = {number: i + 1 for i, number in enumerate(numbers)}
    spoken = numbers[-1]

    for turn in range(len(numbers), rounds):
        seen[spoken], spoken = turn, turn - seen.get(spoken, turn)

    return spoken


numbers = [int(line) for line in sys.stdin.readline().split(",")]

print("Part 1:", play(numbers, 2020))
print("Part 2:", play(numbers, 30000000))
