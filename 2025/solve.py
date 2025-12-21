import sys
from collections import defaultdict

edges = defaultdict(list)

for line in sys.stdin:
    device, outputs = line.split(": ")
    edges[device].extend(outputs.split())

exits = 0


def search(device):
    if device == "out":
        return 1

    return sum(search(neighbor) for neighbor in edges[device])


print("Part 1:", search("you"))
