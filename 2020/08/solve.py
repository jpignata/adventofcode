import sys


def run(instructions):
    pointer, accumulator = 0, 0
    seen = set()

    while pointer < len(instructions):
        cmd, arg = instructions[pointer]

        if cmd == "acc":
            accumulator += arg
            pointer += 1
        elif cmd == "jmp":
            pointer += arg
        else:
            pointer += 1

        if pointer in seen:
            return (False, accumulator)

        seen.add(pointer)

    return (True, accumulator)


def find(instructions):
    changes = {"jmp": "nop", "nop": "jmp"}

    for i, (cmd, arg) in enumerate(instructions):
        if cmd in changes:
            modified = instructions[:]
            modified[i] = (changes[cmd], arg)
            terminated, accumulator = run(modified)

            if terminated:
                return accumulator


instructions = [
    (cmd, int(arg))
    for cmd, arg in [tuple(line.strip().split(" ")) for line in sys.stdin.readlines()]
]

print("Part 1:", run(instructions)[1])
print("Part 2:", find(instructions))
