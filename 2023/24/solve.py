import sys
from itertools import combinations
from re import findall
from sympy import Eq, solve, Symbol, symbols


class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = int(sx)
        self.sy = int(sy)
        self.sz = int(sz)
        self.vx = int(vx)
        self.vy = int(vy)
        self.vz = int(vz)
        self.slope = self.vy / self.vx
        self.intercept = self.sy - self.slope * self.sx


def find(h1, h2, area=(2e14, 4e14)):
    if h1.slope == h2.slope:
        return None

    ix = (h2.intercept - h1.intercept) / (h1.slope - h2.slope)
    iy = h1.slope * ix + h1.intercept
    t1 = (ix - h1.sx) / h1.vx
    t2 = (ix - h2.sx) / h2.vx

    if t1 > 0 and t2 > 0:
        return area[0] <= ix <= area[1] and area[0] <= iy <= area[1]


def throw(hailstones):
    t = []
    eq = []
    x, y, z, vx, vy, vz = symbols("x y z vx vy vz")

    for i, h in enumerate(hailstones):
        t.append(Symbol(f"t{i}"))
        eq.append(Eq(h.sx + h.vx * t[-1], x + vx * t[-1]))
        eq.append(Eq(h.sy + h.vy * t[-1], y + vy * t[-1]))
        eq.append(Eq(h.sz + h.vz * t[-1], z + vz * t[-1]))

    result = solve(eq, (x, y, z, vx, vy, vz, *t), dict=True)

    return result[0][x] + result[0][y] + result[0][z]


hailstones = [Hailstone(*findall(r"-?\d+", line)) for line in sys.stdin]
intersecting = sum(1 for h1, h2 in combinations(hailstones, 2) if find(h1, h2))

print("Part 1:", intersecting)
print("Part 2:", throw(hailstones[:6]))
