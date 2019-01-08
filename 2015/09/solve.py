import sys
import re
from itertools import permutations

locations = set()
distances = dict()
routes = dict()
pattern = r'([\w]+) to ([\w]+) = ([\d]+)'

for line in [line.strip() for line in sys.stdin.readlines()]:
    start, end, distance = re.match(pattern, line).groups()
    locations.update((start, end))
    distances[(start, end)] = int(distance)
    distances[(end, start)] = int(distance)

for route in permutations(locations):
    routes[route] = 0

    for i, location in enumerate(route):
        if i == len(route)-1:
            break

        routes[route] += distances[(location, route[i+1])]

minimum = min(routes, key=routes.get)
maximum = max(routes, key=routes.get)

print('Part 1:', ' -> '.join(minimum), '=', routes[minimum])
print('Part 2:', ' -> '.join(maximum), '=', routes[maximum])
