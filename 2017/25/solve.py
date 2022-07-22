from collections import defaultdict

tape = defaultdict(int)
states = {
    "a": {0: (1, 1, "b"), 1: (0, 1, "f")},
    "b": {0: (0, -1, "b"), 1: (1, -1, "c")},
    "c": {0: (1, -1, "d"), 1: (0, 1, "c")},
    "d": {0: (1, -1, "e"), 1: (1, 1, "a")},
    "e": {0: (1, -1, "f"), 1: (0, -1, "d")},
    "f": {0: (1, 1, "a"), 1: (0, -1, "e")},
}
state = "a"
current = 0

for _ in range(12964419):
    val = tape[current]
    mark, move, state = states[state][val]
    tape[current] = mark
    current = current + move

print("Part 1:", sum(v for v in tape.values() if v == 1))
