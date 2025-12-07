import sys

lines = sys.stdin.readlines()
beams = [int(c == "S") for c in lines[0]]
splits = 0

for line in lines:
    for x, char in enumerate(line):
        if char == "^" and beams[x]:
            splits += 1
            beams[x - 1] += beams[x]
            beams[x + 1] += beams[x]
            beams[x] = 0

print("Part 1:", splits)
print("Part 2:", sum(beams))
