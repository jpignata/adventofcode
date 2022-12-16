import sys
from re import findall


def solve():
    sensors = []

    for line in sys.stdin:
        sx, sy, bx, by = [int(number) for number in findall(r"-?[0-9]+", line.strip())]
        sensors.append(((sx, sy), abs(sx - bx) + abs(sy - by)))

    print("Part 1:", sum(abs(i) for i in inspect(sensors, 2_000_000)[0]))
    print("Part 2:", find(sensors, 4_000_000))


def inspect(sensors, y):
    def merge(intervals):
        intervals.sort()
        merged = []

        for start, end in intervals:
            if not merged or merged[-1][1] < start:
                merged.append((start, end))
            else:
                merged[-1] = (merged[-1][0], max(merged[-1][1], end))

        return merged

    intervals = []

    for (sx, sy), dist in sensors:
        if abs(y - sy) > dist:
            continue

        start = (sx - dist) + abs(y - sy)
        end = (sx + dist) - abs(y - sy)

        intervals.append((start, end))

    return merge(intervals)


def find(sensors, boundary):
    for y in range(boundary + 1, 0, -1):
        intervals = [
            (max(0, interval[0]), min(boundary, interval[1]))
            for interval in inspect(sensors, y)
        ]

        if len(intervals) > 1:
            return (intervals[0][1] + 1) * boundary + y

    return -1


if __name__ == "__main__":
    solve()
