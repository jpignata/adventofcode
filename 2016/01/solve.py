import sys
import operator

directions = [(d[0], int(d[1:])) for d in sys.stdin.readline().split(', ')]
turns = {'L': -1, 'R': 1}
deltas = {'W': (-1, 0), 'N': (0, -1), 'E': (1, 0), 'S': (0, 1)}
orientations = list(deltas.keys())
visited = set()
first_visited_twice = ()
location = (0, 0)
orientation = 'N'

for turn, steps in directions:
    index = orientations.index(orientation) + turns[turn]
    orientation = orientations[index % len(orientations)]

    for _ in range(steps):
        location = tuple(map(operator.add, location, deltas[orientation]))
        if location in visited and not first_visited_twice:
            first_visited_twice = location
        visited.add(location)

print('Print 1:', sum(map(abs, location)))
print('Print 2:', sum(map(abs, first_visited_twice)))
