import sys
from collections import Counter


def generate(counts, steps):
    for _ in range(steps):
        next_counts = Counter()

        for pair, count in counts.items():
            for result in rules[pair]:
                next_counts[result] += count

        counts = next_counts

    elements = Counter()

    for pair, count in counts.items():
        elements[pair[1]] += count

    return max(elements.values()) - min(elements.values())


rules = {}
counts = Counter()

for line in sys.stdin:
    line = line.strip()
    
    if ' -> ' in line:
        pair, result = line.strip().split(' -> ')
        rules[pair] = [pair[0] + result, result + pair[1]]
    elif len(line):
        for j in range(len(line) - 1):
            counts[line[j:j+2]] += 1

print('Part 1:', generate(counts, 10))
print('Part 2:', generate(counts, 40))
