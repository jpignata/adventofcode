import sys


def fill(containers, amount, *, filled, found):
    total = sum(filled)

    if total == amount:
        found.append(filled)
    elif total < amount:
        for i, container in enumerate(containers):
            fill(containers[i+1:], amount, filled=filled + [container],
                 found=found)

    return found


containers = [int(line) for line in sys.stdin.readlines()]
filled = fill(containers, 150, filled=list(), found=list())

print('Part 1:', len(filled))
print('Part 2:', len([c for c in filled if len(c) == min(map(len, filled))]))
