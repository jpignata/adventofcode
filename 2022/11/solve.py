import sys
from collections import deque
from copy import deepcopy
from dataclasses import dataclass, field
from math import prod
from operator import add, floordiv, mod, mul
from typing import Callable, Deque, Dict, Iterable, List, Tuple

Operation = Tuple[Callable[[int, int], int], int]


@dataclass
class Monkey:
    items: Deque[int] = field(default_factory=deque)
    destinations: Dict[bool, int] = field(default_factory=dict)
    operation: Operation = lambda x, y: 0, 0
    divisor: int = 0
    inspections: int = 0

    def inspect(self, reducer: Operation) -> Iterable[Tuple[int, int]]:
        while self.items:
            self.inspections += 1

            item = self.items.popleft()
            item = self.operation[0](item, self.operation[1] or item)
            item = reducer[0](item, reducer[1])
            destination = self.destinations[item % self.divisor == 0]

            yield item, destination

    def add(self, item: int) -> None:
        self.items.append(item)


def solve() -> None:
    monkeys = []

    while line := sys.stdin.readline():
        if line.startswith("Monkey"):
            monkey = Monkey()

            while line := sys.stdin.readline().strip():
                match line.split(": "):
                    case ["Starting items", items]:
                        monkey.items = deque(int(item) for item in items.split(", "))
                    case ["Operation", expression]:
                        _, operator, argument = expression.split(" = ")[-1].split()
                        operation = mul if operator == "*" else add
                        operand = int(argument) if argument.isdigit() else 0
                        monkey.operation = operation, operand
                    case ["Test", condition]:
                        monkey.divisor = int(condition.split()[-1])
                    case ["If true", action]:
                        monkey.destinations[True] = int(action.split()[-1])
                    case ["If false", action]:
                        monkey.destinations[False] = int(action.split()[-1])

            monkeys.append(monkey)

    print("Part 1:", play(monkeys, 20, (floordiv, 3)))
    print("Part 2:", play(monkeys, 10000, (mod, prod(m.divisor for m in monkeys))))


def play(monkeys: List[Monkey], rounds: int, reducer: Operation) -> int:
    monkeys = deepcopy(monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            for item, destination in monkey.inspect(reducer):
                monkeys[destination].add(item)

    return prod(sorted(monkey.inspections for monkey in monkeys)[-2:])


if __name__ == "__main__":
    solve()
