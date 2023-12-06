import sys
from math import prod
from re import findall

for line in sys.stdin:
    numbers = [int(number) for number in findall(r"\d+", line)]

    if line.startswith("Time"):
        times = numbers
    else:
        distances = numbers

wins = [0] * len(times)

for i, (time, distance) in enumerate(zip(times, distances)):
    for j in range(time):
        wins[i] += (j * (time - j)) > distance

time = int("".join(str(time) for time in times))
distance = int("".join(str(distance) for distance in distances))

print("Part 1:", prod(wins))
print("Part 2:", sum(j * (time - j) > distance for j in range(time)))
