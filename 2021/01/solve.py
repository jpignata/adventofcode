import sys


def find(measurements, offset):
    return sum(x > y for x, y in zip(measurements[offset:], measurements))


measurements = [int(line) for line in sys.stdin]

print("Part 1:", find(measurements, 1))
print("Part 2:", find(measurements, 3))
