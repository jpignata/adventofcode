import sys
import operator
from collections import namedtuple
from functools import reduce

Box = namedtuple("Box", ["l", "w", "h"])


def sides(box):
    return [box.l * box.w, box.w * box.h, box.h * box.l]


def area(box):
    return reduce(lambda x, y: (2 * y) + x, sides(box), 0)


def volume(box):
    return reduce(operator.mul, [box.l, box.w, box.h], 1)


def perimeter(box):
    return sum(sorted([box.l, box.w, box.h])[0:2]) * 2


lines = sys.stdin.readlines()
boxes = [Box(*map(int, line.strip().split("x"))) for line in lines]

print("Part 1:", sum([area(box) + min(sides((box))) for box in boxes]))
print("Part 2:", sum([volume(box) + perimeter(box) for box in boxes]))
