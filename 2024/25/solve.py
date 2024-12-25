import sys

schematics, locks, keys = [[]], [], []
matches = 0

for line in sys.stdin:
    if not line.strip():
        schematics.append([])
    else:
        schematics[-1].append(line.strip())

for schematic in schematics:
    cols = [row.count("#") - 1 for row in zip(*schematic)]

    if schematic[0].count("#"):
        locks.append(cols)
    else:
        keys.append(cols)

for lock in locks:
    for key in keys:
        for pin1, pin2 in zip(lock, key):
            if pin1 + pin2 > 5:
                break
        else:
            matches += 1

print("Part 1:", matches)
