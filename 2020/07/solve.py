import sys

rules = {}
gold = 'shiny gold'


def reachable(start):
    return start == gold or any(reachable(bag) for bag in rules[start])


def total(start):
    return 1 + sum(total(bag) * n for bag, n in rules[start].items())


for line in sys.stdin.readlines():
    outer, inner = line[:-2].split(' contain ')
    outer = outer.rsplit(' ', 1)[0]
    rules[outer] = {' '.join(bag.split(' ')[1:-1]): int(bag.split(' ')[0])
                    for bag in inner.split(', ') if inner[0:2] != 'no'}


print('Part 1:', sum(reachable(bag) for bag in rules if bag != gold))
print('Part 2:', total(gold) - 1)
