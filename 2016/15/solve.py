from itertools import count


def find(discs):
    disc = 0

    for second in count(1):
        positions, start = discs[disc]

        if (start + second) % positions == 0:
            disc += 1
        else:
            disc = 0

        if disc == len(discs):
            return second - len(discs)


discs = [(17, 1), (7, 0), (19, 2), (5, 0), (3, 0), (13, 5)]

print('Part 1:', find(discs))
print('Part 2:', find(discs + [(11, 0)]))
