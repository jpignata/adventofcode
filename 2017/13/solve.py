import sys
from itertools import count


def severity(firewall, *, delay=0):
    severity = 0

    for level in range(delay, delay + max(firewall) + 1):
        scanner_range = firewall.get(level - delay, 0)

        if level and scanner_range and level % ((scanner_range - 1) * 2) == 0:
            severity += (level - delay) * scanner_range

            if delay > 0:
                return -1

    return severity


def escape(firewall):
    for i in count(1):
        if severity(firewall, delay=i) == 0:
            return i


firewall = {
    int(depth): int(scanner_range)
    for depth, scanner_range in [
        line.strip().split(": ") for line in sys.stdin.readlines()
    ]
}

print("Part 1:", severity(firewall))
print("Part 2:", escape(firewall))
