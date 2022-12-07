import sys
from dataclasses import dataclass, field
from math import inf
from typing import Dict


@dataclass
class Directory:
    size: int = 0
    parent: "Directory" = None
    children: Dict[str, "Directory"] = field(default_factory=dict)


def solve():
    root = build(Directory())

    print("Part 1:", part1(root))
    print("Part 2:", part2(root, root.size - 40_000_000))


def build(root):
    current = root

    for line in sys.stdin:
        match line.strip().split():
            case ["$", "cd", "/"]:
                current = root
            case ["$", "cd", ".."]:
                current = current.parent
            case ["$", "cd", name]:
                current = current.children[name]
            case ["$", "ls"]:
                continue
            case ["dir", name]:
                current.children[name] = Directory(parent=current)
            case [size, _]:
                node = current

                while node:
                    node.size += int(size)
                    node = node.parent

    return root


def part1(root):
    total = 0

    for node in root.children.values():
        total += part1(node)

        if node.size <= 100_000:
            total += node.size

    return total


def part2(root, min_size):
    smallest = inf

    for node in root.children.values():
        smallest = min(smallest, part2(node, min_size))

        if node.size >= min_size:
            smallest = min(smallest, node.size)

    return smallest


if __name__ == "__main__":
    solve()
