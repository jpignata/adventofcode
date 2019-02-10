import sys
import re
from operator import methodcaller


class Node:
    def __init__(self, name, weight=0):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = list()

    def add(self, node):
        self.children.append(node)
        node.parent = self

    def total(self):
        return self.weight + sum(child.total() for child in self.children)

    def imbalance(self):
        totals = [child.total() for child in self.children]

        if totals and min(totals) != max(totals):
            return (max(self.children, key=methodcaller('total')),
                    max(totals) - min(totals))


def build(lines):
    expr = re.compile(r'(\w+) \((\d+)\) ?(?:-> ([\w, ]*))?')
    nodes = dict()

    for line in lines:
        name, weight, children = expr.match(line).groups()

        if name in nodes:
            nodes[name].weight = int(weight)
        else:
            nodes[name] = Node(name, int(weight))

        if children:
            for child in children.split(', '):
                if child not in nodes:
                    nodes[child] = Node(child)

                nodes[name].add(nodes[child])

    for node in nodes.values():
        if node.parent is None:
            return node


def fix(tree, delta=0):
    imbalance = tree.imbalance()

    if imbalance:
        return fix(*imbalance)
    else:
        return tree.weight - delta


tree = build(sys.stdin.readlines())

print('Part 1:', tree.name)
print('Part 2:', fix(tree))
