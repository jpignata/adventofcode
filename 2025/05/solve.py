import sys

ranges = []
ids = []
merged = []

for line in sys.stdin:
    if line := line.strip():
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end + 1))
        else:
            ids.append(int(line))

ranges.sort()

for start, end in ranges:
    if not merged or merged[-1][1] < start:
        merged.append((start, end))
    else:
        merged[-1][1] = max(merged[-1][1], end)

print(
    "Part 1:",
    sum(1 for _id in ids for start, end in merged if _id in range(start, end)),
)
print("Part 2:", sum(end - start for start, end in merged))
