import sys

instructions = sys.stdin.readline()
floor = 0

print("Part 1:", instructions.count("(") - instructions.count(")"))

for i, char in enumerate(instructions):
    floor += (-1, 1)[char == "("]

    if floor == -1:
        print("Part 2:", i + 1)
        break
