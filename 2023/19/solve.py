import sys
from collections import defaultdict
from math import prod
from operator import gt, lt
from re import findall, split


def run(ratings):
    total = 0
    ops = {"<": lt, ">": gt, None: lambda a, b: True}

    for rating in ratings:
        current = "in"

        while current not in "AR":
            for var, op, value, dest in workflows[current]:
                if ops[op](rating[var], value):
                    current = dest
                    break

        if current == "A":
            total += sum(rating.values())

    return total


def find_in(_range):
    total = 0
    s = [("in", {letter: _range for letter in "xmas"})]

    while s:
        current, ranges = s.pop()

        if current == "A":
            total += prod(c[1] - c[0] + 1 for c in ranges.values())
            continue

        if current == "R":
            continue

        for var, op, value, dest in workflows[current]:
            start, end = ranges[var]

            if op is None:
                s.append((dest, ranges))
            elif op == "<" and start < value:
                s.append((dest, {**ranges, var: (start, min(end, value) - 1)}))
                s.append((current, {**ranges, var: (max(start, value), end)}))
            elif op == ">" and end > value:
                s.append((dest, {**ranges, var: (max(start, value) + 1, end)}))
                s.append((current, {**ranges, var: (start, min(end, value))}))
            else:
                continue

            break

    return total


workflows = defaultdict(list)
ratings = []

for line in sys.stdin:
    if line.startswith("{"):
        ratings.append(
            {var: int(num) for var, num in zip("xmas", findall(r"\d+", line))}
        )
    elif line.strip():
        name, rules = line[:-2].split("{")
        workflows[name] = []

        for rule in rules.split(","):
            if ":" in rule:
                condition, dest = rule.split(":")
                var, op, value = split(r"([<>])", condition)
                workflows[name].append((var, op, int(value), dest))
            else:
                workflows[name].append(("x", None, 0, rule))

print("Part 1:", run(ratings))
print("Part 2:", find_in((1, 4000)))
