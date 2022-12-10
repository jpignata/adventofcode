import sys

register = 1
states = [1]
rows = []

for line in sys.stdin:
    match line.strip().split():
        case ["noop"]:
            states.append(register)
        case ["addx", value]:
            states.extend([register] * 2)
            register += int(value)

for cycle, register in enumerate(states[1:]):
    pos = cycle % 40

    if pos == 0:
        rows.append(["."] * 40)

    if pos in range(register - 1, register + 2):
        rows[-1][pos] = "█"

print("Part 1:", sum(states[i] * i for i in (20, 60, 100, 140, 180, 220)))
print("Part 2:")

for row in rows:
    print("".join(row))
