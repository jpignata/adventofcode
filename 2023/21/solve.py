import sys


def run(grid, active, generations=64):
    maxx, maxy = list(active)[0]

    for _ in range(generations):
        next_active = set()

        for y in range(maxy + 2):
            for x in range(maxx + 2):
                if (x, y) in grid:
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy

                        if (nx, ny) in grid and (nx, ny) in active:
                            next_active.add((x, y))
                            maxx = max(x, maxx)
                            maxy = max(y, maxy)
                            break

        active = next_active

    return len(active)


def extrapolate(grid, start):
    dists = {start: 0}
    steps = 0
    s = [start]

    while s:
        next_s = []

        for x, y in s:
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy

                if (nx, ny) in grid and (nx, ny) not in dists:
                    dists[(nx, ny)] = steps + 1
                    next_s.append((nx, ny))
        s = next_s
        steps += 1

    tiles = 26501365 // (start[0] * 2 + 1)
    odds = sum(dist % 2 for dist in dists.values())
    evens = sum(not dist % 2 for dist in dists.values())
    odds_angle = sum(dist % 2 for dist in dists.values() if dist > 65)
    evens_angle = sum(not dist % 2 for dist in dists.values() if dist > 65)

    total = (tiles + 1) * (tiles + 1) * odds
    total += tiles * tiles * evens
    total += tiles * evens_angle - tiles
    total -= (tiles + 1) * odds_angle

    return total


grid = set()

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == "S":
            start = (x, y)

        if char != "#":
            grid.add((x, y))


print("Part 1:", run(grid, {start}))
print("Part 2:", extrapolate(grid, start))
