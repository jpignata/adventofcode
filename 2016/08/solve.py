import sys
from collections import namedtuple, deque


def parse(line):
    tokens = line.split(' ')

    if len(tokens) == 2:
        return Rect(tuple(map(int, tokens[1].split('x'))))
    else:
        return Rotate(tokens[1], int(tokens[2][2:]), int(tokens[-1]))


def rotate(row, positions):
    vals = deque(row)
    vals.rotate(positions)
    return list(vals)


def transpose(grid):
    return [[row[i] for row in grid] for i in range(len(grid[0]))]


def draw(grid):
    for row in grid:
        for char in row:
            sys.stdout.write(char)

        print()
    print()


Rect = namedtuple('rect', ['size'])
Rotate = namedtuple('rotate', ['type', 'start', 'positions'])
grid = [['.' for _ in range(50)] for _ in range(6)]

for cmd in [parse(line) for line in sys.stdin.readlines()]:
    if isinstance(cmd, Rect):
        for x in range(cmd.size[0]):
            for y in range(cmd.size[1]):
                grid[y][x] = '#'
    elif isinstance(cmd, Rotate):
        if cmd.type == 'row':
            grid[cmd.start] = rotate(grid[cmd.start], cmd.positions)
        elif cmd.type == 'column':
            xposed = transpose(grid)
            xposed[cmd.start] = rotate(xposed[cmd.start], cmd.positions)
            grid = transpose(xposed)

print('Part 1:', sum([row.count('#') for row in grid]))
print('Part 2:')
draw(grid)
