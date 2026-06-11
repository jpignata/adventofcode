import sys
from fractions import Fraction
from itertools import combinations
from math import inf

machines = []

for line in sys.stdin:
    indicator, *buttons, joltage = line.split()
    length = len(indicator) - 2
    buttons = [tuple(map(int, button[1:-1].split(","))) for button in buttons]
    joltage = tuple(map(int, joltage[1:-1].split(",")))
    indicator = int(indicator[1:-1].translate(str.maketrans(".#", "01")), 2)

    machines.append((indicator, buttons, joltage))


part1 = 0
part2 = 0


def button_mask(button, length):
    mask = 0

    for position in button:
        mask |= 1 << (length - 1 - position)

    return mask


def search(indicator, masks):
    for size in range(1, len(masks)):
        for combination in combinations(masks, size):
            candidate = 0

            for mask in combination:
                candidate ^= mask

            if candidate == indicator:
                return len(combination)

    return 0


def search_joltage(buttons, joltage):
    rows = [
        [Fraction(position in button) for button in buttons] + [Fraction(target)]
        for position, target in enumerate(joltage)
    ]
    pivot_columns = []
    pivot_row = 0

    for column in range(len(buttons)):
        row = next(
            (row for row in range(pivot_row, len(rows)) if rows[row][column]),
            None,
        )

        if row is None:
            continue

        rows[pivot_row], rows[row] = rows[row], rows[pivot_row]
        divisor = rows[pivot_row][column]
        rows[pivot_row] = [value / divisor for value in rows[pivot_row]]

        for row in range(len(rows)):
            if row == pivot_row or not rows[row][column]:
                continue

            factor = rows[row][column]
            rows[row] = [
                value - factor * pivot
                for value, pivot in zip(rows[row], rows[pivot_row])
            ]

        pivot_columns.append(column)
        pivot_row += 1

    free_columns = [
        column for column in range(len(buttons)) if column not in pivot_columns
    ]
    bounds = {
        column: min(joltage[position] for position in buttons[column])
        for column in free_columns
    }
    best = inf

    def pivot_values(assigned):
        values = {}

        for row, column in enumerate(pivot_columns):
            value = rows[row][-1]

            for free_column in free_columns:
                value -= rows[row][free_column] * assigned.get(free_column, 0)

            values[column] = value

        return values

    def feasible(assigned, remaining):
        for row, column in enumerate(pivot_columns):
            low = high = rows[row][-1]

            for free_column in free_columns:
                coefficient = -rows[row][free_column]

                if free_column in assigned:
                    low += coefficient * assigned[free_column]
                    high += coefficient * assigned[free_column]
                elif free_column in remaining:
                    if coefficient > 0:
                        high += coefficient * bounds[free_column]
                    else:
                        low += coefficient * bounds[free_column]

            if high < 0:
                return False

        return True

    def dfs(index, assigned, total):
        nonlocal best

        if total >= best:
            return

        remaining = set(free_columns[index:])

        if not feasible(assigned, remaining):
            return

        if index == len(free_columns):
            values = pivot_values(assigned)

            if any(value < 0 or value.denominator != 1 for value in values.values()):
                return

            best = min(best, total + sum(int(value) for value in values.values()))
            return

        column = free_columns[index]

        for count in range(bounds[column] + 1):
            assigned[column] = count
            dfs(index + 1, assigned, total + count)
            del assigned[column]

    dfs(0, {}, 0)

    return best


for machine in machines:
    indicator, buttons, joltage = machine
    masks = [button_mask(button, len(joltage)) for button in buttons]
    part1 += search(indicator, masks)
    part2 += search_joltage(buttons, joltage)

print("Part 1:", part1)
print("Part 2:", part2)
