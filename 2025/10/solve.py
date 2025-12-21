import sys
from itertools import combinations

machines = []

for line in sys.stdin:
    indicator, *buttons, joltage = line.split()
    masks = []

    for button in buttons:
        mask = 0
        length = len(indicator) - 3
        for position in button[1:-1].split(","):
            mask |= 1 << (length - int(position))

        masks.append(mask)

    indicator = int(indicator[1:-1].translate(str.maketrans(".#", "01")), 2)

    machines.append((indicator, masks, joltage))


presses = 0


def search(indicator, masks):
    for size in range(1, len(masks)):
        for combination in combinations(masks, size):
            candidate = 0

            for mask in combination:
                candidate ^= mask

            if candidate == indicator:
                return len(combination)

    return 0


for machine in machines:
    indicator, masks, joltage = machine
    presses += search(indicator, masks)


print("Part 1:", presses)
