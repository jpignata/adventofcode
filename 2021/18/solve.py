import sys
from itertools import permutations
from functools import reduce
from math import floor, ceil


def add(number1, number2):
    numbers = [(number, depth + 1) for number, depth in number1 + number2]

    while True:
        explode = next((i for i, (_, depth) in enumerate(numbers)
                        if depth >= 5), None)

        if explode is not None:
            left, right = numbers[explode:explode+2]

            if (next_left := explode - 1) >= 0:
                numbers[next_left] = (numbers[next_left][0] + left[0],
                                      numbers[next_left][1])

            if (next_right := explode + 2) < len(numbers):
                numbers[next_right] = (numbers[next_right][0] + right[0],
                                       numbers[next_right][1])

            numbers[explode] = (0, left[1] - 1)
            del numbers[explode + 1]
            continue

        split = next((i for i, (number, _) in enumerate(numbers)
                      if number >= 10), None)

        if split is not None:
            halved = numbers[split][0] / 2
            depth = numbers[split][1] + 1
            numbers.insert(split + 1, (ceil(halved), depth))
            numbers[split] = (floor(halved), depth)
            continue

        break

    return numbers


def magnitude(number):
    while len(number) != 1:
        maxdepth = max(depth for _, depth in number)
        i = next(i for i, (_, depth) in enumerate(number) if depth == maxdepth)
        number[i] = (number[i][0] * 3 + number[i + 1][0] * 2, maxdepth - 1)
        del number[i + 1]

    return number[0][0]


numbers = []

for line in sys.stdin:
    next_numbers = []
    depth = 0

    for char in line.strip():
        if char == '[':
            depth += 1
        elif char == ']':
            depth -= 1
        elif char.isdigit():
            next_numbers.append((int(char), depth))

    numbers.append(next_numbers)

total = magnitude(reduce(add, numbers))
largest = max(magnitude(add(n1, n2)) for n1, n2 in permutations(numbers, 2))

print('Part 1:', total)
print('Part 2:', largest)
