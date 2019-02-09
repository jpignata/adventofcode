import operator
from itertools import count, product

dirs = 'ruld'
deltas = {'r': (1, 0), 'u': (0, -1), 'l': (-1, 0), 'd': (0, 1)}
location = (0, 0)
direction = 'r'
seen = {(0, 0): 1}
total = 0
distance = 0
target = 312051


def adjacent_sum(location):
    total = 0

    for delta in product((0, 1, -1), (0, 1, -1)):
        neighbor = tuple(map(operator.add, location, delta))

        if neighbor in seen:
            total += seen[neighbor]

    return total


for i in count(2):
    new_direction = dirs[(dirs.index(direction) + 1) % len(dirs)]
    new_location = tuple(map(operator.add, location, deltas[new_direction]))

    if new_location not in seen:
        direction = new_direction
        location = new_location
    else:
        location = tuple(map(operator.add, location, deltas[direction]))

    seen[location] = adjacent_sum(location)

    if i == target:
        distance = abs(location[0]) + abs(location[1])

    if seen[location] > target and total == 0:
        total = seen[location]

    if distance != 0 and total != 0:
        break


print('Part 1:', distance)
print('Part 2:', total)
