import sys
from collections import defaultdict


def search(max_visits=1):
    s = [[["end"], defaultdict(int)]]
    paths = 0

    while s:
        path, counts = s.pop()

        for cave in edges[path[-1]]:
            if cave == "start":
                paths += 1
            elif cave != "end":
                if cave[0].islower():
                    if any(count == max_visits for count in counts.values()):
                        allowed = 1
                    else:
                        allowed = max_visits

                    if counts[cave] < allowed:
                        next_counts = counts.copy()
                        next_counts[cave] += 1
                        s.append([path + [cave], next_counts])
                else:
                    s.append([path + [cave], counts])

    return paths


edges = defaultdict(list)

for line in sys.stdin:
    cave1, cave2 = line.strip().split("-")
    edges[cave1].append(cave2)
    edges[cave2].append(cave1)

print("Part 1:", search())
print("Part 2:", search(2))
