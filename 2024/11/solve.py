import sys
from collections import Counter


def run(counts, times):
    for _ in range(times):
        next_counts = Counter()

        for stone, count in counts.items():
            digits = str(stone)

            if not stone:
                next_counts[1] += count
            elif not len(digits) % 2:
                mid = len(digits) // 2

                next_counts[int(digits[:mid])] += count
                next_counts[int(digits[mid:])] += count
            else:
                next_counts[stone * 2024] += count

        counts = next_counts

    return sum(counts.values())


stones = Counter(int(number) for number in sys.stdin.read().split())

print("Part 1:", run(stones, 25))
print("Part 2:", run(stones, 75))
