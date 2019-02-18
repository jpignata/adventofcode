import sys
import operator
from itertools import cycle


class Cart:
    DELTAS = {'<': (-1, 0), '^': (0, -1), '>': (1, 0), 'v': (0, 1)}
    DIRS = ('<', '^', '>', 'v')

    def __init__(self, location, direction, track):
        self.location = location
        self.direction = direction
        self.track = track
        self.turns = cycle([-1, 0, 1])

    def go(self):
        delta = self.DELTAS[self.direction]
        self.location = tuple(map(operator.add, self.location, delta))
        index = self.DIRS.index(self.direction)
        flip = -1 if self.direction in ('<', '>') else 1
        char = self.track[self.location[1]][self.location[0]]

        if char == '+':
            self.direction = self.DIRS[(index + next(self.turns)) % 4]
        elif char == '/':
            self.direction = self.DIRS[(index + 1) * flip % 4]
        elif char == '\\':
            self.direction = self.DIRS[(index - 1) * flip]


track = []
carts = []
collisions = []

for y, line in enumerate(sys.stdin):
    track.append([])

    for x, character in enumerate(line):
        if character in ('<', '^', '>', 'v'):
            carts.append(Cart((x, y), character, track))
            track[y].append('|' if character in ('^', 'v') else '-')
        else:
            track[y].append(character)

while len(carts) > 1:
    for cart in carts.copy():
            cart.go()

            for other_cart in carts:
                if other_cart != cart and cart.location == other_cart.location:
                    collisions.append(cart.location)
                    carts.remove(cart)
                    carts.remove(other_cart)
                    break


print('Part 1:', ','.join(map(str, collisions[0])))
print('Part 2:', ','.join(map(str, carts.pop().location)))
