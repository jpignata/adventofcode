import sys
import re
from string import ascii_lowercase as ascii


def react(polymer):
    reacted = ['']

    for char in polymer:
        if reacted[-1].upper() == char.upper() and reacted[-1] != char:
            reacted.pop()
        else:
            reacted.append(char)

    return ''.join(reacted)


polymer = sys.stdin.readline().strip()
lengths = [len(react(re.sub(c, '', polymer, flags=re.I))) for c in ascii]

print('Part 1:', len(react(polymer)))
print('Part 2:', min(lengths))
