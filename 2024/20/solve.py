import sys
from itertools import combinations


def find(grid, start):
    maxx, maxy = len(grid[0]), len(grid)
    distances = {}
    s = [(0, start)]

    while s:
        distance, (x, y) = s.pop()
        distances[(x, y)] = distance

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if 0 <= (nx := x + dx) < maxx and 0 <= (ny := y + dy) < maxy:
                if grid[ny][nx] != "#" and (nx, ny) not in distances:
                    s.append((distance + 1, (nx, ny)))

    return distances.items()


def main():
    grid = [list(line.strip()) for line in sys.stdin]
    start, _ = [
        (x, y)
        for y in range(len(grid))
        for x in range(len(grid[y]))
        if grid[y][x] in "SE"
    ]
    distances = find(grid, start)
    part1 = part2 = 0

    for ((x1, y1), dist1), ((x2, y2), dist2) in combinations(distances, 2):
        cheat_dist = abs(x1 - x2) + abs(y1 - y2)

        if dist2 - dist1 - cheat_dist >= 100:
            part1 += cheat_dist == 2
            part2 += cheat_dist <= 20

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
