import re
import sys
from collections import namedtuple


def parse(line):
    pattern = re.compile(
            r'(?P<action>[\w ]+) (?P<start>[\d,]+) through (?P<stop>[\d,]+)')
    action, start, stop = pattern.match(line).group('action', 'start', 'stop')

    return instruction(action.strip(), tuple(map(int, start.split(','))),
                       tuple(map(int, stop.split(','))))


def run(instructions, actions, start=False):
    grid = [[start] * 1000 for n in range(1000)]

    for instruction in instructions:
        for y in range(instruction.start[1], instruction.stop[1] + 1):
            for x in range(instruction.start[0], instruction.stop[0] + 1):
                grid[y][x] = actions[instruction.action](grid[y][x])

    return grid


instruction = namedtuple('Instruction', ['action', 'start', 'stop'])
instructions = [parse(line.strip()) for line in sys.stdin.readlines()]

actions1 = {'turn on': lambda x: True, 'turn off': lambda x: False,
            'toggle': lambda x: not x}
actions2 = {'turn on': lambda x: x+1, 'turn off': lambda x: max(x-1, 0),
            'toggle': lambda x: x+2}

grid1 = run(instructions, actions1)
grid2 = run(instructions, actions2, start=0)

print('Part 1:', sum([row.count(True) for row in grid1]))
print('Part 2:', sum([sum(row) for row in grid2]))
