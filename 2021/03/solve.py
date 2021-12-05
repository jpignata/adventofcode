import sys
from collections import Counter

LEAST_COMMON = -1
MOST_COMMON = 0


def to_decimal(bits):
    return int(''.join(bits), 2)


def find(numbers, *, strategy, tiebreaker):
    for position in range(len(numbers[0])):
        cols = list(zip(*numbers))
        counts = Counter(cols[position]).most_common()

        if len(counts) == 1:
            target = counts[0][0]
        elif counts[0][1] == counts[1][1]:
            target = tiebreaker
        else:
            target = counts[strategy][0]

        numbers = [number for number in numbers if number[position] == target]

        if len(numbers) == 1:
            return numbers[0]


numbers = [list(line.strip()) for line in sys.stdin]
cols = list(zip(*numbers))

gamma = ['1' if bits.count('1') > len(cols[0]) / 2 else '0' for bits in cols]
epsilon = ['0' if bit == '1' else '1' for bit in gamma]
generator = find(numbers, strategy=MOST_COMMON, tiebreaker='1')
scrubber = find(numbers, strategy=LEAST_COMMON, tiebreaker='0')

print('Part 1:', to_decimal(gamma) * to_decimal(epsilon))
print('Part 2:', to_decimal(generator) * to_decimal(scrubber))
