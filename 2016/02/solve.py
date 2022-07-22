import sys

instructions = [list(line.strip()) for line in sys.stdin.readlines()]
deltas = {"L": (-1, 0), "U": (0, -1), "R": (1, 0), "D": (0, 1)}
grid1 = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
grid2 = [
    ["0", "0", "1", "0", "0"],
    ["0", "2", "3", "4", "0"],
    ["5", "6", "7", "8", "9"],
    ["0", "A", "B", "C", "0"],
    ["0", "0", "D", "0", "0"],
]


def code(grid, start=(1, 1)):
    x, y = start
    code = []

    for row in instructions:
        for char in row:
            dx, dy = deltas[char]
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
                if grid[ny][nx] != "0":
                    x, y = nx, ny
        code.append(grid[y][x])

    return "".join(code)


print("Part 1:", code(grid1))
print("Part 2:", code(grid2, start=(0, 2)))
