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


def find(current, ranges):
    if current == "A":
        return prod(end - start + 1 for start, end in ranges.values())

    if current == "R":
        return 0

    for var, op, value, dest in workflows[current]:
        s = []
        start, end = ranges[var]

        if op == "<" and start < value:
            s.append((dest, (start, min(end, value) - 1)))
            s.append((current, (max(start, value), end)))
        elif op == ">" and end > value:
            s.append((dest, (max(start, value) + 1, end)))
            s.append((current, (start, min(end, value))))

        if not op:
            return find(dest, ranges)
        elif s:
            return sum(find(state, {**ranges, var: r}) for state, r in s)


workflows = defaultdict(list)
ratings = []

for line in sys.stdin:
    if line.startswith("{"):
        nums = findall(r"\d+", line)
        ratings.append({var: int(num) for var, num in zip("xmas", nums)})
    elif line.strip():
        name, rules = line[:-2].split("{")

        for rule in rules.split(","):
            if ":" in rule:
                condition, dest = rule.split(":")
                var, op, value = split(r"([<>])", condition)
                workflows[name].append((var, op, int(value), dest))
            else:
                workflows[name].append(("x", None, 0, rule))

print("Part 1:", run(ratings))
print("Part 2:", find("in", {var: (1, 4000) for var in "xmas"}))
