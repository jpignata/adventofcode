from itertools import count
from collections import deque
from math import floor


class Node:
    def __init__(self, id):
        self.elf = id
        self.next, self.previous = None, None

    def delete(self):
        self.previous.next = self.next
        self.next.previous = self.previous

        return self.next


def steal_left(players):
    elves = deque([*range(1, players + 1)])

    while len(elves) != 1:
        elves.rotate(-1)
        elves.popleft()

    return elves[-1]


def steal_across(players):
    nodes = list(map(Node, range(1, players + 1)))

    for i, node in enumerate(nodes):
        node.previous = nodes[(i - 1) % players]
        node.next = nodes[(i + 1) % players]

    node = nodes[0]
    middle = nodes[floor(players / 2)]

    for i in count(0):
        node = node.next

        if node == node.previous == node.next:
            return node.elf

        middle = middle.delete()

        if (players - i) % 2 == 1:
            middle = middle.next



print('Part 1:', steal_left(3014603))
print('Part 2:', steal_across(3014603))
