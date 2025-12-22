import sys
from collections import defaultdict
from functools import cache

edges = defaultdict(list)

for line in sys.stdin:
    device, outputs = line.split(": ")
    edges[device].extend(outputs.split())


@cache
def search(node, required=tuple(), visited=frozenset()):
    if node == "out":
        return all(req in visited for req in required)

    if node in required:
        visited = frozenset(visited | {node})

    return sum(search(neighbor, required, visited) for neighbor in edges[node])


print("Part 1:", search("you"))
print("Part 2:", search("svr", ("fft", "dac")))
