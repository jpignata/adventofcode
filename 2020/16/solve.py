import sys
from math import prod

rules, valid = [], []
error_rate = 0

while (line := sys.stdin.readline()):
    if 'or' in line:
        parts = line.strip().split(' ')
        rules.append([range(int(begin), int(end) + 1) for begin, end in
                      [r.split('-') for r in [parts[-3], parts[-1]]]])
    elif 'your ticket' in line:
        mine = [int(field) for field in sys.stdin.readline().split(',')]
    elif 'nearby tickets' in line:
        for line in sys.stdin.readlines():
            ticket = [int(field) for field in line.split(',')]

            for field in ticket:
                if not any(field in part for rule in rules for part in rule):
                    error_rate += field
                    break
            else:
                valid.append(ticket)

columns = [[row[i] for row in valid] for i in range(len(mine))]
matches = [set() for _ in range(len(mine))]
positions = [None for _ in range(len(mine))]
found = set()

for i, rule in enumerate(rules):
    for j, column in enumerate(columns):
        for cell in column:
            if not any(cell in part for part in rule):
                break
        else:
            matches[i].add(j)

while len(found) != len(mine):
    for i, match in enumerate(matches):
        if len(match - found) == 1:
            positions[i] = (match - found).pop()
            found.update(match - found)

print('Part 1:', error_rate)
print('Part 2:', prod(mine[pos] for pos in positions[:6]))
