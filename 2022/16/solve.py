import sys
from re import findall
from heapq import heappop, heappush
from collections import namedtuple, defaultdict
from math import inf


def solve():
    Valve = namedtuple("Valve", ["pressure", "tunnels"])

    valves = {
        match[0]: Valve(int(match[1]), tuple(match[2:]))
        for line in sys.stdin
        if (match := findall(r"([A-Z]{2}|[0-9]+)", line))
    }

    print("Part 1:", search(valves))
    print("Part 2:", search2(valves))


def search2(valves):
    queue = [((0, 0), 0, 0, set(), ("AA", "AA"))]
    highest = 0
    visited = defaultdict(lambda: -inf)
    max_flow = sum(valve.pressure for valve in valves.values())

    while queue:
        _, minute, flow, flowing, current = heappop(queue)

        if visited[(minute, current)] >= flow:
            continue

        visited[(minute, current)] = flow

        if minute == 26:
            highest = max(highest, flow)
            continue

        gain = sum(valves[valve].pressure for valve in flowing)

        if gain >= max_flow:
            highest = max(highest, flow + gain * (26 - minute))
            continue

        flow += gain
        minute += 1
        score = gain * -1, minute

        heappush(
            queue,
            (score, minute, flow, flowing.copy(), current),
        )

        for valve1 in set(valves[current[0]].tunnels):
            for valve2 in set(valves[current[1]].tunnels):
                if valve1 == valve2:
                    continue

                heappush(
                    queue,
                    (score, minute, flow, flowing.copy(), (valve1, valve2)),
                )

                if current[0] not in flowing and valves[current[0]].pressure > 0:
                    heappush(
                        queue,
                        (
                            score,
                            minute,
                            flow,
                            flowing.union({current[0]}),
                            (current[0], valve2),
                        ),
                    )
                if current[1] not in flowing and valves[current[1]].pressure > 0:
                    heappush(
                        queue,
                        (
                            score,
                            minute,
                            flow,
                            flowing.union({current[1]}),
                            (valve1, current[1]),
                        ),
                    )

        for valve in current:
            if valve not in flowing and valves[valve].pressure > 0:
                heappush(
                    queue,
                    (
                        score,
                        minute,
                        flow,
                        flowing.union({valve}),
                        current,
                    ),
                )

        if all(
            valve not in flowing and valves[valve].pressure > 0 for valve in current
        ):
            heappush(
                queue,
                (
                    score,
                    minute,
                    flow,
                    flowing.union(set(current)),
                    current,
                ),
            )

    return highest


def search(valves):
    queue = [((0, 0), 0, 0, set(), "AA")]
    highest = 0
    visited = defaultdict(lambda: -inf)
    max_flow = sum(valve.pressure for valve in valves.values())

    while queue:
        _, minute, flow, flowing, valve = heappop(queue)

        if visited[(minute, frozenset(flowing), valve)] >= flow:
            continue

        visited[(minute, frozenset(flowing), valve)] = flow

        if minute == 30:
            highest = max(highest, flow)
            continue

        gain = sum(valves[valve].pressure for valve in flowing)

        if gain >= max_flow:
            highest = max(highest, flow + gain * (30 - minute))
            continue

        flow += gain
        minute += 1
        score = gain * -1, len(flowing) * -1, minute

        heappush(
            queue,
            (score, minute, flow, flowing.copy(), valve),
        )

        for tunnel in valves[valve].tunnels:
            heappush(
                queue,
                (
                    score,
                    minute,
                    flow,
                    flowing.copy(),
                    tunnel,
                ),
            )

        if valve not in flowing and valves[valve].pressure > 0:
            heappush(
                queue,
                (
                    score,
                    minute,
                    flow,
                    flowing.union({valve}),
                    valve,
                ),
            )

    return highest


if __name__ == "__main__":
    solve()
