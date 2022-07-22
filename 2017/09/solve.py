import sys

chars = iter(sys.stdin.readline())
depth = 0
score = 0
garbage = 0

for char in chars:
    if char == "{":
        depth += 1
    elif char == "}":
        score += depth
        depth -= 1
    elif char == "<":
        while char != ">":
            char = next(chars)

            if char == "!":
                next(chars)
            elif char != ">":
                garbage += 1

print("Part 1:", score)
print("Part 2:", garbage)
