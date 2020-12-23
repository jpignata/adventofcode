import sys
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: 'Node'


def play(cups, rounds):
    nodes = {}
    node, prev, tail = None, None, None

    for cup in reversed(cups):
        node = Node(cup, prev)

        if tail is None:
            tail = node

        nodes[cup] = node
        prev = node

    head = node
    tail.next = head
    current = head

    for _ in range(rounds):
        pickup = [current.next.val, current.next.next.val, current.next.next.next.val]
        destination = current.val - 1

        while destination in pickup or destination < 1:
            destination = destination - 1 if destination > 1 else max(cups)

        head = nodes[destination].next
        nodes[destination].next = nodes[pickup[0]]
        current.next = nodes[pickup[2]].next
        nodes[pickup[2]].next = head
        current = current.next

    if len(nodes) > 10:
        return nodes[1].next.val * nodes[1].next.next.val

    final = []
    node = nodes[1]

    while len(final) < len(cups) - 1:
        final.append(node.next.val)
        node = node.next

    return ''.join(str(cup) for cup in final)


part1 = [int(cup) for cup in sys.stdin.readline().strip()]
part2 = list(part1) + list(range(max(part1) + 1, 1_000_001))

print('Part 1:', play(part1, 100))
print('Part 2:', play(part2, 10_000_000))
