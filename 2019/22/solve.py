import sys


def deal_new_stack(cards):
    return cards[::-1]


def cut_cards(cards, n):
    return cards[n:] + cards[:n]


def deal_increment(cards, n):
    pointer = 0
    new_stack = [-1] * len(cards)

    for card in cards:
        new_stack[pointer] = card
        pointer = (pointer + n) % len(cards)

    return new_stack


def deal(cards, lines):
    for line in lines:
        tokens = line.split(" ")

        if tokens[0] == "deal" and tokens[1] == "into":
            cards = deal_new_stack(cards)
        elif tokens[0] == "deal" and tokens[1] == "with":
            cards = deal_increment(cards, int(tokens[3]))
        elif tokens[0] == "cut":
            cards = cut_cards(cards, int(tokens[1]))

    return cards


def inv(a, n):
    return pow(a, n - 2, n)


lines = [line for line in sys.stdin]
cards = deal(list(range(10007)), lines)

n = 119315717514047
M = 101741582076661
a, b = 1, 0

for line in lines:
    tokens = line.split(" ")

    if tokens[0] == "deal" and tokens[1] == "into":
        la, lb = -1, -1
    elif tokens[0] == "deal" and tokens[1] == "with":
        la, lb = int(tokens[3]), 0
    elif tokens[0] == "cut":
        la, lb = 1, int(tokens[1]) * -1

    a = (la * a) % n
    b = (la * b + lb) % n

Ma = pow(a, M, n)
Mb = (b * (Ma - 1) * inv(a - 1, n)) % n

print("Part 1:", {card: pos for pos, card in enumerate(cards)}[2019])
print("Part 2:", ((2020 - Mb) * inv(Ma, n)) % n)
