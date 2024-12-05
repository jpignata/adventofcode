import sys
from functools import cmp_to_key


def cmp_items(a, b):
    return -1 if (a, b) in rules else 1


rules = set()
updates = []
part1 = part2 = 0

for line in sys.stdin:
    if "|" in line:
        rules.add(tuple(map(int, line.strip().split("|"))))
    elif "," in line:
        updates.append(list(map(int, line.strip().split(","))))

for pages in updates:
    mid = len(pages) // 2
    sorted_pages = sorted(pages, key=cmp_to_key(cmp_items))

    if pages == sorted_pages:
        part1 += pages[mid]
    else:
        part2 += sorted_pages[mid]

print("Part 1:", part1)
print("Part 2:", part2)
