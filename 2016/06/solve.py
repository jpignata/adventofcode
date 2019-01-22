import sys
from collections import Counter

messages = [line.strip() for line in sys.stdin.readlines()]
counts = [Counter() for _ in messages[0]]

for message in messages:
    for i, char in enumerate(message):
        counts[i][char] += 1

print('Part 1:', ''.join(list(map(lambda c: c.most_common()[0][0], counts))))
print('Part 2:', ''.join(list(map(lambda c: c.most_common()[-1][0], counts))))
