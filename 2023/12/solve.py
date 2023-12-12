import sys
from functools import cache


@cache
def count(pattern, freqs, current=0):
    total = 0

    if not pattern:
        at_end_of_last_group = len(freqs) == 1 and freqs[0] == current
        no_groups_left = not (freqs or current)

        return at_end_of_last_group or no_groups_left

    if pattern[0] in "?#":
        total += count(pattern[1:], freqs, current + 1)

    if pattern[0] in "?.":
        if (freqs and freqs[0] == current) or not current:
            total += count(pattern[1:], freqs[1:] if current else freqs)

    return total


def total(patterns, multiplier=1):
    return sum(
        count("?".join([pattern] * multiplier), freqs * multiplier)
        for pattern, freqs in patterns
    )


patterns = []

for line in sys.stdin:
    parts = line.strip().split()
    patterns.append((parts[0], tuple(int(n) for n in parts[1].split(","))))

print("Part 1:", total(patterns))
print("Part 2:", total(patterns, 5))
