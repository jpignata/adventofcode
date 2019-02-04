import sys
from itertools import cycle

changes = [int(line.strip()) for line in sys.stdin.readlines()]
frequency = 0
frequencies = dict()

for change in cycle(changes):
    frequency += change

    if frequency in frequencies:
        break

    frequencies[frequency] = True

print('Part 1:', sum(changes))
print('Part 2:', frequency)
