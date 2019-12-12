import sys
import math
from types import SimpleNamespace
from itertools import combinations, count


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


moons = list()

for line in sys.stdin.readlines():
    comps = line[1:-2].split(', ')
    posx, posy, posz = [int(comp.split('=')[1]) for comp in comps]
    moon = SimpleNamespace(pos=[posx, posy, posz], vel=[0, 0, 0])

    moons.append(moon)

xseen, yseen, zseen = set(), set(), set()
xcycle, ycycle, zcycle = 0, 0, 0
total = 0

xseen.add(str([(m.pos[0], m.vel[0]) for m in moons]))
yseen.add(str([(m.pos[1], m.vel[1]) for m in moons]))
zseen.add(str([(m.pos[2], m.vel[2]) for m in moons]))

for step in count(1):
    for pair in combinations(moons, 2):
        for i, (a, b) in enumerate(zip(pair[0].pos, pair[1].pos)):
            if a > b:
                pair[0].vel[i] -= 1
                pair[1].vel[i] += 1
            elif a < b:
                pair[0].vel[i] += 1
                pair[1].vel[i] -= 1

    for moon in moons:
        moon.pos = list(map(sum, zip(moon.pos, moon.vel)))

    if step == 1000:
        total = sum(sum(map(abs, m.pos)) * sum(map(abs, m.vel)) for m in moons)

    xstate = str([(m.pos[0], m.vel[0]) for m in moons])
    ystate = str([(m.pos[1], m.vel[1]) for m in moons])
    zstate = str([(m.pos[2], m.vel[2]) for m in moons])

    if not xcycle and xstate in xseen:
        xcycle = step

    if not ycycle and ystate in yseen:
        ycycle = step

    if not zcycle and zstate in zseen:
        zcycle = step

    if xcycle and ycycle and zcycle:
        break

    xseen.add(xstate)
    yseen.add(ystate)
    zseen.add(zstate)

print(f'Part 1: {total}')
print(f'Part 2: {lcm(xcycle, lcm(ycycle, zcycle))}')
