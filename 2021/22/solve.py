import sys
import re
from collections import Counter

cubes = Counter()
full, initialization = 0, 0

for line in sys.stdin:
    toggle, coords = line.split()
    sign = 1 if toggle == 'on' else -1
    x1, x2, y1, y2, z1, z2 = [int(c) for c in re.findall(r'[-\d]+', coords)]
    next_cubes = Counter()

    for (ox1, ox2, oy1, oy2, oz1, oz2), count in cubes.items():
        nx1 = max(x1, ox1)
        nx2 = min(x2, ox2)
        ny1 = max(y1, oy1)
        ny2 = min(y2, oy2)
        nz1 = max(z1, oz1)
        nz2 = min(z2, oz2)

        if nx1 <= nx2 and ny1 <= ny2 and nz1 <= nz2:
            next_cubes[(nx1, nx2, ny1, ny2, nz1, nz2)] -= count

    if sign == 1:
        next_cubes[(x1, x2, y1, y2, z1, z2)] += sign

    cubes.update(next_cubes)

for (x1, x2, y1, y2, z1, z2), count in cubes.items():
    cubes = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) * count
    full += cubes

    if all(-50 <= c <= 50 for c in (x1, x2, y1, y2, z1, z2)):
        initialization += cubes

print('Part 1:', initialization)
print('Part 2:', full)
