import sys


def generate(grid, active, generations):
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

    tiles = 26501365 // steps
    odds = sum(dist % 2 for dist in dists.values())
    evens = sum(not dist % 2 for dist in dists.values())
    odds_angle = sum(dist % 2 for dist in dists.values() if dist > steps // 2)
    evens_angle = sum(not dist % 2 for dist in dists.values() if dist > steps // 2)

    total = (tiles + 1) ** 2 * odds
    total += tiles**2 * evens
    total += tiles * evens_angle
    total -= (tiles + 1) * odds_angle
    total -= tiles  # account for the halves of the origin tile

    return total


grid = set()
start = (None, None)

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        if char == "S":
            start = (x, y)

        if char != "#":
            grid.add((x, y))


print("Part 1:", generate(grid, {start}, 64))
print("Part 2:", extrapolate(grid, start))
