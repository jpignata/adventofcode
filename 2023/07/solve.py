import sys


def score(hands, order, wild=""):
    ranked = []

    for cards, bid in hands:
        counts = [cards.count(c) for c in set(cards) if c != wild] or [0]
        counts = sorted(counts, reverse=True)
        counts[0] += cards.count(wild)
        strengths = [order.index(c) for c in cards]

        ranked.append(((counts, strengths), int(bid)))

    return sum(bid * (i + 1) for i, (_, bid) in enumerate(sorted(ranked)))


hands = [line.strip().split() for line in sys.stdin]

print("Part 1:", score(hands, "23456789TJQKA"))
print("Part 2:", score(hands, "J23456789TQKA", "J"))
