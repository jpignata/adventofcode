import sys

wins = {1: 3, 2: 1, 3: 2}
losses = {value: key for key, value in wins.items()}
part1 = part2 = 0

for line in sys.stdin:
    symbol1, symbol2 = line.strip().split()
    value1 = ord(symbol1) - ord("A") + 1
    value2 = ord(symbol2) - ord("X") + 1
    part1 += value2

    if value1 == value2:
        part1 += 3
    elif value1 == wins[value2]:
        part1 += 6

    if symbol2 == "X":
        part2 += wins[value1]
    elif symbol2 == "Y":
        part2 += value1 + 3
    elif symbol2 == "Z":
        part2 += losses[value1] + 6

print("Part 1:", part1)
print("Part 2:", part2)
