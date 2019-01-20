from itertools import count


def value_at(target, previous):
    for i in count(start=2):
        for x in range(1, i + 1):
            previous = (previous * 252533) % 33554393

            if (x, i - x + 1) == target:
                return previous


print('Part 1:', value_at((3083, 2978), 20151125))
