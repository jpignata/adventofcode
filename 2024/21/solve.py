import sys
from functools import cache
from itertools import pairwise, product


@cache
def count(code, robots):
    if not robots:
        return len(code)

    return sum(
        min(count(path + "A", robots - 1) for path in paths[char1, char2])
        for char1, char2 in pairwise("A" + code)
    )


paths = {}

for keypad in ("789456123_0A", "_^A<v>"):
    locations = {
        char: (x, y)
        for y, row in enumerate(keypad[i : i + 3] for i in range(0, len(keypad), 3))
        for x, char in enumerate(row)
    }

    for char1, char2 in product(locations, repeat=2):
        x1, y1 = locations[char1]
        x2, y2 = locations[char2]
        dx, dy = x2 - x1, y2 - y1
        mx = ("<" if dx < 0 else ">") * abs(dx)
        my = ("^" if dy < 0 else "v") * abs(dy)

        if char1 == char2:
            paths[char1, char2] = [""]
        elif not dx:
            paths[char1, char2] = [my]
        elif not dy:
            paths[char1, char2] = [mx]
        elif (x2, y1) == locations["_"]:
            paths[char1, char2] = [my + mx]
        elif (x1, y2) == locations["_"]:
            paths[char1, char2] = [mx + my]
        else:
            paths[char1, char2] = [mx + my, my + mx]

codes = [line.strip() for line in sys.stdin]

print("Part 1:", sum(count(code, 3) * int(code[:-1]) for code in codes))
print("Part 2:", sum(count(code, 26) * int(code[:-1]) for code in codes))
