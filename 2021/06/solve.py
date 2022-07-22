import sys
from collections import Counter


def solve(fish, days):
    for i in range(days):
        next_fish = Counter()

        for age, count in fish.items():
            if age == 0:
                next_fish[6] += count
                next_fish[8] += count
            else:
                next_fish[age - 1] += count

        fish = next_fish

    return sum(fish.values())


fish = Counter(int(fish) for fish in sys.stdin.readline().split(","))

print("Part 1:", solve(fish, 80))
print("Part 2:", solve(fish, 256))
