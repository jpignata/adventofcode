import sys


def find(grid, dirs):
    maxx, maxy = len(grid[0]), len(grid)
    start = (grid[0].index("."), 0)
    target = (grid[-1].index("."), len(grid) - 1)
    nodes = [start, target]
    edges = {}

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                continue

            neighbors = 0

            for dx, dy in dirs[cell]:
                nx, ny = dx + x, dy + y

                if 0 <= nx < maxx and 0 <= ny < maxy and grid[ny][nx] != "#":
                    neighbors += 1

            if neighbors > 2:
                nodes.append((x, y))

    for sx, sy in nodes:
        s = [((sx, sy), 0)]
        edges[(sx, sy)] = []
        seen = set()

        while s:
            (x, y), dist = s.pop()

            if (x, y) in seen:
                continue

            seen.add((x, y))

            if (x, y) in nodes and (x, y) != (sx, sy):
                edges[(sx, sy)].append(((x, y), dist))
                continue

            for dx, dy in dirs[grid[y][x]]:
                nx, ny = dx + x, dy + y

                if 0 <= nx < maxx and 0 <= ny < maxy and grid[ny][nx] != "#":
                    s.append(((nx, ny), dist + 1))

    def dfs(node, dist=0, seen=None):
        score = 0

        if node == target:
            return dist

        if not seen:
            seen = set()

        seen.add(node)

        for neighbor, next_dist in edges[node]:
            if neighbor not in seen:
                score = max(score, dfs(neighbor, dist + next_dist, seen))

        seen.remove(node)

        return score

    return dfs(start)


grid = [list(line.strip()) for line in sys.stdin]
dirs = {
    ".": ((1, 0), (-1, 0), (0, 1), (0, -1)),
    "^": ((0, -1),),
    "v": ((0, 1),),
    ">": ((1, 0),),
    "<": ((-1, 0),),
}

print("Part 1:", find(grid, dirs))
print("Part 2:", find(grid, {char: dirs["."] for char in dirs.keys()}))
