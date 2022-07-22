import sys


def solve(search, instructions):
    s = []

    for i in range(len(search)):
        div = int(instructions[i * 18 + 4][-1])
        add_x = int(instructions[i * 18 + 5][-1])
        add_y = int(instructions[i * 18 + 15][-1])

        if div == 1:
            s.append((i, add_y))
        elif div == 26:
            j, add_y = s.pop()
            search[i] = search[j] + add_y + add_x

            if search[i] > 9:
                search[j] -= search[i] - 9
                search[i] = 9
            elif search[i] < 1:
                search[j] += 1 - search[i]
                search[i] = 1

    return "".join(str(char) for char in search)


instructions = [instruction.strip().split() for instruction in sys.stdin]

print("Part 1:", solve([9] * 14, instructions))
print("Part 2:", solve([1] * 14, instructions))
