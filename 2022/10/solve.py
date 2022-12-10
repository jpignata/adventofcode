import sys

register = 1
states = []

for line in sys.stdin:
    match line.strip().split():
        case ["noop"]:
            states.append(register)
        case ["addx", value]:
            states.extend([register, register])
            register += int(value)

print("Part 1:", sum(states[i - 1] * i for i in range(20, len(states), 40)))
print("Part 2:")

for y in range(len(states) // 40):
    for x in range(40):
        if x in range(states[(cycle := y * 40 + x)] - 1, states[cycle] + 2):
            print("█", end="")
        else:
            print(".", end="")

    print()
