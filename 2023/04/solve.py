import sys
from collections import defaultdict

score = 0
cards = defaultdict(lambda: 1)

for i, line in enumerate(sys.stdin):
    winners, numbers = [
        set(block.split())
        for block in line.strip().split(": ")[1].split(" | ")
    ]

    if outcome := len(winners & numbers):
        score += 2 ** (outcome - 1)

        for j in range(i + 1, i + outcome + 1):
            cards[j] += cards[i]

print("Part 1:", score)
print("Part 2:", sum(cards.values()) + 1)
