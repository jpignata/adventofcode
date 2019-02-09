from itertools import permutations
import sys
import re

rows = [list(map(int, re.findall(r'\d+', l))) for l in sys.stdin.readlines()]
checksum = 0
resultsum = 0

for row in rows:
    checksum += max(row) - min(row)

    for dividend, divisor in permutations(row, 2):
        if dividend % divisor == 0:
            resultsum += dividend // divisor

print('Part 1:', checksum)
print('Part 2:', resultsum)
