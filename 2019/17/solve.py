from operator import add
from collections import deque

from intcode import Computer

computer = Computer.load()
grid = list()
row = list()
intersections = list()

computer.run()

while computer.outputs:
    if (char := computer.outputs.popleft()) == 10:
        grid.append(row)
        row = list()
    else:
        row.append(chr(char))

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '#':
            for move in ((0, -1), (0, 1), (-1, 0), (1, 0)):
                dx, dy = tuple(map(add, move, (x, y)))

                if 0 <= dy < len(grid) and 0 <= dx < len(grid[dy]):
                    if grid[dy][dx] == '.':
                        break
            else:
                intersections.append((x, y))

print('Part 1:', sum(x * y for x, y in intersections))

program = """
A,B,A,A,B,C,B,C,C,B
L,12,R,8,L,6,R,8,L,6
R,8,L,12,L,12,R,8
L,6,R,6,L,12
n
"""

computer = computer.load()
computer[0] = 2

for line in program.strip().split('\n'):
    computer.execute(line)

computer.run()

print('Part 2:', computer.outputs.pop())
