import sys
from functools import reduce
from operator import add, mul


def parse_columns(lines):
    problems = [list(line.strip().split()) for line in lines]

    return [
        (operators[problem[-1]], [int(value) for value in problem[:-1]])
        for problem in zip(*problems)
    ]


def parse_digits(lines):
    problems = []
    values = []

    for column in list(zip(*[line[::-1] for line in lines]))[1:]:
        if not "".join(column).strip():
            continue

        values.append(int("".join(column[:-1])))

        if column[-1] in operators:
            problems.append((operators[column[-1]], values))
            values = []

    return problems


data = sys.stdin.readlines()
operators = {"+": add, "*": mul}

print("Part 1:", sum(reduce(op, values) for op, values in parse_columns(data)))
print("Part 2:", sum(reduce(op, values) for op, values in parse_digits(data)))
