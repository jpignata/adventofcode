import sys
from collections import deque
from operator import attrgetter, add
from itertools import count


class Unit:
    def __init__(self, kind, location, power_boost=0):
        self.kind = kind
        self.location = location
        self.attack_power = 3 + power_boost
        self.hit_points = 200
        self.enemy = 'E' if self.kind == 'G' else 'G'

    def isdead(self):
        return self.hit_points <= 0

    def hit(self, attack_power):
        self.hit_points -= attack_power


class Game:
    def __init__(self, survey, power_boost=0):
        self.map = list()
        self.units = list()
        self.rounds = 0
        self.start_elves = 0

        for y, line in enumerate(survey):
            row = list()
            for x, char in enumerate(line.strip()):
                if char in ('G'):
                    self.units.append(Unit(char, (x, y)))
                    row.append('.')
                elif char in ('E'):
                    self.units.append(Unit(char, (x, y), power_boost))
                    row.append('.')
                    self.start_elves += 1
                else:
                    row.append(char)

            self.map.append(row)

    def round(self):
        self.units.sort(key=lambda u: tuple(reversed(u.location)))

        for unit in self.units.copy():
            if unit.isdead():
                continue

            targets = list(filter(lambda u: u.kind == unit.enemy, self.units))
            adjacent = [tuple(map(add, d, unit.location))
                        for d in ((0, -1), (-1, 0), (1, 0), (0, 1))]

            if len(targets) == 0:
                return

            if not set(adjacent) & set(map(attrgetter('location'), targets)):
                locations = list()

                for target in targets:
                    for delta in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                        location = tuple(map(add, delta, target.location))

                        if self.isopen(location):
                            locations.append(location)

                path = self.bfs(unit.location, locations)

                if path:
                    unit.location = path
                    adjacent = [tuple(map(add, d, unit.location))
                                for d in ((0, -1), (-1, 0), (1, 0), (0, 1))]

            enemies = list(filter(lambda t: t.location in adjacent, targets))
            enemies.sort(key=lambda e: (e.hit_points, e.location[1],
                                        e.location[0]))

            if enemies:
                enemies[0].hit(unit.attack_power)
                if enemies[0].isdead():
                    self.units.remove(enemies[0])

        self.rounds += 1

    def bfs(self, location, locations):
        q = deque([[location]])
        visited = list()

        while q:
            path = q.popleft()
            last_location = path[-1]

            if last_location not in visited:
                for delta in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                    new_location = tuple(map(add, delta, last_location))
                    new_path = path + [new_location]

                    if new_location in locations:
                        return new_path[1]
                    elif self.isopen(new_location):
                        q.append(new_path)

            visited.append(last_location)

    def isopen(self, location):
        x, y = location
        occupied = map(attrgetter('location'), self.units)

        return self.map[y][x] == '.' and location not in occupied

    def finished(self):
        return len(set(map(attrgetter('kind'), self.units))) == 1

    def outcome(self):
        return sum(map(attrgetter('hit_points'), self.units)) * self.rounds

    def all_elves_alive(self):
        elves = list(filter(lambda u: u.kind == 'E', self.units))
        return self.start_elves == len(elves)


lines = [line.strip() for line in sys.stdin]
part1 = Game(lines)

while not part1.finished():
    part1.round()

for power_boost in count(1):
    part2 = Game(lines, power_boost)

    while not part2.finished() and part2.all_elves_alive():
        part2.round()

    if part2.all_elves_alive():
        break

print('Part 1:', part1.outcome())
print('Part 2:', part2.outcome())
