import re
import sys

mask = None
v1, v2 = {}, {}

for line in sys.stdin.readlines():
    if match := re.search(r"mask = ([01X]*)", line):
        mask = match.group(1)
    elif match := re.search(r"mem\[(\d*)\] = (\d*)", line):
        index, value = [int(m) for m in match.group(1, 2)]
        initial_index, initial_value = index, value
        positions = []
        indexes = set()

        for position, bit in enumerate(mask):
            if bit == "1":
                value |= 1 << 35 - position
                index |= 1 << 35 - position
            elif bit == "0":
                value &= ~(1 << 35 - position)
            elif bit == "X":
                positions.append(position)

        for position in positions:
            for idx in indexes.copy():
                indexes.add(idx | 1 << 35 - position)
                indexes.add(idx & ~(1 << 35 - position))

            indexes.add(index | 1 << 35 - position)
            indexes.add(index & ~(1 << 35 - position))

        v1[initial_index] = value

        for index in indexes:
            v2[index] = initial_value

print("Part 1:", sum(v1.values()))
print("Part 2:", sum(v2.values()))
