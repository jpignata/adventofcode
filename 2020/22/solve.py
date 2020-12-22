import sys
from collections import deque


def combat(decks):
    while all(decks):
        cards = [decks[0].popleft(), decks[1].popleft()]
        winner = cards.index(max(cards))

        for card in sorted(cards, reverse=True):
            decks[winner].append(card)

    return decks


def recursive(decks):
    seen = set()

    while all(decks):
        if repr(decks) in seen:
            return (decks[0], deque([]))

        seen.add(repr(decks))

        cards = [decks[0].popleft(), decks[1].popleft()]

        if len(decks[0]) >= cards[0] and len(decks[1]) >= cards[1]:
            sub = [deque((c) for j, c in enumerate(decks[i]) if j < cards[i])
                   for i in (0, 1)]

            winner = 0 if recursive(sub)[0] else 1

            decks[winner].append(cards[winner])
            decks[winner].append(cards[(1, 0)[winner]])
        else:
            winner = cards.index(max(cards))

            for card in sorted(cards, reverse=True):
                decks[winner].append(card)

    return decks


def score(decks):
    return sum(card * (len(deck) - i)
               for deck in decks
               for i, card in enumerate(deck)
               if deck)


decks = []

while (line := sys.stdin.readline()):
    if ':' in line:
        deck = []

        while (line := sys.stdin.readline().strip()):
            deck.append(int(line))

        decks.append(deck)

print('Part 1:', score(combat([deque(deck) for deck in decks])))
print('Part 2:', score(recursive([deque(deck) for deck in decks])))
