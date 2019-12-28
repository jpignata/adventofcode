import curses
from operator import itemgetter

from intcode import Computer, Input, Halt


def draw(screen, score):
    maxx = max(screen, key=itemgetter(0))[0]
    maxy = max(screen, key=itemgetter(1))[1]

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if screen[(x, y)] == 0:
                stdscr.addstr(y, x, ' ')
            elif screen[(x, y)] == 1:
                if y == 0:
                    stdscr.addstr(y, x, '+' if x == 0 or x == maxx else '-')
                else:
                    stdscr.addstr(y, x, '|')
            elif screen[(x, y)] == 2:
                stdscr.addstr(y, x, '█')
            elif screen[(x, y)] == 3:
                stdscr.addstr(y, x, '▄')
            elif screen[(x, y)] == 4:
                stdscr.addstr(y, x, '◉')

    stdscr.addstr(0, 2, f'SCORE {score}')
    stdscr.refresh()


computer = Computer.load()
computer.run()

blocks = sum(1 for i, c in enumerate(computer.outputs)
             if c == 2 and (i + 1) % 3 == 0)


computer = Computer.load()
computer.program[0] = 2
screen = dict()
score = 0
paddle = (0, 0)
ball = (0, 0)
stdscr = curses.initscr()

curses.curs_set(False)

while not computer.halted:
    try:
        computer.tick()
    except Input:
        if ball[0] > paddle[0]:
            computer.inputs.append(1)
        elif ball[0] < paddle[0]:
            computer.inputs.append(-1)
        elif ball[0] == paddle[0]:
            computer.inputs.append(0)

        draw(screen, score)
    except Halt:
        pass

    if len(computer.outputs) == 3:
        x, y, tile_or_score = [computer.outputs.popleft() for _ in range(3)]

        if x == -1:
            score = tile_or_score
        else:
            screen[(x, y)] = tile_or_score

            if tile_or_score == 3:
                paddle = (x, y)
            elif tile_or_score == 4:
                ball = (x, y)

curses.endwin()

print(f'Part 1: {blocks}')
print(f'Part 2: {score}')
