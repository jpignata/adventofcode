import sys
from collections import deque, defaultdict

orbits = dict()
connections = defaultdict(set)
part1, part2 = 0, 0

for line in sys.stdin.readlines():
    planets = line.strip().split(")")
    connections[planets[0]].add(planets[1])
    connections[planets[1]].add(planets[0])
    orbits[planets[1]] = planets[0]

for planet, orbiting in orbits.items():
    part1 += 1

    while orbiting in orbits:
        part1 += 1
        orbiting = orbits[orbiting]

q = deque([[orbits["YOU"], 0]])
visited = set()

while q:
    planet, distance = q.popleft()

    if planet not in visited:
        visited.add(planet)

        if planet == "SAN":
            part2 = distance - 1
            break
        else:
            for connection in connections[planet]:
                q.append([connection, distance + 1])

print("Part 1:", part1)
print("Part 2:", part2)
