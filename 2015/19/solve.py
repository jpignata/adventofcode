import sys
from random import shuffle

replacements = list()
molecules = set()

for line in sys.stdin.readlines():
    if "=>" in line:
        search, to = line.strip().split(" => ")
        replacements.append((search, to))
    elif len(line.strip()) > 0:
        molecule = line.strip()

for search, to in replacements:
    i = molecule.find(search)

    while i != -1:
        molecules.add(molecule[0:i] + to + molecule[i + len(search) :])
        i = molecule.find(search, i + len(search))

steps = 0
fabricated = molecule

while fabricated != "e":
    for to, search in replacements:
        if search in fabricated:
            fabricated = fabricated.replace(search, to, 1)
            steps += 1
            break
    else:
        steps = 0
        fabricated = molecule
        shuffle(replacements)

print("Part 1:", len(molecules))
print("Part 2:", steps)
