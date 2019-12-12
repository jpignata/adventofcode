import sys
import math
from types import SimpleNamespace
from itertools import combinations
from functools import reduce

moons = list()

for line in sys.stdin.readlines():
    x, y, z = [int(c.split('=')[1]) for c in line[1:-2].split(', ')]
    moons.append(SimpleNamespace(pos=[x, y, z], vel=[0, 0, 0]))

seen = [{str([m.pos[i], m.vel[i]]) for m in moons} for i in range(3)]
cycles = [0] * 3
total = 0
step = 0

while not all(cycles):
    for pair in combinations(moons, 2):
        for i, (a, b) in enumerate(zip(pair[0].pos, pair[1].pos)):
            if a != b:
                pair[0].vel[i] += 1 if (a < b) else -1
                pair[1].vel[i] += 1 if (b < a) else -1

    for moon in moons:
        moon.pos = list(map(sum, zip(moon.pos, moon.vel)))

    if step == 999:
        total = sum(sum(map(abs, m.pos)) * sum(map(abs, m.vel)) for m in moons)

    for i in range(3):
        state = str([(m.pos[i], m.vel[i]) for m in moons])

        if not cycles[i] and state in seen[i]:
            cycles[i] = step

        seen[i].add(state)

    step += 1

print(f'Part 1: {total}')
print(f'Part 2: {reduce(lambda a, b: abs(a*b) // math.gcd(a, b), cycles)}')
