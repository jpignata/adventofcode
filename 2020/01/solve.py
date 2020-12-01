import sys


def find2(values, target):
    complements = set()

    for value1 in values:
        if (value2 := target - value1) in complements:
            return value1 * value2

        complements.add(value1)


def find3(values, target):
    complements = set(values)

    for value1 in values:
        for value2 in values:
            if (value3 := target - value1 - value2) in complements:
                return value1 * value2 * value3


values = sorted(int(value) for value in sys.stdin.readlines())

print('Part 1:', find2(values, 2020))
print('Part 2:', find3(values, 2020))
