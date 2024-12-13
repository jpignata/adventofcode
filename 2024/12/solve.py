import sys


def dfs(grid, x, y, visited):
    if (x, y) in visited:
        return []

    visited.add((x, y))

    region = [(x, y)]

    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy

        if (nx, ny) in grid and grid[(nx, ny)] == grid[(x, y)]:
            region.extend(dfs(grid, nx, ny, visited))

    return region


def main():
    grid = {
        (x, y): plant
        for y, line in enumerate(sys.stdin)
        for x, plant in enumerate(line.strip())
    }
    part1 = part2 = 0
    visited = set()

    for x, y in grid:
        if region := dfs(grid, x, y, visited):
            perimeter = sides = 0

            for x, y in region:
                perimeter += (x + 1, y) not in region
                perimeter += (x - 1, y) not in region
                perimeter += (x, y + 1) not in region
                perimeter += (x, y - 1) not in region
                sides += (x - 1, y) not in region and (x, y - 1) not in region
                sides += (x + 1, y) not in region and (x, y - 1) not in region
                sides += (x - 1, y) not in region and (x, y + 1) not in region
                sides += (x + 1, y) not in region and (x, y + 1) not in region
                sides += (
                    (x - 1, y) in region
                    and (x, y - 1) in region
                    and (x - 1, y - 1) not in region
                )
                sides += (
                    (x + 1, y) in region
                    and (x, y - 1) in region
                    and (x + 1, y - 1) not in region
                )
                sides += (
                    (x - 1, y) in region
                    and (x, y + 1) in region
                    and (x - 1, y + 1) not in region
                )
                sides += (
                    (x + 1, y) in region
                    and (x, y + 1) in region
                    and (x + 1, y + 1) not in region
                )

        part1 += len(region) * perimeter
        part2 += len(region) * sides

    print("Part 1:", part1)
    print("Part 2:", part2)


if __name__ == "__main__":
    main()
