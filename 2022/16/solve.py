import sys
from collections import deque, namedtuple
from re import findall


def solve():
    def calculate(valve1, valve2):
        q = deque([(valve1, 0)])
        visited = set()

        while q:
            valve, dist = q.popleft()

            if valve == valve2:
                return dist

            for tunnel in valves[valve].tunnels:
                if tunnel not in visited:
                    q.append((tunnel, dist + 1))

            visited.add(valve)

    Valve = namedtuple("Valve", ["pressure", "tunnels", "edges"])
    valves = {
        match[0]: Valve(int(match[1]), tuple(match[2:]), {})
        for line in sys.stdin
        if (match := findall(r"([A-Z]{2}|[0-9]+)", line))
    }

    for valve1 in valves:
        for valve2 in valves:
            if valve1 != valve2 and valves[valve2].pressure:
                valves[valve1].edges[valve2] = calculate(valve1, valve2)

    solo, _ = find(valves)
    player1, visited = find(valves, maximum=26)
    player2, _ = find(valves, visited=visited, maximum=26)

    print("Part 1:", solo)
    print("Part 2:", player1 + player2)


def find(valves, *, current="AA", visited=None, minute=0, maximum=30):
    score = 0

    if not visited:
        visited = []

    if minute >= maximum:
        return score, []

    valve = valves[current]
    score += valve.pressure * (maximum - minute)
    scores = max(
        find(
            valves,
            current=edge,
            visited=visited + [current],
            minute=minute + valve.edges[edge] + 1,
            maximum=maximum,
        )
        for edge in valve.edges
        if edge not in visited
    )

    return score + scores[0], [current] + scores[1]


if __name__ == "__main__":
    solve()
