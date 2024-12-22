import sys
from collections import defaultdict

totals = defaultdict(int)
part1 = 0

for number in list(map(int, sys.stdin.read().split())):
    sequence = []
    seen = set()

    for _ in range(2000):
        prev = number % 10
        number ^= number * 64 % 16777216
        number ^= number // 32
        number ^= number * 2048 % 16777216
        current = number % 10

        sequence.append(current - prev)

        if (subsequence := tuple(sequence[-4:])) not in seen:
            totals[subsequence] += current
            seen.add(subsequence)

    part1 += number

print("Part 1:", part1)
print("Part 2:", max(totals.values()))
