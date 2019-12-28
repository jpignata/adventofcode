import sys
from collections import defaultdict
from operator import itemgetter

from intcode import Computer, Halt


def paint(panel=0):
    c = Computer.load()
    pos = (0, 0)
    dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
    direction = 0
    panels = defaultdict(int)
    panels[(0, 0)] = panel

    while not c.halted:
        c.inputs.append(panels[pos])

        while len(c.outputs) != 2 and not c.halted:
            try:
                c.tick()
            except Halt:
                pass

        if c.outputs:
            panels[pos] = c.outputs.popleft()
            direction = (direction + (-1, 1)[c.outputs.popleft()]) % len(dirs)
            pos = (pos[0] + dirs[direction][0], pos[1] + dirs[direction][1])

    return panels


def draw():
    panels = paint(1)
    maxx = max(panels, key=itemgetter(0))[0]
    maxy = max(panels, key=itemgetter(1))[1]

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if panels[(x, y)] == 1:
                sys.stdout.write('█')
            else:
                sys.stdout.write(' ')

        print()


print(f'Part 1: {len(paint())}')
print('Part 2:')
draw()
