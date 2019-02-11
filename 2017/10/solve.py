import operator
from collections import deque
from itertools import zip_longest
from functools import reduce


def hash(lengths, *, rounds=1):
    numbers = deque(range(0, 256))
    q = deque()
    skip = 0

    for _ in range(rounds):
        for length in lengths:
            for _ in range(length):
                q.append(numbers.popleft())

            while q:
                numbers.appendleft(q.popleft())

            numbers.rotate((length + skip) * -1)
            skip += 1

    numbers.rotate((sum(lengths) * rounds) + sum(range(1, skip)))

    return list(numbers)


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip_longest(*args)


numbers = '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'
sequence1 = list(map(int, numbers.split(',')))
sequence2 = [ord(char) for char in numbers] + [17, 31, 73, 47, 23]
part1 = hash(sequence1)
sparse_hash = hash(sequence2, rounds=64)
dense_hash = [reduce(operator.xor, g) for g in grouper(sparse_hash, 16)]

print('Part 1:', part1[0] * part1[1])
print('Part 2:', ''.join(f'{c:02x}' for c in dense_hash))
