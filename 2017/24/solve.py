import sys
from collections import deque

components = [tuple(map(int, line.split("/"))) for line in sys.stdin]
q = deque([[[], 0, components]])
strongest = 0
longest = (0, 0)

while q:
    bridge, port, components = q.popleft()
    compatible = [c for c in components if port in c]

    if compatible:
        for component in compatible:
            new_bridge = bridge + [component]
            new_port = component[1 if component.index(port) == 0 else 0]
            new_components = [c for c in components if c != component]

            q.append([new_bridge, new_port, new_components])
    else:
        strength = sum(c for c in bridge for c in c)
        strongest = max(strongest, strength)
        longest = max(longest, (len(bridge), strength))

print("Part 1:", strongest)
print("Part 2:", longest[1])
