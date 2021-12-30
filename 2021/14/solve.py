import sys
from itertools import pairwise
from collections import Counter


def generate(counts, steps):
    elements = Counter()

    for _ in range(steps):
        next_counts = Counter()

        for pair, count in counts.items():
            for result in rules[pair]:
                next_counts[result] += count

        counts = next_counts

    for pair, count in counts.items():
        elements[pair[1]] += count

    return max(elements.values()) - min(elements.values())


rules = {}
counts = Counter(''.join(pair)
                 for pair in pairwise(sys.stdin.readline().strip()))

for line in sys.stdin.readlines()[1:]:
    pair, result = line.strip().split(' -> ')
    rules[pair] = (pair[0] + result, result + pair[1])

print('Part 1:', generate(counts, 10))
print('Part 2:', generate(counts, 40))
