import sys
from collections import deque


def solve():
    grid = [list(line.strip()) for line in sys.stdin]

    for y, row in enumerate(grid):
        if "E" in row:
            end = (row.index("E"), y)

    print("Part 1:", bfs(grid, end, "S"))
    print("Part 2:", bfs(grid, end, "a"))


def bfs(grid, start, target):
    def index(letter):
        return ord("a" if letter == "S" else "z" if letter == "E" else letter)

    maxx, maxy = len(grid[0]), len(grid)
    queue = deque([(0, start)])
    visited = set()

    while queue:
        cost, (x, y) = queue.popleft()

        if grid[y][x] == target:
            return cost

        for dx, dy in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < maxx and 0 <= ny < maxy and (nx, ny) not in visited:
                if index(grid[ny][nx]) >= index(grid[y][x]) - 1:
                    queue.append((cost + 1, (nx, ny)))
                    visited.add((nx, ny))


if __name__ == "__main__":
    solve()
