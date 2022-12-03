import sys
from string import ascii_letters

rucksacks = [line.strip() for line in sys.stdin]
duplicates = badges = 0

for rucksack in rucksacks:
    mid = len(rucksack) // 2
    duplicate = set.intersection(set(rucksack[:mid]), set(rucksack[mid:])).pop()
    duplicates += ascii_letters.index(duplicate) + 1

for i in range(0, len(rucksacks), 3):
    badge = set.intersection(
        set(rucksacks[i]), set(rucksacks[i + 1]), set(rucksacks[i + 2])
    ).pop()
    badges += ascii_letters.index(badge) + 1

print("Part 1:", duplicates)
print("Part 2:", badges)
