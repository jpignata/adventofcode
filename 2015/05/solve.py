import re
import sys

part1 = 0
part2 = 0

for line in [line.strip() for line in sys.stdin.readlines()]:
    if all(s not in line for s in ("ab", "cd", "pq", "xy")):
        if sum([line.count(vowel) for vowel in "aeiou"]) >= 3:
            if re.match(r".*([a-z])\1.*", line):
                part1 += 1

    if re.match(r".*([a-z])[a-z]\1.*", line):
        if re.match(r".*([a-z][a-z]).*\1.*", line):
            part2 += 1

print("Part 1:", part1)
print("Part 2:", part2)
