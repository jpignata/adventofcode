import sys
from functools import reduce
from operator import add, mul


def evaluate_columns(data):
    total = 0
    problems = []
    operators = {"+": add, "*": mul}

    for line in data:
        problems.append([])

        for token in line.strip().split():
            if token in operators:
                problems[-1].append(operators[token])
            else:
                problems[-1].append(int(token))

    for problem in list(zip(*problems)):
        total += reduce(problem[-1], problem[:-1])

    return total


def evaluate_digits(data):
    total = 0
    stack = []
    operators = {"+": add, "*": mul}

    for column in list(zip(*[line[::-1] for line in data]))[1:]:
        if not "".join(column).strip():
            continue

        stack.append(int("".join(column[:-1])))

        if column[-1] in operators:
            total += reduce(operators[column[-1]], stack)
            stack = []

    return total


lines = sys.stdin.readlines()
print("Part 1:", evaluate_columns(lines))
print("Part 2:", evaluate_digits(lines))
