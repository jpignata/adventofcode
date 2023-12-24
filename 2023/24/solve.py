import sys
from re import findall
from itertools import combinations
from dataclasses import dataclass


@dataclass
class Hailstone:
    def __init__(self, px, py, pz, vx, vy, vz):
        self.px = int(px)
        self.py = int(py)
        self.pz = int(pz)
        self.vx = int(vx)
        self.vy = int(vy)
        self.vz = int(vz)

    @property
    def slope(self):
        return self.vy / self.vx if self.vx != 0 else -1

    @property
    def intercept(self):
        return self.py - self.slope * self.px if self.vx != 0 else self.px


def find(h1, h2, area):
    if h1.slope == h2.slope:
        return None

    ix = (h2.intercept - h1.intercept) / (h1.slope - h2.slope)
    iy = h1.slope * ix + h1.intercept
    t1 = (ix - h1.px) / h1.vx if h1.vx != 0 else -1
    t2 = (ix - h2.px) / h2.vx if h2.vx != 0 else -1

    if t1 >= 0 and t2 > 0:
        if area[0] <= ix <= area[1] and area[0] <= iy <= area[1]:
            return (ix, iy)

    return None


hailstones = [Hailstone(*findall(r"-?\d+", line)) for line in sys.stdin]
intersecting = sum(
    1 for h1, h2 in combinations(hailstones, 2) if find(h1, h2, (2e14, 4e14))
)

print("Part 1:", intersecting)
print("Part 2:", "wtf")
