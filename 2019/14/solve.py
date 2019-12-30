import sys
import math
from collections import defaultdict, namedtuple


def make(chemical, amount, supply=None):
    if supply is None:
        supply = defaultdict(int)

    if chemical == 'ORE':
        return amount

    recipe = recipes[chemical]
    needed = amount - supply[chemical]
    multiplier = math.ceil(needed / recipe.amount)
    supply[chemical] += recipe.amount * multiplier

    for chemical, amount in recipe.inputs.items():
        make(chemical, amount * multiplier, supply)
        supply[chemical] -= amount * multiplier

    return abs(supply['ORE'])


Chemical = namedtuple('Chemical', ['amount', 'inputs'])
recipes = dict()

for line in [line.strip() for line in sys.stdin]:
    parts = line.split(' => ')
    inputs = {n: int(y) for y, n in [p.strip().split(' ')
                                     for p in parts[0].split(',')]}
    yields, name = parts[1].split(' ')
    recipes[name] = Chemical(int(yields), inputs)

fuel = 1
target = 1000000000000

while make('FUEL', fuel) < target:
    start = fuel
    fuel *= 2
    end = fuel

while end - start > 1:
    mid = (start + end) // 2

    if make('FUEL', mid) > target:
        end = mid
    else:
        start = mid

print('Part 1:', make('FUEL', 1))
print('Part 2:', start)
