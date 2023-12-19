# 132755669099550 - too high

import sys
from re import findall, split
from operator import gt, lt
from math import prod

workflows = {}
ratings = []
ops = {"<": lt, ">": gt}

for line in sys.stdin:
    if line.startswith("{"):
        n = [int(num) for num in findall(r"\d+", line)]
        ratings.append({"x": n[0], "m": n[1], "a": n[2], "s": n[3]})
    elif line.strip():
        name, rules = line[:-2].split("{")
        workflows[name] = []

        for rule in rules.split(","):
            if ":" in rule:
                condition, destination = rule.split(":")
                var, op, value = split(r"([<>])", condition)
                workflows[name].append((var, op, int(value), destination))
            else:
                workflows[name].append((None, None, None, rule))


def run(ratings):
    total = 0

    for rating in ratings:
        current = "in"

        while current not in "AR":
            for rule in workflows[current]:
                var, op, value, destination = rule

                if var:
                    if ops[op](rating[var], value):
                        current = destination
                        break
                else:
                    current = destination

        if current == "A":
            total += sum(rating.values())

    return total


def find(ranges):
    s = [("in", ranges)]
    total = 0

    while s:
        current, ranges = s.pop()

        if current == "R":
            continue

        if current == "A":
            total += prod(c[1] - c[0] + 1 for c in ranges.values())
            continue

        for rule in workflows[current]:
            var, op, value, destination = rule

            if op is None:
                s.append((destination, ranges))
                break

            r = ranges[var]

            if op == "<" and r[0] < value:
                s.append(
                    (
                        destination,
                        {**ranges, var: (r[0], min(r[1], value) - 1)},
                    )
                )
                s.append(
                    (
                        current,
                        {**ranges, var: (max(r[0], value), r[1])},
                    )
                )
                break
            elif op == ">" and r[1] > value:
                print(ranges)
                print(rule)
                print(value)
                print()
                s.append(
                    (
                        destination,
                        {**ranges, var: (max(r[0], value) + 1, r[1])},
                    )
                )
                s.append(
                    (
                        current,
                        {**ranges, var: (r[0], min(r[1], value))},
                    )
                )
                break

    return total


print("Part 1:", run(ratings))
print(
    "Part 2:",
    find({"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}),
)
