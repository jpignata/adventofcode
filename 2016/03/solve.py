import sys
import numpy as np


def count(triangles):
    return sum(1 for a, b, c in triangles if a + b > c and a + c > b and b + c > a)


triangles = np.loadtxt(sys.stdin.readlines())
transposed = triangles.transpose().flatten()
transposed.shape = int(len(transposed) / 3), 3

print("Part 1:", count(triangles))
print("Part 2:", count(transposed))
