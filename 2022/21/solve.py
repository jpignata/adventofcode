import sys
from operator import add, mul, sub, truediv
from re import split


def solve():
    monkeys = {}
    operations = {"+": add, "-": sub, "*": mul, "/": truediv}

    for line in sys.stdin:
        match split(r":? ", line.strip()):
            case [monkey, number]:
                monkeys[monkey] = int(number)
            case [monkey, arg1, operator, arg2]:
                monkeys[monkey] = [operations[operator], arg1, arg2]

    print("Part 1:", int(resolve(monkeys, "root")))
    print("Part 2:", find(monkeys))


def resolve(monkeys, monkey):
    match monkeys[monkey]:
        case int(arg1):
            return arg1
        case [operation, arg1, arg2]:
            return operation(resolve(monkeys, arg1), resolve(monkeys, arg2))


def find(monkeys):
    arg1, arg2 = monkeys["root"][1:]
    lo, hi = 0, int(1e16)

    while lo < hi:
        mid = (lo + hi) // 2
        monkeys["humn"] = mid
        result1 = resolve(monkeys, arg1)
        result2 = resolve(monkeys, arg2)

        if result1 > result2:
            lo = mid + 1
        elif result1 < result2:
            hi = mid
        elif result1 == result2:
            return mid

    return -1


if __name__ == "__main__":
    solve()
