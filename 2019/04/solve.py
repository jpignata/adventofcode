from itertools import groupby

part1, part2 = 0, 0

for password in range(278384, 824796):
    numbers = [int(digit) for digit in str(password)]
    counts = [len(list(s)) for _, s in groupby(numbers)]
    pairs = [(numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1)]

    if all([n1 <= n2 for n1, n2 in pairs]):
        if any([c >= 2 for c in counts]):
            part1 += 1

        if any([c == 2 for c in counts]):
            part2 += 1

print('Part 1:', part1)
print('Part 2:', part2)
