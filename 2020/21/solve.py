import sys
from collections import defaultdict

counter = defaultdict(int)
allergens = defaultdict(list)
suspects = defaultdict(set)

for line in sys.stdin.readlines():
    parts = line.strip()[:-1].split(' (contains ')
    ingredients = set(parts[0].split())

    for ingredient in ingredients:
        counter[ingredient] += 1

    for allergen in tuple(parts[1].split(', ')):
        allergens[allergen].append(ingredients)

for ingredient in counter:
    for allergen, items in allergens.items():
        if all(ingredient in item for item in items):
            suspects[ingredient].add(allergen)

identified = []
seen = set()

while len(identified) < len(allergens):
    for ingredient, group in suspects.items():
        if len(group - seen) == 1:
            identified.append(((group - seen).pop(), ingredient))
            seen.add((group - seen).pop())

print('Part 1:', sum(c for name, c in counter.items() if name not in suspects))
print('Part 2:', ','.join(ingredient for _, ingredient in sorted(identified)))
