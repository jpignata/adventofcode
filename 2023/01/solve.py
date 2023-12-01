import sys
from string import digits
from re import finditer

part1 = part2 = 0
words = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

for line in sys.stdin:
    digit_values = [
        (match.start(), int(digit))
        for digit in digits
        for match in finditer(digit, line)
    ]
    word_values = [
        (match.start(), j + 1)
        for j, word in enumerate(words)
        for match in finditer(word, line)
    ]
    values = digit_values + word_values

    digit_values.sort()
    values.sort()

    part1 += digit_values[0][1] * 10 + digit_values[-1][1]
    part2 += values[0][1] * 10 + values[-1][1]

print("Part 1:", part1)
print("Part 2:", part2)
