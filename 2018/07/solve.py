import re
import sys
from collections import defaultdict
from itertools import count

requirements = defaultdict(set)
steps = set()

for line in sys.stdin.readlines():
    prerequisite, step = re.findall(r' ([A-Z]) ', line)
    steps.add(step)
    steps.add(prerequisite)
    requirements[step].add(prerequisite)


def order():
    order = []

    while len(order) < len(steps):
        for step in sorted(steps - set(order)):
            if all(step in order for step in requirements[step]):
                order.append(step)
                break

    return ''.join(order)


def seconds(num_workers=5):
    visited = set()
    workers = [0] * num_workers
    letters = [None] * num_workers

    for clock in count():
        for i, done in enumerate(workers):
            if done <= clock and letters[i]:
                visited.add(letters[i])
                letters[i] = None

        for i, done in enumerate(workers):
            if done <= clock:
                for step in sorted(steps - visited - set(letters)):
                    if all(step in visited for step in requirements[step]):
                        workers[i] = clock + ord(step) - 4
                        letters[i] = step
                        break

        if not any(letters):
            return clock


print('Part 1:', order())
print('Part 2:', seconds())
