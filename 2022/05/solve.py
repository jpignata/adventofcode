import re
import sys
from collections import defaultdict
from copy import deepcopy


def solve():
    moves = []
    stacks = defaultdict(list)

    for line in sys.stdin:
        if line.startswith("move"):
            moves.append(tuple(int(number) for number in re.findall(r"[0-9]+", line)))
        else:
            for match in re.finditer(r"[A-Z]", line):
                stack = match.start() // 4 + 1
                stacks[stack].insert(0, match[0])

    print("Part 1:", rearrange(stacks, moves, single))
    print("Part 2:", rearrange(stacks, moves, multiple))


def rearrange(stacks, moves, strategy):
    stacks = deepcopy(stacks)
    strategy(stacks, moves)
    return "".join(stacks[i][-1] for i in range(1, len(stacks) + 1))


def single(stacks, moves):
    for quantity, source, destination in moves:
        for _ in range(quantity):
            stacks[destination].append(stacks[source].pop())


def multiple(stacks, moves):
    for quantity, source, destination in moves:
        stacks[destination].extend(stacks[source][-quantity:])
        stacks[source] = stacks[source][:-quantity]


if __name__ == "__main__":
    solve()
