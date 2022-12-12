import sys
from math import inf
from heapq import heappop, heappush
from string import ascii_lowercase


def solve():
    grid = [list(line.strip()) for line in sys.stdin]

    for y, row in enumerate(grid):
        if "E" in row:
            end = (row.index("E"), y)
            break

    print("Part 1:", dijkstra(grid, end, "S"))
    print("Part 2:", dijkstra(grid, end, "a"))


def dijkstra(grid, start, target):
    maxx, maxy = len(grid[0]), len(grid)
    costs = {(x, y): inf for y in range(maxy) for x in range(maxx)}
    costs[start] = 0
    queue = [(0, start)]

    while queue:
        cost, (x, y) = heappop(queue)

        if grid[y][x] == target:
            return cost

        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < maxx and 0 <= ny < maxy:
                if index(grid[ny][nx]) >= index(grid[y][x]) - 1:
                    new_cost = cost + 1

                    if new_cost < costs[(nx, ny)]:
                        costs[(nx, ny)] = new_cost
                        heappush(queue, (new_cost, (nx, ny)))


def index(letter):
    if letter in "SE":
        return ascii_lowercase.index("z")

    return ascii_lowercase.index(letter)


if __name__ == "__main__":
    solve()
