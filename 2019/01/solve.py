import sys

modules = [int(line) for line in sys.stdin]
part1, part2 = 0, 0

for module in modules:
    fuel = module // 3 - 2
    part1 += fuel
    part2 += fuel

    while fuel > 0:
        fuel = max(fuel // 3 - 2, 0)
        part2 += fuel

print('Part 1:', part1)
print('Part 2:', part2)
