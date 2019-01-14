import sys
import re
from operator import eq, gt, lt


def find(sues, attributes, *, comparisons=dict()):
    for i, sue in enumerate(sues):
        for attribute, value in sue.items():
            comparison = comparisons.get(attribute, eq)
            if not comparison(value, attributes[attribute]):
                break
        else:
            return i + 1


sues = [dict(sue) for sue in
        [map(lambda match: (match[0], int(match[1])), matches) for matches in
        [re.findall(r'(\w+): (\d+)', line) for line in sys.stdin.readlines()]]]
attributes = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,
              'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2,
              'perfumes': 1}
comparisons = {'cats': gt, 'trees': gt, 'pomeranians': lt, 'goldfish': lt}

print('Part 1:', find(sues, attributes))
print('Part 2:', find(sues, attributes, comparisons=comparisons))
