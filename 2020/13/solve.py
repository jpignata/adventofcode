import sys
from itertools import count


def find_bus(start, buses):
    for minute in count(start):
        for _, bus in buses:
            if minute % bus == 0:
                return bus * (minute - start)


def find_pattern(buses):
    start, step = 1, 1

    for offset, bus in buses:
        for minute in count(start, step):
            if (minute + offset) % bus == 0:
                start = minute
                step *= bus
                break

    return start


start = int(sys.stdin.readline())
buses = [
    (i, int(bus)) for i, bus in enumerate(sys.stdin.readline().split(",")) if bus != "x"
]

print("Part 1:", find_bus(start, buses))
print("Part 2:", find_pattern(buses))
