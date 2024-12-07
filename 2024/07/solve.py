import sys
from operator import add, mul


def evaluate(current, numbers, value, *, ops):
    if not numbers:
        return value == current

    return any(
        evaluate(op(current, numbers[0]), numbers[1:], value, ops=ops) for op in ops
    )


def concat(a, b):
    return int(str(a) + str(b))


def main():
    equations = []

    for line in sys.stdin:
        value, numbers = line.split(":")
        equations.append((list(map(int, numbers.split())), int(value)))

    part1 = sum(
        value
        for numbers, value in equations
        if evaluate(numbers[0], numbers[1:], value, ops=(add, mul))
    )
    part2 = sum(
        value
        for numbers, value in equations
        if evaluate(numbers[0], numbers[1:], value, ops=(add, mul, concat))
    )

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
