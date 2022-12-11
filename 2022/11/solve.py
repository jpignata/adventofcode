import sys
from collections import deque
from copy import deepcopy
from dataclasses import dataclass, field
from math import prod
from operator import add, floordiv, mod, mul
from typing import Callable, Deque, Dict, List, Tuple

Operation = Tuple[Callable[[int, int], int], int]


@dataclass
class Monkey:
    items: Deque[int] = field(default_factory=deque)
    outcomes: Dict[bool, int] = field(default_factory=dict)
    operation: Operation = lambda x, y: 0, 0
    divisible_by: int = 0
    inspections: int = 0

    def inspect(self, reducer: Operation) -> Tuple[int, int]:
        self.inspections += 1

        item = self.items.popleft()
        item = self.operation[0](item, self.operation[1] or item)
        item = reducer[0](item, reducer[1])
        destination = self.outcomes[item % self.divisible_by == 0]

        return item, destination

    def add(self, item: int) -> None:
        self.items.append(item)

    def has_items(self) -> bool:
        return len(self.items) > 0


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
                    case ["Test", divisible_by]:
                        monkey.divisible_by = int(divisible_by.split()[-1])
                    case ["If true", outcome]:
                        monkey.outcomes[True] = int(outcome.split()[-1])
                    case ["If false", outcome]:
                        monkey.outcomes[False] = int(outcome.split()[-1])

            monkeys.append(monkey)

    print("Part 1:", simulate(deepcopy(monkeys)))
    print("Part 2:", simulate(deepcopy(monkeys), 10_000))


def simulate(monkeys: List[Monkey], rounds: int = 20) -> int:
    if rounds <= 20:
        reducer = floordiv, 3
    else:
        reducer = mod, prod(monkey.divisible_by for monkey in monkeys)

    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.has_items():
                item, destination = monkey.inspect(reducer)
                monkeys[destination].add(item)

    return prod(sorted(monkey.inspections for monkey in monkeys)[-2:])


if __name__ == "__main__":
    solve()
