import sys

steps = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
dirs = tuple(steps.keys())


def direct(instructions, *, pos, heading):
    for cmd, arg in instructions:
        if cmd == 'L':
            heading = (heading - arg) % 360
        elif cmd == 'R':
            heading = (heading + arg) % 360
        else:
            if cmd == 'F':
                cmd = dirs[heading // 90]

            pos = tuple(xy + dxy * arg for xy, dxy in zip(pos, steps[cmd]))

    return sum(abs(c) for c in pos)


def relative(instructions, *, pos, waypoint):
    for cmd, arg in instructions:
        if cmd == 'L':
            for _ in range(arg // 90):
                waypoint = (waypoint[1] * -1, waypoint[0])
        elif cmd == 'R':
            for _ in range(arg // 90):
                waypoint = (waypoint[1], waypoint[0] * -1)
        elif cmd == 'F':
            pos = tuple(xy + dxy * arg for xy, dxy in zip(pos, waypoint))
        else:
            waypoint = tuple(xy + dxy * arg for xy, dxy
                             in zip(waypoint, steps[cmd]))

    return sum(abs(c) for c in pos)


instructions = [(line[0], int(line[1:])) for line in sys.stdin.readlines()]

print('Part 1:', direct(instructions, pos=(0, 0), heading=90))
print('Part 2:', relative(instructions, pos=(0, 0), waypoint=(10, 1)))
