import sys
from ast import literal_eval
from functools import cmp_to_key
from math import prod


def compare(left, right):
    def cmp(a, b):
        return (a > b) - (a < b)

    if isinstance(left, list) and isinstance(right, list):
        for vleft, vright in zip(left, right):
            if result := compare(vleft, vright):
                return result

        return cmp(len(left), len(right))

    if isinstance(left, list):
        return compare(left, [right])

    if isinstance(right, list):
        return compare([left], right)

    return cmp(left, right)


packets = [literal_eval(line) for line in sys.stdin if line.strip()]
dividers = [[[2]], [[6]]]
part1 = sum(
    i + 1
    for i, (packet1, packet2) in enumerate(zip(packets[::2], packets[1::2]))
    if compare(packet1, packet2) == -1
)
part2 = prod(
    i + 1
    for i, packet in enumerate(sorted(packets + dividers, key=cmp_to_key(compare)))
    if packet in dividers
)

print("Part 1:", part1)
print("Part 2:", part2)
