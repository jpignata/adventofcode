import sys

grid = {}
moves = {
    "|": ((0, -1), (0, 1)),
    "-": ((1, 0), (-1, 0)),
    "L": ((0, -1), (1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, 1), (-1, 0)),
    "F": ((0, 1), (1, 0)),
}

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        grid[(x, y)] = char

        if char == "S":
            grid[(x, y)] = "7"
            start = (x, y)

s = [start]
visited = set()
steps = inside = 0

while s:
    x, y = s.pop()
    steps += 1
    visited.add((x, y))

    for dx, dy in moves[grid[(x, y)]]:
        nx, ny = x + dx, y + dy

        if grid[(nx, ny)] != "." and (nx, ny) not in visited:
            s.append((nx, ny))

for x, y in set(grid) - visited:
    crosses = [
        (x1, y)
        for x1 in range(x)
        if (x1, y) in visited and grid[(x1, y)] in "|JL"
    ]
    inside += len(crosses) % 2

print("Part 1:", (steps - 1) // 2)
print("Part 2:", inside)
