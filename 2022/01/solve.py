import sys

calories = [0]

for line in sys.stdin:
    if line := line.strip():
        calories[-1] += int(line)
    else:
        calories.append(0)

calories.sort()

print("Part 1:", calories[-1])
print("Part 2:", sum(calories[-3:]))
