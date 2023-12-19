import sys
from collections import defaultdict
from math import prod
from operator import gt, lt
from re import findall, split

workflows = defaultdict(list)
ratings = []

for line in sys.stdin:
    if line.startswith("{"):
        ratings.append(
            {
                letter: int(number)
                for letter, number in zip("xmas", findall(r"\d+", line))
            }
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
                workflows[name].append((None, None, None, rule))


def run(ratings):
    total = 0

    for rating in ratings:
        current = "in"

        while current not in "AR":
            for rule in workflows[current]:
                var, op, value, dest = rule

                if var:
                    if {"<": lt, ">": gt}[op](rating[var], value):
                        current = dest
                        break
                else:
                    current = dest

        if current == "A":
            total += sum(rating.values())

    return total


def find(start=(1, 4000)):
    total = 0
    s = [("in", {"x": start, "m": start, "a": start, "s": start})]

    while s:
        current, ranges = s.pop()

        if current == "R":
            continue

        if current == "A":
            total += prod(c[1] - c[0] + 1 for c in ranges.values())
            continue

        for rule in workflows[current]:
            var, op, value, dest = rule

            if op is None:
                s.append((dest, ranges))
                break

            r = ranges[var]

            if op == "<" and r[0] < value:
                s.append((dest, {**ranges, var: (r[0], min(r[1], value) - 1)}))
                s.append((current, {**ranges, var: (max(r[0], value), r[1])}))
                break
            elif op == ">" and r[1] > value:
                s.append((dest, {**ranges, var: (max(r[0], value) + 1, r[1])}))
                s.append((current, {**ranges, var: (r[0], min(r[1], value))}))
                break

    return total


print("Part 1:", run(ratings))
print("Part 2:", find())
