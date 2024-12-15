import sys
from copy import deepcopy


def expand(grid):
    return [
        [
            char
            for cell in line
            for char in {"#": "##", "O": "[]", "@": "@.", ".": ".."}[cell]
        ]
        for line in grid
    ]


def score(grid, target):
    return sum(
        100 * y + x
        for y, line in enumerate(grid)
        for x, cell in enumerate(line)
        if cell == target
    )


def part1(grid, moves, sx, sy):
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
        if move(sx, sy, dx, dy):
            sx, sy = sx + dx, sy + dy

    return score(grid, "O")


def part2(grid, moves, sx, sy):
    grid = expand(grid)
    sx *= 2

    def move(x, y, dx, dy):
        s = [(x, y)]
        seen = set()

        while s:
            x, y = s.pop()

            if grid[y][x] == "#":
                return []

            if grid[y][x] == "@":
                s.append((x + dx, y + dy))
            elif grid[y][x] == "[":
                if dy and (x + 1, y) not in seen:
                    s.append((x + 1, y))
                s.append((x + dx, y + dy))
            elif grid[y][x] == "]":
                if dy and (x - 1, y) not in seen:
                    s.append((x - 1, y))
                s.append((x + dx, y + dy))

            if grid[y][x] != ".":
                seen.add((x, y))

        return seen

    for dx, dy in moves:
        if edges := move(sx, sy, dx, dy):
            changes = {}

            for x, y in sorted(edges):
                nx, ny = x + dx, y + dy
                changes[(nx, ny)] = grid[y][x]
                grid[y][x] = "."

            for x, y in changes:
                grid[y][x] = changes[(x, y)]

            sx, sy = sx + dx, sy + dy

    return score(grid, "[")


def main():
    dirs = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    grid = []
    moves = []
    sx, sy = 0, 0

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
