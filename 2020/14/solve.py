import re
import sys

mask = None
version1, version2 = {}, {}

for line in sys.stdin.readlines():
    if line.startswith('mask'):
        mask = line.split(' ')[-1].strip()
    elif (match := re.search(r'mem\[(\d*)\] = (\d*)', line)):
        index = int(match.group(1))
        value = int(match.group(2))
        original_index = index
        original_value = value
        floating = []
        indexes = set()

        for i, bit in enumerate(mask):
            if bit == '1':
                value |= 1 << 35-i
                index |= 1 << 35-i
            elif bit == '0':
                value &= ~(1 << 35-i)
            elif bit == 'X':
                floating.append(i)

        for position in floating:
            for idx in indexes.copy():
                indexes.add(idx | 1 << 35-position)
                indexes.add(idx & ~(1 << 35-position))

            indexes.add(index | 1 << 35-position)
            indexes.add(index & ~(1 << 35-position))

        version1[original_index] = value

        for index in indexes:
            version2[index] = original_value

print('Part 1:', sum(version1.values()))
print('Part 2:', sum(version2.values()))
