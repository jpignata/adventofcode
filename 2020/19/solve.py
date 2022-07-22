import re
import sys


def build(rules, start="0", depth=0):
    if depth > 15:
        return ""

    expression = ""

    for token in rules[start].split():
        if token.isdigit():
            expression += build(rules, token, depth + 1)
        else:
            expression += token

    return "(" + expression + ")"


rules, msgs = {}, []

for line in sys.stdin.readlines():
    if ":" in line:
        num, rule = line.strip().split(": ")
        rules[num] = rule.replace('"', "")
    else:
        msgs.append(line.strip())

part1 = build(rules)
rules["8"] = "42 | 42 8"
rules["11"] = "42 31 | 42 11 31"
part2 = build(rules)

print("Part 1:", sum(1 for msg in msgs if re.fullmatch(part1, msg)))
print("Part 2:", sum(1 for msg in msgs if re.fullmatch(part2, msg)))
