import sys

rules = {}
gold = 'shiny gold'


def reachable(start, target):
    if start == target:
        return True
    else:
        return any(reachable(bag, target) for bag in rules[start])


def total(start):
    return 1 + sum(total(bag) * n for bag, n in rules[start].items())


for line in sys.stdin.readlines():
    outer, inner = line[:-2].split(' contain ')
    outer = outer.rsplit(' ', 1)[0]
    rules[outer] = {}

    for bag in inner.split(', '):
        if bag != 'no other bags':
            parts = bag.split(' ')
            rules[outer][' '.join(parts[1:3])] = int(parts[0])


print('Part 1:', sum(reachable(bag, gold) for bag in rules if bag != gold))
print('Part 2:', total(gold) - 1)
