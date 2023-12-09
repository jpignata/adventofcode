import sys

part1 = part2 = 0

for line in sys.stdin:
    numbers = [int(number) for number in line.strip().split()]
    heads = [numbers[0]]
    tails = [numbers[-1]]
    prev = 0

    while any(numbers):
        numbers = [num2 - num1 for num1, num2 in zip(numbers, numbers[1:])]
        heads.append(numbers[0])
        tails.append(numbers[-1])

    for num in heads[::-1]:
        prev = num - prev

    part1 += sum(tails)
    part2 += prev

print("Part 1:", part1)
print("Part 2:", part2)
