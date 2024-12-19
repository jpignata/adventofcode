import sys
from functools import cache

patterns = sys.stdin.readline().strip().split(", ")
designs = [line.strip() for line in sys.stdin if line.strip()]


@cache
def count(design):
    if not design:
        return 1

    return sum(
        count(design[len(pattern) :])
        for pattern in patterns
        if design.startswith(pattern)
    )


print("Part 1:", sum(1 for design in designs if count(design)))
print("Part 2:", sum(count(design) for design in designs))
