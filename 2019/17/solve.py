from operator import add

from intcode import Computer


def alignment_parameters(grid):
    moves = ((0, -1), (0, 1), (-1, 0), (1, 0))
    intersections = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                for move in moves:
                    dx, dy = tuple(map(add, move, (x, y)))

                    if 0 <= dy < len(grid) and 0 <= dx < len(grid[dy]):
                        if grid[dy][dx] == '.':
                            break
                else:
                    intersections.append((x, y))

    return sum(x * y for x, y in intersections)


computer = Computer.load()
grid = []
row = []

computer.run()

while computer.outputs:
    char = computer.outputs.popleft()

    if char == 10:
        grid.append(row)
        row = []
    else:
        row.append(chr(char))

print('Part 1:', alignment_parameters(grid))
