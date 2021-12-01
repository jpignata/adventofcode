import math
import sys

measurements = [int(line) for line in sys.stdin]
count = [0, 0]
prev = (math.inf, math.inf)

for i, measurement in enumerate(measurements):
    window = sum(measurements[i:i+3])

    if measurement > prev[0]:
        count[0] += 1

    if window > prev[1]:
        count[1] += 1

    prev = (measurement, window)

print('Part 1:', count[0])
print('Part 2:', count[1])
