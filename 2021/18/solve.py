import sys
from itertools import permutations
from functools import reduce
from math import floor, ceil


def add(number1, number2):
    numbers = [(number, depth + 1) for number, depth in number1 + number2]

    while True:
        to_explode = (i for i, (_, depth) in enumerate(numbers) if depth >= 5)
        to_split = (i for i, (number, _) in enumerate(numbers) if number >= 10)

        if (i := next(to_explode, None)) is not None:
            left, right = numbers[i:i+2]

            if (j := i - 1) >= 0:
                numbers[j] = (left[0] + numbers[j][0], numbers[j][1])

            if (j := i + 2) < len(numbers):
                numbers[j] = (right[0] + numbers[j][0], numbers[j][1])

            numbers[i] = (0, left[1] - 1)
            del numbers[i + 1]
            continue

        if (i := next(to_split, None)) is not None:
            numbers.insert(i + 1, (ceil(numbers[i][0] / 2), numbers[i][1] + 1))
            numbers[i] = (floor(numbers[i][0] / 2), numbers[i][1] + 1)
            continue

        return numbers


def magnitude(number):
    while len(number) != 1:
        maxdepth = max(depth for _, depth in number)
        i = next(i for i, (_, depth) in enumerate(number) if depth == maxdepth)
        number[i] = (number[i][0] * 3 + number[i+1][0] * 2, maxdepth - 1)
        del number[i + 1]

    return number[0][0]


numbers = []

for line in sys.stdin:
    numbers.append([])
    depth = 0

    for char in line.strip():
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char.isdigit():
            numbers[-1].append((int(char), depth))

total = magnitude(reduce(add, numbers))
largest = max(magnitude(add(n1, n2)) for n1, n2 in permutations(numbers, 2))

print('Part 1:', total)
print('Part 2:', largest)
