import sys
from re import findall


def parse(text, *, advanced=False, enabled=True):
    total = 0

    for match in findall(r"(mul\((\d+),(\d+)\)|do(n't)*\(\))", text):
        if match[0].startswith("mul") and enabled:
            total += int(match[1]) * int(match[2])
        elif match[0].startswith("do") and advanced:
            enabled = match[0] == "do()"

    return total


program = sys.stdin.read()

print("Part 1:", parse(program))
print("Part 2:", parse(program, advanced=True))
