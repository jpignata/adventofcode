from itertools import count

banks = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]
first = 0
second = 0
seen = []

for i in count(1):
    idx = banks.index(max(banks))
    size = banks[idx]
    banks[idx] = 0

    for j in range(idx + 1, idx + size + 1):
        banks[j % len(banks)] += 1

    if seen.count(str(banks)) == 1 and not first:
        first = i

    if seen.count(str(banks)) == 2:
        second = i
        break

    seen.append(str(banks))

print('Part 1:', first)
print('Part 2:', second - first)
