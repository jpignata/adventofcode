import sys


def find2(values, target, lo=0):
    hi = len(values) - 1

    while (lo < hi):
        total = values[lo] + values[hi]

        if total == target:
            return values[lo] * values[hi]
        elif total < target:
            lo += 1
        else:
            hi -= 1


def find3(values, target):
    for i, value in enumerate(values):
        if (match := find2(values, target - value, i + 1)):
            return match * value


values = sorted(int(value) for value in sys.stdin.readlines())

print('Part 1:', find2(values, 2020))
print('Part 2:', find3(values, 2020))
