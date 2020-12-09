import sys


def find_invalid(numbers, size=25):
    for i, number in enumerate(numbers[size:]):
        complements = set(numbers[i:i+size])

        for addend in complements:
            if number - addend in complements:
                break
        else:
            return number


def find_range(numbers, target):
    lo, hi = 0, 1

    while hi < len(numbers):
        seq = numbers[lo:hi]

        if (total := sum(seq)) == target:
            return min(seq) + max(seq)
        elif total > target:
            lo += 1
        elif total < target:
            hi += 1


numbers = [int(line) for line in sys.stdin.readlines()]
invalid = find_invalid(numbers)

print('Part 1:', invalid)
print('Part 2:', find_range(numbers, invalid))
