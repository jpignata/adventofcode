import sys
from copy import deepcopy


def expand(grid):
    next_grid = []

    for line in grid:
        next_line = []

        for char in line:
            match char:
                case "#":
                    next_chars = "##"
                case "O":
                    next_chars = "[]"
                case "@":
                    next_chars = "@."
                case _:
                    next_chars = ".."

            next_line.extend(next_chars)

        next_grid.append(next_line)

    return next_grid


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

    return sum(
        100 * y + x
        for y, line in enumerate(grid)
        for x, cell in enumerate(line)
        if cell == "O"
    )


def part2(grid, moves, sx, sy):
    grid = expand(grid)

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

            for x, y in changes:
                grid[y][x] = changes[(x, y)]

            for x, y in set(edges) - set(changes):
                grid[y][x] = "."

            sx, sy = sx + dx, sy + dy

    return sum(
        100 * y + x
        for y, line in enumerate(grid)
        for x, cell in enumerate(line)
        if cell == "["
    )


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
    print("Part 2:", part2(grid, moves, sx * 2, sy))


if __name__ == "__main__":
    main()
