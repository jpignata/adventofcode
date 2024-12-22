import sys
from collections import defaultdict
from itertools import pairwise


def evolve(number, times=1):
    for _ in range(times):
        number ^= number * 64
        number %= 16777216
        number ^= number // 32
        number %= 16777216
        number ^= number * 2048
        number %= 16777216

        yield number


def main():
    numbers = list(map(int, sys.stdin.read().split()))
    sequences = []
    totals = defaultdict(int)

    for number in numbers:
        sequences.append([])

        for previous, current in pairwise(evolve(number, 2000)):
            current_price, previous_price = current % 10, previous % 10

            sequences[-1].append(
                (current, current_price, current_price - previous_price)
            )

    for sequence in sequences:
        seen = set()

        for i in range(3, len(sequence)):
            price = sequence[i][1]
            subsequence = tuple(sequence[j][2] for j in range(i - 3, i + 1))

            if subsequence not in seen:
                totals[subsequence] += price
                seen.add(subsequence)

    print("Part 1:", sum(sequence[-1][0] for sequence in sequences))
    print("Part 2:", max(totals.values()))


if __name__ == "__main__":
    main()
