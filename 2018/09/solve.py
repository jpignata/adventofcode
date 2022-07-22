from itertools import cycle, count
from collections import deque


def play(number_of_players, last_marble):
    scores = [0 for _ in range(number_of_players)]
    marbles = deque([0])

    for player, next_marble in zip(cycle(range(number_of_players)), count(1)):
        if next_marble == last_marble:
            return max(scores)

        if next_marble % 23 == 0:
            scores[player] += next_marble
            marbles.rotate(-7)
            scores[player] += marbles.popleft()
            marbles.rotate(1)
        else:
            marbles.rotate(1)
            marbles.appendleft(next_marble)


print("Part 1:", play(424, 71482))
print("Part 2:", play(424, 7148200))
