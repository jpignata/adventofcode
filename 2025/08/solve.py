import sys
from collections import deque
from itertools import combinations
from math import dist, prod

junctions = [tuple(map(int, line.split(","))) for line in sys.stdin]
roots = {junction: junction for junction in junctions}
sizes = {junction: 1 for junction in junctions}


def find(junction):
    while roots[junction] != junction:
        junction = roots[junction]

    return junction


def union(a, b):
    root_a, root_b = find(a), find(b)

    if root_a == root_b:
        return 0

    if sizes[root_a] < sizes[root_b]:
        root_a, root_b = root_b, root_a

    roots[root_b] = root_a
    sizes[root_a] += sizes[root_b]

    del sizes[root_b]

    return a[0] * b[0]


def main():
    distances = deque(sorted(combinations(junctions, 2), key=lambda pair: dist(*pair)))
    last = None

    for _ in range(len(junctions)):
        union(*distances.popleft())

    print("Part 1:", prod(sorted(sizes.values())[-3:]))

    while distances:
        if result := union(*distances.popleft()):
            last = result

    print("Part 2:", last)


if __name__ == "__main__":
    main()
