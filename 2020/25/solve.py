import sys


def find(number):
    result = 1
    size = 0

    while result != number:
        result *= 7
        result %= 20201227
        size += 1

    return size


def calculate(size, number):
    result = 1

    for _ in range(size):
        result *= number
        result %= 20201227

    return result


public_keys = [int(line) for line in sys.stdin.readlines()]

print('Part 1:', calculate(find(public_keys[0]), public_keys[1]))
