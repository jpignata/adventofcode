import sys


def find2(values, target, lo=0):
    hi = len(values) - 1

    while lo < hi:
        total = values[lo] + values[hi]

        if total < target:
            lo += 1
        elif total > target:
            hi -= 1
        else:
            return values[lo] * values[hi]


def find3(values, target):
    for i, value in enumerate(values):
        if (match := find2(values, target - value, i + 1)):
            return match * value

    return None


expenses = sorted(int(value) for value in sys.stdin.readlines())

print('Part 1:', find2(expenses, 2020))
print('Part 2:', find3(expenses, 2020))
