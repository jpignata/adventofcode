import sys


def solve():
    cubes = [
        tuple(int(coord) for coord in line.strip().split(",")) for line in sys.stdin
    ]

    print("Part 1:", surfaces(cubes))
    print("Part 2:", reachable(cubes))


def surfaces(cubes):
    count = len(cubes) * 6

    for cube in cubes:
        for neighbor in neighbors(cube):
            if neighbor in cubes:
                count -= 1

    return count


def neighbors(cube):
    deltas = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))

    for delta in deltas:
        yield (cube[0] + delta[0], cube[1] + delta[1], cube[2] + delta[2])


def reachable(cubes):
    minx = min(x for x, _, _ in cubes) - 1
    miny = min(y for _, y, _ in cubes) - 1
    minz = min(z for _, _, z in cubes) - 1
    maxx = max(x for x, _, _ in cubes) + 1
    maxy = max(y for _, y, _ in cubes) + 1
    maxz = max(z for _, _, z in cubes) + 1

    s = [(minx, miny, minz)]
    visited = set()
    count = 0

    while s:
        position = s.pop()

        if position in visited:
            continue

        visited.add(position)

        for nx, ny, nz in neighbors(position):
            if (nx, ny, nz) in cubes:
                count += 1
            elif minx <= nx <= maxx and miny <= ny <= maxy and minz <= nz <= maxz:
                s.append((nx, ny, nz))

    return count


if __name__ == "__main__":
    solve()
