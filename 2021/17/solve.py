import re
import sys

x1, x2, y1, y2 = [int(c) for c in re.findall(r"[-\d]+", sys.stdin.readline())]
target = {(x, y) for y in range(y1, y2 + 1) for x in range(x1, x2 + 1)}
maxes = []

for y in range(-abs(y1), abs(y1) + 1):
    for x in range(-abs(x2), abs(x2) + 1):
        maxy = 0
        px, py = 0, 0
        vx, vy = x, y

        while px <= x2 and py >= y1:
            px += vx
            py += vy
            maxy = max(maxy, py)
            vy -= 1

            if vx != 0:
                vx += 1 if vx < 0 else -1

            if (px, py) in target:
                maxes.append(maxy)
                break

print("Part 1:", max(maxes))
print("Part 2:", len(maxes))
