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
steps = inside = 0
found = []
visited = set()

for y, line in enumerate(sys.stdin):
    for x, char in enumerate(line.strip()):
        grid[(x, y)] = char

        if char == "S":
            start = (x, y)

for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
    nx, ny = start[0] + dx, start[1] + dy

    if grid[(nx, ny)] in moves and (dx * -1, dy * -1) in moves[grid[(nx, ny)]]:
        found.append((dx, dy))

for char, delta in moves.items():
    if sorted(found) == sorted(delta):
        grid[start] = char

s = [start]

while s:
    x, y = s.pop()
    steps += 1
    visited.add((x, y))

    for dx, dy in moves[grid[(x, y)]]:
        nx, ny = x + dx, y + dy

        if (nx, ny) not in visited:
            s.append((nx, ny))

for x, y in set(grid) - visited:
    crosses = [
        (x1, y)
        for x1 in range(x)
        if (x1, y) in visited and grid[(x1, y)] in "|JL"
    ]
    inside += len(crosses) % 2

print("Part 1:", steps // 2)
print("Part 2:", inside)
