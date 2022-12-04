import sys
import re

contains = overlaps = 0

for line in sys.stdin:
    sections = [int(number) for number in re.findall(r"\d+", line)]
    elf1 = range(sections[0], sections[1] + 1)
    elf2 = range(sections[2], sections[3] + 1)

    if elf1[0] in elf2 and elf1[-1] in elf2 or elf2[0] in elf1 and elf2[-1] in elf1:
        contains += 1

    if max(elf1[0], elf2[0]) <= min(elf1[-1], elf2[-1]):
        overlaps += 1

print("Part 1:", contains)
print("Part 2:", overlaps)
