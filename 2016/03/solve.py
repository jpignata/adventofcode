import sys
import re


def count(triangles):
    count = 0
    for a, b, c in triangles:
        if a + b > c and a + c > b and b + c > a:
            count += 1
    return count


triangles = [list(map(int, re.split(r'\s+', line.strip())))
             for line in sys.stdin.readlines()]
rows = count(triangles)
cols = 0

for i in range(0, len(triangles), 3):
    transposed = ([], [], [])
    for j in range(0, 3):
        for k in range(0, 3):
            transposed[j].append(triangles[i+k][j])
    cols += count(transposed)

print('Part 1:', rows)
print('Part 2:', cols)
