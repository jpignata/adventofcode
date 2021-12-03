import sys
from collections import Counter
from enum import IntEnum


class Disposition(IntEnum):
    LEAST_COMMON = -1
    MOST_COMMON = 0


def to_decimal(binary):
    return int(''.join(binary), 2)


def find(numbers, disposition, *, tiebreaker):
    for position in range(len(numbers[0])):
        rotated = list(zip(*numbers[::-1]))
        counts = Counter(rotated[position]).most_common()

        if len(counts) == 1:
            target = counts[0][0]
        elif counts[0][1] == counts[1][1]:
            target = tiebreaker
        else:
            target = counts[disposition][0]

        numbers = [number for number in numbers if number[position] == target]

        if len(numbers) == 1:
            return to_decimal(numbers[0])


numbers = [list(line.strip()) for line in sys.stdin]
rotated = list(zip(*numbers[::-1]))
half = len(rotated[0]) // 2

gamma = ['1' if bits.count('1') > half else '0' for bits in rotated]
epsilon = ['0' if bit == '1' else '1' for bit in gamma]
generator = find(numbers, Disposition.MOST_COMMON, tiebreaker='1')
scrubber = find(numbers, Disposition.LEAST_COMMON, tiebreaker='0')

print('Part 1:', to_decimal(gamma) * to_decimal(epsilon))
print('Part 2:', generator * scrubber)
