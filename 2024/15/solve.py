import sys
from copy import deepcopy


def score(grid):
    return sum(
        100 * y + x
        for y, line in enumerate(grid)
        for x, cell in enumerate(line)
        if cell in "[O"
    )


def part1(grid, moves, cx, cy):
    grid = deepcopy(grid)

    def move(x, y, dx, dy):
        nx, ny = x + dx, y + dy

        if grid[ny][nx] == ".":
            grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
            return True

        if grid[ny][nx] == "O":
            if move(nx, ny, dx, dy):
                grid[y][x], grid[ny][nx] = grid[ny][nx], grid[y][x]
                return True

        return False

    for dx, dy in moves:
        if move(cx, cy, dx, dy):
            cx, cy = cx + dx, cy + dy

    return score(grid)


def part2(grid, moves, cx, cy):
    expansions = {"#": "##", "O": "[]", "@": "@.", ".": ".."}
    grid = [[char for cell in line for char in expansions[cell]] for line in grid]
    cx *= 2

    def find(x, y, dx, dy):
        s = [(x, y)]
        seen = set()

        while s:
            x, y = s.pop()

            if grid[y][x] == "#":
                return set()

            if grid[y][x] != ".":
                s.append((x + dx, y + dy))
                seen.add((x, y))

            if grid[y][x] == "[" and dy and (x + 1, y) not in seen:
                s.append((x + 1, y))
            elif grid[y][x] == "]" and dy and (x - 1, y) not in seen:
                s.append((x - 1, y))

        return seen

    for dx, dy in moves:
        if edges := find(cx, cy, dx, dy):
            changes = {}

            for x, y in sorted(edges):
                changes[(x + dx, y + dy)] = grid[y][x]
                grid[y][x] = "."

            for x, y in changes:
                grid[y][x] = changes[(x, y)]

            cx, cy = cx + dx, cy + dy

    return score(grid)


def main():
    dirs = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    sx, sy = -1, -1
    grid = []
    moves = []

    for y, line in enumerate(sys.stdin):
        if line := line.strip():
            grid.append(list(line))

            if "@" in line:
                sx, sy = line.index("@"), y
        else:
            while line := sys.stdin.readline():
                moves.extend([dirs[move] for move in line.strip()])

    print("Part 1:", part1(grid, moves, sx, sy))
    print("Part 2:", part2(grid, moves, sx, sy))


if __name__ == "__main__":
    main()
