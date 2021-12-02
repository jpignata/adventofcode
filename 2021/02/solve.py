import sys

position = 0
aim = 0
depth = 0

for direction, units in [line.split() for line in sys.stdin]:
    units = int(units)

    if direction == 'down':
        aim += units
    elif direction == 'up':
        aim -= units
    elif direction == 'forward':
        depth += aim * units
        position += units

print('Part 1:', aim * position)
print('Part 2:', depth * position)
