import sys


class Node:
    def __init__(self, children, metadata):
        self.children = children
        self.metadata = metadata

    def sum(self):
        return sum(self.metadata) + sum(child.sum() for child in self.children)

    def value(self):
        if self.children:
            return sum(
                self.children[i - 1].value()
                for i in self.metadata
                if i - 1 < len(self.children)
            )
        else:
            return self.sum()


def build(digits):
    num_children = next(digits)
    num_metadata = next(digits)

    children = [build(digits) for _ in range(num_children)]
    metadata = [next(digits) for _ in range(num_metadata)]

    return Node(children, metadata)


tree = build(map(int, sys.stdin.readline().strip().split(" ")))

print("Part 1:", tree.sum())
print("Part 2:", tree.value())
