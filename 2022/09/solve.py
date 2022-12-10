import sys


def solve():
    motions = []
    deltas = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

    for line in sys.stdin:
        direction, steps = line.strip().split()
        motions.append((deltas[direction], int(steps)))

    print("Part 1:", simulate(motions))
    print("Part 2:", simulate(motions, 9))


def simulate(motions, size=1):
    def compare(a, b):
        return (a > b) - (a < b)

    head = (0, 0)
    knots = [(0, 0) for _ in range(size)]
    visited = {(0, 0)}

    for delta, steps in motions:
        for _ in range(steps):
            prev = head = (head[0] + delta[0], head[1] + delta[1])

            for i, knot in enumerate(knots):
                if abs(prev[0] - knot[0]) > 1 or abs(prev[1] - knot[1]) > 1:
                    knots[i] = (
                        knot[0] + compare(prev[0], knot[0]),
                        knot[1] + compare(prev[1], knot[1]),
                    )

                prev = knot

            visited.add(knots[-1])

    return len(visited)


if __name__ == "__main__":
    solve()
