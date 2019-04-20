import sys

components = dict()

for c1 in [tuple(map(int, line.strip().split(','))) for line in sys.stdin]:
    components[c1] = []
    matches = []

    for component in components:
        for c2 in components[component]:
            dist = (abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) +
                    abs(c1[2] - c2[2]) + abs(c1[3] - c2[3]))

            if dist <= 3:
                matches.append(component)
                break

    components[c1].append(c1)

    for match in matches:
        components[c1].extend(components.pop(match))

print('Part 1:', len(components))
