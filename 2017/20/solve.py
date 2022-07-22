import re
import sys
from collections import defaultdict
from operator import add, methodcaller


class Particle:
    def __init__(self, id, p1, p2, p3, v1, v2, v3, a1, a2, a3):
        self.id = id
        self.position = (p1, p2, p3)
        self.velocity = (v1, v2, v3)
        self.acceleration = (a1, a2, a3)

    def tick(self):
        self.velocity = tuple(map(add, self.velocity, self.acceleration))
        self.position = tuple(map(add, self.position, self.velocity))

    def speed(self):
        return sum(map(abs, self.acceleration))


def closest():
    return min(particles, key=methodcaller("speed")).id


def survivors():
    for _ in range(40):
        positions = defaultdict(set)

        for particle in particles:
            particle.tick()
            positions[particle.position].add(particle)

        for collisions in positions.values():
            if len(collisions) > 1:
                for particle in collisions:
                    particles.remove(particle)

    return len(particles)


particles = [
    Particle(i, *map(int, re.findall(r"(-?\d+)", line)))
    for i, line in enumerate(sys.stdin)
]

print("Part 1:", closest())
print("Part 2:", survivors())
