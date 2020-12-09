import sys


def find_invalid(numbers, size=25):
    for i, number in enumerate(numbers[size:]):
        sums = {numbers[i + j] + numbers[i + j + k] for k in range(size)
                for j in range(size)}

        if number not in sums:
            return number


def find_range(numbers, target):
    lo, hi = 0, 1

    while lo < len(numbers):
        total = sum(numbers[lo:hi])

        if total == target:
            return max(numbers[lo:hi]) + min(numbers[lo:hi])
        elif total > target:
            lo += 1
            hi = lo + 1
        elif total < target:
            hi += 1


numbers = [int(line) for line in sys.stdin.readlines()]
invalid = find_invalid(numbers)

print('Part 1:', invalid)
print('Part 2:', find_range(numbers, invalid))
