import sys

part1, part2 = 0, 0

for line in sys.stdin:
    left, right = line.strip().split(' | ')
    patterns = [set(pattern) for pattern in left.split()]
    output = [set(pattern) for pattern in right.split()]
    digits = [None] * 10

    digits[1] = next(p for p in patterns if len(p) == 2)
    digits[4] = next(p for p in patterns if len(p) == 4)
    digits[7] = next(p for p in patterns if len(p) == 3)
    digits[8] = next(p for p in patterns if len(p) == 7)
    digits[9] = next(p for p in patterns
                     if len(p) == 6 and digits[4] < p)
    digits[3] = next(p for p in patterns
                     if len(p) == 5 and digits[7] < p)
    digits[0] = next(p for p in patterns
                     if len(p) == 6 and p != digits[9] and digits[1] & p == digits[1])
    digits[6] = next(p for p in patterns
                     if len(p) == 6 and p != digits[0] and p != digits[9])
    digits[5] = next(p for p in patterns
                     if len(p) == 5 and p < digits[6])
    digits[2] = next(p for p in patterns
                     if len(p) == 5 and p != digits[3] and p != digits[5])

    part1 += len([pattern for pattern in output if len(pattern) in (2, 3, 4, 7)])
    part2 += int(''.join([str(digits.index(pattern)) for pattern in output]))

print('Part 1:', part1)
print('Part 2:', part2)
