import sys
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
        (i, int(char)) for i, char in enumerate(line) if char.isdigit()
    ]
    word_values = [
        (match.start(), j + 1)
        for j, word in enumerate(words)
        for match in finditer(word, line)
    ]
    values = sorted(digit_values + word_values)

    part1 += digit_values[0][1] * 10 + digit_values[-1][1]
    part2 += values[0][1] * 10 + values[-1][1]

print("Part 1:", part1)
print("Part 2:", part2)
