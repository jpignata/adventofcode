import re
import sys
from itertools import cycle
from collections import defaultdict


class Reindeer:
    def __init__(self, speed, fly_duration, rest_duration):
        self.speed = speed
        self.durations = {"fly": fly_duration, "rest": rest_duration}
        self.states = cycle(("fly", "rest"))
        self.distance = 0
        self.duration = 0

    def tick(self):
        if self.duration == 0:
            self.state = next(self.states)
            self.duration = self.durations[self.state]

        if self.state == "fly":
            self.distance += self.speed

        self.duration -= 1


def parse(line):
    pattern = re.compile(
        r"\w+ can fly (\d+) km/s for (\d+) seconds, "
        r"but then must rest for (\d+) seconds."
    )
    speed, fly_duration, rest_duration = map(int, pattern.match(line).groups())

    return Reindeer(speed, fly_duration, rest_duration)


def run(reindeer, stop):
    clock = 0
    points = defaultdict(int)

    while clock != stop:
        for racer in reindeer:
            racer.tick()

        further_distance = max(map(lambda r: r.distance, reindeer))
        winners = filter(lambda r: r.distance == further_distance, reindeer)

        for winner in winners:
            points[winner] += 1

        clock += 1

    return max(map(lambda r: r.distance, reindeer)), max(points.values())


reindeer = [parse(line) for line in sys.stdin.readlines()]
distance, points = run(reindeer, 2503)

print("Part 1:", distance)
print("Part 2:", points)
