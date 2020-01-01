import sys
import os
import itertools
import re

from intcode import Computer, Input


def run_until_input(computer):
    try:
        computer.run()
    except Input:
        return


items = list()
computer = Computer.load(filename=f'{os.path.dirname(__file__)}/memory.out')

for execute in ('west', 'north', 'west', 'west', 'west'):
    computer.execute(execute)

run_until_input(computer)

for line in computer.screen().split('\n'):
    if line == 'Items here:':
        items = list()
    elif line.startswith('- '):
        items.append(line[2:])

for i in range(len(items)):
    for combination in itertools.combinations(items, i):
        for item in combination:
            computer.execute(f'take {item}')

        computer.execute('north')
        run_until_input(computer)

        if match := re.search('get in by typing (\d*)', computer.screen()):
            print('Part 1:', match[1])
            break

        for item in combination:
            computer.execute(f'drop {item}')
