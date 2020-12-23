import sys
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: type['Node']


def play(cups, times):
    nodes = {}
    node, prev = None, None

    for cup in reversed(cups):
        node = Node(cup, prev)
        nodes[cup] = node
        prev = node

    head, tail = node, node

    while tail.next:
        tail = tail.next

    tail.next = head
    current = head

    for _ in range(times):
        pickup = []
        node = current

        for _ in range(3):
            pickup.append(node.next.val)
            node = node.next

        destination = current.val - 1

        while destination in pickup or destination < 1:
            destination -= 1

            if destination < 1:
                destination = max(cups)

        node = nodes[destination]
        oldnext = node.next

        for label in pickup:
            node.next = nodes[label]
            node = nodes[label]

        current.next = node.next
        node.next = oldnext

        current = current.next

    if len(nodes) > 10:
        return nodes[1].next.val * nodes[1].next.next.val

    final = []
    node = nodes[1]

    while len(final) < len(cups) - 1:
        final.append(node.next.val)
        node = node.next

    return ''.join(str(v) for v in final)


cups = [int(cup) for cup in sys.stdin.readline().strip()]
part2 = list(cups) + list(range(max(cups) + 1, 1_000_001))

print('Part 1:', play(cups, 100))
print('Part 2:', play(part2, 10_000_000))
