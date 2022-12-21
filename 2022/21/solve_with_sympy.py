import sys
from re import split

from sympy import simplify
from sympy import solve as sympy_solve
from sympy.abc import x


def solve():
    monkeys = {}

    for line in sys.stdin:
        match split(r":? ", line.strip()):
            case [monkey, number]:
                monkeys[monkey] = int(number)
            case [monkey, arg1, operator, arg2]:
                monkeys[monkey] = [operator, arg1, arg2]

    def build(monkey):
        match monkey:
            case [operator, *names]:
                left, right = [build(monkeys[name]) for name in names]
                return f"({left} {operator} {right})"
            case _:
                return monkey

    def find():
        monkeys["humn"] = x
        left, right = [build(monkeys[name]) for name in monkeys["root"][1:]]

        return sympy_solve(f"Eq({left}, {right})", x)[0]

    print("Part 1:", simplify(build(monkeys["root"])))
    print("Part 2:", find())


if __name__ == "__main__":
    solve()
