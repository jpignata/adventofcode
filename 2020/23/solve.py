import sys


def play(cups, rounds):
    nodes = [None] * (len(cups) + 1)
    prev = None

    for cup in cups[::-1]:
        nodes[cup] = prev
        prev = cup

    nodes[cups[-1]] = prev
    current = prev

    for _ in range(rounds):
        pickup = (p1 := nodes[current], p2 := nodes[p1], p3 := nodes[p2])
        dest = current - 1

        while dest in pickup or dest < 1:
            dest = dest - 1 if dest > 1 else max(cups)

        nodes[current] = nodes[p3]
        nodes[p3] = nodes[dest]
        nodes[dest] = p1
        current = nodes[current]

    if len(nodes) == 10:
        final = ""
        node = nodes[1]

        while node != 1:
            final += str(node)
            node = nodes[node]

        return final

    return nodes[1] * nodes[nodes[1]]


part1 = tuple(int(cup) for cup in sys.stdin.readline().strip())
part2 = part1 + tuple(range(max(part1) + 1, 1_000_001))

print("Part 1:", play(part1, 100))
print("Part 2:", play(part2, 10_000_000))
