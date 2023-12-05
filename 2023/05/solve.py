import sys
from itertools import count

maps = []
seeds = [
    int(number)
    for number in sys.stdin.readline().strip().split(": ")[-1].split()
]

for line in sys.stdin:
    if line == "\n":
        maps.append([])
    elif line[0].isdigit():
        dest, src, r = [int(number) for number in line.strip().split()]
        maps[-1].append(((dest, dest + r), (src, src + r)))
        maps[-1].sort()

lowest = float("inf")

for seed in seeds:
    node = seed
    for map in maps:
        for (dest_start, dest_end), (src_start, src_end) in map:
            if src_start <= node <= src_end:
                node = (node - src_start) + dest_start
                break

    lowest = min(lowest, node)

print("Part 1:", lowest)

sources = [(start, start + r) for start, r in zip(seeds[0::2], seeds[1::2])]

for node in count():
    orig = node
    for map in maps[::-1]:
        for (dest_start, dest_end), (src_start, src_end) in map:
            if dest_start <= node <= dest_end:
                node = (node - dest_start) + src_start
                break

    for start, end in sources:
        if node in range(start, end):
            print("Part 2:", orig)
            exit()
