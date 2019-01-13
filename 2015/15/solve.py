import sys
import re
import operator
from functools import reduce


def amount_generator(to, size):
    if size == 1:
        yield (to,)
        return

    for i in range(to + 1):
        for t in amount_generator(to - i, size - 1):
            yield (i,) + t


high_score = 0
high_score_500_cals = 0
ingredients = [tuple(map(int, re.findall(r'-?\d+', line)))
               for line in sys.stdin.readlines()]

for amounts in amount_generator(100, len(ingredients)):
    attributes = [tuple(map(lambda attr: attr * amount, attrs))
                  for attrs, amount in zip(ingredients, amounts)]
    properties = tuple(map(sum, zip(*attributes)))

    if min(properties[0:4]) > 0:
        score = reduce(operator.mul, properties[0:4], 1)
        high_score = max(score, high_score)

        if properties[-1] == 500:
            high_score_500_cals = max(score, high_score_500_cals)

print('Part 1:', high_score)
print('Part 2:', high_score_500_cals)
