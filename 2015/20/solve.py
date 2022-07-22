target = 36000000
search_max = 1000000
part1 = [0] * search_max
part2 = [0] * search_max

for elf in range(1, search_max):
    for house in range(elf, search_max, elf):
        part1[house] += elf * 10

    for house in range(elf, min(elf * 50, search_max), elf):
        part2[house] += elf * 11

for house in part1:
    if house >= target:
        print("Part 1:", part1.index(house))
        break

for house in part2:
    if house >= target:
        print("Part 2:", part2.index(house))
        break
