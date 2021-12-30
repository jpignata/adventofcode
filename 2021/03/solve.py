import sys
from collections import Counter


def find(numbers, *, strategy, tiebreaker):
    for position in range(len(numbers[0])):
        positions = list(zip(*numbers))
        counts = Counter(positions[position]).most_common()

        if len(counts) == 1:
            target = counts[0][0]
        elif counts[0][1] == counts[1][1]:
            target = tiebreaker
        else:
            target = counts[strategy][0]

        numbers = [number for number in numbers if number[position] == target]

        if len(numbers) == 1:
            return numbers[0]


def to_decimal(bits):
    return int(''.join(bits), 2)


numbers = [list(line.strip()) for line in sys.stdin]
gamma = [str(int(pos.count('1') > len(numbers) / 2)) for pos in zip(*numbers)]
epsilon = [str(int(bit == '0')) for bit in gamma]
generator = find(numbers, strategy=0, tiebreaker='1')
scrubber = find(numbers, strategy=1, tiebreaker='0')

print('Part 1:', to_decimal(gamma) * to_decimal(epsilon))
print('Part 2:', to_decimal(generator) * to_decimal(scrubber))
