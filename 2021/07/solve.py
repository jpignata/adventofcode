import math
import sys
from functools import cache


@cache
def fuel(move):
    return sum(range(1, move + 1))


positions = [int(number) for number in sys.stdin.readline().split(",")]
part1, part2 = math.inf, math.inf

for meeting in range(max(positions)):
    tally1, tally2 = 0, 0

    for crab in positions:
        move = abs(meeting - crab)
        tally1 += move
        tally2 += fuel(move)

    part1 = min(tally1, part1)
    part2 = min(tally2, part2)

print("Part 1:", part1)
print("Part 2:", part2)
