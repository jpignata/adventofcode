import sys
import re
from collections import defaultdict

grid = defaultdict(list)

for line in sys.stdin.readlines():
    id, x, y, w, h = map(int, re.findall(r"\d+", line))

    for iy in range(y, y + h):
        for ix in range(x, x + w):
            grid[(ix, iy)].append(id)

in_one_cell = set(i for l in grid.values() for i in l if len(l) == 1)
in_multiple_cells = set(i for l in grid.values() for i in l if len(l) > 1)

print("Part 1:", sum(1 for cell in grid if len(grid[cell]) > 1))
print("Part 2:", (in_one_cell - in_multiple_cells).pop())
