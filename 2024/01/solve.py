import sys

left, right = zip(*(map(int, line.split()) for line in sys.stdin))
total = sum(abs(id1 - id2) for id1, id2 in zip(sorted(left), sorted(right)))
similarity = sum(id * right.count(id) for id in left)

print("Part 1:", total)
print("Part 2:", similarity)
