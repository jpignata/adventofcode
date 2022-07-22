import sys
from itertools import cycle, repeat


def fft(digits, pattern, phases=100):
    for _ in range(phases):
        out = []

        for i, _ in enumerate(digits):
            next_digits = []
            multiplier = cycle(pattern)

            if i == 0:
                next(multiplier)

            for j, d in enumerate(digits):
                if j == 0 or (j + 1) % (i + 1) == 0:
                    p = next(multiplier)

                next_digits.append(d * p)

            out.append(int([d for d in str(sum(next_digits))][-1]))

        digits = out

    return "".join(str(d) for d in digits[:8])


def find(digits, phases=100):
    offset = int("".join(map(str, digits[:7])))
    digits = digits[offset:]

    for _ in range(phases):
        total = 0

        for i in range(len(digits) - 1, -1, -1):
            digits[i] = total = (total + digits[i]) % 10

    return "".join(str(d) for d in digits[:8])


digits = [int(c) for c in sys.stdin.readline().strip()]

print("Part 1:", fft(digits, [0, 1, 0, -1]))
print("Part 2:", find(digits * 10000))
