import re
import sys

guards = []
maxx = maxy = seconds = 0

for line in sys.stdin:
    px, py, vx, vy = list(map(int, re.findall(r"-?\d+", line)))
    maxx = max(maxx, px + 1)
    maxy = max(maxy, py + 1)

    guards.append(((px, py), (vx, vy)))

while True:
    if seconds == 100:
        midx, midy = maxx // 2, maxy // 2
        counts = [0] * 4

        for (px, py), _ in guards:
            if px < midx and py < midy:
                counts[0] += 1
            elif px < midx and py > midy:
                counts[1] += 1
            elif px > midx and py < midy:
                counts[2] += 1
            elif px > midx and py > midy:
                counts[3] += 1

        print("Part 1:", counts[0] * counts[1] * counts[2] * counts[3])

    if len(guards) == len({(x, y) for (x, y), _ in guards}):
        print("Part 2:", seconds)
        break

    guards = [
        ((((px + vx) % maxx, (py + vy) % maxy)), (vx, vy))
        for (px, py), (vx, vy) in guards
    ]
    seconds += 1
