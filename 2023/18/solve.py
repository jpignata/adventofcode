import sys


def dig(moves):
    x = y = perimeter = area = 0

    for (dx, dy), steps in moves:
        x, y = x + dx * steps, y + dy * steps
        area += x * dy * steps
        perimeter += steps

    return area + perimeter // 2 + 1


directions = [line.strip().split() for line in sys.stdin]
dirs = {"R": (1, 0), "D": (0, 1), "L": (-1, 0), "U": (0, -1)}
moves = [[] for _ in range(2)]

for dir, steps, color in directions:
    hex_dir = list(dirs.values())[int(color[-2:-1], 16)]
    hex_steps = int(color[2:-2], 16)

    moves[0].append((dirs[dir], int(steps)))
    moves[1].append((hex_dir, hex_steps))


print("Part 1:", dig(moves[0]))
print("Part 2:", dig(moves[1]))
