import sys


def combat(deck1, deck2):
    while deck1 and deck2:
        card1, card2 = deck1.pop(0), deck2.pop(0)

        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    return deck1, deck2


def recursive(deck1, deck2):
    seen = set()

    while deck1 and deck2:
        if (sig := (tuple(deck1), tuple(deck2))) in seen:
            return (deck1, [])

        seen.add(sig)

        card1, card2 = deck1.pop(0), deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            player1_wins, _ = recursive(deck1[:card1], deck2[:card2])
        else:
            player1_wins = card1 > card2

        if player1_wins:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]

    return deck1, deck2


def score(result):
    return sum(card * (len(deck) - i) for deck in result for i, card in enumerate(deck))


decks = []

while line := sys.stdin.readline():
    if ':' in line:
        deck = []

        while line := sys.stdin.readline().strip():
            deck.append(int(line))

        decks.append(deck)

print('Part 1:', score(combat(decks[0][:], decks[1][:])))
print('Part 2:', score(recursive(decks[0][:], decks[1][:])))
