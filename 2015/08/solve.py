import sys
import re
from collections import deque


def escape(line):
    original = deque(line)
    escaped = []

    while len(original) != 0:
        char = original.popleft()

        if char == '"':
            escaped.append('\\"')
        elif char == "\\" and original[0] == '"':
            original.popleft()
            escaped.append('\\\\\\"')
        elif char == "\\" and original[0] == "\\":
            original.popleft()
            escaped.append("\\\\\\\\")
        elif char == "\\" and original[0] == "x":
            escaped.append("\\\\")
        else:
            escaped.append(char)

    return '"' + "".join(escaped) + '"'


lines = [lines.strip() for lines in sys.stdin.readlines()]
raw = [bytes(l[1:-1], "utf-8").decode("unicode_escape") for l in lines]
escaped = [escape(line) for line in lines]

print("Part 1:", sum([len(l) for l in lines]) - sum([len(s) for s in raw]))
print("Part 2:", sum([len(l) for l in escaped]) - sum([len(l) for l in lines]))
