from itertools import count


def find(discs):
    disc = 0

    for second in count(1):
        if disc == len(discs):
            return second - len(discs) - 1
        elif (discs[disc][1] + second) % discs[disc][0] == 0:
            disc += 1
        else:
            disc = 0


discs = [(17, 1), (7, 0), (19, 2), (5, 0), (3, 0), (13, 5)]

print('Part 1:', find(discs))
print('Part 2:', find(discs + [(11, 0)]))
