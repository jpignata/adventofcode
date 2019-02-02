import hashlib
import operator
from string import ascii_lowercase


def paths_for(passcode, position=(0, 0), route=''):
    def open_doors():
        md5 = hashlib.md5()
        md5.update(bytearray(passcode + route, encoding='ASCII'))

        deltas = ((-1, 0), (1, 0), (0, -1), (0, 1))
        directions = ('U', 'D', 'L', 'R')
        doors = tuple([c in ascii_lowercase[1:6] for c in md5.hexdigest()[:4]])

        for delta, direction, open in zip(deltas, directions, doors):
            x, y = map(operator.add, position, delta)

            if open and 0 <= x <= 3 and 0 <= y <= 3:
                yield (x, y), route + direction

    if position == (3, 3):
        yield route
    else:
        for next_postion, next_route in open_doors():
            yield from paths_for(passcode, next_postion, next_route)


paths = sorted(paths_for('yjjvjgan'), key=len)

print('Part 1:', paths[0])
print('Part 2:', len(paths[-1]))
