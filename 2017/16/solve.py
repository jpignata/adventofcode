import sys
from string import ascii_lowercase


def dance(moves, *, rounds=1):
    programs = list(ascii_lowercase[0:16])
    seen = list()

    for i in range(rounds):
        signature = "".join(programs)

        if signature in seen:
            return seen[rounds % i]

        seen.append(signature)

        for move in moves:
            if move[0] == "s":
                steps = int(move[1:])
                programs = programs[-steps:] + programs[:-steps]
            elif move[0] == "x":
                idx1, idx2 = map(int, move[1:].split("/"))
                programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
            elif move[0] == "p":
                char1, char2 = move[1:].split("/")
                idx1, idx2 = programs.index(char1), programs.index(char2)
                programs[idx1], programs[idx2] = char2, char1

    return "".join(programs)


moves = sys.stdin.readline().strip().split(",")

print("Part 1:", dance(moves))
print("Part 2:", dance(moves, rounds=1000000000))
